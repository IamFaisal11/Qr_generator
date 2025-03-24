from flask import Flask, send_from_directory, render_template, request, send_file
import qrcode
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    qr = qrcode.make(data)
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

# ✅ Corrected ads.txt serving
@app.route('/ads.txt')
def ads_txt():
    file_path = os.path.join(os.getcwd(), "ads.txt")
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='text/plain')
    else:
        return "ads.txt not found", 404

if __name__ == '__main__':
    app.run(debug=True)
