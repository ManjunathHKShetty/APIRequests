import pytest
import allure
from libs import api_cookies
from utils.logger import LogGen
from tests.helpers import Helpers
from utils.string_utils import generate_random_email


logger = LogGen.loggen()


@pytest.mark.high
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
        {"name": "John API Automation Labs", "email": generate_random_email(), "gender": "male", "status": "inactive"},
        {"name": "John API Automation Labs", "email": generate_random_email(), "gender": "female", "status": "active"}
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
    try:
        logger.info("Downloading the file...")
        Helpers.download_file(apis)
        logger.info("File downloaded successfully.")
    except AssertionError as ae:
        logger.error(f"Assertion failed during file download: {ae}")
        pytest.fail(f"Test failed due to assertion error: {ae}")
    except Exception as e:
        logger.exception("Unexpected error during file download.")
        pytest.fail(f"Test failed due to unexpected error: {e}")


@pytest.mark.high
@pytest.mark.api
@pytest.mark.parametrize("cookies", [{"location": "New York"}])
@allure.severity(allure.severity_level.MINOR)
def test_cookie(cookies):
    logger.info("Getting Cookies...")
    Helpers.get_cookies(api_cookies, cookies)
    logger.info("Successfully generated the cookies")
