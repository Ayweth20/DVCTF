### What's Up ?
**Category:** Web - **Points:** 46 - **Solves:** 11  
**Description:** Find the Flag in the files of the website

**Infos:**  
To preserve the health of the server, brute-force tools such as Gobuster are not allowed.  
http://davincicode.fr:5000/

**Hints:** *Request Headers* & *admin portal*

**Solution:**  
To solve this challenge you need to examine the requests sends to the server and her responses.  
To do that you need to use OWASP ZAP.  
So the challenge is decomposed in 2 steps :
1. Display the site tree for finding the admin portal page URL  



https://user-images.githubusercontent.com/90919471/133905348-19525828-3962-4203-8f9d-e098c0263fdb.mp4



[Admin Portal URL](http://davincicode.fr:5000/53Cr374DM1NP0r741)  
Once find, you can go this URL but you are stopped because you are not an admin.
To change that, you need to update your requests and cookies for change the user type (normal by admin)  

2. Update the user type (normal by admin)



https://user-images.githubusercontent.com/90919471/133905497-ff0eb613-b269-4e5e-86cd-ad0229294063.mp4



You have discovered the FLAG in the code of the page and is also displayed on the website.

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{c00k1ng_m4m4_l0v3s_s0me_c00k1es}
  ```
</details>
