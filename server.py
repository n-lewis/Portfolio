from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/help')
def about():
    return render_template('components.html')
