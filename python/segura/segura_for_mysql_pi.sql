CREATE DATABASE IF NOT EXISTS SEGURA;
USE SEGURA;
DROP TABLE IF EXISTS tblBiznizRulez;
DROP TABLE IF EXISTS tblTransactionCategoryCodeMapping;
DROP TABLE IF EXISTS tblMaster;

CREATE TABLE tblMaster (id INTEGER AUTO_INCREMENT NOT NULL,
selfAccount VARCHAR(50) NOT NULL,
currency VARCHAR(10) NOT NULL,
processDate DATE NOT NULL,
debcred VARCHAR(10) NOT NULL,
amount NUMERIC(15,2) NOT NULL,
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
kenmerkMachtiging VARCHAR (50),
raboOriginal TINYINT(1) DEFAULT 1,
MssqlId INT,
PRIMARY KEY (id));

CREATE TABLE tblTransactionCategoryCodeMapping (
id INT NOT NULL AUTO_INCREMENT,
masterId INT NOT NULL UNIQUE,
categoryCode VARCHAR(10) NOT NULL,
notes TEXT,
PRIMARY KEY (id),
FOREIGN KEY (masterId) REFERENCES tblMaster(id));

CREATE TABLE tblBiznizRulez (
id INT NOT NULL AUTO_INCREMENT,
categoryCode VARCHAR(10) NOT NULL,
categoryDescription VARCHAR(255) NOT NULL,
PRIMARY KEY (id));

DROP VIEW IF EXISTS vwMaster;
CREATE VIEW vwMaster AS
SELECT
	tblMaster.selfAccount,
	tblMaster.currency,
	tblMaster.processDate,
	CASE WHEN tblMaster.debcred = 'D' THEN
		tblMaster.amount * -1
	ELSE
		tblMaster.amount
	END AS amount,
	tblMaster.crossAccount,
	tblMaster.crossAccountHolder,
	tblMaster.interestDate,
	tblMaster.typ,
	CONCAT(
	IFNULL(tblMaster.description1, ''), 
	IFNULL(tblMaster.description2, ''), 
	IFNULL(tblMaster.description3, ''), 
	IFNULL(tblMaster.description4, '')) AS description,
	tblMaster.transactionReference,
	tblMaster.incassantId,
	tblMaster.kenmerkMachtiging,
	tblMaster.raboOriginal,
	tblMaster.id,
	tblMaster.MssqlId,
	tblTransactionCategoryCodeMapping.categoryCode
FROM tblMaster
LEFT JOIN tblTransactionCategoryCodeMapping ON tblMaster.id=tblTransactionCategoryCodeMapping.masterId;


DROP VIEW IF EXISTS vwSaving;
CREATE VIEW vwSaving AS
SELECT
    vwMaster.selfAccount,
    vwMaster.currency,
    vwMaster.processDate,
    vwMaster.amount,
    vwMaster.crossAccount,
    vwMaster.crossAccountHolder,
    vwMaster.interestDate,
    vwMaster.typ,
    vwMaster.description,
    vwMaster.id,
    vwMaster.categoryCode,
    vwMaster.MssqlId
FROM vwMaster
WHERE vwMaster.selfAccount = 'NL33RABO3152168691';

DROP VIEW IF EXISTS vwChecking;
CREATE VIEW vwChecking AS
SELECT
    vwMaster.selfAccount,
    vwMaster.currency,
    vwMaster.processDate,
    vwMaster.amount,
    vwMaster.crossAccount,
    vwMaster.crossAccountHolder,
    vwMaster.interestDate,
    vwMaster.typ,
    vwMaster.description,
    vwMaster.id,
    vwMaster.categoryCode,
	vwMaster.MssqlId
FROM vwMaster
WHERE vwMaster.selfAccount = 'NL44RABO0363964991';
