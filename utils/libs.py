def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"

def assert_response_contains_field(response_json, field_name):
    assert field_name in response_json, f"Response JSON does not contain the field '{field_name}'"

def assert_field_value(response_json, field_name, expected_value):
    assert response_json.get(field_name) == expected_value, (
        f"Expected '{field_name}' to be '{expected_value}', but got '{response_json.get(field_name)}'"
    )
