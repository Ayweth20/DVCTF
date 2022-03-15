### MP3
**Category:** Steganography - **Points:** 500 (at the beginning) then 10 (at the end) - **Solves:** 218  
**Description:** The flag in the audio is given without the tag format ! You must fill in : `dvCTF{%flag%}`  

**Infos:**    
> A .mp3 file is provided (MP3.mp3)  

**Solution:**  
To solve this challenge you need to decrypt the message.  
With the title chall, we quickly find that the encryption use is ROT13.   

So when we go on this website ([rot13.com](https://rot13.com/)) and copy/paste the encrypted message, the flag is decrypted.    

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{3ncRypt1on_1s_e4sy}
  ```
</details>
