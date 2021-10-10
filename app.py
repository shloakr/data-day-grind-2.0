from flask import Flask, request, render_template
from flask.json import jsonify
import data
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods =["GET", "POST"])
def search():
    if request.method == "POST":
       search = request.form.get("search")
       res = data.search(search)
       print(res)
       return render_template('results.html', records = res)
    return render_template("search.html")

@app.route('/data')
def viewData():
    return render_template('Table/Table.html')

if __name__ == "__main__":
    app.run(
        host = "localhost",
        port = 5000,
        debug = True
    )