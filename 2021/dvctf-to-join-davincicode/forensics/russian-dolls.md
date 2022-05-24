# Russian Dolls

**Category:** Forensics - **Points:** 10 - **Solves:** 62\
**Description:** You need to find the FLAG hidden in a .txt file among all the folders

**Infos:**

> None info

**Solution:**\
To solve this challenge you need to find the .txt file that contains the FLAG. So if you are a veeeeeryyyyy patient person, you can search the file manually but it is not effective and you are not sure to find that one good file. So to get around this problem, you will have to develop a small automatic script that will examine all the files contained in these folders. I choose Python because it is a very convenient and simple language to develop little scripts like that. I used the glob and open method to explore the content of the files and I put the results in a file named all.txt. When the research is done, I search the start of the FLAG as we know it (DVC{). And the FLAG is here in clear and I copied and pasted the FLAG on the CTF website.

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
DVC{ru5514n_d0ll5}
```

</details>
