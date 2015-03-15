# third party modules
from flask import (Flask, render_template, request)

# project modules
import config
from logic import Database


# instanciate application and database object
app = Flask(__name__)
db = Database(config)

# configure the web abb according to the config object
app.host = config.APP_HOST
app.port = config.APP_PORT
app.debug = config.APP_DEBUG

@app.route('/', methods=['GET'])
def splash():
    """Render the landing page"""
    return render_template('search.html')


@app.route('/search', methods=['GET'])
def search():
    """Render the search results page"""

    # get the query from the request object
    query = request.args.get('query')

    # get search results
    results = db.search_venues(query)

    return render_template('results.html', query=query, results=results)


@app.route('/venue/<venue_id>', methods=['GET'])
def show_venue(venue_id):
    """Render the page for each venue"""

    # get comments and venue information
    venue = db.get_venue(venue_id)
    comments = list(db.get_comments(venue_id))

    return render_template('venue.html', venue=venue,
                           comments=enumerate(comments),
                           cnt_comments=len(comments))

if __name__ == '__main__':
    app.run()
