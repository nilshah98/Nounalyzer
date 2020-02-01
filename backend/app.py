from flask import Flask, request 
from flask_cors import CORS, cross_origin
import feedparser

app = Flask(__name__) 
CORS(app)
    
@app.route('/rss',methods = ['POST']) 
@cross_origin()
def login(): 
   rssLink = request.form['rssLink'] 
   data = feedparser.parse(rssLink)
   print(data['feed'])
   # refer - https://www.pythonforbeginners.com/feedparser/using-feedparser-in-python to use feedparser
   # pass data to NLP processing
   return data.feed.subtitle
  
if __name__ == '__main__': 
   app.run(debug = True) 