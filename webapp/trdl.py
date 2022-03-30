from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route("/")
def main():
    return "42"

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' \
                             % page_name, 404)
    return response

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)