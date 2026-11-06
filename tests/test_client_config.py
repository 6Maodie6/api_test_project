import pytest
import requests


def test_default_timeout(api_client, monkeypatch):
    captured = {}

    def fake_request(self, *args, **kwargs):
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(
        requests.Session,
        "request",
        fake_request
    )

    api_client.get("/posts/1")

    assert captured["timeout"] == 10


def test_custom_timeout(api_client, monkeypatch):
    captured = {}

    def fake_request(self, *args, **kwargs):
        captured.update(kwargs)
        return requests.Response()

    monkeypatch.setattr(
        requests.Session,
        "request",
        fake_request
    )

    api_client.get("/posts/1", timeout=3)

    assert captured["timeout"] == 3



def test_api_client_close(api_client, monkeypatch):
    called = {"closed": False}

    def fake_close():
        called["closed"] = True

    monkeypatch.setattr(
        api_client.session,
        "close",
        fake_close
    )

    api_client.close()

    assert called["closed"] is True