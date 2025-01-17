# Database Setup Guide

This guide covers database setup and configuration for Live Agent Studio agents.

## Supported Databases

1. **Supabase**
   - Managed PostgreSQL
   - Built-in authentication
   - Vector embeddings
   - Real-time subscriptions

2. **PostgreSQL**
   - Self-hosted option
   - Direct connection
   - Full control
   - Custom extensions

## Schema Design

### Core Tables

1. **Messages Table**
```sql
CREATE TABLE messages (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    session_id TEXT NOT NULL,
    message JSONB NOT NULL
);

CREATE INDEX idx_messages_session_id ON messages(session_id);
CREATE INDEX idx_messages_created_at ON messages(created_at);
```

2. **Vector Storage** (Optional)
```sql
-- Enable vector extension
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE embeddings (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    content TEXT NOT NULL,
    embedding vector(1536),
    metadata JSONB
);

CREATE INDEX ON embeddings USING ivfflat (embedding vector_cosine_ops);
```

## Setup Process

1. **Database Creation**
   ```sql
   -- Create database
   CREATE DATABASE live_agent_studio;
   
   -- Enable extensions
   CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
   CREATE EXTENSION IF NOT EXISTS pgcrypto;
   ```

2. **User Setup**
   ```sql
   -- Create application user
   CREATE USER agent_user WITH PASSWORD 'your_password';
   
   -- Grant permissions
   GRANT CONNECT ON DATABASE live_agent_studio TO agent_user;
   GRANT USAGE ON SCHEMA public TO agent_user;
   GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO agent_user;
   ```

3. **Table Creation**
   - Run schema migrations
   - Create indexes
   - Set up permissions

4. **Environment Configuration**
   ```env
   DATABASE_URL=postgresql://user:password@host:port/dbname
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   ```

## Migrations

### Structure
```
migrations/
├── 0001_initial.sql
├── 0002_add_vector_support.sql
└── 0003_add_indexes.sql
```

### Running Migrations
```bash
# Using provided script
python tools/run_migrations.py

# Manual execution
psql -U username -d dbname -f migrations/0001_initial.sql
```

## Performance Optimization

1. **Indexing**
   - Session ID index
   - Timestamp index
   - Vector similarity index
   - JSON field index

2. **Connection Pooling**
   - PgBouncer setup
   - Connection limits
   - Pool sizing
   - Timeout configuration

3. **Query Optimization**
   - Efficient joins
   - Proper indexing
   - Query planning
   - Regular VACUUM

4. **Monitoring**
   - Query performance
   - Connection usage
   - Disk space
   - Cache hits

## Security

1. **Access Control**
   - Role-based access
   - Row-level security
   - Column encryption
   - Audit logging

2. **Backup Strategy**
   - Regular backups
   - Point-in-time recovery
   - Backup testing
   - Retention policy

## Troubleshooting

Common issues and solutions:
1. Connection problems
2. Performance issues
3. Migration failures
4. Permission errors

## Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Supabase Documentation](https://supabase.com/docs)
- [PgBouncer Documentation](https://www.pgbouncer.org/) 