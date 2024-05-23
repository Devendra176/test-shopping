CREATE TABLE product(id integer primary key, name text, cost int);

INSERT INTO product
VALUES
    (1, 'Alihotsy Draught', 30),
    (2, 'Anti-Paralysis Potion', 40),
    (3, 'Antidote to Veritaserum', 50),
    (4, 'Amortentia', 500);

-- TODO: Add new tables

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    buyer TEXT NOT NULL,
    cost INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id)
);