INSERT INTO "offre_abonnement"                      
VALUES (                                         
    "abonnement black friday",
    10,
    1
);

INSERT INTO "offre_abonnement"                                                     
VALUES (                                         
    "NOEL 2022 1",
    15,
    1
);
INSERT INTO "offre_abonnement"                                                                        
VALUES (                                         
    "NOEL 2022 2",
    40,
    3
);

INSERT INTO "offre_abonnement"                                                                                                             
VALUES (                                         
     "NOEL 2022 3",
     160,
     12
);

---------------------------------------------------------------------------------------------------

UPDATE offre_abonnement
SET 
nom_abonnement = "BLACK FRIDAY 2021",
prix = 30,
duree = 3
WHERE
nom_abonnement = "abonnement black friday";

---------------------------------------------------------------------------------------------------

DELETE FROM "offre_abonnement" 
WHERE nom_abonnement = "NOEL 2021";

---------------------------------------------------------------------------------------------------

SELECT * FROM offre_abonnement
ORDER BY "prix" 

SELECT "nom_abonnement" FROM client

---------------------------------------------------------------------------------------------------

SELECT "nom_abonnement"
FROM "offre_abonnement"
WHERE duree = 1;

SELECT * 
FROM "offre_abonnement" 
WHERE prix < 150;

---------------------------------------------------------------------------------------------------

SELECT cours_collectif.nom_du_cours, employe.prenom, employe.nom, employe.adresse
FROM employe
INNER JOIN cours_collectif
ON employe.numero_employe = cours_collectif.numero_employe
ORDER BY employe.adresse

SELECT materiel.numero_etablissement, materiel.emplacement, materiel.numero_du_materiel, type_de_materiel.nom_du_materiel 
FROM materiel
INNER JOIN type_de_materiel
ON materiel.nom_du_materiel = type_de_materiel.nom_du_materiel
ORDER BY materiel.numero_etablissement, materiel.emplacement, materiel.nom_du_materiel

---------------------------------------------------------------------------------------------------

SELECT etablissement.adresse, passage.numero_du_client
FROM passage
INNER JOIN etablissement
ON passage.numero_etablissement = etablissement.numero_etablissement
WHERE passage.numero_du_passage <= 20
ORDER BY etablissement.adresse, passage.numero_du_client

SELECT client.prenom, client.nom, passage.numero_du_passage, passage.date, passage.numero_etablissement
FROM passage
INNER JOIN client
ON passage.numero_du_client = client.numero_du_client
WHERE passage.date < "22/09/01"
ORDER BY passage.numero_du_client, passage.numero_du_passage

SELECT employe.numero_employe, employe.age, employe.type_de_contrat, employe.numero_etablissement, etablissement.adresse
FROM employe
INNER JOIN etablissement
ON employe.numero_etablissement = etablissement.numero_etablissement
WHERE employe.numero_etablissement = 2 OR employe.numero_etablissement = 3 OR employe.numero_etablissement = 5 OR employe.numero_etablissement = 7 OR employe.numero_etablissement = 8
ORDER BY employe.type_de_contrat DESC, employe.numero_employe 

SELECT offre_abonnement.nom_abonnement, client.prenom, client.nom, client.age
FROM offre_abonnement
INNER JOIN client
ON offre_abonnement.nom_abonnement = client.nom_abonnement 
WHERE client.age <= 25
ORDER BY client.age