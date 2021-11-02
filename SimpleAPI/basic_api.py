
import hashlib
import hmac
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def generate_HMAC_token():
    passed_in_message = request.get_data()
    stripped_message = f"{passed_in_message[3:]}"
    key = b'0f8f13f4368f11ec8d3d0242ac130003'

    signiture = hmac.new(
        key,
        str.encode(stripped_message),
        hashlib.sha256
    ).hexdigest()
    return passed_in_message.decode('utf-8') + f"&Signature={signiture}"

if __name__ == "__main__":
    app.run()
