from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.qrcode_creator_controller import QRCodeCreatorController


class QRCodeCreatorView:
    def validate_and_create(self, http_request: HttpRequest):
        qrcode_creator_controller = QRCodeCreatorController()

        body = http_request.body
        code = body["code"]

        formatted_response = qrcode_creator_controller.create(code)

        return HttpResponse(status_code=200, body=formatted_response)
