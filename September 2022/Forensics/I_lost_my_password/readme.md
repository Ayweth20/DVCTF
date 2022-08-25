### I lost my password
**Category:** Forensics - **Difficulty:** Medium    
**Description:**  
I lost the password of my [.rar file](./protected.rar) but I’m sure I took it from a passwords list. This list is named [*richelieu_DVC.txt*](./richelieu_DVC.txt).  
:warning: *This challenge is make to find the password from the hash*  

**Solution:**  
Pour résoudre ce challenge, vous devez réussir à cracker le mot de passe du [fichier .rar](./protected.rar) en utilisant le hash du mot de passe et la liste de mots de passes fournie.  
Dans un premier temps, il faut récupérer le hash du mot de passe qui nous servira par la suite.  
Pour ce faire nous allons utiliser l'outil *rar2john*. La commande suivante permet de mettre le hash dans le fichier rar.hashes : `rar2john protected.rar > rar.hashes`.  
Si nous voulons voir le hash, un simple `cat` sur le fichier suffit :  
![image](https://user-images.githubusercontent.com/91023285/186752414-a64d7c83-2406-4e0a-82b9-ef20a25c3c28.png)  

L'étape la plus importante (et intéressante) est celle du "crackage" de mot de passe. Pour ce faire, nous allons utiliser l'outil john tout en spécifiant notre liste de mot de passe : `john --wordlist=richelieu_DVC.txt rar.hashes`  
En fonction de l'emplacement (dans le fichier) de notre mot de passe et de la rapidité de la machine, le mot de passe est rapidement trouvé (ici 3 secondes) :  
![image](https://user-images.githubusercontent.com/91023285/186753826-7ef5be87-00a4-40b7-a081-07ccc2ce6de0.png)  

Une fois le mot de passe obtenu (*DVC92*) il suffit simplement d'extraire le contenu du fichier .rar et de fournir le mot de passe :  
![image](https://user-images.githubusercontent.com/91023285/186754241-43e73598-a873-423c-bdde-a23e39dc794b.png)  
  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{175_345Y_70_cR4cK_R4r}
  ```
</details>
