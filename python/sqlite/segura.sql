DROP TABLE IF EXISTS tblRabobankMaster;
CREATE TABLE tblRabobankMaster (id INTEGER PRIMARY KEY AUTOINCREMENT,
selfAccount VARCHAR(20) NOT NULL,
amount REAL NOT NULL,
crossAccount VARCHAR(20) NOT NULL,
description TEXT);
INSERT INTO tblRabobankMaster (selfAccount, amount, crossAccount, description) VALUES ('NL12RABO123456', 103, 'NL32HAAS004031932', 'contributie');
