# Broken Portrait

**Category:** Forensics - **Points:** 10 - **Solves:** 41\
**Description:** My friend sent me this image but I can't open it! Can you find out what's wrong with it?

**Infos:**

> _A corrupted .png file is provided (chall.png)_\
> Error when try to open the .png file : _"Could not load image "chall.png" Fatal error readin PNG image file: Not a PNG file"_ (on Linux)

**Solution:**\
To solve this challenge you need to find a solution to open the .PNG file because the FLAG is drawn on it. To do this you need to search why the system can't recognize the .PNG extension. So here is the problem, it is the first two bytes of the file. To modify the hexadecimal code of the file, you need to find utils like GHex on Linux or HexEd on the internet. When you open the chall.png file, you can see that the two bytes are 89 0A 0A 0A 0D 0A 1A 0A. But in a real .PNG file, it is 89 50 4E 47 0D 0A 1A 0A. So you need to change these bytes and save the modifications and after you will be able to open the image and see the FLAG wrote in clear.

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
DVC{020514a3a69e0ebce2975efb64d5c19d}
```

</details>
