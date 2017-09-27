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
        self.curr = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute_query(self, query='', option=None):
        try:
            self.curr.execute(query)
            self.conn.commit()
        except Exception as e:
            mess = ''
            if option != None:
                mess = option
            return (str(mess) + str(e))
        return ('OK')

    def insert(self, where=None, param=None, option=None):
        if param == None or where == None:
            return ('No param to insert')
        keys = ''
        values = ''
        i = 0
        for key, value in param.items():
            virgule = ''
            if i == 0:
                virgule = ''
            else:
                virgule = ', '
            keys += virgule +  key
            if isinstance(value, str):
                value = "'" + value + "'"
            values += virgule + str(value)
            i += 1
        query = 'INSERT INTO ' +  where +'('+ keys + ')' \
                + ' VALUES (' + values + ')'
        print(query)
        return (self.execute_query(query, option))

    def select(self, param=None):
        result = []
        if param == None:
            return
        query = 'SELECT ' + param['values'] + ' FROM ' + param['table']
        try:
            self.curr.execute(query)
            result = self.curr.fetchall()
            self.conn.commit()
        except Exception as e:
            return (None)
        return (result)

    def copy_from(self, file_name='', table='', sep='\t', columns=(), null='NULL'):
        if file_name == '':
            return ('file_name is required')
        if table == '':
            return ('file_name is required')
        f = open(file_name, 'r')
        try:
            self.curr.copy_from(f, table, sep, null, 42, columns)
            self.conn.commit()
        except Exception as e:
            return (e)
        return ('OK')
