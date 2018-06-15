class DBBase():
    _counter = None
    _open_msg = None
    _close_msg = None

    def __init__(self):
        """"Open a connection with database. Very costly operation"""
        self.count = self._counter
        type(self)._counter += 1
        print(f'### {self._open_msg}: {self.count}')

    def close(self):
        """"Closes database connection"""
        print(f'### {self._close_msg}: {self.count}')

class Connection(DBBase):
    _counter = 1
    _open_msg = 'Opening database connection'
    _close_msg = 'Closing database connection'

class Session(DBBase):
    _counter = 1
    _open_msg = 'Opening session'
    _close_msg = 'Closing session'

if __name__ == '__main__':
    db_objects = [Connection() for i in range(3)]
    db_objects.extend([Session() for i in range(3)])
    for conn in db_objects:
        conn.close()
