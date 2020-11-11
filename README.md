# CS627_SQL
SQL with Python Project Repository

## Schema
![Schema](https://github.com/ViswanathanAR96/CS627_SQL/blob/maseter_v2/Drawing1.jpg)

## Reducing Schema to Entity Relationship
- Product (prodId, pname, price)/
- Depot (depId, addr, volume)/
- Stock (prodId, depId, quantity)/

### Algorithm
- 	Product has Stock (1N):\
    Stock (quantity, depId)\
    *Since prodId is the PK(Product) and FK(Stock) - > Removing prodId from the Stock table*\
    Product (prodId, pname, price)
- 	Stock stored in Depot (N1)\
    Stock (quantity)\
    *Since depId is the PK(Depot) and FK(Stock) -> Removing depId from Stock Table*\
    Depot(depId, addr, volume)

### Entity Relationship
- Product (prodId, pname, price), PK = prodId
- Depot (depId, addr, volume), PK = depId
- Stock (quantity)

## ER Diagram
![ER Diagram](https://github.com/ViswanathanAR96/CS627_SQL/blob/maseter_v2/ERDiagram.jpg)
