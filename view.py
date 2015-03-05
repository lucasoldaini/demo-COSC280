# third party modules
from flask import (Flask, render_template, request)

# project modules
import config
from logic import Database

def setup():
app = Flask(__name__)
db = Database(config)


@app.route('/', methods=['GET'])
def splash():
    return render_template('search.html')


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = db.search_venues(query)
    return render_template('results.html', query=query, results=results)


@app.route('/venue/<venue_id>', methods=['GET'])
def show_venue(venue_id):
    venue = db.get_venue(venue_id)
    comments = list(db.get_comments(venue_id))

    return render_template('venue.html', venue=venue,
                           comments=enumerate(comments),
                           cnt_comments=len(comments))

app.host = config.app_host
app.port = config.app_port
app.debug = config.app_debug

if __name__ == '__main__':
    app.run()


