from Pysql import SQLConnect
import psycopg2

class InsertIntoDB(SQLConnect):
    def insertIntoStockTable(self):
        connection, cursor = super().connect()
        try:
            cursor.execute("INSERT INTO  Stock VALUES ('p1', 'd1', 1000);")
            cursor.execute("INSERT INTO  Stock VALUES ('p1', 'd2', -100);")
            cursor.execute("INSERT INTO  Stock VALUES ('p1', 'd4', 1200);")
            cursor.execute("INSERT INTO  Stock VALUES ('p3', 'd1', 3000);")
            cursor.execute("INSERT INTO  Stock VALUES ('p3', 'd4', 2000);")
            cursor.execute("INSERT INTO  Stock VALUES ('p2', 'd4', 1500);")
            cursor.execute("INSERT INTO  Stock VALUES ('p2', 'd1', -400);")
            cursor.execute("INSERT INTO  Stock VALUES ('p2', 'd2', 2000);")
            connection.commit()
            return True
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
            return False

    def insertIntoProductsTable(self):
        connection, cursor = super().connect()
        try:
            cursor.execute("INSERT INTO  Products VALUES ('p1', 'tape', 2.5);")
            cursor.execute("INSERT INTO  Products VALUES ('p2', 'tv', 250);")
            cursor.execute("INSERT INTO  Products VALUES ('p3', 'vcr', 80);")
            connection.commit()
            return True
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
            return False

    def insertIntoDepotTable(self):
        connection, cursor = super().connect()
        try:
            cursor.execute("INSERT INTO  Depot VALUES ('d1', 'New York', 9000);")
            cursor.execute("INSERT INTO  Depot VALUES ('d2', 'Syracuse', 6000);")
            cursor.execute("INSERT INTO  Depot VALUES ('d4', 'New York', 2000);")
            connection.commit()
            return True
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
            return False
