SELECT employe.numero_employe, employe.age, employe.type_de_contract, employe.numero_etablissement, etablissement.adresse
FROM employe
INNER JOIN etablissement
ON employe.numero_etablissement = etablissement.numero_etablissement
WHERE employe.numero_etablissement = 2 OR employe.numero_etablissement = 3 OR employe.numero_etablissement = 5 OR employe.numero_etablissement = 7 OR employe.numero_etablissement = 8
ORDER BY employe.type_de_contract DESC, employe.numero_employe 

--SELECT client.prenom, client.nom, passage.numero_du_passage, passage.date, passage.numero_etablissement
--FROM passage
--INNER JOIN client
--ON passage.numero_du_client = client.numero_du_client
--WHERE passage.date < "22/09/01"
--ORDER BY passage.numero_du_client, passage.numero_du_passage

--SELECT etablissement.adresse, passage.numero_du_client
--FROM passage
--INNER JOIN etablissement
--ON passage.numero_etablissement = etablissement.numero_etablissement
--WHERE passage.numero_du_passage <= 20
--ORDER BY etablissement.adresse, passage.numero_du_client

--SELECT materiel.numero_etablissement, materiel.emplacement, materiel.numero_du_materiel, type_de_materiel.nom_du_materiel --, etablissement.adresse
--FROM materiel
--INNER JOIN type_de_materiel--, etablissement
--ON materiel.nom_du_materiel = type_de_materiel.nom_du_materiel
--ORDER BY materiel.numero_etablissement, materiel.emplacement, materiel.nom_du_materiel

--SELECT cours_collectif.nom_du_cours, employe.prenom, employe.nom, employe.adresse
--FROM employe
--INNER JOIN cours_collectif
--ON employe.numero_employe = cours_collectif.numero_employe
--ORDER BY employe.adresse

--SELECT offre_abonnement.nom_abonnement, client.prenom, client.nom, client.adresse
--FROM offre_abonnement
--INNER JOIN client
--ON offre_abonnement.nom_abonnement = client.nom_abonnement
--WHERE client.age <= 25
--ORDER BY client.adresse
