from flask import Blueprint, render_template, request, redirect, url_for
from models.model import add_task, mostra_tasks

taskControler = Blueprint('taskController', __name__)

@taskControler.route("/")
def hello_world():
    return render_template("index.html")

@taskControler.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        add_task(task)
    return redirect(url_for('taskController.index'))