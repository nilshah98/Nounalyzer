# Nounalyzer
A basic app to visualise RSS feed

## Folder and Files structure
- `/frontend` - Used for taking inputs and D3 visualizations.
- `/backend` - Used for fetching data from RSS feeds, to avoid CORS error, and also to do analyze the RSS data to visualize

## Frontend
- Taking input and making `POST` requests to `http://localhost:5000/rss`, so make sure the `/backend` runs at port `5000`
- Additionally using `Bootstrap` for basic styling, `jQuery` to make easier `AJAX` requests, and `D3` to visualize data, so creating a mashup of various RIA [Rich Internet Applications]

## Backend
- A simple flask server, which exposes `/rss` route and provides `CORS` support through `flask-cors` package
- Also should be running on port `5000` as the requests are made on that
- Additionally using `feedparser` to get RSS feed data, a basic tutorial for feedparser can be found [here](https://www.pythonforbeginners.com/feedparser/using-feedparser-in-python)
- Using virtual env here, and the dependencies for the project can hence be found at `requirements.txt`

## Steps to run
#### Frontend
- Serve `/frontend` through some extension or package such as [live-server](https://www.npmjs.com/package/live-server)
- **Note:** Make sure to serve it on anyother port except `5000` since API calls are made there

#### Backend
- Serve `/backend` in another terminal, either by installing dependencies using [venv](https://docs.python.org/3/library/venv.html) or by installing globally
- Make sure it is served on port `5000` if not, make appropriate changes at - `/frontend/script.js`