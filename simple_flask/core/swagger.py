from flask import Blueprint, send_from_directory, current_app

swagger_bp = Blueprint('swagger_endpoint', __name__)


@swagger_bp.route('/swagger.yaml')
def swagger_yaml():
    return send_from_directory(current_app.config['BASE_DIR'],
                               current_app.config['SWAGGER_CONFIG'])


@swagger_bp.route('/swagger-ui/<path:path>')
def swagger_ui(path):
    return send_from_directory(current_app.config['SWAGGER_UI'], path)


@swagger_bp.route('/swagger-ui')
def swagger_ui_index():
    return send_from_directory(current_app.config['SWAGGER_UI'], 'index.html')