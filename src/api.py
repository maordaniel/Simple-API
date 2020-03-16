from api_functions import *
from login_and_registration import *


app = Flask(__name__, static_url_path="/tmp")
app.secret_key = os.urandom(12)
CORS(app, supports_credentials=True)


@app.route('/api/login', methods=['POST'])
def app_login():
    return login()


@app.route('/api/register', methods=['POST'])
def app_register():
    return register()


@app.route('/api/logout', methods=['GET'])
def app_logout():
    return logout()



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
