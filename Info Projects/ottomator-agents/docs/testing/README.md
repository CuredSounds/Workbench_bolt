# Testing Procedures Guide

This guide covers testing methodologies and procedures for Live Agent Studio agents.

## Testing Types

### 1. Unit Testing
```python
# Example test using pytest
import pytest
from app.agent import process_query

def test_process_query():
    query = "Hello, agent!"
    result = process_query(query)
    assert result.success == True
    assert isinstance(result.response, str)
```

### 2. Integration Testing
```python
# Example integration test
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_agent_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/agent",
            json={
                "query": "Test query",
                "user_id": "test_user",
                "request_id": "test_request",
                "session_id": "test_session"
            }
        )
        assert response.status_code == 200
        assert response.json()["success"] == True
```

### 3. Load Testing
```python
# Using locust for load testing
from locust import HttpUser, task, between

class AgentUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def query_agent(self):
        self.client.post(
            "/api/agent",
            json={
                "query": "Load test query",
                "user_id": "load_test_user",
                "request_id": "load_test_request",
                "session_id": "load_test_session"
            }
        )
```

## Test Environment Setup

1. **Local Testing Environment**
```bash
# Set up test database
docker-compose -f docker-compose.test.yml up -d

# Install test dependencies
pip install -r requirements.test.txt

# Run tests
pytest tests/
```

2. **CI/CD Pipeline**
```yaml
# GitHub Actions example
name: Test Agent

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements.test.txt
      - name: Run tests
        run: pytest tests/
```

## Test Categories

### 1. Functional Testing
- API endpoint testing
- Request validation
- Response format
- Error handling
- Edge cases

### 2. Performance Testing
- Response time
- Concurrent users
- Resource usage
- Database performance
- Memory leaks

### 3. Security Testing
- Authentication
- Input validation
- SQL injection
- XSS protection
- Rate limiting

### 4. Integration Testing
- Database operations
- External APIs
- Message queues
- File operations
- Caching

## Test Data Management

1. **Fixtures**
```python
# pytest fixtures
@pytest.fixture
def test_data():
    return {
        "query": "Test query",
        "user_id": "test_user",
        "request_id": "test_request",
        "session_id": "test_session"
    }

@pytest.fixture
async def test_db():
    # Set up test database
    await setup_test_db()
    yield
    # Clean up
    await cleanup_test_db()
```

2. **Mock Data**
```python
# Mock external services
@pytest.fixture
def mock_openai(mocker):
    return mocker.patch('app.ai.openai.Completion.create')
```

## Continuous Testing

1. **Automated Testing**
- Pre-commit hooks
- CI/CD pipeline
- Scheduled tests
- Coverage reports

2. **Monitoring**
- Error tracking
- Performance metrics
- Usage statistics
- Alert thresholds

## Best Practices

1. **Test Organization**
```
tests/
├── unit/
│   ├── test_agent.py
│   └── test_database.py
├── integration/
│   ├── test_api.py
│   └── test_external.py
├── performance/
│   └── test_load.py
└── conftest.py
```

2. **Code Coverage**
```bash
# Run tests with coverage
pytest --cov=app tests/

# Generate coverage report
coverage html
```

## Troubleshooting

Common testing issues:
1. Flaky tests
2. Database conflicts
3. Race conditions
4. Resource leaks

## Resources

- [Pytest Documentation](https://docs.pytest.org)
- [Locust Documentation](https://locust.io)
- [Coverage.py](https://coverage.readthedocs.io)
- [GitHub Actions](https://docs.github.com/en/actions) 