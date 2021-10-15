from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# 通过命令行执行一下命令：
# set FLASK_APP=hello
# flask run