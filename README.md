# CI/CD Deployment Pipeline Lab

A lightweight CI/CD pipeline project demonstrating automated code quality checks, unit testing, Docker image builds, container integration testing, and deployment using Docker Compose.

## Project Features

- Automated linting with Ruff
- Automated unit testing with pytest
- Docker image build automation
- HTTP health endpoint integration testing
- Non-root Docker container execution
- Docker Compose deployment
- Automated container health monitoring

## Technology Stack

- Python 3.12
- pytest
- Ruff
- Docker
- Docker Compose
- GitHub Actions

## CI Pipeline

The GitHub Actions workflow contains three jobs:

1. **Lint:** checks Python code using Ruff.
2. **Test:** executes application unit tests using pytest.
3. **Docker Build and Integration:** builds the Docker image, verifies the HTTP health endpoint, and checks that the container runs as a non-root user.

The Docker integration job runs after linting and unit tests succeed.

## Application Endpoints

| Endpoint | Description | Expected Response |
|---|---|---|
| `/` | Application information | HTTP 200 |
| `/health` | Application health check | HTTP 200 |
| Other paths | Not found | HTTP 404 |

## Run Locally

Build and start the application:

```bash
docker compose up --build -d
```

Check application health:

```bash
curl http://127.0.0.1:18002/health
```

Check container status:

```bash
docker compose ps
```

Stop the application:

```bash
docker compose down
```

## Run Tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run unit tests:

```bash
python -m pytest -v
```

Run lint checks:

```bash
ruff check app tests
```

## Docker Security

The application container runs as a dedicated non-root user with UID 10001. Docker Compose also configures an HTTP healthcheck to monitor application availability.

## Project Structure

```text
app/                    Python application and HTTP server
tests/                  Application unit tests
.github/workflows/      GitHub Actions CI workflow
Dockerfile              Application container definition
docker-compose.yml      Local deployment configuration
pyproject.toml          Ruff configuration
requirements-dev.txt    Development dependencies
```
