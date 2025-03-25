import requests
import constants


def api_get(auth_token, endpoint):
    headers = {"Authorization": auth_token, "Content-Type": "application/json"}
    url = f"{constants.BASE_URL}/{endpoint}"
    return requests.get(url, headers=headers)

def api_post(auth_token, endpoint, user_data):
    headers = {"Authorization": auth_token, "Content-Type": "application/json"}
    url = f"{constants.BASE_URL}/{endpoint}"
    return requests.post(url, json=user_data, headers=headers)

def api_put(auth_token, endpoint, user_data):
    headers = {"Authorization": auth_token, "Content-Type": "application/json"}
    url = f"{constants.BASE_URL}/{endpoint}"
    response = requests.put(url, json=user_data, headers=headers)
    return response

def api_delete(auth_token, endpoint):
    headers = {"Authorization": auth_token, "Content-Type": "application/json"}
    url = f"{constants.BASE_URL}/{endpoint}"
    response = requests.delete(url, headers=headers)
    return response


def api_file_upload():
    url = constants.UPLOAD_URL
    file_path = r"C:\Users\Ifomet\Desktop\students.json"
    with open(file_path, "rb") as file:
        files = {"file": ("students.json", file, "application/json")}
        response = requests.post(url, files=files)
    return response

def api_file_download():
    url = constants.DOWNLOAD_URL
    file_path_d = r"C:\Users\Ifomet\Desktop\downloaded_file.bin"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(file_path_d, "wb") as file:
            file.write(response.content)
        return file_path_d, response
    else:
        raise ValueError(f"Download failed: {response.status_code}")