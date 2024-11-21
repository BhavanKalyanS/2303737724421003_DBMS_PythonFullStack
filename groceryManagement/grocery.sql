CREATE DATABASE grocery_db;

USE grocery_db;

CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,        
    item_name VARCHAR(255) NOT NULL,           
    category VARCHAR(255) NOT NULL,            
    quantity INT NOT NULL,                   
    unit_price DECIMAL(10, 2) NOT NULL,        
    supplier_name VARCHAR(255),                
    entry_time DATETIME NOT NULL,              
);

INSERT INTO inventory (item_name, category, quantity, unit_price, supplier_name, entry_time)
VALUES
('Milk', 'Dairy', 100, 1.20, 'ABC Suppliers', NOW()),
('Bread', 'Bakery', 50, 0.80, 'XYZ Bakery', NOW()),
('Apples', 'Fruits', 200, 0.50, 'Fruit World', NOW()),
('Rice', 'Grains', 300, 0.90, 'Grain Mart', NOW());

select * from inventory;