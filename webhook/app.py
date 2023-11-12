from flask  import Flask,request
import os
from pathlib import Path

app = Flask(__name__)
path = Path(__file__).parent.resolve()
print(path)

@app.route("/webhook", methods=["POST"])
def webhook():
  if request.method == "POST":
    print(f"Data received")
    event = request.json["hook"]["events"]
    repository = request.json["repository"]["name"]
    if event[0] == "push":
      Redeploy(repository)


    return "received"
  
def Redeploy(repository):
  match repository:
    case "smolander.dev":
      os.system("sh Deploy_smolander.dev.sh")