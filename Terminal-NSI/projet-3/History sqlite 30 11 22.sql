--- 30-11-2022 10:15:20
--- sqlite (1).db
SELECT * FROM client;

--- 30-11-2022 10:15:36
--- sqlite (1).db
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:18:25
--- sqlite (1).db
SELECT * FROM client;

--- 30-11-2022 10:20:00
--- sqlite (1).db
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:26:51
--- sqlite (1).db.1
/***** ERROR ******
no such table: nom_abonnement
 ----- 
--INSERT INTO "nom_abonnement"
--VALUES (
--	"nom", --nom_abonnement
--	20, --prix
--  	1 --duree 
--);
UPDATE "nom_abonnement"
SET
nom_abonnement ="chouette"
WHERE
"ALL-INCLUSIVE 3";
*****/

--- 30-11-2022 10:27:10
--- sqlite (1).db.1
--INSERT INTO "nom_abonnement"
--VALUES (
--	"nom", --nom_abonnement
--	20, --prix
--  	1 --duree 
--);
UPDATE "offre_abonnement"
SET
nom_abonnement ="chouette"
WHERE
"ALL-INCLUSIVE 3";

--- 30-11-2022 10:27:16
--- sqlite (1).db.1
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:29:09
--- sqlite (1).db.2
/***** ERROR ******
no such column: attribut1
 ----- 
UPDATE "offre_abonnement"
SET
attribut1 ="BASIQ 1",
attribut2 ="chose"
WHERE
"nom_abonnement";
*****/

--- 30-11-2022 10:30:49
--- sqlite (1).db.2
/***** ERROR ******
near "WHERE": syntax error
 ----- 
UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
WHERE
"BASIQ 1";
*****/

--- 30-11-2022 10:34:29
--- sqlite (1).db.2
/***** ERROR ******
near "WHERE": syntax error
 ----- 
UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix ="a",
duree ="a",
WHERE
"BASIQ 1";
*****/

--- 30-11-2022 10:35:34
--- sqlite (1).db.2
/***** ERROR ******
near "WHERE": syntax error
 ----- 
UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix ="a",
duree ="a",
WHERE
1;
*****/

--- 30-11-2022 10:35:42
--- sqlite (1).db.2
/***** ERROR ******
near "WHERE": syntax error
 ----- 
UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix ="a",
duree ="a",
WHERE 1;
*****/

--- 30-11-2022 10:35:47
--- sqlite (1).db.2
/***** ERROR ******
near "WHERE": syntax error
 ----- 
UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix ="a",
duree ="a",
WHERE 1;
*****/

--- 30-11-2022 10:37:57
--- sqlite (1).db.2
/***** ERROR ******
near "WHERE": syntax error
 ----- 
UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix ="a",
duree ="a",
WHERE nom_abonnement = "abonnement black friday";
*****/

--- 30-11-2022 10:39:27
--- sqlite (1).db.1
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:39:53
--- sqlite (1).db.2
/***** ERROR ******
no such table: nom_abonnement
 ----- 
INSERT INTO "nom_abonnement"
VALUES (
    "abonnement black friday", --nom_abonnement
    20, --prix
      1 --duree 
);

UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix =25,
duree =1,
WHERE 
nom_abonnement = "abonnement black friday";
*****/

--- 30-11-2022 10:42:13
--- sqlite (1).db.2
/***** ERROR ******
near "WHERE": syntax error
 ----- 
INSERT INTO "offre_abonnement"
VALUES (
    "abonnement black friday", --nom_abonnement
    20, --prix
      1 --duree 
);

UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix =25,
duree =1,
WHERE 
nom_abonnement = "abonnement black friday";
*****/

--- 30-11-2022 10:43:38
--- sqlite (1).db.2
/***** ERROR ******
UNIQUE constraint failed: offre_abonnement.nom_abonnement
 ----- 
INSERT INTO "offre_abonnement"
VALUES (
    "abonnement black friday", --nom_abonnement
    20, --prix
      1 --duree 
);

UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix =25,
duree =1
WHERE 
nom_abonnement = "abonnement black friday";
*****/

--- 30-11-2022 10:43:52
--- sqlite (1).db.1
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:44:29
--- sqlite (1).db.2
/***** ERROR ******
UNIQUE constraint failed: offre_abonnement.nom_abonnement
 ----- 
INSERT INTO "offre_abonnement"
VALUES (
    "abonnement black friday", --nom_abonnement
    20, --prix
      1 --duree 
);

UPDATE "offre_abonnement"
SET
nom_abonnement ="a",
prix =25,
duree =1
WHERE 
nom_abonnement = "abonnement black friday";
*****/

--- 30-11-2022 10:45:11
--- sqlite (1).db.2
/***** ERROR ******
UNIQUE constraint failed: offre_abonnement.nom_abonnement
 ----- 
INSERT INTO "offre_abonnement"
VALUES (
    "abonnement black friday", --nom_abonnement
    20, --prix
      1 --duree 
);

UPDATE offre_abonnement
SET
nom_abonnement ="a",
prix =25,
duree =1
WHERE 
nom_abonnement = "abonnement black friday";
*****/

--- 30-11-2022 10:45:30
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

UPDATE offre_abonnement
SET
nom_abonnement ="a",
prix =25,
duree =1
WHERE 
nom_abonnement = "abonnement black friday";

--- 30-11-2022 10:45:38
--- sqlite (1).db.1
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:55:44
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

INSERT INTO "offre_abonnement"
VALUES (
    "NOEL 2021", --nom_abonnement
    150, --prix
      12 --duree 
);

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "abonnement black friday";

--- 30-11-2022 10:55:47
--- sqlite (1).db.1
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:55:56
--- sqlite (1).db.2
/***** ERROR ******
UNIQUE constraint failed: offre_abonnement.nom_abonnement
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

INSERT INTO "offre_abonnement"
VALUES (
    "NOEL 2021", --nom_abonnement
    150, --prix
      12 --duree 
);

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "abonnement black friday";
*****/

--- 30-11-2022 10:57:22
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "abonnement black friday";

--- 30-11-2022 10:57:27
--- sqlite (1).db.1
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:57:39
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "abonnement black friday";

--- 30-11-2022 10:57:40
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "abonnement black friday";

--- 30-11-2022 10:57:41
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "abonnement black friday";

--- 30-11-2022 10:57:41
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "abonnement black friday";

--- 30-11-2022 10:57:45
--- sqlite (1).db.1
SELECT * FROM offre_abonnement;

--- 30-11-2022 10:58:49
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "NOEL 2021";

--- 30-11-2022 10:59:07
--- sqlite (1).db.1
SELECT * FROM offre_abonnement;

--- 30-11-2022 11:21:39
--- sqlite (1).db.2
/***** ERROR ******
no such column: attribut
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT
prix ,
duree
FROM "offre_abonnement"
ORDER BY
attribut;
*****/

--- 30-11-2022 11:22:10
--- sqlite (1).db.2
/***** ERROR ******
near "FROM": syntax error
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT
"1" ,
FROM "offre_abonnement"
ORDER BY
"duree";
*****/

--- 30-11-2022 11:23:07
--- sqlite (1).db.2
/***** ERROR ******
near "FROM": syntax error
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT
duree = "1" ,
FROM "offre_abonnement"
ORDER BY
"duree";
*****/

--- 30-11-2022 11:24:31
--- sqlite (1).db.3
SELECT * FROM client;

--- 30-11-2022 11:29:02
--- SQLite.1 (1).sql
/***** ERROR ******
no such table: demo
 ----- 
DROP TABLE demo;
--DROP TABLE client;

CREATE TABLE "client"(
    "numero_du_client" INTEGER,
    "prenom" TEXT,
    "nom" TEXT,
    "age" INTEGER,
    "adresse" TEXT,
    "telephone" INTEGER,
  	"date_de_fin" TEXT,
  	PRIMARY KEY("numero_du_client")
);

CREATE TABLE "passage"(
    "numero_du_passage" INTEGER,
    "date" TEXT,
  	PRIMARY KEY("numero_du_passage")
);

CREATE TABLE "materiel"(
    "numero_du_materiel" INTEGER,
    "poids" TEXT,
  	"taille" INTEGER,
  	"emplacement" TEXT,
  	PRIMARY KEY("numero_du_materiel")
);

CREATE TABLE "type_de_materiel"(
    "nom_du_materiel" TEXT,
  	PRIMARY KEY("nom_du_materiel")
);

CREATE TABLE "etablissement"(
    "numero_etablissement" INTEGER,
  	PRIMARY KEY("numero_etablissement")
);

CREATE TABLE "employe"(
    "numero_employe" INTEGER,
  	"prenom" TEXT,
  	"nom" TEXT,
  	"age" INTEGER,
  	"adresse" TEXT,
  	"telephone" INTEGER,
  	"date_arrivee" TEXT,
  	"type_de_contract" TEXT,
  	PRIMARY KEY("numero_employe")
);

CREATE TABLE "cours_collectif"(
    "nom_du_cours" TEXT,
  	PRIMARY KEY("nom_du_cours")
);

CREATE TABLE "cours_collectifs_possible"(
    "identifiant_du_cours" INTEGER,
  	PRIMARY KEY("identifiant_du_cours")
);

CREATE TABLE "offre_abonnement"(
    "nom_abonnement" TEXT,
  	"prix" INTEGER,
  	"duree" INTEGER,
  	PRIMARY KEY("nom_abonnement")
);

ALTER TABLE "client" ADD COLUMN "nom_abonnement" TEXT REFERENCES "offre_abonnement"("nom_abonnement");
ALTER TABLE "passage" ADD COLUMN "numero_du_client" TEXT REFERENCES "client"("numero_du_client");
ALTER TABLE "passage" ADD COLUMN "numero_etablissement" TEXT REFERENCES "etablissement"("numero_etablissement");
ALTER TABLE "materiel" ADD COLUMN "numero_etablissement" TEXT REFERENCES "etablissement"("numero_etablissement");
ALTER TABLE "materiel" ADD COLUMN "nom_du_materiel" TEXT REFERENCES "type_de_materiel"("nom_du_materiel");
ALTER TABLE "employe" ADD COLUMN "numero_etablissement" TEXT REFERENCES "etablissement"("numero_etablissement");
ALTER TABLE "cours_collectif" ADD COLUMN "numero_employe" TEXT REFERENCES "employe"("numero_employe");
ALTER TABLE "cours_collectifs_possible" ADD COLUMN "nom_abonnement" TEXT REFERENCES "abonnement"("nom_abonnement");
ALTER TABLE "cours_collectifs_possible" ADD COLUMN "nom_du_cours" TEXT REFERENCES "cours_collectif"("nom_du_cours");

INSERT INTO "client"
VALUES (
	1,
	"Josette",
  	"BALMAIN",
  	63,
  	"6, rue de la fontaine, Paris",
  	0654789532,
	"21/12/22",
  	1
);

INSERT INTO "client"
VALUES (
	1,
	"Josette",
  	"BALMAIN",
  	63,
  	"6, rue de la fontaine, Paris",
  	0654789532,
	"21/12/22",
  	1
);

VALUES (
	1,
	"Régis",
  	"BORDEAUX",
  	46,
  	"4, rue Jobert, Bernartini",
  	0414763429,
	"27/09/23",
  	3
);
*****/

--- 30-11-2022 11:29:42
--- sqlite (1).db
/***** ERROR ******
UNIQUE constraint failed: client.numero_du_client
 ----- 
INSERT INTO "client"
VALUES (
	1,
	"Régis",
  	"BORDEAUX",
  	46,
  	"4, rue Jobert, Bernartini",
  	0414763429,
	"27/09/23",
  	3
);
*****/

--- 30-11-2022 11:29:53
--- sqlite (1).db
INSERT INTO "client"
VALUES (
	3,
	"Régis",
  	"BORDEAUX",
  	46,
  	"4, rue Jobert, Bernartini",
  	0414763429,
	"27/09/23",
  	3
);

--- 30-11-2022 11:29:59
--- sqlite (1).db
SELECT * FROM client;

--- 30-11-2022 11:33:08
--- sqlite (1).db.2
/***** ERROR ******
near "FROM": syntax error
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT
duree = "1" ,
FROM "offre_abonnement"
where
"duree";
*****/

--- 30-11-2022 11:33:36
--- sqlite (1).db.2
/***** ERROR ******
near "FROM": syntax error
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT
duree,
FROM "offre_abonnement"
where
"duree";
*****/

--- 30-11-2022 11:33:48
--- sqlite (1).db.2
/***** ERROR ******
near "FROM": syntax error
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT
"duree",
FROM "offre_abonnement"
where
"duree";
*****/

--- 30-11-2022 11:34:15
--- sqlite (1).db.2
/***** ERROR ******
near "FROM": syntax error
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT
"duree",
FROM "offre_abonnement"
where
duree = 1;
*****/

--- 30-11-2022 11:35:38
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT "duree"
FROM "offre_abonnement"
where
duree = 1;

--- 30-11-2022 11:35:52
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT *
FROM "offre_abonnement"
where
duree = 1;

--- 30-11-2022 11:37:11
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

SELECT "nom_abonnement"
FROM "offre_abonnement"
where
duree = 1;

--- 30-11-2022 11:39:35
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

--SELECT "nom_abonnement"
--FROM "offre_abonnement"
--where duree = 1;

SELECT *
FROM "offre_abonnement"
where prix > 150;

--- 30-11-2022 11:39:43
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

--SELECT "nom_abonnement"
--FROM "offre_abonnement"
--where duree = 1;

SELECT *
FROM "offre_abonnement"
where prix < 150;

--- 30-11-2022 11:47:51
--- sqlite (1).db.3
SELECT * FROM client;

--- 30-11-2022 11:48:14
--- sqlite (1).db.2
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

--SELECT "nom_abonnement"
--FROM "offre_abonnement"
--where duree = 1;

--SELECT *
--FROM "offre_abonnement"
--where prix < 150;

SELECT "nom_abonnement" FROM client;

--- 30-11-2022 11:55:51
--- sqlite (1).db.2
/***** ERROR ******
ambiguous column name: nom_abonnement
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

--SELECT "nom_abonnement"
--FROM "offre_abonnement"
--where duree = 1;

--SELECT *
--FROM "offre_abonnement"
--where prix < 150;

--SELECT "nom_abonnement" FROM client 

SELECT "nom_abonnement"
FROM client
INNER JOIN offre_abonnement
ON client."nom_abonnement" = offre_abonnement."nom_abonnement";
*****/

--- 30-11-2022 11:56:11
--- sqlite (1).db.2
/***** ERROR ******
ambiguous column name: nom_abonnement
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

--SELECT "nom_abonnement"
--FROM "offre_abonnement"
--where duree = 1;

--SELECT *
--FROM "offre_abonnement"
--where prix < 150;

--SELECT "nom_abonnement" FROM client 

SELECT "nom_abonnement"
FROM client
INNER JOIN offre_abonnement;
--ON client."nom_abonnement" = offre_abonnement."nom_abonnement";
*****/

--- 30-11-2022 11:56:38
--- sqlite (1).db.2
/***** ERROR ******
ambiguous column name: nom_abonnement
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

--SELECT "nom_abonnement"
--FROM "offre_abonnement"
--where duree = 1;

--SELECT *
--FROM "offre_abonnement"
--where prix < 150;

--SELECT "nom_abonnement" FROM client 

SELECT "nom_abonnement"
FROM "client"
INNER JOIN "offre_abonnement";
--ON client."nom_abonnement" = offre_abonnement."nom_abonnement";
*****/

--- 30-11-2022 11:56:51
--- sqlite (1).db.2
/***** ERROR ******
ambiguous column name: nom_abonnement
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

--SELECT "nom_abonnement"
--FROM "offre_abonnement"
--where duree = 1;

--SELECT *
--FROM "offre_abonnement"
--where prix < 150;

--SELECT "nom_abonnement" FROM client 

SELECT "nom_abonnement"
FROM "client"
INNER JOIN "offre_abonnement";
ON client."nom_abonnement" = offre_abonnement."nom_abonnement";
*****/

--- 30-11-2022 12:00:04
--- sqlite (1).db.2
/***** ERROR ******
ambiguous column name: nom_abonnement
 ----- 
--INSERT INTO "offre_abonnement"
--VALUES (
--    "abonnement black friday", --nom_abonnement
--    20, --prix
--      1 --duree 
--);

--UPDATE offre_abonnement
--SET
--	nom_abonnement ="CLASSIQUE",
--	prix = 40,
--	duree = 3
--WHERE 
--	nom_abonnement = "abonnement black friday";

--INSERT INTO "offre_abonnement"
--VALUES (
--    "NOEL 2021", --nom_abonnement
--    150, --prix
--      12 --duree 
--);

--DELETE FROM "offre_abonnement" 
--WHERE nom_abonnement = "NOEL 2021";

--SELECT "nom_abonnement"
--FROM "offre_abonnement"
--where duree = 1;

--SELECT *
--FROM "offre_abonnement"
--where prix < 150;

--SELECT "nom_abonnement" FROM client 

SELECT nom_abonnement
FROM client
INNER JOIN offre_abonnement
ON client.nom_abonnement = offre_abonnement.nom_abonnement;
*****/

