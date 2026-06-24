from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os
from module import check

app = Flask(__name__)

app.secret_key = "binary_classifier"

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

file_arr = []


def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def upload():

    file1 = request.files["file1"]
    file2 = request.files["file2"]

    if not file1 or not file2:
        flash("Please upload both files")
        return render_template("index.html")

    if allowed_file(file1.filename) and allowed_file(file2.filename):

        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)

        path1 = os.path.join(app.config["UPLOAD_FOLDER"], filename1)
        path2 = os.path.join(app.config["UPLOAD_FOLDER"], filename2)

        file1.save(path1)
        file2.save(path2)

        result1, result2 = check(path1, path2)

        if result2 == "photos":
            flash("Upload only one photograph")

        elif result2 == "signatures":
            flash("Upload only one signature")

        else:
            file_arr.clear()
            file_arr.extend([result1, result2])

            return render_template(
                "result.html",
                photo=os.path.basename(result1),
                sign=os.path.basename(result2)
            )

    else:
        flash("Only png, jpg, jpeg allowed")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
