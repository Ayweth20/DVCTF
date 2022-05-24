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
We can try to do a bruteforce attack... But after multiple tests any technique works.  
And earlier we found infos ! We can test with theses infos : "62", "78475110", "V3K4N64r00", "6278475110V3K4N64r00"...  
The good password is : **6278475110V3K4N64r00**  
We can dezip the 7z file and analyze extract datas. The folders names contain 4 digits and 40 numbers (0 or 1) who make a big binary.  

But what can we do with these folders names ? Convert in hexa ? Build an image ? Range them in ascending order ?  
I decided to range the binary in create date order. So at the end we have this :  
<details>
  <summary>Looooooong datas</summary>

  ```
  0000000000000000000000000000000000000000000000000000000000000000000000000000000000110110010010011011001001101101100100000011011011001001001100100100010010111000001101111000011000110001100000000111110000110110001110011100000001111110011110000011011000111001110000000111111001110000001111111000011000000011111100100001110000111111100001100000001111110010000111000011000111111001100011000001001001100000001111111111000000110000000000011111110000111111111100000011000000000001111111000011011000110110000000011001001111100000001110000100111111001001100100011101110000111000010011111100110110010001100111000011011111000111101100100001001110000000001101111100011110110110001100111000000000111000011110000111111001111101111011000011111111000000011111100111000000000000001111111100000001111110011100000000000000110111111110011111001001110001100111000011011111111101111100100111000010011100001101100011111001111101100011000001000000110111001111000011110110000010000111000011011110111000001111011000001000011100001100000100100001110000011011100000000000110000010010000111000001101110000000000011100000000110011111000111001000011100001100011111100001001110011000011001100000110001111110000100111001000000100100000011100001110001110000000000110001111100001100000011000011111110000100000110000000110000001100000111111000010000011000000011000111001001101100111110110000011100001100011100100110010011110011000001110000110111101100000000110000001101100100000011111111111111111111111111111111111100001111111111111111111111111111111111110000000000000000000000000000000000000000000000000000000000000000000000000000000000
  ```
</details>

And the last step is to build an image with this big datas block. The website who do that is this one : [Dcode - Convert Binary in Image](https://www.dcode.fr/image-binaire)  
After generating the image we just need to find a tool who can "read" the *Data Matrix barcode* :  
![image](https://user-images.githubusercontent.com/91023285/158325296-1b54ef03-be7f-461f-85d3-ffaabef681a2.png)  
With some searches, we found this website [Aspose](https://products.aspose.app/barcode/fr/recognize/datamatrix#) and after this image analyse, the flag is displayed.

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{4U57r4114_P057_4_57473}
  ```
</details>
