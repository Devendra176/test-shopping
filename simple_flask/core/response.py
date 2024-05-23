from flask import Response, json


class CustomResponse(Response):
    @classmethod
    def success(cls, data=None, status=200):
        return cls(json.dumps(data), status=status, mimetype='application/json')

    @classmethod
    def error(cls, message="Error", errors=None, status=400):
        payload = {
            "status": "error",
            "message": message,
        }
        return cls(json.dumps(payload), status=status, mimetype='application/json')
