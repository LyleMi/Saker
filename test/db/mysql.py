import unittest
from saker.db.mysql import MySQLWrapper


class MysqlTest(unittest.TestCase):

    opts = {
        "host": "localhost",
        "user": "root",
        "pwd": "test",
        "db": "test"
    }

    def setUp(self):
        self.db = MySQLWrapper(self.opts)
        create_sql = """CREATE TABLE `user` (
            `username` VARCHAR(40), 
            `password` VARCHAR(40)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
        self.db.cur.execute(create_sql)

    def test_info(self):
        print(self.db.showDBs())
        print(self.db.showTables())

    def test_insert(self):
        db = self.db
        db.cur.execute("delete from user")
        sql = "INSERT INTO `user` (`username`, `password`) VALUES (%s, %s)"
        db.insert(sql, ["admin", "admin"])
        db.insert(sql, [["2", "3"], ["4", "5"]], True)
        sql = "SELECT * FROM user WHERE username = %s"
        print(db.select(sql, "admin"))
        sql = "SELECT * FROM user"
        print(db.select(sql))

    def tearDown(self):
        drop_sql = """DROP TABLE `user`;"""
        self.db.cur.execute(drop_sql)

if __name__ == '__main__':
    unittest.main()
