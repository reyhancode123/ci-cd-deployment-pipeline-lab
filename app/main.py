import os


def get_app_info():
    return {
        "name": "CI/CD Deployment Pipeline Lab",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "status": "healthy"
    }
