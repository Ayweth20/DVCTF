# Sus USB

**Category:** Forensics - **Points:** 49 - **Solves:** 7\
**Description:** I found a weird USB stick on the floor in my office building's parking. I plugged it in before my colleague yelled at me and proceeded to investigate the USB stick. He only managed to extract this; can you make any sense out of it? What have I done to my pc!

**Infos:**

> A .bin file is provided (dump.bin)

**Solution:**\
To solve this challenge you need to imagine the situation written in the description. So there is a person who finds a USB key on the floor of his work building. He plugs the USB on a computer and there is nothing on the key. His coworker finds just the "cracking" file by doing deep researches on the key. What can be this USB key? A Rubber Ducky USB !!! So now we need to find a decrypter of Rubber Ducky code and it is good. There is [DuckToolkit](https://ducktoolkit.com/decode). When we upload the file on the website, it returns the script (duckycode.txt) contain in the file and we can find the FLAG in it.

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="1f6a9">🚩</span> FLAG</summary>

```
DVC{u5b_4r3_d4n63r0u5}
```

</details>
