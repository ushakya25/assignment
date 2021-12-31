from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


def validate_input_request(request_json):
    if (len(request_json) >= 2):
        return "", 201
    else:
        return "", 400


@app.route('/jsonapi', methods=['POST'])
def validate():
    try:
        request_json = request.get_json()
        return validate_input_request(request_json)
    except:
        return "", 400


@app.route('/', methods=['GET'])
def render():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
