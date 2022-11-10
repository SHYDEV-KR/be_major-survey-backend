import json
from flask import Flask, make_response, request
from api import generate_new_page_in_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/submit', methods=["POST"])
def submit():
	if request.method == "POST":
		json_data = request.get_json(force=True)
		resp = generate_new_page_in_db("b39bb1d822de42ef8c67290a8ba60e07", {
				"age": json_data["age"],
				"gender": json_data["gender"],
				"major": json_data["major"],
				"career": json_data["career"],
				"correlation": json_data["correlation"],
				"needs": json_data["needs"],
				"feedback": json_data["feedback"],
				"insta": json_data["insta"],
				"phone": json_data["phone"],
				}
		)
		return make_response({"result" : resp}, 200)