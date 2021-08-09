import os
import hashlib
import redis
from flask import Flask,request,jsonify


app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"))


@app.route('/messages/<hash_val>')
def get_message(hash_val):
	msg = r.get(hash_val)
	if not msg:
		return jsonify(err_msg="Message Not Found"), 404

	msg = msg.decode()
		
	return jsonify(message=msg)

	
    
@app.route('/messages', methods=['POST'])
def store_message():
	message = request.get_json()["message"]
	hash_val = hashlib.sha256(message.encode("utf-8")).hexdigest()

	r.set(hash_val,message)

	return jsonify(digest=hash_val)
	

