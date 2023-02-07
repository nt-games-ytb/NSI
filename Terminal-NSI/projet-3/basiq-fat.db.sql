SELECT offre_abonnement.nom_abonnement, client.prenom, client.nom, client.age
FROM offre_abonnement
INNER JOIN client
ON offre_abonnement.nom_abonnement = client.nom_abonnement
--ORDER BY offre_abonnement.nom_abonnement
WHERE client.age <= 25
ORDER BY client.age