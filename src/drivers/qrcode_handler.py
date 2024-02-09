from qrcode import make
from .path_handler import PathHandler


class QRcodeHandler:
    def create_qrcode(self, code: str) -> str:
        path_handler = PathHandler()
        img = make(code)
        # essa lib não adiciona extensões por padrão
        img_path = f"{path_handler.sanatize_name(code)}.png"
        print(img_path)
        img.save(img_path)

        return img_path
