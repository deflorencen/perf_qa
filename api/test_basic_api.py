import pytest

@pytest.fixture
def obj_id(obj_api):
    payload = {
        "name": "Google Pixel 6 Pro",
        "data": {"color": "Cloudy White", "capacity": "128 GB"}
    }
    response = obj_api.create_object(payload)
    data = response.json()
    yield data["id"]
    obj_api.delete_object(data["id"])


def test_get_data_from_json(obj_api, obj_id):
    response = obj_api.create_object(payload={
        "name": "Google Pixel 6 Pro",
        "data": {"color": "Cloudy White", "capacity": "128 GB"}
    })
    resp_data = response.json()
    print(resp_data)

    assert response.status == 200

def test_delete_data(obj_api, obj_id):
    response = obj_api.delete_object(obj_id)
    assert response.status == 200
    check_delete = obj_api.get_object(obj_id)
    assert check_delete.status == 404


def test_get_data_from_id(obj_api, obj_id):
    response = obj_api.get_object(obj_id)
    resp_json = response.json()
    assert response.status == 200
    assert resp_json["id"] == obj_id