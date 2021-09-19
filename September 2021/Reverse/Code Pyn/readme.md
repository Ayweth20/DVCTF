### Code Pyn
**Category:** Reverse - **Points:** 34 - **Solves:** 20  
**Description:** I lost my pin code. Can you help me find it?

**Infos:**
> A .pyc file is provided (pyn.pyc)

**Solution:**  
To solve this challenge you need to find a solution to decrypt the .pyc file or to recover the program code.  
To do this I chose to develop a little python script (*bruteforcePYC.py*).  
The script recove the program structure and we can see what he is doing.  
For example the python script return this :  
```py
  8          24 LOAD_NAME                4 (len)
             26 LOAD_NAME                3 (pin)
             28 CALL_FUNCTION            1
             30 LOAD_CONST               5 (4)
```
This block indicate that the PIN is composed by 4 digits (*LOAD_CONST (4)*)  
After theses lines indicate that we need to do a [XOR](https://xor.pw/#) between 5 and 3 :  
```py
60 LOAD_CONST               6 (5)
62 BINARY_XOR
64 LOAD_CONST               7 (3)
```  
And it's the same for the 2 following PIN   
```py
86 LOAD_CONST               7 (3)
88 BINARY_XOR
90 LOAD_CONST               6 (5)
```
```py
112 LOAD_CONST              10 (8)
114 BINARY_XOR
116 LOAD_CONST               8 (1)
```  
So we have the 3 first digits (669) and the fourth need to be find manually.  
When we test the last digit, we found speedly that is 1.  
So we know the PIN code : 6691 and the FLAG is the PIN so...  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  DVC{6691}
  ```
</details>

