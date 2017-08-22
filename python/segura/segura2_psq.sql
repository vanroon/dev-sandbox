-- Table: public."tblMaster"

-- DROP TABLE public."tblMaster";

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

-- Table: public."tblTransactionCategoryCodeMapping

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
