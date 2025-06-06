CREATE TABLE IF NOT EXISTS orders (
    product_code TEXT NOT NULL PRIMARY KEY,
    product_name TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    order_date TEXT NOT NULL,
    delivery_time INTEGER NOT NULL CHECK(delivery_time BETWEEN 1 AND 10),
    order_cost REAL NOT NULL
);
