from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO
import base64

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')
        if link:
            img = qrcode.make(link)
            buffered = BytesIO()
            img.save(buffered, format='PNG')
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return render_template('index.html', img_data=img_str)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)