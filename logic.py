import pymysql


class CursorIterator(object):
    """Iterator for the cursor object."""

    def __init__(self, cursor):
        """ Instantiate a cursor object"""
        self.__cursor = cursor

    def __iter__(self):
        return self

    def next(self):
        elem = self.__cursor.fetchone()

        if elem is None:
            self.__cursor.close()
            raise StopIteration()
        else:
            return elem


class Database(object):
    """Database object"""

    def __init__(self, opts):
        """Initalize database object"""
        super(Database, self).__init__()
        self.opts = opts
        self.__connect()

    def __connect(self):
        """Connect to the database"""
        self.conn = pymysql.connect(self.opts.DB_HOST, self.opts.DB_USER,
                                    self.opts.DB_PASSWORD, self.opts.DB_NAME)

    def search_venues(self, query):
        """Search for a venue in the database"""
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        query = pymysql.escape_string(query)
        cur.execute('SELECT id, name, address, type, lat, lng FROM venues WHERE'
                    '(name LIKE "%%{0}%%" OR address LIKE "%%{0}%%");'
                    ''.format(query))

        return CursorIterator(cur)

    def get_venue(self, venue_id):
        """Fetch a veuw from the database"""
        cur = self.conn.cursor(pymysql.cursors.DictCursor)

        venue_id = pymysql.escape_string(venue_id)
        cur.execute('SELECT * FROM venues WHERE id = {0};'.format(venue_id))

        resp = cur.fetchone()
        cur.close()
        return resp if resp is not None else []


    def get_comments(self, venue_id):
        """Get comments for a venue"""
        cur = self.conn.cursor(pymysql.cursors.DictCursor)

        venue_id = pymysql.escape_string(venue_id)
        cur.execute('SELECT * FROM comments WHERE venue_id = {0};'.format(venue_id))

        return CursorIterator(cur)
