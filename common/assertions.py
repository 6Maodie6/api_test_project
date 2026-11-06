
def assert_status_code(response, expected_code):
    """
    检查接口响应状态码
    """
    actual_code = response.status_code

    assert actual_code == expected_code, (
        f"状态码错误，预期：{expected_code}，实际：{actual_code}"
    )


def assert_json_field(response, field, expected_value):
    """
    检查响应 JSON 中指定字段的值
    """
    result = response.json()

    assert field in result, f"响应中缺少字段：{field}"

    actual_value = result[field]

    assert actual_value == expected_value, (
        f"字段 {field} 校验失败，"
        f"预期：{expected_value}，实际：{actual_value}"
    )
