from flask import Blueprint

bp = Blueprint('api', __name__)
# 创建蓝图

#写在后面是为了防止循环导入，ping.py文件也会导入bp
from app.api import ping
