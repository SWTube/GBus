from flask import Flask, render_template, url_for,Blueprint
from werkzeug.utils import redirect

bp = Blueprint('main',__name__,url_prefix='/')


@bp.route('/')
def index():
    info_message = "정류장을 클릭하여 버스 도착 정보를 확인하세요."
    return render_template('buspage/bus_main.html', info_message=info_message)

@bp.route('/busstop/<id>/')
def bus_stop(id):
    info_message = f"{id} 정류장 버스 도착 정보입니다."
    return render_template('buspage/bus_info/bus_info.html', info_message=info_message)




