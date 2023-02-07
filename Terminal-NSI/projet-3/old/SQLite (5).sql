--DROP TABLE demo;
--DROP TABLE client;

CREATE TABLE "client"(
    "numero_du_client" INTEGER,
    "prenom" TEXT,
    "nom" TEXT,
    "age" INTEGER,
    "adresse" TEXT,
    "telephone" INTEGER,
  	"date_de_fin" INTEGER,
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
  	PRIMARY KEY("type_de_materiel")
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
  	"type_de_contract TEXT,
  	PRIMARY KEY("numero_employe")
);

CREATE TABLE "cours_collectif"(
    "nom_du_cours" TEXT,
  	PRIMARY KEY("numero_etablissement")
);

CREATE TABLE "cours_collectifs_possible"(
    "identifiant_du_cours" INTEGER,
  	PRIMARY KEY("Identifiant_du_cours")
);

CREATE TABLE "offre_abonnement"(
    "nom_abonnement" TEXT,
  	"prix" INTEGER,
  	"duree" INTEGER,
  	PRIMARY KEY("nom_abonnement")
);