from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Enable CSRF protection
csrf = CSRFProtect(app)


# ────────────────────────────────────────────
# MAIN ROUTES
# ────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    name    = request.form.get('name', '').strip()
    email   = request.form.get('email', '').strip()
    subject = request.form.get('subject', '').strip()
    message = request.form.get('message', '').strip()

    if not all([name, email, subject, message]):
        flash('All fields are required.', 'danger')
        return redirect(url_for('index') + '#contact')

    # Print to console (development)
    print("\n📩 New Contact Message")
    print(f"Name   : {name}")
    print(f"Email  : {email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}\n")

    flash('Your message has been sent successfully!', 'success')
    return redirect(url_for('index') + '#contact')


# ────────────────────────────────────────────
# FOOTER ROUTES
# ────────────────────────────────────────────

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/faqs')
def faqs():
    return render_template('faqs.html')


@app.route('/help')
def help_page():
    return render_template('help.html')


# ────────────────────────────────────────────
# OPTIONAL EMAIL FUNCTION
# ────────────────────────────────────────────

def send_email(name, sender_email, subject, message):
    SMTP_HOST     = 'smtp.gmail.com'
    SMTP_PORT     = 587
    SMTP_USER     = 'your-email@gmail.com'
    SMTP_PASSWORD = 'your-app-password'
    RECIPIENT     = 'your-email@gmail.com'

    msg = MIMEMultipart()
    msg['From']    = SMTP_USER
    msg['To']      = RECIPIENT
    msg['Subject'] = f"[Portfolio Contact] {subject}"

    body = f"""
New contact form submission:

Name   : {name}
Email  : {sender_email}
Subject: {subject}

Message:
{message}
"""
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, RECIPIENT, msg.as_string())


# ────────────────────────────────────────────
# RUN
# ────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=True)