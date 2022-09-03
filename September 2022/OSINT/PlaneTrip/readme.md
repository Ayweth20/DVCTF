### Plane Trip
**Category:** OSINT - **Difficulty:** Easy    
**Description:**  
A student of our association will travel for his studies but we don't know where he's going. We only know he’s leaving on September 3, 2022.  
We only have his flight number: *AF7982*  
Help us to find out where he’s going so we can find him quickly.  

> Flag format : DVC{City_HH:mm-City_HH:mm}  

**Solution:**  
Pour résoudre ce challenge, il faut tout simplement chercher le vol avec le numéro de l'avion.  
Très vite nous trouvons qu'il s'agit d'un vol au départ de Paris et qui va à Riga.  
Ensuite pour les horaires, il ne faut pas prendre celles avec les retards mais celles prévues initialement.  
Avec ça le flag vient tout seul.


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{Paris_10:05-Riga_13:50}
  ```
</details>
