### Donloaded Image
**Category:** Forensics - **Difficulty:** Easy    
**Description:**  
I went to a website and I think that during the loading of the page, an item was downloaded.  
Try to find it as it might be the flag ¯\_(ツ)_/¯  

**Solution:**  
Pour résoudre ce challenge, vous devez analyser la [capture .pcapng](./my_capture.pcapng) et essayer de trouver le flag.  
Comme nous pouvons le comprendre dans le titre, le fichier comprends le téléchargement d'une image.  
En examinant le fichier, nous pouvons voir que dans le paquet 15 qu'il y a une requête *GET* vers une image (flag.png).  
Si nous allons au paquet 17, nous pouvons voir qu'il y a bien le code hexa d'une image png. Si nous double-cliquons sur le lien *Reassembled PDU in frame: 696*, nous allons directement être redirigé vers le paquet contenant toute l'image :  
![image](https://user-images.githubusercontent.com/91023285/186723232-4ee526b1-7f5b-46fb-8306-35d3a552bfcc.png)  

En allant au paquet 696, nous pouvons retrouver le bloc *Portable Network Graphics* contenant toute l'image :  
![image](https://user-images.githubusercontent.com/91023285/186723870-a49b32e7-07b1-4d2a-b981-d11e8a808e7c.png)  

Soit 



  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{flag}
  ```
</details>
