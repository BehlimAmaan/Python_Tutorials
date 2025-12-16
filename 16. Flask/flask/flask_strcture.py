from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def message():
        return 'Welcom To Home Page'

@app.route("/Home")
def Home():
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)