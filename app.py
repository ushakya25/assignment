import requests
from flask import Flask, jsonify, render_template
import json

app = Flask(__name__,template_folder='templates')


URL = "http://localhost:3000/employee"


PARAMS = {
    
      "empname":"Deepak",
      "company":"HCL",
      "Salary":5000,
      "Designatio":"Jr. Developer"
    }
    
if len(PARAMS)<2:
    print("Invalid Input Code:400")
else:
    r = requests.post(url = URL, data = PARAMS)
    print('Valid Input Code:', r.status_code)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
   