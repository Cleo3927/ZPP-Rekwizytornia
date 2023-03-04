from flask import Flask, render_template, Response
from flask import request, redirect
import cv2
import sys

sys.path.append("../driver")
sys.path.append("../")
sys.path.append("../../")

import driver
from const_values import photo_series, camera_usb_port_front, camera_usb_port_left, camera_usb_port_up 

app = Flask(__name__, template_folder="templates")

camera = driver.Camera(0)

def get_template_for_response(result):
    if result == "OK":
        return render_template("result_ok.html")
    else:
        return render_template("result_fail.html")

@app.route("/")
def menu():
    return render_template("admin.html")

@app.route('/video_feed')
def video_feed():
    return Response(camera.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/add_element")
def add_element():
    return render_template("add_element.html")

@app.route("/add_result", methods=["GET", "POST"])
def add_result():
    add_database = request.form.get("add")
    result = "OK"

    if add_database == "on":
        print("adding to catalogue")

    camera.make_photo("nazwa")
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
    