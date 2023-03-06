from flask import Flask, render_template, Response
from flask import request, redirect
import cv2
import sys
import logging
import os

sys.path.append("../driver")
sys.path.append("../")
sys.path.append("../../")

import driver
from const_values import photo_series, camera_usb_port_front, camera_usb_port_left, camera_usb_port_up 

app = Flask(__name__, template_folder="templates")

cameras = {"front": driver.Camera(0), "left": driver.Camera(2)}

def get_template_for_response(result):
    if result == "OK":
        return render_template("result_ok.html")
    else:
        return render_template("result_fail.html")

def get_photo_name(id, type, series):
    return "#id:" + str(id) + "#type:" + type + "#series:" + str(series)

@app.route("/")
def menu():
    return render_template("admin.html")

@app.route('/video_feed_front')
def video_feed_front():
    return Response(cameras["front"].gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_left')
def video_feed_left():
    return Response(cameras["left"].gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_up')
def video_feed_up():
    return Response(cameras["front"].gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/add_element/front")
def add_element_front():
    return render_template("add_element.html", camera="front")

@app.route("/add_element/left")
def add_element_left():
    return render_template("add_element.html", camera="left")

@app.route("/add_element/up")
def add_element_up():
    return render_template("add_element.html", camera="up")

@app.route("/add_result", methods=["GET", "POST"])
def add_result():
    add_database = request.form.get("add")

    # TODO 
    # id = get_id()
    id = 0
    os.mkdir("../../photos/" + str(id))

    for number_series in range(photo_series):
        for type in cameras:
            cameras[type].make_photo(get_photo_name(id, type, number_series), id)
        # get_rotation()

    if add_database == "on":
        print("Adding element to catalogue")
        # add_to_catalogue

    result = "OK"
    return get_template_for_response(result)

@app.route("/train_model")
def train_model():
    return render_template("train_model.html")

@app.route("/train_model_result", methods=["GET", "POST"])
def train_model_result():
    result = "OK"
    return get_template_for_response(result)

@app.route("/stop_model")
def stop_model():
    return render_template("stop_model.html")

@app.route("/stop_model_result", methods=["GET", "POST"])
def stop_model_result():
    result = "OK"
    return get_template_for_response(result)

if __name__ == "__main__":
    run()
    