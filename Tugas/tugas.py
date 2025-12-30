from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("index1.html")

@app.route("/login", methods=["GET"])
def login():
    name = request.args.get("nama_mhs", "nilai_default")
    nim = request.args.get("nim_mhs", "nilai_default")
    kelas = request.args.get("kelas_mhs", "nilai_default")
    mata_kuliah = request.args.get("mata_kuliah", "nilai_default")

    return render_template(
        "index2.html",
        name2=name,
        nim2=nim,
        kelas2=kelas,
        mata_kuliah2=mata_kuliah
    )

if __name__ == "__main__":
    app.run(debug=True)