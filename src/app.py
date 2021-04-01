from flask import Flask,request,jsonify
import hashlib

app = Flask(__name__)
D = {}


@app.route('/messages/<hash_val>')
def get_message(hash_val):
	if hash_val in D:
		return jsonify(message=D[hash_val])

	return jsonify(err_msg="Message Not Found"), 404
    
@app.route('/messages', methods=['POST'])
def store_message():
	message = request.get_json()["message"]
	hash_val = hashlib.sha256(message).hexdigest()

	D[hash_val] = message

	return jsonify(digest=hash_val)
	

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')