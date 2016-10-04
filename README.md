nbtranslate
===========

Translate content of jupyter notebook using gettext tools.

Install
-------

```
$ git clone https://github.com/devrt/nbtranslate.git
$ cd nbtranslate
$ sudo pip install -r requirements.txt
$ sudo ./setup.py install
```

or

```
$ pip install git+https://github.com/devrt/nbtranslate.git
```

Usage
-----

Extract text to translate from the jupyter notebook:

```
$ nbtranslate --pot en.pot notebook_en.ipynb
```

Translate ``en.pot`` using your favorite gettext translation tool
(I recommend [poedit](https://poedit.net/) or [google translator toolkit](https://translate.google.com/toolkit/)).

Save the translated result to ``entoja.po`` and then apply the translation:

```
$ nbtranslate --po entoja.po notebook_en.ipynb > notebook_ja.ipynb
```

License
-------

New-BSD

by Yosuke Matsusaka, MID Academic Promotions Inc.