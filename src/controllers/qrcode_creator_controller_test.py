from unittest.mock import patch
from src.drivers.qrcode_handler import QRcodeHandler
from .qrcode_creator_controller import QRCodeCreatorController


@patch.object(QRcodeHandler, "create_qrcode")
def test_create(mock_create_qrcode):
    mock_value = "image_path"
    mock_create_qrcode.return_value = f'{mock_value}.png'
    tag_creator_controller = QRCodeCreatorController()

    result = tag_creator_controller.create(mock_value)

    print(f"\n{result}")

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "QR Code Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f"{mock_value}.png"
