from flask import Flask, render_template
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://edf04e6fd4ea4abcb569d0af006c7313@o375751.ingest.sentry.io/5195705",
    integrations=[FlaskIntegration()]
)

application = Flask(__name__)


@application.route('/')
def index():
    return render_template("index.html")


@application.route('/restaurantes')
def restaurants():
    return render_template("restaurantes.html")


@application.route('/cidades')
def cities():
    return render_template("cidades.html")
