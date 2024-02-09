from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:
    """
    responsable for interecting with hTPP
    """

    def validate_and_create(self, http_request: HttpRequest):
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body["productCode"]

        #  lógica de regra de negócio
        formatted_response = tag_creator_controller.create(product_code)

        # retorno htpp
        return HttpResponse(status_code=200, body=formatted_response)
