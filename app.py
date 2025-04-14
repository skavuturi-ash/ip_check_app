
from flask import Flask, request, redirect, make_response

app = Flask(__name__)

ALLOWED_IP = "183.82.122.72"
GOOGLE_FORM_URL = "https://forms.gle/hwDy6VZb3BA8TM18A"

@app.route("/")
def home():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        ip = request.remote_addr

    if ip == ALLOWED_IP:
        return redirect(GOOGLE_FORM_URL, code=302)
    else:
        html = f"""
        <html>
            <body style="font-family: Arial; text-align: center; margin-top: 100px;">
                <h2>Access Denied</h2>
                <p>This form is only available on the authorized Wi-Fi network.</p>
                <p>Your IP: {ip}</p>
            </body>
        </html>
        """
        response = make_response(html)
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
