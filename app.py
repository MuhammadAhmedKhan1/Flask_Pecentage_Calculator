from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["GET","POST"])
def result():
    Python = float(request.form["python"])
    Java = float(request.form["java"])
    Javascript = float(request.form["javascript"])
    Typescript = float(request.form["typescript"])
    Flask = float(request.form["flask"])

    Percentage=(Python+Java+Javascript+Typescript+Flask)*100/500

    return render_template("result.html", percentage=Percentage)
if __name__=="__main__":
    app.run(debug=True,port=5000)