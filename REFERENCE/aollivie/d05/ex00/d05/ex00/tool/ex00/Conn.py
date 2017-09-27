import psycopg2
from django.conf import settings

class Conn(object):
    """docstring for ."""
    def __init__(self):
        self.conn  = psycopg2.connect(
                        database = settings.POSTGRES['database'],
                        host = settings.POSTGRES['host'],
                        user = settings.POSTGRES['user'],
                        password = settings.POSTGRES['password']
                        )
        self.mess_execute = ''
        self.mess_commit = ''

    def execute_query(self, query=''):
        try:
            self.curr = self.conn.cursor()
            self.curr.execute(query)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            return (e)
        return ('OK')
