from flask import Flask, render_template, request, redirect, session

app = Flask(_name_)
app.config['SECRET_KEY'] = 'chave-super-secreta'

@app.route("/")
def index():
    if 'lista' not in session:
      session['lista'] = []
    return render_template('tarefas.html', lista=session['lista'])
    


if _name_ == '_main_':
    app.run(debug=True)