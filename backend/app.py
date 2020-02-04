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
   # refer - https://www.pythonforbeginners.com/feedparser/using-feedparser-in-python to use feedparser
   # pass data to NLP processing
   # processing the length of content in each entry in RSS
   print(data["feed"])
   analysis = []
   for entry in data["entries"]:
      analysis.append(len(entry["summary"]))
   print(analysis)
   return { "dataset": analysis, "feeds": data["entries"]}
  
if __name__ == '__main__': 
   app.run(debug = True) 