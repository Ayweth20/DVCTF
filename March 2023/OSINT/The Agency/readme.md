### The Agency

### Final version
**Category:** OSINT - **Difficulty:** Easy - **Solves:** 63     
**Description:**  
I don't remember where I did my reservation ... Give me the exact address of the nearest agency.  

> Flag format : dvCTF{\[streetnumber\]\_\[street_name\]} 
> Example : dvCTF{g8_rue_de_rivoli}

**Solution:**  
To solve this challenge, you must first find the approximate location of the photo.  
By sending the photo to Yandex, the location is quickly found. On Google Image, you must reduce the search area to the children's park.  
Result :  *Cap Estérel, 83700 Saint-Raphaël, France*  
After that, you have to find the "exact" location of the photograph and therefore take into account the different references to find (children's park, view on the sea, rails, road).  
![image](https://user-images.githubusercontent.com/91023285/224772593-b28908da-a90d-4e32-b3b5-c863c4ae93bd.png)  
Once the location is in hand (*[43.426016, 6.850646](https://goo.gl/maps/v6Tw3gCAeASyPtyG7)*), you need to check the street name : `All. des Fleurs`.  
And to find the street number, you can use StreetView and look the wall : `F1`  
![image](https://user-images.githubusercontent.com/91023285/224773040-9720aa3a-cc51-4e09-839a-0ba44a363495.png)  
With all this data, the flag can be reconstructed.  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{f1_allee_des_fleurs}
  ```
</details>


### 1st version

⚠️ This version was deleted because the Maps point was been moved.  

**Category:** OSINT - **Difficulty:** Medium    
**Description:**  
I don't remember where I did my shopping ... Give me the exact address of the nearest supermarket.  

> Flag format : dvCTF{\[streetnumber\]\_\[street_name\]\_\[name_of_supermarket\]} 
> Example : dvCTF{g8_rue_de_rivoli_carrefour}

**Solution:**  
To solve this challenge, you must first find the approximate location of the photo.  
By sending the photo to Yandex, the location is quickly found. On Google Image, you must reduce the search area to the children's park.  
Result :  *Cap Estérel, 83700 Saint-Raphaël, France*  
After that, you have to find the "exact" location of the photograph and therefore take into account the different references to find (children's park, view on the sea, rails, road).  
Once the location is in hand (*[43.426016, 6.850646](https://goo.gl/maps/v6Tw3gCAeASyPtyG7)*), it is enough to find the nearest supermarket (U Express).  
![image](https://user-images.githubusercontent.com/91023285/209794015-70d53f31-7b73-4be5-815c-efd5bdd97339.png)  
With all this data, the flag can be reconstructed.  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{f1_allee_des_fleurs_u_express}
  ```
</details>
