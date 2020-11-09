import psycopg2
from Pysql import SQLConnect
# def createStockTable(self, cursor):
#         cursor.execute("SELECT version();")
#         record = cursor.fetchone()
#         print("You are connected to - ", record,"\n")

class CreateTables(SQLConnect):
    def __init__(self, user, password, host, port, database):
        super().__init__(user, password, host, port, database)

    def createStockTable(self):
        connection, cursor = super().connect()
        try:
            cursor.execute("CREATE TABLE Stock (prod_id VARCHAR(5), dep_id VARCHAR(5), quantity INTEGER);")
            cursor.execute("ALTER TABLE Stock ADD CONSTRAINT fk_Stock_prodid FOREIGN KEY (prod_id)  REFERENCES Products(prod_id);")
            cursor.execute("ALTER TABLE Stock ADD CONSTRAINT fk_Stock_depid FOREIGN KEY (dep_id)  REFERENCES Depot(dep_id);")
            connection.commit()
            return True
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
            return False

    def createProductsTable(self):
        connection, cursor = super().connect()
        try:
            cursor.execute("CREATE TABLE Products (prod_id VARCHAR(5), pname VARCHAR(50), price INTEGER);")
            cursor.execute("ALTER TABLE Products ADD CONSTRAINT pk_Product_prodid PRIMARY KEY (prod_id);")
            connection.commit()
            return True
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
            return False

    def createDepotTable(self):
        connection, cursor = super().connect()
        try:
            cursor.execute("CREATE TABLE Depot (dep_id VARCHAR(5), addr VARCHAR(50), volume INTEGER);")
            cursor.execute("ALTER TABLE Depot ADD CONSTRAINT pk_Depot_depid PRIMARY KEY (dep_id);")
            connection.commit()
            return True
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
            return False

#d = CreateTables(user = "postgres", password = "user", host = "127.0.0.1", port = "5432", database = "test_db")
#d.test()