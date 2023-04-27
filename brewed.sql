CREATE TABLE `Employee` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `hourly_rate`   INTEGER NOT NULL
);

CREATE TABLE `Product` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL,
    `price` REAL NOT NULL
);

CREATE TABLE `Order` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `employee_id`   INTEGER NOT NULL,
    `product_id`   INTEGER NOT NULL,
    `timestamp` TIMESTAMP NOT NULL,

    FOREIGN KEY(`employee_id`) REFERENCES `Employee`(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`)
);

INSERT INTO `Employee` VALUES (null, 'Dale Gribble', 'governmentBad@texas.gov', 15);
INSERT INTO `Employee` VALUES (null, 'Sharon', 'governmentBad2@texas.gov', 16);

INSERT INTO `Product` VALUES (null, 'Squeek Toy', 20);
INSERT INTO `Product` VALUES (null, 'Holy Roller', 30);

INSERT INTO `Order` VALUES (null, 1, 2, 19991231);
INSERT INTO `Order` VALUES (null, 2, 1, 20000101);

SELECT o.id order_id, p.*, e.*
FROM `Order` o
JOIN Product p ON o.product_id = p.id
JOIN Employee e ON o.employee_id = e.id

SELECT 
    o.id,
    o.employee_id,
    o.product_id,
    e.name,
    e.hourly_rate,
    e.email,
    p.name,
    p.price,
    o.timestamp
FROM "order" o
INNER JOIN Employee e
    ON e.id = o.employee_id
INNER JOIN Product p
    ON p.id = o.product_id
