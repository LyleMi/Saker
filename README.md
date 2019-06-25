<p align="center"><a href="" target="_blank" rel="noopener noreferrer"><img width="200" src="https://raw.githubusercontent.com/LyleMi/Saker/master/logo.jpg" alt="Saker logo"></a></p>

[![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](http://www.python.org/download/)
![](https://img.shields.io/github/issues/lylemi/saker.svg)
![](https://img.shields.io/github/forks/lylemi/saker.svg)
![](https://img.shields.io/github/stars/lylemi/saker.svg)
![](https://img.shields.io/github/license/lylemi/saker.svg)

[中文版本(Chinese version)](README.zh-cn.md)

Saker is a tool for fuzz Web Applications. It can be used to penetrate website, fuzz some vulnerabilities, brute password and dirs.

This project is for research and study only, do not use Saker for unauthorized penetration testing.

## Install

```bash
git clone https://github.com/LyleMi/Saker.git
pip install -r requirements.txt
python setup.py install
```

or by pip

```bash
pip install Saker
```

or via Github

```bash
pip install git+https://github.com/lylemi/saker
```

## Features

### Scan Website

```python
>>> from saker.core.scaner import Saker
>>> s = Saker("http://127.0.0.1")
>>> s.scan(filename="index.php", ext="php")
```

or by shell

```bash
python -m saker

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

```python
>>> from saker.fuzzers.ssi import SSI
>>> payloads = SSI.test()
```

### Brute password or others

```python
>>> from saker.brute.dir import DirBrute
>>> dirBrute = DirBrute("php", "index.php")
>>> paths = dirBrute.weakfiles()
```

now support brute http basic auth, ftp, mysql, ssh, telnet, zipfile...

### Call Some API

```python
>>> from saker.api.dnsdumper import DNSdumpster
>>> DNSdumpster("github.com")
```

### Handle HTML

```python
>>> from saker.handler.htmlhandler import HTMLHandler
>>> h = HTMLHandler("<html><head><title>title</title></head><body></body></html>")
>>> print(h.title)
```

### Port Scanner

```python
>>> from saker.port.nmap import Nmap
>>> n = Nmap(domain)
>>> ret = n.run()
>>> print(n.ret)
```

## TODO

- FingerPrint
  - CMS
  - Framework
  - Language
  - OS
  - WAF
- AutoTest

## Contributing

Contributions, issues and feature requests are welcome.

Feel free to check [issues page](https://github.com/lylemi/saker/issues) if you want to contribute.

## Show your support

Please star this repository if this project helped you.

## License

Copyright © 2019 [Lyle](https://github.com/lylemi).

This project is [GPLv3](https://github.com/lylemi/saker/blob/master/LICENSE) licensed.
