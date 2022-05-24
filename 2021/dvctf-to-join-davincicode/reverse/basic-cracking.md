# Basic Cracking

**Category:** Reverse - **Points:** 42 - **Solves:** 15\
**Description:** You need to find to FLAG

**Infos:**

> A file without extension is provided (cracking)

**Solution:**\
To solve this challenge you need to do researches about the file.\
On Linux with the command `file cracking` you can find that is an ELF file.\
So after this discovery, you can orient your researches on this file type.\
After a few researches I found the [Ghidra](https://ghidra-sre.org/) util. It is a very helpful program.\
So I opened my file with this program and I saw a main function. After examine these function I saw the characters of the FLAG.

![image](https://user-images.githubusercontent.com/90919471/133922011-d87e3c8b-b3fe-4844-a701-b2f133c9723d.png)

(_In yellow it is the characters order and in blue that the characters who compose the FLAG_)

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
DVC{CrAckInG_Is_HaRd}
```

</details>
