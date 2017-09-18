# Saker

CTF Web framework and fuzz tool, can help you scan website, fuzz it with some payloads

## install

```
git clone https://github.com/LyleMi/Saker.git
python setup.py install
```

## usage

### scan website

```python
from saker.classes.saker import Saker
s = Saker("http://127.0.0.1")
s.scan(filename="index.php", ext="php")
```

or by shell

```
usage: saker.py [options]
CTF Web framework and fuzz tool

optional arguments:
  -h, --help            show this help message and exit
  -s, --scan            run with list model
  -f file, --file file  scan specific file
  -e ext, --ext ext     scan specific ext
  -i, --interactive     run with interactive model
  -u URL, --url URL     define specific url
  -t INTERVAL, --timeinterval INTERVAL
                        set time interval
```

### generate fuzz payload

```python
>>> from saker.payloads.misc import Misc
>>> payload = Misc.fuzzErrorUnicode(payload)
```