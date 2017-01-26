--CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

--drop table "data"

CREATE TABLE "data"
(
  id uuid NOT NULL,
  date int NULL,
  key int NULL,
  name character varying(256) NULL,
  value numeric NULL,
  CONSTRAINT data_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "data"
  OWNER TO pt;


select * from data

insert into data
select uuid_generate_v4(),20170101,1,'A',10.00
union select uuid_generate_v4(),20170101,2,'B',20.00