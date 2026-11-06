import json
from pathlib import Path

import pytest


# =========================
# 1. 加载测试数据
# =========================

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "post_cases.json"
)

with open(DATA_FILE, "r", encoding="utf-8") as file:
    POST_CASES = json.load(file)


# =========================
# 2. 公共异常响应校验
# =========================

def assert_not_found_response(response):
    """校验资源不存在时的响应"""
    assert response.status_code == 404
    assert response.json() == {}


# =========================
# 3. 文章接口测试
# =========================

def test_get_all_post(api_client):
    response = api_client.get("/posts")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.parametrize("case", POST_CASES)
def test_get_post_by_id(api_client, case):
    response = api_client.get(f"/posts/{case['post_id']}")

    assert response.status_code == case["expected_status"]

    data = response.json()

    # 字段存在性校验
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

    # 字段类型校验
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)

    # 字段值校验
    assert data["id"] == case["post_id"]

    # 非空校验
    assert data["title"].strip()
    assert data["body"].strip()


def test_create_post(api_client):
    payload = {
        "title": "API automation test",
        "body": "Test post creation",
        "userId": 1
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    assert "id" in data
    assert isinstance(data["id"], int)


# =========================
# 4. 用户嵌套 JSON 测试
# =========================

def test_get_user_nested_fields(api_client):
    response = api_client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    # 第一层字段
    assert "id" in data
    assert data["id"] == 1

    assert "address" in data
    assert isinstance(data["address"], dict)

    # 第二层字段
    address = data["address"]

    assert "city" in address
    assert isinstance(address["city"], str)
    assert address["city"].strip()

    assert "geo" in address
    assert isinstance(address["geo"], dict)

    # 第三层字段
    geo = address["geo"]

    assert "lat" in geo
    assert "lng" in geo

    assert isinstance(geo["lat"], str)
    assert isinstance(geo["lng"], str)


# =========================
# 5. 正常边界测试
# =========================

@pytest.mark.parametrize("post_id", [1, 100])
def test_get_post_valid_boundary(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == post_id


# =========================
# 6. 异常输入测试
# =========================

@pytest.mark.parametrize(
    "post_id",
    [0, -1, 101, "abc"]
)
def test_get_post_invalid_boundary(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")

    assert_not_found_response(response)


# =========================
# 7. 不存在资源的异常响应测试
# =========================

def test_get_nonexistent_post(api_client):
    response = api_client.get("/posts/999999")

    assert_not_found_response(response)



