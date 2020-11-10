import psycopg2
from Pysql import SQLConnect

class Transaction(SQLConnect):
    def __init__(self, user, password, host, port, database):
        super().__init__(user, password, host, port, database)

    def manageTransaction(self, prodId, upd_ProdId, upd_ProdId2):
        connection, cursor = super().connect()
        connection.autocommit = False
        
        # try:
        #     cursor.execute("ALTER TABLE Stock DROP CONSTRAINT fk_stock_prodid;")
        #     connection.commit()
        # except (Exception, psycopg2.Error) as error:
        #     connection.rollback()
        #     cursor.close()
        #     connection.close()
        #     return
        try:
            cursor.execute("ALTER TABLE Stock DROP CONSTRAINT fk_stock_prodid;")
            cursor.execute(f"UPDATE Products SET prod_id = \'{upd_ProdId}\' WHERE prod_id = \'{prodId}\';")
            cursor.execute(f"UPDATE Stock SET prod_id = \'{upd_ProdId}\' WHERE prod_id = \'{prodId}\';")
            cursor.execute("ALTER TABLE Stock ADD CONSTRAINT fk_stock_prodid FOREIGN KEY (prod_id) REFERENCES Products(prod_id);")
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            connection.rollback()
            super().connect_close(connection, cursor)
            
v = Transaction(user = "postgres", password = "user", host = "127.0.0.1", port = "5432", database = "test_db")
v.manageTransaction('p1', 'pp1', 'pp2')
