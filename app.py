from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(password_length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(password_length))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password_length = int(request.form.get('length', 10))  # default password length is 10
        include_uppercase = request.form.get('uppercase', False)
        include_lowercase = request.form.get('lowercase', False)
        include_numbers = request.form.get('numbers', False)
        include_special_chars = request.form.get('special_chars', False)

        password = generate_password(password_length, include_uppercase,
                                     include_lowercase, include_numbers,
                                     include_special_chars)

        return render_template('index.html', password=password, password_length=password_length)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
