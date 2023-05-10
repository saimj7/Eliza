# Eliza
A small improvement with language translation where Eliza will aim to understand different languages via text and respond on the go.

> Based on https://en.wikipedia.org/wiki/ELIZA and https://github.com/jezhiggins/eliza.py

---

## Usage

1. **Install the requirements**

```
pip install langdetect google_trans_new
```

2. **To run** 

```
python eliza.py
```

3. **Example output**

We detect the input language using langdetect and translate using google_trans_new:

```

************** Chat with Eliza **************

[Eliza]: Hi! How can I help you?
[You]: tack sa mycket

[Info] Your input language is: sv

[Eliza]:  How do you feel when you say that? | (In sv: Hur mår du när du säger det?
[You]:

```
---

Note: If you run into any problems during language translation, please refer to the official API: https://github.com/lushan88a/google_trans_new

---

_saimj7/ 2023 © <a href="http://saimj7.github.io" target="_blank">Sai_Mj</a>_
