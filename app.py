from flask import Flask, url_for, send_file

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/images")
def provide_images():
    image_path = "static/fire.jpg"
    return send_file(image_path, mimetype='image/jpg')