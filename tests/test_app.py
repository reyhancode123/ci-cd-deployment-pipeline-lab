from app.main import get_app_info


def test_app_name():
    assert get_app_info()["name"] == "CI/CD Deployment Pipeline Lab"

def test_default_version():
    assert get_app_info()["version"] == "1.0.0"

def test_app_status():
    assert get_app_info()["status"] == "healthy"
