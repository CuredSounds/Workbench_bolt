#!/bin/bash

# Check if .env already exists
if [ -f .env ]; then
    echo "Warning: .env file already exists"
    read -p "Do you want to overwrite it? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled"
        exit 1
    fi
fi

# Copy .env.example to .env if it doesn't exist or user agreed to overwrite
cp .env.example .env

echo "Created .env file from template"
echo "Please edit .env and add your API keys"
echo "The following environment variables need to be configured:"
echo
grep -v '^#' .env | grep '=' | while read -r line; do
    var_name=$(echo "$line" | cut -d'=' -f1)
    echo "- $var_name"
done

# Make the script executable
chmod +x setup.sh

echo
echo "Setup complete! Edit .env to configure your environment"
