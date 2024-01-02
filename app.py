from flask import Flask, render_template, request
from CipherBreaker import CipherBreaker
from CipherMaker import CipherMaker

app = Flask(__name__)

cipher_maker = CipherMaker()
cipher_breaker = CipherBreaker(cipher_maker)

@app.route("/")
def home():
    return render_template('form.html')

@app.route('/encrypt/', methods = ['POST'])
def encrypt_http():
    form_data = request.form
    ciphertext = cipher_maker.encrypt(int(form_data["Key"]), form_data["Plaintext"])

    return render_template('data.html', form_data = form_data, text=ciphertext)

@app.route('/decrypt/', methods = ['POST'])
def decrypt_http():
    form_data = request.form
    plaintext = cipher_maker.decrypt(int(form_data["Key"]), form_data["Ciphertext"])

    return render_template('data.html', form_data = form_data, text= plaintext)

@app.route('/break/', methods = ['POST'])
def break_http():
    form_data = request.form
    key, plaintext = cipher_breaker.caesar_brute_force(form_data["Ciphertext"])

    return render_template('break.html', key=key, text = plaintext)