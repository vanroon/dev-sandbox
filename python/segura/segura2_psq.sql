-- Table: public."tbl_master"

DROP TABLE IF EXISTS public.tbl_master cascade;
DROP TABLE IF EXISTS public.tbl_transaction_category_code_mapping CASCADE;
DROP TABLE IF EXISTS public.tbl_bizniz_rulez CASCADE;
drop VIEW IF EXISTS public.vw_master CASCADE;
DROP VIEW IF EXISTS public.vw_checking CASCADE;
DROP VIEW IF EXISTS public.vw_saving CASCADE;



CREATE TABLE public.tbl_master
(
    id                      serial,
    selfaccount             character varying(50) COLLATE pg_catalog."default" NOT NULL,
    currency                character varying(10) COLLATE pg_catalog."default" NOT NULL,
    processdate             date NOT NULL,
    debcred                 character varying(10) COLLATE pg_catalog."default" NOT NULL,
    amount                  money NOT NULL,
    crossaccount            character varying(50) NOT NULL,
    crossaccountholder      character varying(100),
    interestdate            DATE,
    type                    character varying(10),
    unknown1                character varying(200),
    description1            character varying(200),
    description2            character varying(200),
    description3            character varying(200),
    description4            character varying(200),
    unknown2                character varying(200),
    unknown3                character varying(200),
    transactionreference    character varying(200),
    incassantid             character varying(50),
    kenmerkmachtiging       character varying(50),
    mssql_id                integer,
    CONSTRAINT tbl_master_pkey PRIMARY KEY (id)
);

-- Table: public."tbl_transaction_category_code_mapping

CREATE TABLE public.tbl_transaction_category_code_mapping
(
    id serial,
    masterid integer,
    categorycode character varying(10) COLLATE pg_catalog."default" NOT NULL,
    notes text COLLATE pg_catalog."default",
    CONSTRAINT tbl_transaction_category_code_mapping_pkey PRIMARY KEY (id),
    CONSTRAINT tbl_transaction_category_code_mapping_masterid_fkey FOREIGN KEY (masterid)
        REFERENCES public.tbl_master (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
-- Table: public."tblBiznezRulez"

CREATE TABLE public."tbl_bizniz_rulez"
(
    id serial,
    categorycode            character varying(10) NOT NULL,
    categorycodedescription character varying(255) NOT NULL,
    CONSTRAINT "tbl_bizniz_rulez_pkey" PRIMARY KEY (id)
);

CREATE VIEW vw_master AS
SELECT
	tbl_master.selfAccount,
	tbl_master.currency,
	tbl_master.processDate,
	CASE WHEN tbl_master.debcred = 'D' THEN
		tbl_master.amount * -1
	ELSE
		tbl_master.amount
	END AS amount,
	tbl_master.crossAccount,
	tbl_master.crossAccountHolder,
	tbl_master.interestDate,
	tbl_master.type,
	concat(
    	(SELECT coalesce(tbl_master.description1, '')),
        (SELECT coalesce(tbl_master.description2, '')),
        (SELECT coalesce(description3, '')),
    	(SELECT coalesce(description4, ''))
    ) AS description,
	tbl_master.transactionReference,
	tbl_master.incassantId,
	tbl_master.kenmerkmachtiging,
	tbl_master.id,
	tbl_master.mssql_id,
	tbl_transaction_category_code_mapping.categorycode
FROM tbl_master
LEFT JOIN tbl_transaction_category_code_mapping ON tbl_master.id=tbl_transaction_category_code_mapping.masterId;

CREATE VIEW vw_saving AS
select
    vw_master.selfAccount,
    vw_master.currency,
    vw_master.processDate,
    vw_master.amount,
    vw_master.crossAccount,
    vw_master.crossAccountHolder,
    vw_master.interestDate,
    vw_master.type,
    vw_master.description,
    vw_master.id,
    vw_master.categorycode
 FROM vw_master
 WHERE vw_master.selfAccount = 'NL44INGB1234567890';

CREATE VIEW vw_checking AS
select
    vw_master.selfAccount,
    vw_master.currency,
    vw_master.processDate,
    vw_master.amount,
    vw_master.crossAccount,
    vw_master.crossAccountHolder,
    vw_master.interestDate,
    vw_master.type,
    vw_master.description,
    vw_master.id,
    vw_master.categorycode
 FROM vw_master
 WHERE vw_master.selfAccount = 'NL44RABO1234567890';


 --Example queries
 
INSERT INTO tbl_master (selfAccount, currency, processDate, debcred, amount, crossAccount, description1) VALUES ('NL33RABO1234567890', 'EUR', '2017-01-01', 'D', 132, 'SE32haas19321932', '103-0, sparen');
INSERT INTO tbl_master (selfAccount, currency, processDate, debcred, amount, crossAccount, description1) VALUES ('NL33RABO1234567890', 'EUR', '2017-01-02', 'D', 132, 'SE32haas19321932', '104-1, Two wheeler');
INSERT INTO tbl_master (selfAccount, currency, processDate, debcred, amount, crossAccount, description1) VALUES ('NL33RABO1234567890', 'EUR', '2017-01-03', 'C', 28, 'SE32haas19321932', '105-2, electronics');
INSERT INTO tbl_master (selfAccount, currency, processDate, debcred, amount, crossAccount, description1) VALUES ('NL44INGB1234567890', 'EUR', '2017-01-04', 'C', 122, 'SE32haas19321932', '103-1, sparen');
INSERT INTO tbl_master (selfAccount, currency, processDate, debcred, amount, crossAccount, description1) VALUES ('NL44INGB1234567890', 'EUR', '2017-01-05', 'C', 122, 'SE32haas19321932', '103-5, EV');
INSERT INTO tbl_master (selfAccount, currency, processDate, debcred, amount, crossAccount, description1, description4) VALUES ('NL44INGB1234567890', 'EUR', '2017-01-06', 'D', 92, 'SE32haas19321932', 'Two wheeler 104-1', ' 4th description field!');
INSERT INTO tbl_transaction_category_code_mapping (masterId, categorycode, notes) VALUES (1, '103-0', 'some notes');
INSERT INTO tbl_transaction_category_code_mapping (masterId, categorycode, notes) VALUES (2, '104-1', 'some notes');
INSERT INTO tbl_transaction_category_code_mapping (masterId, categorycode, notes) VALUES (3, '105-2', 'some notes');
INSERT INTO tbl_transaction_category_code_mapping (masterId, categorycode, notes) VALUES (4, '103-1', 'some notes');
INSERT INTO tbl_transaction_category_code_mapping (masterId, categorycode, notes) VALUES (5, '103-5', 'some notes');
INSERT INTO tbl_transaction_category_code_mapping (masterId, categorycode, notes) VALUES (6, '104-1', 'some notes');
INSERT INTO tbl_bizniz_rulez (categorycode, categorycodedescription) VALUES ('103-0', 's_long_term');
INSERT INTO tbl_bizniz_rulez (categorycode, categorycodedescription) VALUES ('104-1', 's_long_term');
INSERT INTO tbl_bizniz_rulez (categorycode, categorycodedescription) VALUES ('105-2', 's_long_term');
INSERT INTO tbl_bizniz_rulez (categorycode, categorycodedescription) VALUES ('103-1', 's_long_term');
INSERT INTO tbl_bizniz_rulez (categorycode, categorycodedescription) VALUES ('103-5', 's_long_term');


