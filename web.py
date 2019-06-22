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

    cuvinte = list(dict.fromkeys(cuvinte))
    resultat = []
    for i in cuvinte:
        i = "".join(i) + "\n"
        if i in contents:
            resultat.append(i)
    return jsonify({"result" : (''.join(str(i) for i in resultat))+'\n'})


if __name__ == "__main__":
    app.run(debug=True)
