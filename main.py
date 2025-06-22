from flask import *
import subprocess

app = Flask(__name__) 

@app.route("/")
def home():
    
    return render_template('index.html')
@app.route("/done")
def done():
    subprocess.call(["python","speechautomation.py"])
if __name__ == '__main__':
    app.run(host='localhost',port=1921,debug=True)