import requests
from flask import Flask,render_template,url_for
from flask import request as req


application = Flask(__name__)
app=application
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method== "POST":
        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-6-6"
        headers = {"Authorization": "Bearer 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"}
        #headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

        data=req.form["data"]

        maxL=int(req.form["maxL"])
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs":data,
            "parameters":{"min_length":minL,"max_length":maxL},
        })
        
        return render_template("index.html",result=output)
    else:
        return render_template("index.html")
    

if __name__=='__main__':
    app.run('0.0.0.0')