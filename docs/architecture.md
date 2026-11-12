# CI/CD Deployment Pipeline Architecture

## Overview

This project automates code validation, testing, Docker image creation, and container deployment.

## CI/CD Workflow

```mermaid
flowchart TD
    A[Developer Push or Pull Request] --> B[GitHub Actions]
    B --> C[Ruff Linting]
    B --> D[Pytest Unit Tests]
    C --> E{Validation Passed?}
    D --> E
    E -->|Yes| F[Docker Image Build]
    F --> G[Container Integration Test]
    G --> H[HTTP Health Check]
    G --> I[Non-root User Verification]
    H --> J[CI Result]
    I --> J
    E -->|No| K[Pipeline Failed]
```

## Deployment Architecture

```mermaid
flowchart LR
    A[Host Machine] --> B[Docker Compose]
    B --> C[Application Container]
    C --> D[Python HTTP Server]
    E[HTTP Client] -->|Port 18002| C
    F[Docker Healthcheck] -->|Port 8000| C
```

## Security

- Application runs as non-root user `appuser` with UID 10001.
- Application port is published on localhost only.
- Docker healthcheck monitors the HTTP health endpoint.

## CI Pipeline Jobs

- **Lint:** validates Python code using Ruff.
- **Test:** runs unit tests using pytest.
- **Docker Build:** creates the application image.
- **Integration Test:** verifies HTTP health and non-root execution.
