# Snoop's Mission

**Category:** Progra - **Points:** 16 - **Solves:** 29\
**Description:** I'm too high to remember the code of my weed stash. Can you help me remember?

**Infos:**

> http://davincicode.fr:6969/\
> The PIN is composed by 4 digits

**Solution:**\
To solve this challenge you need to find the PIN to access the secret portal.\
To find the PIN you need to test all combinations.\
So if you are veeeeeryyyyy patient, you can test PIN manually but it is not effective and you are not sure to find the good PIN.\
So to get around this problem, you will have to develop a small automatic script that will test all PINs from 0000 to 9999.\
I choose Python because is a very pratic and simple language to develop little scripts like that.\
I used the _requests_ library to send requests to the server.\
When the PIN is good, the python program stops and writes in .txt file the information with the PIN and the FLAG.\
_The PIN is **4420**_\
So if you don't want to enter the PIN on the website connect screen, you can copy the FLAG.\
But if you test to enter the PIN on the website, you go to a web page that display the FLAG.

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
DVC{bl4ze_1t}
```

</details>
