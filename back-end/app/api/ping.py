from flask import jsonify
from app.api import bp 

@bp.route('/ping', methods=['GET'])
def ping():
    '''前端vue.js 用来测试与后端的flask api 联通性'''
    return jsonify('Pong!!!')