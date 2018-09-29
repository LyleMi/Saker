<p align="center"><a href="" target="_blank" rel="noopener noreferrer"><img width="200" src="./logo.jpg" alt="Saker logo"></a></p>

[![Python 2.7](https://img.shields.io/badge/Python-2.7-blue.svg)](http://www.python.org/download/)
![License](https://img.shields.io/aur/license/yaourt.svg)

Saker is a tool for fuzz Web Applications. It can be used to penetrate website, fuzz some vulnerabilities or brute password and dirs. This project is for research and study only, do not use Saker for unauthorized penetration testing.

## Install

```
git clone https://github.com/LyleMi/Saker.git
python setup.py install
```

## Features

### Scan Website

```python
>>> from saker.main import Saker
>>> s = Saker("http://127.0.0.1")
>>> s.scan(filename="index.php", ext="php")
```

or by shell

```
usage: main.py [options]
Tool For Fuzz Web Applications

optional arguments:
  -h, --help            show this help message and exit
  -s, --scan            run with list model
  -f file, --file file  scan specific file
  -e ext, --ext ext     scan specific ext
  -i, --interactive     run with interactive model
  -u URL, --url URL     define specific url
  -p PROXY, --proxy PROXY
                        proxy url
  -t INTERVAL, --timeinterval INTERVAL
                        scan time interval, random sleep by default
```

### Generate fuzz payload

```python
>>> from saker.fuzzer.code import Code
>>> payload = Code.fuzzErrorUnicode(payload)
```

### Brute password or others


```python
>>> from saker.brute.dir import DirBrute
>>> dirBrute = DirBrute("php", "index.php")
>>> paths = dirBrute.weakfiles()
```

now support brute http basic auth, ftp, mysql, ssh, telnet, zipfile...

## TODO

- FingerPrint
- AutoTest
