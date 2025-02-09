import numpy as np
import scipy as sp
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Remove Streamlit code since we're using Flask
# Keep only the Flask routes

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
