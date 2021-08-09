from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates")


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST', 'GET'])
def upload_file1():
    if request.method == 'POST':
        my_file = request.files['file']
        my_file.save(secure_filename(my_file.filename))
        return 'File Upload Successfully'


if __name__ == "__main__":
    app.run(debug=True)
