DROP TABLE demo;

CREATE TABLE "jeu" (
  "id_jeu" INTEGER,
  "nom" TEXT,
  "prix" INTEGER,
  "plateforme" TEXT,
  "stock" BOOLEAN,
  "telechargement_digital" BOOLEAN,
  PRIMARY KEY("id_jeu")
);

CREATE TABLE "plateforme" (
  "nom_plateforme" TEXT,
  "launcher" TEXT,
  PRIMARY KEY("nom_plateforme")
  );
 
CREATE TABLE "client" (
  "id_client" INTEGER,
  "nom" TEXT,
  "prenom" TEXT,
  "email" TEXT,
  "mot_de_passe" TEXT,
  "date_de_naissance" INTEGER,
  "pays" TEXT,
  PRIMARY KEY("id_client")
);

CREATE TABLE "article" (
  "id_article" INTEGER,
  "nom_du_jeu" TEXT,
  "plateforme_du_jeu" TEXT,
  "id_jeu" INT,
  "nom_plateforme" TEXT,
  PRIMARY KEY("id_article")
  FOREIGN KEY("id_jeu") REFERENCES "jeu"("id_jeu")
  FOREIGN KEY("nom_plateforme") REFERENCES "plateforme"("nom_plateforme")
);

CREATE TABLE "commande" (
  "id_commande" INTEGER,
  "jeu" TEXT,
  "prix" INTEGER,
  "client" TEXT,
  "date_de_livraison" TEXT,
  "adresse_de_livraison" TEXT,
  "id_client" INTEGER,
  PRIMARY KEY("id_commande")
  FOREIGN KEY("id_client") REFERENCES "client"("id_client")
);

CREATE TABLE "article_commande"(
  "id" INTEGER,
  "id_article" INTEGER,
  "id_commande" INTEGER,
  PRIMARY KEY("id")
  FOREIGN KEY("id_article") REFERENCES "article"("id_article")
  FOREIGN KEY("id_commande") REFERENCES "commande"("id_commande")
);

INSERT INTO jeu VALUES(21896,'Pokémon Violet',60,'Switch',TRUE,TRUE);
INSERT INTO jeu VALUES(10230,'GTA V',50,'PC/PS4/PS5/XBOX ONE/ ONE S/XBOX SERIE S/X',TRUE,TRUE);
INSERT INTO jeu VALUES(99088,'Goat Simulateur 3',30,'PC',TRUE,TRUE);
INSERT INTO jeu VALUES(29103,'Call of Duty Cold War',60,'PC/PS4/PS5/XBOX ONE/ONE S/XBOX SERIE S/X',FALSE,TRUE);
INSERT INTO jeu VALUES(79446,'Minecraft',25,'PC/PS4/PS5/XBOX ONE/ONE S/XBOX SERIE S/X',TRUE,TRUE);
INSERT INTO jeu VALUES(48999,'Fall Guys',20,'PC/PS4/PS5/XBOX ONE/ONE S/XBOX SERIE S/X',TRUE,TRUE);
INSERT INTO jeu VALUES(55512,'Cities Skylines',28,'PC',TRUE,TRUE);
INSERT INTO jeu VALUES(43363,'NBA2K23',32,'PC/PS4/PS5/XBOX ONE/ONE S/XBOX SERIE S/X',TRUE,FALSE);


INSERT INTO plateforme VALUES('PC','Steam/Ubisoft/Origin/Battle/Rockstar/Microsoft/Epic');
INSERT INTO plateforme VALUES('PS4','NONE');
INSERT INTO plateforme VALUES('PS5','NONE');
INSERT INTO plateforme VALUES('XBOX ONE','NONE');
INSERT INTO plateforme VALUES('XBOX ONE S','NONE');
INSERT INTO plateforme VALUES('XBOX SERIE S','NONE');
INSERT INTO plateforme VALUES('XBOX SERIE X','NONE');
INSERT INTO plateforme VALUES('Switch','NONE');

INSERT INTO article VALUES(98127,'Pokemon Violet','Switch',21896,'Switch');
INSERT INTO article VALUES(57766,'Goat Simulateur 3','PC',99088,'PC');
INSERT INTO article VALUES(84689,'Call of Duty Cold War','PS5',29103,'PS5');
INSERT INTO article VALUES(66197,'Minecraft','XBOX SERIE X',79446,'XBOX SERIE X');
INSERT INTO article VALUES(46816,'NBA2K23','PC',43363,'PC');
INSERT INTO article VALUES(15190,'Cities Skylines','PC',55512,'PC');
INSERT INTO article VALUES(84203,'Fall Guys','PS4',48999,'PS4');
INSERT INTO article VALUES(21188,'GTA V','XBOX ONE S',10230,'XBOX ONE S');

INSERT INTO client VALUES(81827,'Boulette','Sergio','sergio@gamil.com','dK6fC4','25/10/2005','France');
INSERT INTO client VALUES(27436,'Boulette','Tylian','tylian@gamil.com','m6D6Sj','25/10/2005','France');
INSERT INTO client VALUES(75185,'Croissant','Max','max@gamil.com','XYr2c7','01/06/2005','Italie');
INSERT INTO client VALUES(20771,'Le-Potaufeu','Mathieu','mathieu@gamil.com','R89mxC','20/01/2005','France');
INSERT INTO client VALUES(28438,'Salade','Kevin','kevin@gamil.com','i7m4ZK','06/01/2005','Espagne');
INSERT INTO client VALUES(87302,'Poulet-Braise','Tibo','tibo@gamil.com','sD5Zv6','23/03/2005','France');
INSERT INTO client VALUES(26545,'Napolitain','Esteban','esteban@gamil.com','6sx4FG','08/11/2005','France');
INSERT INTO client VALUES(92760,'Guimauve','Rayan','rayan@gamil.com','fgDH59','24/05/2005','Maroc');

INSERT INTO commande VALUES(66671,'GTA V',50,'Sergio','6/2/2012','43 Cours Marechal-Joffre',81827);
INSERT INTO commande VALUES(65308,'Pokemon Violet',60,'Rayan','25/9/2022',"15 rue de l'Epeule",92760);
INSERT INTO commande VALUES(11652,'Minecraft',25,'Mathieu','15/11/2018','91 Rue de Verdun',20771);
INSERT INTO commande VALUES(89379,'Cities Skylines',28,'Kevin','8/5/2039','51 rue du Paillle en queue',28438);
INSERT INTO commande VALUES(35633,'Goat Simulateur 3',30,'Tibo','31/12/2050','87 rue de Lille',87302);
INSERT INTO commande VALUES(45930,'NBA2K23',32,'Esteban','5/6/2023','21 boulevard Albin Durand',26545);
INSERT INTO commande VALUES(50831,'Call of Duty Cold War',60,'Max','21/8/2002','4 place Maurice-Charretier',75185);
INSERT INTO commande VALUES(65671,'Fall Guys',20,'Tylian','26/1/2064','4 Boulevard de Normandie',27436);