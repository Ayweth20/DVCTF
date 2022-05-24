# Unbreakable encryption

**Category:** Crypto - **Points:** 50 - **Solves:** 2\
**Description:** My friend stole this flag, but I don't care I've encrypted it with a super secret key that he'll never find!

**Infos:**

> 0x1050a3732753d7e13632d673b7f093c633c3e09353f7d7d387260317b2b

**Hint:** _Known plain_

**Solution:**\
To solve this challenge you need to do researches thanks for the hint.\
Effectively, the hint is helpful because when you search "Known Plain" on the web, you discover a lot of information about an attack, the Known Plaintext Attack (or KPA).\
Look at the CTFs and a lot of documentation that explains how to resolve this attack. After a few documentations readings, you have surely seen you need to use the XOR resolve.\
And that's the case, you need to calculate the FLAG with your message (0x1050a37\[...]) and a key to decipher the correct FLAG.\
But the problem is that you don't the key... And for finding this key you have to imagine and test keys about your CTF or information of the CTF organizer.\
So that is the best practice. In our case, the CTF is organized by a student of our establishment.\
So we need to test all information about the school (director name, city of the school, school name...)\
So there are very many possibilities. So you need to test all possibilities and sort them in importance and logical order.\
For this CTF we can test : Léonard, Vinci, Défense, IIM, ESILV, EMLV and others...\
To test the compatibility with the message and this key, we can go on two different websites that can decrypt XOR: [dCode.fr](https://www.dcode.fr/chiffre-xor) or [CyberChef](https://gchq.github.io/CyberChef/)\
⚠️ The message is in hexadecimal and I saw on a website that it is necessary to remove the first "x" of the message...\
Once these changes are done, you must enter the message and the key in the right places and the FLAG will be calculated automatically.

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
DVC{d0n7_5h4r3_y0ur_pl41n73x7}
```

</details>
