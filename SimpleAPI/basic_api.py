
import hashlib
import hmac
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def generate_HMAC_token():
    data = request.form.get('id')
    key = b'0f8f13f4368f11ec8d3d0242ac130003'

    signiture = hmac.new(
        key,
        str.encode(data),
        hashlib.sha256
    ).hexdigest()

    payload = {"id": f"{data}", "signiture": signiture}
    return jsonify(payload)



if __name__ == "__main__":
    app.run()
