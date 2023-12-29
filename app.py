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

def decrypt_key(key, ciphertext):

    ciphertext = ciphertext.lower()
    key = int(key)
    plaintext_arr = [None] * len(ciphertext)

    for idx, char in enumerate(ciphertext):

        ciph_idx = ALPHA_LIST.index(char)
        if ciph_idx == -1:
            plaintext_arr[idx] = char
            continue

        plaintext_arr[idx] = ALPHA_LIST[(ciph_idx + 26 - key) % 26]

    return ''.join(plaintext_arr).lower()

@app.route('/encrypt/', methods = ['POST'])
def encrypt_http():
    form_data = request.form
    ciphertext = encrypt(form_data["Key"], form_data["Plaintext"])

    return render_template('data.html', form_data = form_data, text=ciphertext)

@app.route('/decrypt/', methods = ['POST'])
def decrypt_http():
    form_data = request.form
    plaintext = decrypt_key(form_data["Key"], form_data["Ciphertext"])

    return render_template('data.html', form_data = form_data, text= plaintext)