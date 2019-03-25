CREATE TABLE cards (id INT NOT NULL AUTO_INCREMENT, 
            name VARCHAR(50), 
            set_code VARCHAR(50),
            image_uri VARCHAR(50),
            picks INT,
            appearances INT,
            layout VARCHAR(50),
            PRIMARY KEY ( id ) 
            ) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;  

