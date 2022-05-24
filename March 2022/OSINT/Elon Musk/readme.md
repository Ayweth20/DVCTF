### EBG13
**Category:** Cryptography - **Points:** 500 (at the beginning) then 120 (at the end) - **Difficulty:** Easy - **Solves:** 115  
**Description:** 
```
Hi,
I'm a huge fan of Elon Musk so I invested all my money in cryptocurrencies. However, I I got lost in the cryptoworld and I lost something, can you help me find it?
Sincerely,
@IL0veElon  
```
**Infos:**    

**Solution:**  
Thanks to the chall description, we quickly find that a message from (or for) Twitter.   

So we go on Twitter and search the [*IL0veElon* account](https://twitter.com/IL0veElon).   
![image](https://user-images.githubusercontent.com/91023285/158395296-0e51f718-7050-4ea9-8fbd-5c5e636ca651.png)

In first step, we can see in bio that there is only one `$EGLD` in the multiple `$DOGE` and `$SHIB`. We can search on the EGLD Blockchain like here : [elrond.com](https://explorer.elrond.com/)  
But to find infos, we need to have a token id transaction...  
So after we analyze all tweets, only single one is not retweeting. So we can go furthur on this way.  
![image](https://user-images.githubusercontent.com/91023285/158399259-ad580b07-02ee-42c6-ad62-ead31124155d.png)

Copy/Paste the token id on the website and all infos about the transaction are displayed.  
In the *Input Data* (message) there is the flag.  
![image](https://user-images.githubusercontent.com/91023285/158399091-fa51f420-977c-4007-a55e-6254824fc81d.png)


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{Bl0cKcH4In_Rul3S}
  ```
</details>
