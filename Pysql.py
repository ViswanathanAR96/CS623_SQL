import psycopg2

class SQLConnect:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        #connection, cursor = self.connect()
        #self.connect_close(connection, cursor)
    
    def connect(self):
        try:
            connection = psycopg2.connect(user = self.user,
                                        password = self.password,
                                        host = self.host,
                                        port = self.port,
                                        database = self.database)

            cursor = connection.cursor()
            # Print PostgreSQL Connection properties
                      
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        return connection, cursor

    def connect_close(self, connection, cursor):
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

# a = SQLConnect(user = "postgres", password = "user", host = "127.0.0.1", port = "5432", database = "test_db")
# connection, cursor = a.connect()
# a.connect_close(connection, cursor)

