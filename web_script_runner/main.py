from flask import Flask, request

from runner import run_script

app = Flask(__name__)


@app.route('/')
def main():
	return 'Hello, World!'

@app.route("/<string:script>", methods=["POST"])
def run(script):
	return run_script(script, request.data)


app.run()