from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.info('We are testing logger module')
    return "CI CD pipeline has been established."

if __name__=="__main__":
    app.run(debug=True)
