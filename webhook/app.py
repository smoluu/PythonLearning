from flask  import Flask,request
import json
import os

app = Flask(__name__)
filecount = 0
abs_path = os.getcwd()
data_path = os.path.join(abs_path,"data/")
print(data_path)
@app.route("/webhook", methods=["POST"])
def webhook():
  if request.method == "POST":
    print(f"Data received")
    data = json.dumps(request.json, indent=4)
    filename = "data" + str(filecount) + ".json"
    with open(os.path.join(data_path,filename),"w") as file:
      file.write(data)
    print("data saved!")
    filecount + 1
    return "received"
  
app.run(host="0.0.0.0",port=8000, debug=True)