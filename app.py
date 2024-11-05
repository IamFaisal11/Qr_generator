from flask import Flask, send_file, render_template, request, redirect, url_for
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Get the data from the form
    data = request.form['data']
    
    # Generate QR code
    qr = qrcode.make(data)
    
    # Save QR code to a BytesIO object
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Send the image as a file to download
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

if __name__ == '__main__':
    app.run(debug=True)
