import os
import pytest
import configparser
from datetime import datetime
from apis import APIs
from tests.helpers import Helpers
from utils.logger import LogGen
from apis import api_get, api_post, api_put, api_delete, api_file_upload, api_file_download

logger = LogGen.loggen()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{reports_dir}/report_{now}.html"


config = configparser.ConfigParser()
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.ini"))
config.read(config_path)


@pytest.fixture(scope="session")
def apis():
    """Setup: Initialize API session with authentication token"""
    if "Auth" not in config or "bearer_token" not in config["Auth"]:
        raise ValueError("ERROR: Missing [Auth] section or bearer_token in config.ini")

    auth_token = config["Auth"]["bearer_token"]

    session = {
        "get": lambda endpoint: api_get(auth_token, endpoint),
        "post": lambda endpoint, data: api_post(auth_token, endpoint, data),
        "put": lambda endpoint, data: api_put(auth_token, endpoint, data),
        "delete": lambda endpoint: api_delete(auth_token, endpoint),
        "file_upload": lambda: api_file_upload(),
        "file_download": lambda: api_file_download(),
    }

    logger.info("API session setup completed.")
    yield session

    # Teardown (if necessary)
    logger.info("API session teardown completed.")


@pytest.fixture(scope='session', autouse=True)
def auth_token():
    if "Auth" not in config:
        raise ValueError("Missing [Auth] section in config.ini")
    return config.get("Auth", "bearer_token")


@pytest.fixture(scope="module")
def apis(auth_token):
    logger.info("Creating APIs instance")
    return APIs(auth_token)


@pytest.fixture(scope="module")
def user_id(apis):
    logger.info("Fixture Auth Token & User ID")
    response = Helpers.post_user(apis)
    user_id = response[0]
    return user_id
