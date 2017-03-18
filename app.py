import os #split yml or json
import base64 #decode
import sys   
import yaml  
import json  


from flask import Flask
from github import Github

g =Github()

username = sys.argv[1].split("https://github.com/")[1]  #get input url argument


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello from Dockerized Flask App!!"


@app.route("/v1/<name>")   #get and return the file under repo 
def hello2(name):
	repo = g.get_repo(username)
	filename, file_extension = os.path.splitext(name)
	
	# transfer format both on yml and json
	if file_extension == ".yml":
	   content = base64.b64decode(repo.get_file_contents(name).content)
	if file_extension ==".json":
	   contentyml = base64.b64decode(repo.get_file_contents(filename+".yml").content)
	   content = json.dumps(yaml.load(contentyml),sort_keys=True, indent=2)
	
	return content



if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
