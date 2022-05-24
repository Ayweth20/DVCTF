# Have I Been Pwned

**Category:** Web - **Points:** 49 - **Solves:** 7\
**Description:** Find the Flag in the files of the website

**Infos:** To preserve the health of the server, brute-force tools such as Gobuster are not allowed. http://davincicode.fr:5000/

**Solution:**\
To solve this challenge you need to find the file who contains the FLAG.\
If you inspect the response header, you can see that the website is built with Werkzeug/2.0.1 and Python/3.9.5 When we connect to the website, we have been offered a basic homepage with just a simple input.\
So when you do a few researches you rapidly find that you can use the SSTI attack.\
The SSTI consist to use native template syntax to inject a malicious payload into a template, which is then executed server-side.\
One article who helped me to make an SSTI attack is published here : [SSTI attack writeup](https://anasblp.medium.com/tamu-ctf-2019-web-writeups-science-41f173ba3203). The author explains all steps to finish the attack. So after a few explanations, we start to view the results on our website. So we do a lot of commands who are update step by step. The command who gives the FLAG is :

```
{{url_for.__globals__.os.popen('cat ls cd ChallengeWeb1/flag.txt').read()}}
```

This command displays the FLAG on the web page.

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
DVC{n0_sh4refl4g_pls}
```

</details>
