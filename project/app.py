from flask import Flask, request, session, render_template, flash, redirect, url_for
from controllers.controller import loginController
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'chave' 
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/submit', methods=['POST'])
def submit():
    flash('Formulário enviado com sucesso!', 'success') 
    return redirect(url_for('dashboard'))  

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.before_request
def log_request_info():
    print(f'Método: {request.method}, URL: {request.url}')

app.register_blueprint(loginController)

@app.errorhandler(401)
def page_not_found_401(e):
    return render_template("401.html"), 401

@app.errorhandler(403)
def page_not_found_403(e):
    return render_template("403.html"), 403

@app.errorhandler(404)
def page_not_found_404(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found_500(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)
