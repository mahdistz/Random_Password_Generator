from flask import Flask, render_template, request
import random
import string
from zxcvbn import zxcvbn

app = Flask(__name__)

password_difficulty_text = {
    0: 'Weak',
    1: 'Medium',
    2: 'Good',
    3: 'Strong',
    4: 'Very Strong'
}


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
        include_uppercase = request.form.get('uppercase')
        include_lowercase = request.form.get('lowercase')
        include_numbers = request.form.get('numbers')
        include_special_chars = request.form.get('special_chars')

        password = generate_password(
            password_length,
            include_uppercase,
            include_lowercase,
            include_numbers,
            include_special_chars
        )

        difficulty_password_result = zxcvbn(password)
        password_difficulty_score = difficulty_password_result['score']

        return render_template('index.html',
                               password=password,
                               password_length=password_length,
                               password_difficulty_score=password_difficulty_score,
                               password_difficulty_text=password_difficulty_text[password_difficulty_score]
                               )

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
