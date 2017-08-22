DROP DATABASE IF EXISTS SEGURA;
CREATE DATABASE SEGURA;
DROP TABLE IF EXISTS tblMaster;
CREATE TABLE tblMaster (id INTEGER PRIMARY KEY AUTOINCREMENT,
selfAccount VARCHAR(50) NOT NULL,
currency VARCHAR(10) NOT NULL,
processDate DATE NOT NULL,
debcred VARCHAR(10) NOT NULL,
amount REAL NOT NULL,
crossAccount VARCHAR(50) NOT NULL,
crossAccountHolder VARCHAR (100),
interestDate DATE,
typ VARCHAR(10),
unknown1 VARCHAR(200),
description1 VARCHAR(200),
description2 VARCHAR(200),
description3 VARCHAR(200),
description4 VARCHAR(200),
unknown2 VARCHAR(200),
unknown3 VARCHAR(200),
transactionReference VARCHAR(200),
incassantId VARCHAR(50),
kenmerkMachtiging VARCHAR (50));

DROP VIEW IF EXISTS vwSaving;
CREATE VIEW vwSaving AS
SELECT
    tblMaster.selfAccount,
    tblMaster.currency,
    tblMaster.processDate,
    tblMaster.debcred,
    CASE WHEN
        tblMaster.debcred = 'D' THEN
            tblMaster.amount * -1
        ELSE
            tblMaster.amount
        END AS amount,
    tblMaster.crossAccount,
    tblMaster.crossAccountHolder,
    tblMaster.interestDate,
    tblMaster.typ,
    IFNULL(tblMaster.description1, '') ||
    IFNULL(tblMaster.description2, '') ||
    IFNULL(tblMaster.description3, '') ||
    IFNULL(tblMaster.description4, '') AS description,
    tblMaster.id
FROM tblMaster
WHERE tblMaster.selfAccount = 'NL33RABO3152168691'
