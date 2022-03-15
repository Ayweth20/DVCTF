### RSA
**Category:** Cryptography - **Points:** 500 (at the beginning) then 87 (at the end) - **Difficulty:** Easy - **Solves:** 79  
**Description:** Our team has found a cipher text: there seems to be some clues to decipher it. Can you help us to read it?   
**Hint:** There is another decoding step after the decryption!  
**Infos:**    
```
n = 0x7CD1020889B4382BE84B3F14EAAE242755CC1BD56F431B348F4FF8F207A96F41AFCF3EBDF4C17CB6537AD4B01B9FF9497763B22D013B614C8FCDB0C34F9D88F1A523013791EDFEB1FBBA160799892C118892FB7F199C9957DF5A26DAB4D776E5226F06ACD05412F6DD2B1B75D24CE9DC2DDAC513BCB96CD9B97F9BEF8543A3A1
phi = 0x7CD1020889B4382BE84B3F14EAAE242755CC1BD56F431B348F4FF8F207A96F41AFCF3EBDF4C17CB6537AD4B01B9FF9497763B22D013B614C8FCDB0C34F9D88F037D2317D3864035ECE8BCDD458711B788B5B3FDFD5164F7D736D0A56F416E8C16126E3868D73F54AF4D61F6033E069994319C849460C60A725A0F4DD97EDCC84
e = 0x10001
ct = 0x268D7D5F5593EA30F536635B58585620B51D2D143AFE4734635C259278D61413D0C89678E81EDF466B1E45E27EBF802F62F61263E499A516465163C7CB668F94258B3424C3E2BD76634923DECD670E4B6034F8FD00C76F9DAD00A72DB22B70B9408C89FCEE4C9B0D2D4B5664284328711BFAD57FBE1EDCC0854AAD57390DCAD6
```  


**Solution:**  
To solve this challenge you need to decrypt the message.  
So to try to decrypt the hidden message, I decide to use this site : [dCode - RSA](https://www.dcode.fr/rsa-cipher)  
After we put the infos in the valid place, we received a list of numbers : `100118678470123102108521039599861127251114116518811695988695828352125`  
![image](https://user-images.githubusercontent.com/91023285/158364540-95b312ee-61c2-449e-b9f3-714f0eb33e07.png)
Personally, I don't reconize what's the encryption type. So I use this ([dCode - Recognize Cipher](https://www.dcode.fr/identification-chiffrement)) to find the cipher method.  
Some tests later, we find that ASCII encryption. We can now decrypt the message with this website : [dCode - ASCII Code](https://www.dcode.fr/code-ascii).  
The flag is displayed immediately.  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{fl4g_cVpH3rt3Xt_bV_RS4}
  ```
</details>
