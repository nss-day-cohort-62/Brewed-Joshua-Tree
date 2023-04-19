CREATE TABLE `Employee` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `hourly_rate`   INTEGER NOT NULL
);

CREATE TABLE `Product` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL,
    `price` FLOAT NOT NULL
);

CREATE TABLE `Order` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `employee_id`   INTEGER NOT NULL,
    `product_id`   INTEGER NOT NULL,
    `timestamp` TIMESTAMP NOT NULL,

    FOREIGN KEY(`employee_id`) REFERENCES `Employee`(`id`),
    FOREIGN KEY(`product_id`) REFERENCES `Product`(`id`)
);