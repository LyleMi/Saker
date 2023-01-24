import pymysql


class MySQLWrapper(object):

    """MySQL Database Wrapper

    Attributes:
        conn (obj): mysql connection
        cur (obj): mysql connection cursor
    """

    def __init__(self, opts={}):
        """init connection

        Args:
            opts (dict): mysql connection config
        """
        self.conn = pymysql.connect(
            host=opts.get("host", "localhost"),
            user=opts.get("user", "root"),
            passwd=opts.get("pwd", "password"),
            db=opts.get("db", ""),
            charset=opts.get("charset", "utf8")
        )
        self.cur = self.conn.cursor()

    def enableDBG(self):
        pymysql.connections.DEBUG = True

    def showDBs(self):
        """show mysql dbs

        Returns:
            dict: databases
        """
        self.cur.execute("SHOW DATABASES")
        return [r[0] for r in self.cur.fetchall()]

    def showTables(self):
        """show mysql tables

        Returns:
            dict: tables
        """
        self.cur.execute("SHOW TABLES")
        return [r[0] for r in self.cur.fetchall()]

    def select(self, sql, data=None):
        """select data

        Args:
            sql (str): sql query
            data (str): condition

        Returns:
            dict: select data
        """
        self.cur.execute(sql, data)
        return self.cur.fetchall()

    def insert(self, sql, data=None, multip=False):
        """insert data

        Args:
            sql (str): sql query
            data (str or list or tuple or dict): data to be insterted
            multip (bool, optional): executemany or one

        Returns:
            int: number of affected rows
        """
        if multip:
            ret = self.cur.executemany(sql, data)
        else:
            ret = self.cur.execute(sql, data)
        self.conn.commit()
        return ret

    def execute(self, sql, data=None):
        """excute raw sql

        Args:
            sql (str): SQL query to be executed
            data (None, optional): parameters used with query
        """
        return self.cur.execute(sql, data)

    def close(self):
        """close connection
        """
        self.cur.close()
        self.conn.close()
