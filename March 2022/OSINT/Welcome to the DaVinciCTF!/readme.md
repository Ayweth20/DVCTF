### Welcome to the DaVinciCTF!
**Category:** OSINT - **Points:** 500 (at the beginning) then 440 (at the end) - **Difficulty:** Easy - **Solves:** 46  
**Description:**  

**Infos:**    
> A .jpg file is provided (img.jpg)  

**Solution:**  
To solve this challenge you need to analyse all details in the image.     

We can see differents details : Post-It (x3), Seed Phrase Card, Websites...  
-> **Post-It n°1 (left) :** *Binance elonmusk78@gmail.com Password01*  
  I try to connect on this Google account, but the password is incorrect. And searches infos [here](https://tools.epieos.com/?q=elonmusk78%40gmail.com). I didn't insist on this track.  
-> **Post-It n°2 (top right) :** *CTFd admin ThisIsAVerySecurePassword*  
  I try to connect on the CTF platform and on CTFd but obviously these creds didn't work.  
-> **Post-It n°3 (bottom right) :** *TODO : - Acheter du BTC - Acheter du DegenAPE - Devenir riche - Préparer la page d'accueil du CTF*  
  Nothing is really usable here...  
-> **Seed Phrase Card (bottom left) :** *minor casino able rare pretty stuff token embrace awake good infant crack news mix edge style this is not my private key sorry dude*  
  I try to connect with the seed phrase on Binance, but she is incorrect. It's true that the image isn't very clear...  
-> **Webpages :** *Binance / TradingView / DigitalOcean / GitHub / dvCTF*  
  I search all website but I don't find anything...  
  After reviewing the image, I see that the dvCTF URL is strange : *https://ctfd.davincicode.fr/_*. So I go to the website and if you analyze the source code, you can see that the flag is on the bottom page, but the css color the text to white.  
  ![image](https://user-images.githubusercontent.com/91023285/158388360-3386a267-f254-4a2d-8170-fd0a6d22e61d.png)

  
<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{8a878c2bd9c1844aac17cd051585e2f0}
  ```
</details>
