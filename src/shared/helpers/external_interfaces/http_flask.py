import json
from flask import request, make_response

from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class FlaskHttpResponse(HttpResponse):
    """
    A class to represent an HTTP response for Flask.
    """
    status_code: int = 200
    body: any = {"message": "No response"}
    headers: dict = {"Content-Type": "application/json"}

    def __init__(self, body: any = None, status_code: int = None, headers: dict = None, **kwargs) -> None:
        """
        Constructor for HttpResponse.
        Args:
            body: The body of the response. Can be a string or a dict.
            status_code: The status code of the response. Defaults to 200.
            headers: The headers of the response. Defaults to {"Content-Type": "application/json"}.
            **kwargs: Configuration of the HTTP response. Possible values: add_default_cors_headers (default is True)
        """
        _body = body or FlaskHttpResponse.body
        _headers = headers or FlaskHttpResponse.headers

        _status_code = status_code or FlaskHttpResponse.status_code

        if kwargs.get("add_default_cors_headers", True):
            _headers.update({"Access-Control-Allow-Origin": "*"})

        self.body = _body
        self.headers = _headers
        self.status_code = _status_code

    def to_flask_response(self):
        """
        Returns a Flask response object.
        """
        response = make_response(json.dumps(self.body), self.status_code)
        for key, value in self.headers.items():
            response.headers[key] = value
        return response

    def __repr__(self):
        return (
            f"""HttpResponse (status_code={self.status_code}, body={
                self.body}, headers={self.headers})"""
        )


class FlaskHttpRequest(HttpRequest):
    """
    A class to represent an HTTP request for Flask.
    """

    def __init__(self, flask_request=None) -> None:
        """
        Constructor for HttpRequest.
        """
        if flask_request is None:
            flask_request = request

        self.method = flask_request.method
        self.path = flask_request.path
        self.headers = flask_request.headers
        self.query_params = flask_request.args
        self.body = flask_request.get_json(silent=True)

    def get_data(self):
        """
        Returns the data of the request.
        """
        return {
            "method": self.method,
            "path": self.path,
            "headers": dict(self.headers),
            "query_params": self.query_params,
            "body": self.body
        }

    @property
    def data(self) -> dict:
        return self.get_data().get("body")

    @data.setter
    def data(self, value: dict):
        self._data = value

    def __repr__(self):
        return (
            f"""HttpRequest (method={self.method}, path={self.path}, headers={
                self.headers}, query_params={self.query_params}, body={self.body})"""
        )


class HttpResponseRedirect(HttpResponse):
    def __init__(self, location: str) -> None:
        super().__init__(status_code=302, headers={"Location": location})

    def to_flask_response(self):
        """
        Returns a Flask response object for redirection.
        """
        response = make_response("", self.status_code)
        response.headers["Location"] = self.headers["Location"]
        return response
