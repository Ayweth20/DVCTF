# Painting Spot

**Category:** OSINT - **Points:** 500 (at the beginning) then 426 (at the end) - **Solves:** 51\
**Description:** Found a nice painting spot, took a picture of it. But I can't remember where it is... The flag is in the form of `dvCTF{}` and has the flag wrapper already

**Infos:**

> A .zip file is provided (paintingSpot.jpg)

**Solution:**\
To solve this challenge we need to found the place displayed on the .jpg file provided in the .zip file.\
So to get infos about this image, I upload him on [Aperisolve](https://aperisolve.fr/) and find intresting infos :\
![image](https://user-images.githubusercontent.com/91023285/158411538-6c93321f-0639-4c24-9a8a-bc0fc3383eb2.png)\
That's comment in Portuguese. So we can focus on Portugal.\
We search _Portugal_ but we don't find any intresting infos, _Portugal Island_ who give us intresting infos about an island named **Sao Miguel Island**\
We go directly on Google Maps to search this island.\
On the image we can see an island from the Sao Miguel Island. So we search an island near to the main island. It's very simple, there is only one island\
![image](https://user-images.githubusercontent.com/91023285/158416160-039f92f0-3ccc-492d-9cd9-2c4d326f0e17.png) Now we need to find the good spot view and infos.\
We found the good place : **Praia do Corpo Santo**. When we analyse the advisers, we find the flag.\
![image](https://user-images.githubusercontent.com/91023285/158417662-b0ef2d0c-6159-4a6c-b32a-e5db921df017.png)

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
dvCTF{g3o_sp0tt3d}
```

</details>
