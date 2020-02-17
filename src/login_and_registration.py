from api_functions import *


def register():
    try:
        ip = request.remote_addr
        action = "Create Customer"
        content = json.loads(request.data.decode())
        if not create_customer(content):
            return "This phone number is already in use"
        return make_response("Your registration has been successful\n You will immediately be taken to the homepage", 201)
    except:
        return not_found()


def login():
    ip = request.remote_addr
    action = "Login"
    content = json.loads(request.data.decode())
    mydoc = search_db("_id", content['_id'], my_customers)
    for user in mydoc:
        if user["Password"] == content['Password']:
            session['logged_in'] = True
            session['username'] = content['_id']
            print(session)
            return make_response(
                {"alert": "hello " + user['Name'] + " \nYou will immediately be taken to the homepage",
                 "name": user['Name'].split(" ", 1)[0]}, 201)
        return "The details are incorrect, please try again"
    return "The details are incorrect, please try again"


def logout():
    ip = request.remote_addr
    action = 'Logout'
    if session.get('logged_in') and request.headers["Origin"] == 'appname':
        try:
            session['logged_in'] = False
            session.clear()
            return "OK"
        except:
            return not_found()
    return not_auth()
