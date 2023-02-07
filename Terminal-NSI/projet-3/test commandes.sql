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