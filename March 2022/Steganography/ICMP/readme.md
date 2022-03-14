### ICMP
**Category:** Steganography - **Points:** 500 (at the beginning) then 292 (at the end) - **Difficulty:** Medium - **Solves:** 292  
**Description:**  

**Infos:**
> A .pcap file is provided (ICMP.pcap)  

**Solution:**  
To solve this challenge you need to analyse (with Wireshark) the Info column in .pcap file.  
When you do that you can see there are **seq** elements :
![icmp](https://user-images.githubusercontent.com/91023285/158177587-04565fc3-6cbc-41e6-aa33-1398f8ea50b4.png)

Now you just need to range the seq elements in ascending order and take the **id** value.

When you have all elements you need to convert them in hex then Base64 :  
5a485a4456455a376144466b5a475675587a46755833526f5a5638785a4830  
From Hex ==> ZHZDVEZ7aDFkZGVuXzFuX3RoZV8xZH0  
From Base64 ==> *The flag*  

Or you can do the 2 steps in 1 with [CyberChef](https://gchq.github.io/CyberChef/) :
![image](https://user-images.githubusercontent.com/91023285/158179549-e10f2440-1985-49c4-8e38-698fed00656c.png)



<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  dvCTF{h1dden_1n_the_1d}
  ```
</details>

