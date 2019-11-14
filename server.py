from flask import Flask, render_template, request, flash, redirect
import os
app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submint_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        if data['email'] and data['subject'] and data['message']:
            flash('Form submitted! I will get back to you as soon as I can.')
            return redirect('index.html')
        else:
            flash('Invalid submission')
            return redirect('index.html')
    else:
        flash('Something went wrong with your submission')
        return redirect('index.html')
