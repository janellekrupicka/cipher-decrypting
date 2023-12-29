from flask import Flask, render_template, request

app = Flask(__name__)

ALPHA = "abcdefghijklmnopqrstuvwxyz"
ALPHA_LIST = list(ALPHA)

@app.route("/")
def home():
    return render_template('form.html')

def encrypt(key, plaintext):

    plaintext = plaintext.lower()
    key = int(key)
    cipher_arr = [None] * len(plaintext)

    for idx, char in enumerate(plaintext):

        ciph_idx = ALPHA_LIST.index(char)
        if ciph_idx == -1:
            cipher_arr[idx] = char
            continue
        
        cipher_arr[idx] = ALPHA_LIST[(ciph_idx + key) % 26]

    return ''.join(cipher_arr).upper()

@app.route('/encrypt/', methods = ['POST'])
def encrypt_http():
    form_data = request.form
    ciphertext = encrypt(form_data["Key"], form_data["Plaintext"])

    return render_template('data.html', form_data = form_data, ciphertext=ciphertext)