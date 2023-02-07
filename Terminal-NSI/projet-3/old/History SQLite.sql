--- 29-11-2022 17:00:49
--- SQLite
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

--- 29-11-2022 17:01:15
--- SQLite
SELECT * FROM client;

