from SqlCreate import CreateTables
from InsertRecords import InsertIntoDB

class Setup():
    def __init__(self):
        self.user = "postgres"
        self.password = "user"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "test_db"   
        
    def setup(self):
        prodCreated = depCreated = stockCreated = False
        createObj = CreateTables(self.user, self.password, self.host, self.port, self.database)
        prodCreated = createObj.createProductsTable()
        if prodCreated == True:
            depCreated = createObj.createDepotTable()
        if depCreated == True:
            stockCreated = createObj.createStockTable()
            return stockCreated
        return False

    def insert(self):
        prodInserted = depInserted = stockInserted = False
        if self.setup() == True:
            insertObj = InsertIntoDB(self.user, self.password, self.host, self.port, self.database)
            prodInserted = insertObj.insertIntoProductsTable()
            if prodInserted == True:
                depInserted = insertObj.insertIntoDepotTable()
            if depInserted == True:
                stockInserted = insertObj.insertIntoStockTable()
                return stockInserted

obj = Setup()
print(obj.insert())   

