from flask import Flask
from housing.exception import CustomException
from housing.logger import logging
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("raising the exception here")
    except Exception as e:
        logging.info("passed the exception here.")
        housing=CustomException(e,sys)
        logging.info(housing.error_message)
    return "the fourth ml project practice."

if __name__=="__main__":
    app.run(debug=True)
