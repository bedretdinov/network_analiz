from flask import Flask, request, redirect, url_for, flash
from flask import render_template

app = Flask(__name__)
app.secret_key = 'nv'

@app.route('/')
def index():

    return render_template('index.html')

app.run(host='0.0.0.0', port=7000 , debug=True)

