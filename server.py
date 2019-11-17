from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Loads env variables for email information
load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(12)

# Settings for sending me an email notification on contact form submission
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)


def send(data):
    """Sends the data passed in to the email specified in the env variable EMAIL_RECIPIENT"""
    msg = Message(subject=data['subject'],
                  sender=app.config.get("MAIL_USERNAME"),
                  recipients=[os.environ['EMAIL_RECIPIENT']],
                  body=f"Email: {data['email']} Body: {data['message']}")
    mail.send(msg)
    print('Message Sent')


@app.route('/')
def root():
    """Renders index.html"""
    return render_template('index.html')


@app.route('/<page_name>')
def html_page(page_name):
    """Renders the passed in page as long as it exists"""
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submint_form():
    """Takes in the input form and preps the data to be passed to send() and alerts user of submission status. 
    In all cases returns a redirect to index.html"""
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        if data['email'] and data['subject'] and data['message']:
            flash('Form submitted! I will get back to you as soon as I can.')
            send(data)
            return redirect('index.html')
        else:
            flash('Invalid submission')
            return redirect('index.html')
    else:
        flash('Something went wrong with your submission')
        return redirect('index.html')
