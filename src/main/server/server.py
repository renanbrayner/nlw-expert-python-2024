from flask import Flask
from src.main.routes.routes import tags_routes_bp
from src.main.routes.routes import qrcode_routes_bg

app = Flask(__name__)

app.register_blueprint(tags_routes_bp)
app.register_blueprint(qrcode_routes_bg)
