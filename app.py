from flask import Flask, render_template, request
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"].encode('utf-8')

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.environ.get('EMAIL'), password=os.environ.get('PASSWORD'))
            connection.sendmail(
                from_addr=os.environ.get('EMAIL'),
                to_addrs=os.environ.get("RECEIVING_EMAIL"),
                msg=f"Subject:A new user enrolled in your website\n\n\n"
                    f"Data of the user\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"message: {message}\n"
            )
        return render_template("index.html")
    return render_template("contact.html")



