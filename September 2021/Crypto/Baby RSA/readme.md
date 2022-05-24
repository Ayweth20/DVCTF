### Baby RSA
**Category:** Crypto - **Points:** 10 - **Solves:** 41  
**Description:** Wow, this time I can't compute the the private key! Or can I?

**Infos:**
> N= 0x25b8f38aed4a22b31dde75e46e276d0d  
> e= 0x10001  
> ct= 0x10891034ce51c23bfe2f7bf29a62938e

**Solution:**  
To solve this challenge you need to calculate the p and q parameters for the RSA key.  
To do this you need to decompose the N value in prime factor. For this, the following website is great: [Prime Factor Calculator](https://www.dcode.fr/decomposition-nombres-premiers#:~:text=Qu%27est%20ce%20que%20la,un%20produit%20de%20nombres%20premiers)    
After having calculated the 2 parameters (*p: 5665192965464669089 and q: 8850847341676960237*), you can go to the following website to calculate the RSA key: [RSA Calculator](https://www.dcode.fr/rsa-cipher)  
Once on this website, you can enter the informations in the right places and the FLAG will be calculated automatically.  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{f4c70rDB}
  ```
</details>
