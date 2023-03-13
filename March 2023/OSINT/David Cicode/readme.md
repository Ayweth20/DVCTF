### David Cicode 2/2
**Category:** OSINT - **Difficulty:** Easy - **Solves:** 32    
**Description:**  
You found David's gmail account in the first part of the challenge, let's see what informations you can recover from it.  
  
> Flag format : dvCTF{part1_part2_part3}  

**Solution:**  

Gmail account: dav1d.c1cod3@gmail.com

To solve this challenge, you need to use Ghunt and follow the steps below:  

- Ghunt email : *ghunt email dav1d.c1cod3@gmail.com*
- We can find his Maps account : https://www.google.com/maps/contrib/116570179360508069806/reviews
- There are 4 photos on his Maps account and the 1st one has a flag part (see the white price tag)
- Then we can also find his Calendar account : http://calendar.google.com/calendar/ical/dav1d.c1cod3@gmail.com/public/basic.ics
- In this file, we can find one event with a flag part (VERY IMPORTANT - Restaurant on February 14th) and a link to a Google Groups (March Event on January 26th)
- Once we are on the Google Groups, we can check all the mails and find the last flag part (March Event 💻)

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{gHun7_c4N_b3_U53fU1_jYyMjk4NWRk}
  ```
</details>
