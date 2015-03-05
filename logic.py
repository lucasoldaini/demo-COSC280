import pymysql

class CursorIterator(object):
    """docstring for CursorIterator"""
    def __init__(self, cursor):
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
    """docstring for Model"""
    def __init__(self, opts):
        super(Database, self).__init__()
        self.opts = opts
        self.__connect()

    def __connect(self):
        self.conn = pymysql.connect(self.opts.db_host, self.opts.db_user,
                                    self.opts.db_password, self.opts.db_name)

    def search_venues(self, query):
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        query = pymysql.escape_string(query)
        cur.execute('SELECT id, name, address, type, lat, lng FROM venues WHERE'
                    '(name LIKE "%%{0}%%" OR address LIKE "%%{0}%%");'
                    ''.format(query))

        return CursorIterator(cur)

    def get_venue(self, venue_id):
        cur = self.conn.cursor(pymysql.cursors.DictCursor)

        venue_id = pymysql.escape_string(venue_id)
        cur.execute('SELECT * FROM venues WHERE id = {0};'.format(venue_id))

        resp = cur.fetchone()
        cur.close()
        return resp if resp is not None else []


    def get_comments(self, venue_id):
        cur = self.conn.cursor(pymysql.cursors.DictCursor)

        venue_id = pymysql.escape_string(venue_id)
        cur.execute('SELECT * FROM comments WHERE venue_id = {0};'.format(venue_id))

        return CursorIterator(cur)

if __name__ == '__main__':
    import config

    m = Database(config)
    c = m.search_venues('pizzeria')
    c = m.get_venue('1')
    c = m.get_comments('4')

    print list(c)
