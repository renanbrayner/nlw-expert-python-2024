from typing import Dict
from src.drivers.qrcode_handler import QRcodeHandler


class QRCodeCreatorController:
    def create(self, code: str) -> Dict:
        path_from_tag = self.__create_qrcode(code)
        formatted_response = self.__format_response(path_from_tag)
        return formatted_response

    def __create_qrcode(self, code: str) -> str:
        qrcode_handler = QRcodeHandler()
        path_from_tag = qrcode_handler.create_qrcode(code)

        return path_from_tag

    def __format_response(self, path_from_tag: str) -> Dict:
        return {
            "data": {
                "type": "QR Code Image",
                "count": 1,
                "path": path_from_tag
            }
        }
