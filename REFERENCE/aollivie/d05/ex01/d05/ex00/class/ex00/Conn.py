import psycopg2
from django.conf import settings

class Conn(object):
    """docstring for ."""
    def __init__(self):
        self.conn  = psycopg2.connect(
                        database = settings.DATABASES['NAME'],
                        host = settings.DATABASES['HOST'],
                        user = settings.DATABASES['USER'],
                        password = settings.DATABASES['PASSWORD']
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
