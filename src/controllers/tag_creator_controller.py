from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler


class TagCreatorController:
    def create(self, code: str) -> Dict:
        path_from_tag = self.__create_tag(code)
        formatted_response = self.__format_response(path_from_tag)
        return formatted_response

    def __create_tag(self, code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(code)

        return path_from_tag

    def __format_response(self, path_from_tag: str) -> Dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f"{path_from_tag}.png"
            }
        }
