DROP TABLE IF EXISTS tblRabobankMaster;
CREATE TABLE tblRabobankMaster (id INTEGER PRIMARY KEY AUTOINCREMENT,
selfAccount VARCHAR(20) NOT NULL,
amount REAL NOT NULL,
crossAccount VARCHAR(20) NOT NULL,
debcred VARCHAR(10) NOT NULL,
description TEXT);

