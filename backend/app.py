from flask import Flask, request 
from flask_cors import CORS, cross_origin
import feedparser

app = Flask(__name__) 
CORS(app)
    
# Defining the route to listen to and the method allowed
@app.route('/rss',methods = ['POST']) 
# To bypass CORS error only for this route, using @cross_origin() wrapper
@cross_origin()
def login(): 
   # Getting the data received from the frontend
   rssLink = request.form['rssLink'] 
   # Parsing the received RSS feed link using `feedparser`
   data = feedparser.parse(rssLink)
   print(data["feed"])
   # Analysing the amount of data in each entry in feed
   analysis = []
   for entry in data["entries"]:
      analysis.append(len(entry["summary"]))
   print(analysis)
   # Returning the analysis and the entries in the feed
   return { "dataset": analysis, "feeds": data["entries"]}
  
if __name__ == '__main__': 
   app.run(debug = True) 