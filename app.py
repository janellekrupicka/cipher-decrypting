from flask import Flask, render_template, request

app = Flask(__name__)

ALPHA = "abcdefghijklmnopqrstuvwxyz"
ALPHA_LIST = list(ALPHA)

@app.route("/")
def home():
    return render_template('form.html')

def key_operations(key, text):
    text = text.lower()
    new = [None] * len(text)

    for idx, char in enumerate(text):

        if char not in ALPHA_LIST:
            new[idx] = char
            continue

        new_idx = ALPHA_LIST.index(char)
        new[idx] = ALPHA_LIST[(new_idx + key) % 26]

    return ''.join(new).upper()

@app.route('/encrypt/', methods = ['POST'])
def encrypt_http():
    form_data = request.form
    ciphertext = key_operations(int(form_data["Key"]), form_data["Plaintext"])

    return render_template('data.html', form_data = form_data, text=ciphertext)

@app.route('/decrypt/', methods = ['POST'])
def decrypt_http():
    form_data = request.form
    plaintext = key_operations(26 - int(form_data["Key"]), form_data["Ciphertext"])

    return render_template('data.html', form_data = form_data, text= plaintext)