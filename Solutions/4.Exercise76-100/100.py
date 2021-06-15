from flask import Flask, render_template_string, request

app = Flask(__name__)

homepage = """
<form action="{{url_for('proceed')}}" method="post">
    <input type="text" name="uname" id="uname" placeholder="Enter your username." required>
    <input type="password" name="pword" id="pword" placeholder="Enter your password." required>
    <button class="go" type="submit"> Submit </button>
</form>
"""


@app.route("/")
def home():
    return render_template_string(homepage)


@app.route("/proceed", methods=['GET', 'POST'])
def proceed():
    username = None
    password = None

    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pword']

        # username and password
    while True:
        usr = username
        with open("users.txt", "r") as file:
            users = file.readlines()
            # print(users)
            users = [i.strip("\n") for i in users]
        if usr in users:
            render_template_string("Username exists")
            continue
        else:
            render_template_string("Username is fine")
            break

    while True:
        msg = []
        psw = password

        if not any(i.isdigit() for i in psw):
            msg.append("You need at least one number! ")
        if not any(i.isupper() for i in psw):
            msg.append("You need at least one upper case character")
        if not len(psw) >= 5:
            msg.append("Password must be at least 5 characters long")
        if (len(msg) == 0):
            render_template_string("Thanks, Accepted!")
            break
        else:
            render_template_string("Please check the following: ")
            for texts in msg:
                render_template_string(texts)


if __name__ == "__main__":
    app.run(debug=True)

