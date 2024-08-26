import os
from flask import Flask, request
from src.modules.create_alert.app.create_alert_presenter import create_alert_presenter
from src.modules.get_actual_status_battery.app.get_actual_status_battery_presenter import get_actual_status_battery_presenter
from src.modules.get_all_alerts.app.get_all_alerts_presenter import get_all_alerts_presenter
from src.modules.get_solar_panel_production.app.get_solar_panel_production_presenter import get_solar_panel_production_presenter
from src.modules.get_status_battery_history.app.get_battery_status_history_presenter import get_battery_status_history_presenter
from src.shared.helpers.external_interfaces.http_flask import FlaskHttpRequest, FlaskHttpResponse

app = Flask(__name__)


@app.route('/', methods=['GET'])
def health_check():
    return "Solar System API is running"


def flask_route(request, presenter):
    flask_request = FlaskHttpRequest(request)
    res = presenter(flask_request)
    return FlaskHttpResponse(body=res.body, status_code=res.status_code).to_flask_response()


@app.route('/get-all-alerts', methods=['GET'])
def get_all_alerts():
    return flask_route(request, get_all_alerts_presenter)


@app.route('/create-alert', methods=['POST'])
def create_alert():
    return flask_route(request, create_alert_presenter)


@app.route('/get-actual-status-battery', methods=['POST', 'GET'])
def get_actual_status_battery():
    return flask_route(request, get_actual_status_battery_presenter)


@app.route('/get-solar-panel-production', methods=['POST', 'GET'])
def get_solar_panel_production():
    return flask_route(request, get_solar_panel_production_presenter)


@app.route('/get-battery-status-history', methods=['POST', 'GET'])
def get_status_battery_history():
    return flask_route(request, get_battery_status_history_presenter)


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
