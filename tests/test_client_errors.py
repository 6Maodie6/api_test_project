import pytest
import requests
import logging


@pytest.mark.parametrize(
    "error_type",
    [
        requests.Timeout,
        requests.ConnectionError
    ]
)
def test_api_client_network_errors(
    api_client, monkeypatch, error_type, caplog
):
    def fake_request(self, *args, **kwargs):
        raise error_type("模拟网络异常")

    monkeypatch.setattr(
        requests.Session,
        "request",
        fake_request
    )

    # 让命名日志记录器的日志可以被 caplog 捕获
    monkeypatch.setattr("common.client.logger.propagate", True)
    caplog.set_level(logging.ERROR, logger="api_test")

    with pytest.raises(error_type, match="模拟网络异常"):
        api_client.get("/posts/1")

    # 验证日志中包含异常信息
    assert "模拟网络异常" in caplog.text
    assert "request failed" in caplog.text