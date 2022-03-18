### CyberStreak v1.0
**Category:** Web - **Points:** 500 (at the beginning) then 367 (at the end) - **Difficulty:** Easy - **Solves:** 68  
**Description:**  
Hello,  
I am a student and I would like to improve my web development skills. To practice, I am creating my first web application. This application is a kind of cybercoach. Example: you want to do sports. A sport goal could be to do 100 push-ups per day for 1 month. The application will allow you to create this "challenge" and each day, you will have to do the number of push-ups you have set and note it in the application. If you don't do the push-ups for 3 days, it's a failure and you lose your streak.  

This first version of the application gives you the possibility to create an account and to do the challenge of the example.  

Can you test the security of my application ?  

**xXx-michel-xXx**  

http://challs.dvc.tf:5001

*Brute force is strictly forbidden and useless.*    

**Solution:**  
To solve this challenge you need to bypass the login screen.  

In first time, we complete the registration/login forms to see what's going on.  
When a user login, a cookie is built with the user infos :  
`Cookie: session=eyJ1c2VybmFtZSI6IkF5d2V0aDIwIn0.YjR4nQ.-CVhEOLLoNn3A4IISosy5ut-7LM`  
If we decipher this cookie with a Base64 decoder we found interesting infos : `{"username":"Ayweth20"}���'@%a�âË Ù÷���J�2æë{,` The first cookie part is about the username.  

So at this moment I didn't know how I can continue... After some researches I found that the cookie is a Flask cookie (the 3 points `.` is characteristic about this cookie type.  

Now with a tool named [`flask-unsign`](https://pypi.org/project/flask-unsign/) I can brute-force the secret key with this command : `flask-unsign --unsign --cookie "<cookie value>"`  
Thanks to this tool, we can find the secret key contain in the cookie : `s3cr3t`  
The admin might be **xXx-michel-xXx**  as say in the note of the challenge. So we use this username and the secret key to build the admin cookie.  

With this command : `flask-unsign --sign --cookie "{'username': 'xXx-michel-xXx'}" --secret 's3cr3t'` we can have the admin cookie : `eyJ1c2VybmFtZSI6InhYeC1taWNoZWwteFh4In0.YjR-fg.n7h94NZbSUXDOBymQHaBuwVhZCQ`  

Now if we try to login to the web app with this cookie (thanks to BURP or Firefox) we arrived on the admin page with the flag :  
![image](https://user-images.githubusercontent.com/91023285/159005756-24b880ee-9ee8-4741-ad38-d0f4f0e33788.png)



<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{80b8d1A92G6a13a98Dc7b546a7a7Y35}
  ```
</details>

