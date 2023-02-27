from flask import Flask, render_template, Response
from flask import request, redirect
import cv2
import sys

sys.path.append("../database")
sys.path.append("../driver")

import driver
import database

app = Flask(__name__, template_folder="templates")

database = database.Database()
camera = driver.Camera(0)

def get_template_for_response(result):
    print(result)
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
    name = request.form.get("name")
    count = request.form.get("count")
    price = request.form.get("price")
    result = "OK"
    
    camera.make_photo(name)
    number = database.get_index()
    return get_template_for_response(result)

if __name__ == "__main__":
    run()
    
