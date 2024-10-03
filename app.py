import qrcode 
from flask import Flask, request, render_template, send_file 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_qr():
    if request.method == "POST":
        data = request.form["data"]
        qr_img = qrcode.make(data)
        
        qr_path = "static/qr_code.png"
        qr_img.save(qr_path)
        
        return send_file(qr_path, mimetype='image/png')
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    