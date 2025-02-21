import requests
import json
import string
import random

#base url:
base_url = "https://gorest.co.in"

#Auth token:
auth_token = "Bearer 62b7d2d686e7bc8f69f7ff576e688a843e50361834c1c43655b4ad9c837166d4"

def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = "".join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email



def get_request():
    url = base_url + "/public/v2/users/"
    print("GET url:" + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body:", json_str)
    print("GET USER IS DONE.....")
    print("....=====================....")


def post_request():
    url = base_url + "/public/v2/users/"
    print("POST url:" + url)
    headers = {"Authorization": auth_token}
    data = {
    "name": "John Automation",
    "email": generate_random_email(),
    "gender": "male",
    "status": "active"
}
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body:", json_str)
    assert response.status_code == 201
    user_id = json_data["id"]
    print("user id ===>> ", user_id)
    assert 'name' in json_data
    assert json_data['name'] == "John Automation"
    return user_id

def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url:" + url)
    headers = {"Authorization": auth_token}
    data = {
    "name": "John Automation Labs",
    "email": generate_random_email(),
    "gender": "male",
    "status": "inactive"
}
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body:", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "John Automation Labs"
    print("PUT USER IS DONE.....")
    print("....=====================....")

def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("DELETE USER IS DONE.....")




get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)