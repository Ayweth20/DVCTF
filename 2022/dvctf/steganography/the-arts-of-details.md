# The Arts of Details

**Category:** Steganography - **Points:** 500 (at the beginning) then 50 (at the end) - **Difficulty:** Easy - **Solves:** 145\
**Description:** A simple detail can make a big difference Always beware of the first element

**Infos:**

> A .docx file is provided (The\_Art\_of\_Details.docx)

**Solution:**\
:fr: Français :\
Pour résoudre ce challenge nous devons donc examiner le fichier .docx\
Dans un premier temps nous pouvons l'ouvrir pour voir son contenu. Après avoir regardé, rien d'intéressant dans ce contenu.\
Comme il n'y a rien dans le contenu du fichier, nous allons voir s'il n'y a pas quelques choses dans la partie "non visible" du fichier : ![image](https://user-images.githubusercontent.com/91023285/158761298-9865c103-42c3-4b1b-ac80-db91a25e2e8b.png) Avec la commande `unzip <filename>` nous extrayons tous les documents "cachés" dans le fichier. Et enfin la commande `tree` nous permet de voir tous les fichiers extraits.\
Nous pouvons donc voir qu'il y a 3 images :\
![image](https://user-images.githubusercontent.com/91023285/158762535-4daca864-725b-40d8-949c-b191db20c7c4.png) Si nous scannons ces images, nous obtenons des infos très importantes :

* image1.png : `aXRpc25vdHRoZWZsYWc=`
* image2.png : `dGhla2V5ezRBajgyRDZoUlpLQThocXA1dG01fQ==`
* image3.png : `defaw{u1qeuugx&crl0gl_4_r_fbe4a_f4hli0rm}` (ça ressemble beaucoup à un flag de la forme `dvCTF{flag}`)\
  Ces 2 premières chaines de caractères sont encodées en Base64. Si nous les décodons cela nous donne :
* Base64 : `aXRpc25vdHRoZWZsYWc=` => `itisnottheflag`
* Base64 : `dGhla2V5ezRBajgyRDZoUlpLQThocXA1dG01fQ==` => `thekey{4Aj82D6hRZKA8hqp5tm5}`\
  Après avoir recueillis tous ces éléments, nous pouvons voir que nous avons une clé et le flag encodé...\
  Nous allons donc nous diriger vers une attaque Vigenère (avec [CyberChef](https://gchq.github.io/CyberChef)) :\
  ![TheArtsOfDetailsError](https://user-images.githubusercontent.com/91023285/158764380-2417a8a9-b823-49da-b557-fd6b2857ea78.png) Mais nous avons un problème. Il n'accepte pas la clé que nous avons mise, car il n'accepte que les clés composées uniquement de lettres.\
  Donc voici comment faire :\
  ![image](https://user-images.githubusercontent.com/91023285/158764854-e977fd44-0f46-4e39-a1ff-6e125f0557c1.png)

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
dvCTF{v1genere&qrc0de_4_a_gre4t_p4ssw0rd}
```

</details>
