import os
from flask import Flask, request
from src.modules.create_alert.app.create_alert_presenter import create_alert_presenter
from src.modules.get_actual_status_battery.app.get_actual_status_battery_presenter import get_actual_status_battery_presenter
from src.modules.get_all_alerts.app.get_all_alerts_presenter import get_all_alerts_presenter
from src.shared.helpers.external_interfaces.http_flask import FlaskHttpRequest, FlaskHttpResponse

app = Flask(__name__)


@app.route('/', methods=['GET'])
def health_check():
    return "Solar System API is running"


@app.route('/get-all-alerts', methods=['GET'])
def get_all_alerts():
    flask_request = FlaskHttpRequest(request)
    res = get_all_alerts_presenter(flask_request)
    return FlaskHttpResponse(body=res.body, status_code=res.status_code).to_flask_response()


@app.route('/create-alert', methods=['POST'])
def create_alert():
    flask_request = FlaskHttpRequest(request)
    res = create_alert_presenter(flask_request)
    return FlaskHttpResponse(body=res.body, status_code=res.status_code).to_flask_response()


@app.route('/get-actual-status-battery', methods=['POST'])
def get_actual_status_battery():
    flask_request = FlaskHttpRequest(request)
    res = get_actual_status_battery_presenter(flask_request)
    return FlaskHttpResponse(body=res.body, status_code=res.status_code).to_flask_response()


def solar_system_api(request):
    with app.request_context(request.environ):
        try:
            rv = app.preprocess_request()
            if rv is None:
                rv = app.dispatch_request()
        except Exception as e:
            rv = app.handle_user_exception(e)
        response = app.make_response(rv)
        return app.process_response(response)


if os.getenv('ENV') == 'DEV':
    if __name__ == '__main__':
        print('Running in DEV mode')
        app.run(debug=True)
