import requests
from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__,template_folder='templates')


URL = "http://localhost:3000/employee"



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/jsonapi', methods=['POST'])
def validate_data():
    f_name = request.form.get('fname')
    l_name = request.form.get('lname')
    company_name = request.form.get('cmp')
    city = request.form.get('loc')

    

    load_data = {
        "fname": f_name,
        "lname": l_name,
        "company": company_name,
        "location": city
    }

    if len(load_data)<2:
       
        return "Bad Request Error Code:400"
    else:
        r = requests.post(url = URL, data = load_data)
        print('Valid Input Code:', r.status_code)
        return jsonify({'data':load_data}) , r.status_code

    

if __name__ == "__main__":
    app.run(debug=True)
   