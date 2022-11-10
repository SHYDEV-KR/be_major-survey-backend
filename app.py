from flask import Flask, make_response, request
from api import generate_new_page_in_db

app = Flask(__name__)

@app.route('/api/v1/submit', methods=["POST"])
def submit():
	if request.method == "POST":
		resp = generate_new_page_in_db("b39bb1d822de42ef8c67290a8ba60e07", {
				"age": request.form.get("age"),
				"gender": request.form.get("gender"),
				"major": request.form.get("major"),
				"career": request.form.get("career"),
				"correlation": request.form.get("correlation"),
				"needs": request.form.get("needs"),
				"feedback": request.form.get("feedback"),
				"insta": request.form.get("insta"),
				"phone": request.form.get("phone"),
				}
		)
		return make_response({"result" : resp}, 200)