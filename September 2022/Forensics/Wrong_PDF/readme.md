### Wrong PDF
**Category:** OSINT - **Difficulty:** Easy    
**Description:**  
Where the flag can be hidden? The PDF file is a bit strange but the flag is apparently present.  

**Solution:**  
Pour résoudre ce challenge, vous devez analyser le [fichier PDF](./wrong.pdf) et essayer de trouver le flag.  
Comme nous pouvons le voir dans le fichier PDF il y a des barres noires qui cachent potentiellement du texte :  
![image](https://user-images.githubusercontent.com/91023285/186934019-289799d6-8ffc-4122-927e-b4918af59e6f.png)  

Pour essayer de voir le texte, nous pourrions tenter d'enlever ces bandes noires mais impossible de le faire car le fichier ne peut être modifié...  
L'une des dernières possibilités (après en avoir cherché et testé d'autres), est de copier les parties cachées et de les mettre dans un bloc notes :  
![image](https://user-images.githubusercontent.com/91023285/186936307-e401f080-faf8-468d-86d5-18cae8cd38d0.png)  

C'est déjà un bon début mais les parties cachées ne nous ont pas aidé. Cela est étrange mais le flag est forcément dans le fichier.  
Essayons une dernière chose en faisons un *CTRL+A* pour copier tout le contenu du fichier :  
![image](https://user-images.githubusercontent.com/91023285/186938820-ec9ae012-558a-43c0-b2e0-636aa198bf4f.png)  

Le flag était bien bien dans le fichier mais écrit en blanc sur le fond blanc de la page :  
![image](https://user-images.githubusercontent.com/91023285/186939165-65cd3c7f-7f4d-4eb1-bc00-36408e543fa9.png)  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{7h15 _f149_F0r_Y0u}
  ```
</details>
