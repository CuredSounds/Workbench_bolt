import os
from pathlib import Path

def create_project_structure(base_path: str):
    """Create the initial project directory structure."""
    
    # Define the directory structure
    directories = [
        '.github/workflows',
        'docs',
        'infra/terraform/modules',
        'infra/terraform/main',
        'infra/kubernetes/helm_charts',
        'infra/kubernetes/kustomize',
        'infra/kubernetes/manifests',
        'project_starter_gui',
        'src/scraping',
        'src/ml',
        'src/devops/docker',
        'src/devops/ci_cd',
        'src/utils',
        'src/cli_tools',
        'tests/terraform',
        'tests/python',
        'tests/c++',
    ]
    
    # Create directories
    for directory in directories:
        Path(base_path, directory).mkdir(parents=True, exist_ok=True)
        # Create __init__.py for Python packages
        if directory.startswith(('src/', 'tests/python/')):
            init_file = Path(base_path, directory, '__init__.py')
            init_file.touch()
    
    print(f"Created project structure in: {base_path}")

if __name__ == '__main__':
    create_project_structure('.') 