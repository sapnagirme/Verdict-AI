# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 12:05:03 2025

@author: Lenovo
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)