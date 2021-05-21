import itertools
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    litere = request.form["letters"].lower()
    
    nr_lit = int(request.form["len"])

    file_name ="cuv/" + str(nr_lit) + "lit.txt"
    with open(file_name, "r") as f:
        contents = f.readlines()        
    cuvinte = list(itertools.permutations(litere, nr_lit))

    resultat = num1 + num2
    return jsonify({"result" : resultat})


if __name__ == "__main__":
    app.run(debug=True)
