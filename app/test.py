import os
import requests
import json
import hashlib
import unittest

url = "http://localhost:5000/messages"

def url_for_get(hash_val):
	return url + "/" + hash_val

def payload_for_post(message):
	return {"message": message}


class TestStringMethods(unittest.TestCase):

	def test_error_response(self):
		test_message = "unseen"
		hash_of_test_message = hashlib.sha256(test_message).hexdigest()
		r1 = requests.get(url_for_get(hash_of_test_message))

		self.assertEqual(r1.status_code,404)
		self.assertEqual(r1.json()["err_msg"],"Message Not Found")

	def test_post_request(self):
		test_message = "hello my name is Zachary"
		hash_of_test_message = hashlib.sha256(test_message).hexdigest()
		r1 = requests.post(url, json=payload_for_post(test_message))

		self.assertEqual(r1.status_code, 200)
		self.assertEqual(r1.json()["digest"], hash_of_test_message)


	def test_get_request(self):
		test_message = "hello my name is Zachary"
		hash_of_test_message = hashlib.sha256(test_message).hexdigest()
		r1 = requests.get(url_for_get(hash_of_test_message))


		self.assertEqual(r1.status_code, 200)
		self.assertEqual(r1.json()["message"], test_message)





if __name__ == '__main__':
    unittest.main(verbosity=2)