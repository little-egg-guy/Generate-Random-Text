from flask import Flask, jsonify, render_template, request
import random
import string

app = Flask(__name__)

# Route to generate a random password
@app.route('/generate-password')
def generate_password():
    length = int(request.args.get('length', 12))  # Default length is 12
    length = min(length, 31)  # Enforce maximum length of 31
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return jsonify(password=password)

# Route to generate a random username
@app.route('/generate-username')
def generate_username():
    length = int(request.args.get('length', 8))  # Default length is 8
    length = min(length, 15)  # Enforce maximum length of 15
    adjectives = ['Quick', 'Lazy', 'Happy', 'Sad', 'Bright', 'Dark']
    nouns = ['Fox', 'Dog', 'Cat', 'Mouse', 'Bear', 'Wolf']
    username = random.choice(adjectives) + random.choice(nouns)
    if length > len(username):
        username += ''.join(random.choices(string.digits, k=length - len(username)))
    return jsonify(username=username)

# Route to generate random text for typing speed tests
@app.route('/generate-text')
def generate_text():
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    text = ' '.join(random.choices(words, k=50))
    return jsonify(text=text)

# Home route
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)