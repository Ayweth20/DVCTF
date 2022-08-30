### Cupp of coffee
**Category:** Social Engineering - **Difficulty:** Medium / Hard    
**Description:**  
My brother-in-law set up his new internet box, but after a month he forgot his WiFi password. He doesn't manage to find it but he knows that he configured it in his office (photo: [desktop.png](./desktop.png)) so we can try to crack the password.  
It’s up to you to find him thanks to the details you will see and the [wifi capture](./gaspar-01.cap) who I made in his house.

**Solution:**  
Pour résoudre ce challenge, nous devons observer la photo du bureau de Gaspar. Sur cette dernière il y a de nombreuses informations (minimes ou inutiles pour certain(e)s) qui nous aideront à savoir qui est Gaspar.  
Ici nous savons qu'il faut cracker le mot de passe WiFi donc pour cela il va falloir générer un liste de mot de passe potentielle. Mais d'abord voyons comment débuter.  

Dans un premier temps, il faut récupérer le maximum d'infos sur la photo. Nous pouvons y trouver :  
> - Des onglets web ouverts (sur Chrome) dont un Facebook et un Panel Bbox.
> - Une carte pliante d'une "Rubber Ducky v2" avec la clé posée sur le bureau.
> - Une photo d'un enfant (surement son fils) qui fête ses 4 ans le 03/12/2021. Nous pouvons très facilement en déduire sa date de naissance : 03/12/2017.
> - Une carte de visite Thales
> - Un calendrier de Novembre 2022 avec de nombreuses infos : des RDVs, l'nniversaire d'une "Capu" qui fête ses 28 ans, des jours de congés, le mariage d'un "Matteo L." et d'autres infos...  
> - Un badge d'entreprise
> - Une attestation de cession d'animaux non domestiques où il a acheté un axolotl prénommé "Marley"
> - Une adresse à Osny : 32 rue de Gency, 95520, Osny (sur le document cité juste au dessus)

Avec ces infos (et celles trouvées sur la page Facebook ouverte) nous pouvons établir un profil assez complet :  
> - **Son NOM Prénom :** *MARCOUX Gaspar*
> - **Sa date de naissance :** *28/05/1996*
> - **Son surnom :** *Gas*
> - **Son adresse :** *32 rue de Gency, 95520, Osny*
> - **Sa société :** *Thales*
> - **Sa date de mariage :** *24/06/2018*
> - **Sa femme :** *MARCOUX Capucine* née le *08/11/1994*
> - **Son fils :** *MARCOUX Eliot* né le *03/12/2017*
> - **Son animal :** *Axolotl* prénommé *Marley*
> - **Une potentielle amante :** *Solène* (grâce à l'onglet Chrome et au *❤️S* le 22/11)
> - **Une passion (folle) :** *cybersécurité* (avec l'onglet *DaVinciCode*, la *Rubber Ducky* et le sticker *PentesterLab*)

Maintenant que nous avons trouvé toutes ces infos, nous allons passer à l'étape de la création de la liste de mot de passe.  
Pour ce faire, nous allons utiliser l'outil *Cupp*, donné en indice dans le titre, qui créera une liste en fonction des infos que nous lui donnons :  
![image](https://user-images.githubusercontent.com/91023285/187502808-62a64bd0-e156-4e80-a0e9-56899b8b17db.png)  

(Pour avoir d'avantages de mot de passes, il vaut mieux mettre *Yes* à toutes les options de la fin).  
Avec cette liste (d'environ 45k) de mot de passe, nous allons donc passer à la troisième et dernière étape : Le crackage de la clé WiFi.  

Afin de faire cela, nous pouvons utiliser l'outil *aircrack-ng* sur le fichier *.cap*.  
Avec la commande `aircrack-ng gaspar-01.cap -w gaspar.txt` le mot de passe est trouvé en 10 secondes :  
![image](https://user-images.githubusercontent.com/91023285/187506579-10da4623-580d-4777-af72-01e0c69ef9b5.png)  

Voici donc le mot de passe de son réseau WiFi : **G45m4rc0ux7**
  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{G45m4rc0ux7}
  ```
</details>
