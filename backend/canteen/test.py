from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('try2.html')

@app.route('/scan', methods=['POST'])
def scan():
    result = subprocess.run(['python', 'D:/Smart-Canteen-master/smart-canteen/backend/canteen/templates/try.py'], capture_output=True)
    barcode_data = result.stdout.decode('utf-8').strip()
    return barcode_data

if __name__ == '__main__':
    app.run(debug=True)
