from flask import Flask,request,jsonify
import hashlib
import redis

app = Flask(__name__)

r = redis.Redis(host='microservice-fun_redis_1', port=6379)


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
	

