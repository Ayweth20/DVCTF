### New Website
**Category:** OSINT - **Difficulty:** Easy    
**Description:**  
A new member of the association bought a domain name for his website but it looks pretty recent.  
Can you give us his creation date?  
> Flag format : DVC{dd-mm-yyyyThh:mm:ssZ}

Website : [https://davincicode.fr](https://davincicode.fr)

**Solution:**  
Pour résoudre ce challenge, il faut trouver la date de création du domaine *davincicode.fr*.  
Très simplement il faut aller chercher dans les whois du site.  
Avec le site [whois.domaintools](https://whois.domaintools.com/) ou avec un terminal (Windows ou Linux) en tapant la commande `whois davincicode.fr` le résultat apprait rapidement :  
![image](https://user-images.githubusercontent.com/91023285/187077367-05cf2012-0fbb-48b5-ad4c-092d8ae046e5.png)  


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{2021-08-23T17:47:39Z}
  ```
</details>
