from barcode import Code128
from barcode.writer import ImageWriter
from .path_handler import PathHandler


class BarcodeHandler:
    def create_barcode(self, code: str) -> str:
        path_handler = PathHandler()
        tag = Code128(code, writer=ImageWriter())
        path_from_tag = f"{path_handler.sanatize_name(code)}"
        print(path_from_tag)
        tag.save(path_from_tag)

        return path_from_tag
