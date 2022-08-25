### Russian Dolls
**Category:** Forensics - **Difficulty:** Easy    
**Description:**  
You need to find the FLAG hidden in a .txt file among all the folders

**Solution:**  
Pour résoudre ce challenge, vous devez retrouver **LE** fichier contenant le flag parmis ces 10k fichiers.  
Pour ce faire, il y a 2 méthodes. Une très simple avec une simple ligne de commande et une autre en créant un petit script Python.  

Commençons par méthode avec **le script Python** :  
:information_source: Le script que je vais vous donner ici n'est en aucun cas le seul fonctionnel ni même le plus optimisé.  
```py
import glob

def resolve():
	files = glob.glob('./**/*.txt', recursive = True)
	with open('all.txt', 'a') as ff:
		for file in files:
			with open(file, 'r') as f:
				ff.write(file + ' => ' + f.read() + '\n')
				
resolve()
```  

Pour expliquer rapidement ce que fait ce script, c'est qu'il parcourt récursivement tous les répertoires un par un en regroupant le contenu de chaque fichier dans un seul et unique (*all.txt*).  
Après cela, il n'y a pas plus qu'à chercher le flag à la l'intérieur de ce fichier avec un *CTRL+F* > DVC{ et le flag apparait.

Et enfin la méthode avec **la ligne de commande** :  
Cette méthode est la plus simple (et la plus rapide). Pour ce faire nous utilisons la commande : `grep -rnw . -e 'DVC'` qui permet de rechercher dans tous les fichiers, les fois où le bouut de mot *DVC* apparait.  
Ici nous n'avons pas mis de piège alors la commande renvoie qu'une seule réponse :  
![image](https://user-images.githubusercontent.com/91023285/186760145-736d2e54-0fcd-4520-9d5a-f8367d57c89e.png)  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{Ru5514N_D01Ls_4R3_345y}
  ```
</details>
