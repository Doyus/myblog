from flask import Blueprint

bp = Blueprint('api', __name__)

# ping也会导入 bp ， 防止循环导入
from app.api  import ping 