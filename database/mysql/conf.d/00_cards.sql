CREATE TABLE IF NOT EXISTS cards (id INT NOT NULL AUTO_INCREMENT, 
            name VARCHAR(100), 
            set_code VARCHAR(50),
            image_uri VARCHAR(100),
            picks INT,
            appearances INT,
            layout VARCHAR(50),
            PRIMARY KEY ( id ) 
            ) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;  

INSERT IGNORE INTO cards VALUES (1, 'Animate Wall', 'lea', '001-Animate-Wall', 0, 0, 'normal');