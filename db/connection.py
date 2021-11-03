import psycopg2 as db


class Config:
    def __init__(self):
        self.config = {
            'postgres': {
                'user': 'postgres',
                'password': 'nexter32',
                'host': 'localhost',
                'port': '5432',
                'database': 'db_game_words'
            }
        }


class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config['postgres'])
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Erro na conexão: ', e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


class WordSecret(Connection):
    def __init__(self):
        Connection.__init__(self)

    def select_word(self, id):
        return self.query(f'SELECT palavra FROM words WHERE id={id}')

    def select_last_id(self):
        return self.query(f'SELECT id FROM words ORDER BY id desc limit 1')


if __name__ == '__main__':
    conn = WordSecret()

