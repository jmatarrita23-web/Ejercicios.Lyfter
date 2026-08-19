

CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    Code INTEGER NOT NULL UNIQUE,
    Name TEXT NOT NULL,
    Price NUMERIC NOT NULL,
    Entry_Date TEXT NOT NULL,
    Brand TEXT NOT NULL,
    Stock_Available INTEGER NOT NULL DEFAULT 0
);


CREATE TABLE Shopping_Cart (
    CartID INTEGER PRIMARY KEY AUTOINCREMENT,
    Buyer_Email TEXT NOT NULL,
    Created_Date TEXT NOT NULL
);


CREATE TABLE Cart_Details (
    CartDetailID INTEGER PRIMARY KEY AUTOINCREMENT,
    CartID INTEGER NOT NULL,
    ProductID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    Unit_Price NUMERIC NOT NULL,
    Total_Amount NUMERIC NOT NULL,

    FOREIGN KEY (CartID) REFERENCES Shopping_Cart(CartID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


CREATE TABLE Invoices (
    InvoiceID INTEGER PRIMARY KEY AUTOINCREMENT,
    Invoice_Number TEXT NOT NULL UNIQUE,
    Purchase_Date TEXT NOT NULL,
    Buyer_Email TEXT NOT NULL,
    Total_Amount NUMERIC NOT NULL
);


CREATE TABLE Invoice_Details (
    DetailID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER NOT NULL,
    InvoiceID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    Unit_Price NUMERIC NOT NULL,
    Total_Amount NUMERIC NOT NULL,

    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID)
);



-- ALTER TABLE


ALTER TABLE Invoices
ADD COLUMN Buyer_Phone TEXT;

ALTER TABLE Invoices
ADD COLUMN Cashier_Employee_Code TEXT;



-- SELECT 1


SELECT *
FROM Products;



-- SELECT 2


SELECT *
FROM Products
WHERE Price > 50000;



-- SELECT 3



SELECT
    ID.DetailID,
    ID.InvoiceID,
    ID.ProductID,
    P.Name,
    ID.Quantity,
    ID.Unit_Price,
    ID.Total_Amount
FROM Invoice_Details AS ID
JOIN Products AS P
    ON ID.ProductID = P.ProductID
WHERE ID.ProductID = 1;


-- SELECT 4


SELECT
    P.ProductID,
    P.Name,
    SUM(ID.Quantity) AS Total_Quantity_Purchased
FROM Invoice_Details AS ID
JOIN Products AS P
    ON ID.ProductID = P.ProductID
GROUP BY P.ProductID, P.Name;


-- SELECT 5


SELECT *
FROM Invoices
WHERE Buyer_Email = 'cliente@gmail.com';



-- SELECT 6


SELECT *
FROM Invoices
ORDER BY Total_Amount DESC;



-- SELECT 7


SELECT *
FROM Invoices
WHERE Invoice_Number = 'FAC-001'
LIMIT 1;