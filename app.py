from flask import Flask, request, render_template
from bardapi import Bard
import os

app = Flask(__name__)

os.environ["_BARD_API_KEY"] = "cggms6llea1ZqbxW2zQFt4g-Xyt7Vsk2XSq-bKnUZ_gvOBNFkiTFi4HHDSrAI_zDUl30dw."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def get_answer():
    user_text = request.form['user_text']
    response = Bard().get_answer(user_text)['content']
    return response

if __name__ == "__main__":
    app.run(debug=True)
