from flask import Flask, request, jsonify, render_template
import smtplib
import ssl

app = Flask(__name__)

my_email = "altairraphael19@gmail.com"
my_password = "rmxjyerckzjuyrot"
my_smtp_server = "smtp.gmail.com"
receiver_email = "chijioke914@gmail.com"


def send_email(message, receiver_email, sender, password, smtp):
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(host=smtp, port=465, context=context) as connection:
                    connection.login(user=sender, password=password)
                    connection.sendmail(from_addr=sender, to_addrs=receiver_email, msg=message)
        except Exception as e:
            return e
        


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    name = request.form['name']
    email = request.form['email']
    msg = request.form['message']
    phone = request.form['phone']

    message = f"Subject: {name}\n\nName: {name}, Email: {email}, Phone: {phone} \n\n Message: {msg}"

    send_email(message, receiver_email, my_email, my_password, my_smtp_server)
    if send_email:
        return render_template('data.html')
    return f"Name: {name}, Email: {email} \n\n Message: {message}" 





   
    
 

if __name__=="__main__":
    app.run(debug=True)