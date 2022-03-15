### FrenchFlag
**Category:** Forensic - **Points:** 500 (at the beginning) then 10 (at the end) - **Solves:** 614  
**Description:** Can you find the data present in our flag ?  

**Infos:**
> A .png file is provided (flag.png)  

**Solution:**  
To solve this challenge you need to analyse the .png file.  
To analyse an image I know some commands who are basic.   
```
file *<filename>*
strings *<filename>*
exiftool *<filename>*
```  
So I tested these commands but the first didn't gave me the flag...  
But the second and third command display the flag in the .png infos :
![image](https://user-images.githubusercontent.com/91023285/158329634-a540b45f-340c-4781-91f5-617584eff53c.png)


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{flagception}
  ```
</details>

