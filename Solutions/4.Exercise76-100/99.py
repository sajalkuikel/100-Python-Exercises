from flask import Flask, render_template_string, request

app = Flask(__name__)
html = """

                <form action="{{url_for('sent')}}" method="GET">
                    <input title= "hehe" type="text" name="line" placeholder="Enter a line" required /> <br>
                    <input title= "hehe" type="text" name="line2" placeholder="Enter a line" required /> <br>
                    
                    <button class= "go" type= "submit"> Submit </button>
                </form>
                
"""


@app.route("/")
def index():
    return render_template_string(html)


@app.route("/sent",  methods=['GET', 'POST'])
def sent():
    line = None
    line2 =None
    if request.method == 'POST':
        line = request.form['line']
        line2= request.form['line2']
        with open("user_input_flask.txt", "a+") as file:
            file.write(line + "," + line2 + "\n")
        return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)