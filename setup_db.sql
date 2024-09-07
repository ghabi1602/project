-- prepare and configure new database

CREATE database IF NOT EXISTS tvs_db;
CREATE user IF NOT EXISTS 'tvs_admin'@'localhost' IDENTIFIED BY 'betty';
GRANT ALL PRIVILEGES ON tvs_db.* TO 'tvs_admin'@'localhost';
GRANT SELECT ON performance_schema.* TO 'tvs_admin'@'localhost';
FLUSH PRIVILEGES;