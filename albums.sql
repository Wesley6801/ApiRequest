CREATE DATABASE IF NOT EXISTS album_info;

CREATE TABLE albums( 
    id INT(8) UNSIGNED NOT NULL auto_increment,
    name VARCHAR(255) default NULL,
    release_date DATE,
    PRIMARY KEY (id)
) AUTO_INCREMENT=1;