import pytest
import allure
from apis import APIs
from utils.logger import LogGen
from tests.helpers import Helpers
from utils.string_utils import generate_random_email

logger = LogGen.loggen()

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

@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
def test_get_users(apis):
    logger.info("Getting users......")
    json_str = Helpers.get_users(apis)
    logger.info(f"json GET response body: {json_str}")
    logger.info("Get user is done.....")

@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize(
    "user_data",
    [
        {"name": "John Automation Labs", "email": generate_random_email(), "gender": "male", "status": "active"}
    ],
)
@allure.severity(allure.severity_level.NORMAL)
def test_post_user(apis, user_data):
    logger.info(f"Adding the user: {user_data}......")
    user_id, json_str = Helpers.post_user(apis, user_data)
    logger.info(f"user id ===>> {user_id}")
    logger.info(f"json POST response body: {json_str}")
    logger.info("Post user is done.....")

@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize(
    "user_data",
    [
        {"name": "John API Automation Labs", "email": generate_random_email(), "gender": "male", "status": "inactive"}
    ],
)
@allure.severity(allure.severity_level.NORMAL)
def test_put_user(apis, user_id, user_data):
    logger.info(f"Updating the user: {user_data}......")
    json_str = Helpers.put_user(apis, user_id, user_data)
    logger.info(f"json PUT response body: {json_str}")
    logger.info("Update user is done.....")

@pytest.mark.high
@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
def test_delete_user(apis, user_id):
    logger.info("Deleting the user.....")
    Helpers.delete_user(apis, user_id)
    logger.info("Delete user is done.....")
    logger.info("End of API Testing")

@pytest.mark.low
@pytest.mark.file
@allure.severity(allure.severity_level.MINOR)
def test_upload_file(apis):
    logger.info("Uploading the file.......")
    Helpers.upload_file(apis)
    logger.info("Successfully uploaded the file")

@pytest.mark.low
@pytest.mark.file
@allure.severity(allure.severity_level.MINOR)
def test_download_file(apis):
    logger.info("Downloading the file.......")
    Helpers.download_file(apis)
    logger.info("Successfully downloaded the file")