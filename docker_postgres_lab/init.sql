-- Initialisatie script voor PostgreSQL database
-- Dit script wordt automatisch uitgevoerd bij eerste start

-- Maak users tabel aan
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Maak products tabel aan
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Voeg test data toe aan users tabel
INSERT INTO users (name, email) VALUES 
    ('John Doe', 'john@example.com'),
    ('Jane Smith', 'jane@example.com'),
    ('Bob Johnson', 'bob@example.com'),
    ('Alice Williams', 'alice@example.com'),
    ('Charlie Brown', 'charlie@example.com');

-- Voeg test data toe aan products tabel
INSERT INTO products (name, price, stock) VALUES 
    ('Laptop', 899.99, 15),
    ('Mouse', 29.99, 50),
    ('Keyboard', 79.99, 30),
    ('Monitor', 299.99, 20),
    ('Webcam', 89.99, 25);

-- Maak een view voor product overzicht
CREATE VIEW product_summary AS
SELECT 
    name,
    price,
    stock,
    (price * stock) AS total_value
FROM products;
