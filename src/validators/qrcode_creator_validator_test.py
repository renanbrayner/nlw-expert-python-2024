from src.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)
from .qrcode_creator_validator import qrcode_creator_validator


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_creator_validator():
    req = MockRequest(json={"code": "123-456-789"})
    qrcode_creator_validator(req)


def test_tag_creator_validator_with_error():
    req = MockRequest(json={"code": 123456789})

    try:
        qrcode_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)


def test_tag_creator_validator_with_old_key():
    req = MockRequest(json={"productCode": "123-456-789"})

    try:
        qrcode_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)


def test_tag_creator_validator_with_original_project_key():
    req = MockRequest(json={"product_code": "123-456-789"})

    try:
        qrcode_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
