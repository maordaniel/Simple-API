from api_functions import *


def register():
    try:
        ip = request.remote_addr
        action = "Create Customer"
        content = json.loads(request.data.decode())
        if not create_customer(content):
            return "מספר פלאפון זה כבר נמצא בשימוש"
        return make_response("הרשמתך נקלטה בהצלחה\n מיד תועבר לדף הבית", 201)
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
                {"alert": "שלום " + user['Name'] + " \nמיד תועבר לדף הבית", "name": user['Name'].split(" ", 1)[0]}, 201)
        return "הפרטיים הינם שגויים, נסו שנית"
    return "הפרטיים הינם שגויים, נסו שנית"


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
