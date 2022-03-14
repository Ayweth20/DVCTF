### ICMP
**Category:** OSINT & Steganography - **Points:** 500 (at the beginning) then 490 (at the end) - **Difficulty:** Easy - **Solves:** 20  
**Description:** My dear friend "Bob" made a tool online to uncover the truth behind that map.  

**Infos:**
> A .jpg file is provided (map.jpg)  

**Solution:**  
To solve this challenge you need to analyze the jpg file in first step.  
The image contain an Australian map and there are stanges rods on the bottom left corner.  
But what represent these rods ?  
![image](https://user-images.githubusercontent.com/91023285/158216518-bf520b38-7de1-4be6-bcfa-1d1c28e10490.png)  
After many searches we found that this image correspond to an *Australian Post 4-State Code*. Now we "just" need to found a reader for this barcode...  
When we search *Australian Post 4-State Code reader* we find a website named [*bobcodes*](http://bobcodes.weebly.com/auspost.html). What's name of our dear friend ? "Bob", exactly. We are now on the good way.  
So now, we need to convert the barcode in letters (T, D, A or H) to extract the infos. Here is the "rule" to convert :  
![image](https://user-images.githubusercontent.com/91023285/158220451-c5b22d38-bb8f-4859-9e78-69c5b3e8c707.png)  
After convert the "code" is : **ATDFFDDADDAADAADFAFAFFDAFTFDAFATAFAAATADTAFDTDDDDDDDTTTDFFTDDADFAAT** and we collect some infos :  
```
Format Control Code : 62
Sorting Code : 78475110
Customer Information Field : V3K4N64r00
```  
We don't need these infos for the moment, but we keep them near to us.

We can now analize the first image with a steganography tool. To analyze an image in steganography, I always use [Aperisolve](https://aperisolve.fr/).  
When we upload the file on the website, we can see there is a .7z file in backgroung data :
![image](https://user-images.githubusercontent.com/91023285/158197207-b068b87c-4453-4a44-ae7c-cfcc425a18f0.png)
We download them but this .7z file is locked with password...

So now, we have to find this password. 



<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{4U57r4114_P057_4_57473}
  ```
</details>
