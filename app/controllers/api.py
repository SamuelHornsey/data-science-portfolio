from flask import Blueprint, request, jsonify

mod_api = Blueprint('mod_api', __name__, url_prefix='/api')

from app.lib.analyse import run_model

@mod_api.route('/')
def api():
    return jsonify({'api': 'api'})

@mod_api.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    task = run_model.delay(data)

    url = '/api/status/' + task.id

    return jsonify({}), 202, {'Location': url}

@mod_api.route('/status/<string:id>')
def status(id):
    task = run_model.AsyncResult(id)
    if task.state == 'PENDING':
        return jsonify({ 'status': task.state })
    elif task.state == 'SUCCESS':
        return jsonify({ 'status': task.state, 'result': task.info})