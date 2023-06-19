"""Database Wrapper for SQLite client
"""

import sqlite3


class Sqlite(object):

    """
    sqlite Database Wrapper

    Attributes:
        conn (obj): sqlite connect
    """

    def __init__(self, database="test.db"):
        """init

        Args:
            database (str, optional): database name, or `:memory:`
        """
        super(Sqlite, self).__init__()
        self.conn = sqlite3.connect(database)

    def get_tables(self):
        cur = self.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [i for i in cur]

    def insert(self, sql, data, multip=False):
        """insert data

        Args:
            data (str): data to be inserted
        """
        if multip:
            ret = self.conn.executemany(sql, data)
        else:
            ret = self.conn.execute(sql, data)
        self.conn.commit()

    def select(self, sql, data):
        """select data

        Args:
            data (str): data to be select

        Returns:
            list: select result
        """
        cursor = self.conn.execute(sql, [data])
        return [i for i in cursor]

    def execute(self, sql):
        """execute raw sql

        Args:
            sql (str): sql query
        """
        cursor = self.conn.execute(sql)
        self.conn.commit()
        return cursor

    def interrupt(self):
        '''Older SQLite versions had issues with sharing connections between threads. 
        That's why the Python module disallows sharing connections and cursors between threads. 
        If you still try to do so, you will get an exception at runtime.
        The only exception is calling the interrupt() method, which only makes sense to call from a different thread.
        '''
        self.conn.interrupt()

    def close(self):
        """close connection
        """
        self.conn.close()


if __name__ == '__main__':
    db = DB(":memory:")
    db.execute("""
        CREATE TABLE `test` (
          `test` varchar(64) NOT NULL
        );
    """)
    db.insert('INSERT INTO `test` (`test`) VALUES (?)', '1')
    print(db.select("SELECT * FROM test WHERE test = ?", '1'))
    db.interrupt()
    print(db.select("SELECT * FROM test WHERE test = ?", '1'))
    db.close()
