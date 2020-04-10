from flask import Flask, render_template
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://edf04e6fd4ea4abcb569d0af006c7313@o375751.ingest.sentry.io/5195705",
    integrations=[FlaskIntegration()]
)

application = Flask(__name__)


@application.route('/')
def hello_world():
    return render_template("index.html")
