from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.views.qrcode_creator_view import QRCodeCreatorView

from src.errors.error_handler import handle_errors

from src.validators.tag_creator_validator import tag_creator_validator
from src.validators.qrcode_creator_validator import qrcode_creator_validator

tags_routes_bp = Blueprint("tags_routes", __name__)
qrcode_routes_bg = Blueprint("qrcode_routes", __name__)


@qrcode_routes_bg.route("/create_qrcode", methods=["POST"])
def create_qrcode():
    response = None
    try:
        qrcode_creator_validator(request)
        qrcode_creator_view = QRCodeCreatorView()

        http_request = HttpRequest(body=request.json)
        response = qrcode_creator_view.validate_and_create(http_request)
    except Exception as exception:
        response = handle_errors(exception)

    return jsonify(response.body), response.status_code


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags():
    response = None
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
        response = handle_errors(exception)

    return jsonify(response.body), response.status_code
