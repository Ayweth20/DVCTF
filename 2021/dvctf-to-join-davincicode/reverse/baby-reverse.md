# Baby Reverse

**Category:** Reverse - **Points:** 33 - **Solves:** 21\
**Description:** I hid my flag in my script, but I don't what happened the file was deleted! The only thing left is this folder... Is my flag lost forever?

**Infos:**

> A .pyn file is provided (baby\_rev.cpython-39.pyn)

**Solution:**\
To solve this challenge you need to find a solution to decrypt the .pyc file.\
To do this you can use a python editor like [EduPython](http://maths-sciences-lp.ac-amiens.fr/568-edupython.html) or [PyScripter](https://sourceforge.net/projects/pyscripter/)\
After you installed the program, you need to open the .pyc file and examine the code that it returns you.\
The decrypt code is written like this :

![image](https://user-images.githubusercontent.com/90919471/133919974-bcb7caca-39db-43c0-a323-366ccc35cffe.png)

So you need to see the start FLAG and search the rest...\
All letters highlighted in green compose the FLAG but two characters are missing (where there are two red points)\
So we need to guess these 2 characters (n and y).

When you have finished to find all letters you have the FLAG.

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
DVC{py7h0n_b1n4ry}
```

</details>
