import allure
from common.assertions import (
    assert_status_code,
    assert_json_field
)


@allure.feature("文章管理模块")
@allure.story("创建文章")
@allure.title("创建文章并验证响应数据")
def test_create_post_and_validate_response(api_client):
    payload = {
        "title": "接口自动化测试",
        "body": "这是一次 POST 接口测试",
        "userId": 1
    }

    response = api_client.post("/posts", json=payload)

    assert_status_code(response, 201)

    assert_json_field(response, "title", payload["title"])
    assert_json_field(response, "body", payload["body"])
    assert_json_field(response, "userId", payload["userId"])

    result = response.json()
    assert "id" in result
    assert result["id"] > 0




def test_create_post_without_title(api_client):
    payload = {
        "body": "没有标题的文章",
        "userId": 1
    }

    response = api_client.post("/posts", json=payload)

    # JSONPlaceholder 是模拟服务，
    # 不会真正执行业务字段校验
    assert response.status_code == 201
    assert response.json()["body"] == payload["body"]
    assert "title" not in response.json()
