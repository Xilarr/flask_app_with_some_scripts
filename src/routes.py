from flask import request
from flask import render_template

from src import app
from src import report
from src.build_data import build_drivers_data, find_driver
from src.config import FOLDER_PATH


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/report/')
def common_statistics():
    return render_template("order.html", time_report=report.build_report(FOLDER_PATH))


@app.route('/report/drivers/', methods=['GET'])
def drivers_statistics():

    args = request.args
    order = args.get('order')
    driver_id = args.get('driver_id')
    if driver_id:
        driver_id = driver_id.upper()
    abb_dict = build_drivers_data()

    if not order and not driver_id:
        result = render_template('drivers_list.html', driver_keys=abb_dict.keys(), drivers_dict=abb_dict)

    elif order == 'asc':
        result = render_template("order.html", time_report=report.build_report(FOLDER_PATH))
    elif order == 'desc':
        result = render_template("order.html", time_report=(reversed(report.build_report(FOLDER_PATH))))

    elif driver_id in abb_dict.keys():  # if driver_id == None,driver_id.upper() raise an err.
        driver_dict = find_driver(abb_dict.get(driver_id))
        result = render_template("driver_stats.html", driver_report=driver_dict)
    else:
        result = 'something'

    return result
