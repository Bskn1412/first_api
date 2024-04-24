from flask import Flask, jsonify, request
from flask_cors import CORS
from mail_notes import send_notes_email,decodeBase64
from sql_database import database

app = Flask(__name__)
CORS(app)  


@app.route('/submit/<email>/<key>', methods=['POST', 'GET'])
def submit(email, key):
    if request.method == "POST":
        print(email)
        print(key)
        result = database(key)
        if len(result) != 0:
           print(result)
           notes = decodeBase64(result)
           print(notes)
           result = send_notes_email(email, notes)
           if result == 'done':
               return jsonify({"key": "Sent"})
           else:
              return jsonify({"key": "Not Sent"})
        else:
            print("No Data Found")
            return jsonify({"key": "Not Sent"})


if __name__ == "__main__":
    app.run(debug=True)
