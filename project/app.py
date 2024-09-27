from flask import Flask, Blueprint
from controllers.controller import taskControler

app = Flask(__name__)

app.register_blueprint(taskControler)

if __name__ == "__main__":
    app.run(debug=True)

