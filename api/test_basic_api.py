import pytest

@pytest.fixture
def obj_id(obj_api):
    payload = {
        "name": "Google Pixel 6 Pro",
        "data": {"color": "Cloudy White", "capacity": "128 GB"}
    }
    response = obj_api.create_object(payload)
    assert response.status == 200
    data = response.json()
    yield data["id"]
    obj_api.delete_object(data["id"])


def test_get_data_from_json(obj_api):
    payload = {
        "name": "Google Pixel 6 Pro",
        "data": {"color": "Cloudy White", "capacity": "128 GB"}
    }
    response = obj_api.create_object(payload)
    resp_data = response.json()

    assert response.status == 200
    assert resp_data["name"] == payload["name"]
    assert resp_data["data"] == payload["data"]


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


def test_patch_data(obj_api, obj_id):

    patch_payload = {
        "name": "Google Pixel 6 Pro - Updated",
        "data": {"color": "Stormy Black", "capacity": "128 GB", "RAM": "12 GB"}
    }
    response = obj_api.patch_object(obj_id, patch_payload)
    assert response.status == 200

    resp_json = response.json()
    assert resp_json["name"] == "Google Pixel 6 Pro - Updated"
    assert resp_json["data"]["color"] == "Stormy Black"
    assert resp_json["data"]["capacity"] == "128 GB"
    assert resp_json["data"]["RAM"] == "12 GB"