import json
import pytest
import allure
from utils.apis import APIs
from utils.helpers import generate_random_email

@pytest.fixture(scope="module")
def apis(auth_token):
    return APIs(auth_token)


@allure.severity(allure.severity_level.NORMAL)
def test_get_users(apis):
    response = apis.get("/public/v2/users")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body:", json_str)
    print("GET USER IS DONE.....")


@allure.severity(allure.severity_level.NORMAL)
def test_post_user(apis):
    user_data = {
        "name": "John Automation",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = apis.post("/public/v2/users/", user_data)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body:", json_str)
    assert response.status_code == 201
    user_id = json_data["id"]
    print("user id ===>> ", user_id)
    assert 'name' in json_data
    assert json_data['name'] == "John Automation"
    print("POST USER IS DONE.....")

@allure.severity(allure.severity_level.NORMAL)
@pytest.fixture(scope="module")
def user_id(apis):
    user_data = {
        "name": "John Automation",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = apis.post("/public/v2/users/", user_data)
    json_data = response.json()
    return json_data["id"]

@allure.severity(allure.severity_level.NORMAL)
def test_put_user(apis, user_id):
    user_data = {
    "name": "John Automation Labs",
    "email": generate_random_email(),
    "gender": "male",
    "status": "inactive"
}
    response = apis.put(f"/public/v2/users/{user_id}", user_data)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body:", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "John Automation Labs"
    print("UPDATE USER IS DONE.....")
    print("....=====================....")

@allure.severity(allure.severity_level.NORMAL)
def test_delete_user(apis, user_id):
    response = apis.delete(f"/public/v2/users/{user_id}")
    assert response.status_code == 204
    print("DELETE USER IS DONE.....")