from flask import Blueprint, Flask

from mwdb.core.rate_limit import limiter

from .service import Service

app = Flask(__name__, static_folder=None)
api_blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Service(app, api_blueprint)
app.register_blueprint(api_blueprint)

limiter.init_app(app)
