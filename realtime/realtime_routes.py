# In realtime_routes.py
from flask import Blueprint, render_template

realtime_bp = Blueprint('realtime', __name__)

@realtime_bp.route('/')
def realtime():
    return render_template('realtime.html')
