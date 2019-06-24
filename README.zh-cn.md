<p align="center"><a href="" target="_blank" rel="noopener noreferrer"><img width="200" src="https://raw.githubusercontent.com/LyleMi/Saker/master/logo.jpg" alt="Saker logo"></a></p>

[![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](http://www.python.org/download/)
![](https://img.shields.io/github/issues/lylemi/saker.svg)
![](https://img.shields.io/github/forks/lylemi/saker.svg)
![](https://img.shields.io/github/stars/lylemi/saker.svg)
![](https://img.shields.io/github/license/lylemi/saker.svg)

[中文版本(Chinese version)](README.zh-cn.md)

Saker是一个辅助测试Web站点的工具，有信息收集、渗透测试、爆破路径等功能。

本工具仅供学习和交流使用，请勿在未授权的测试中使用。

## 安装

```bash
git clone https://github.com/LyleMi/Saker.git
pip install -r requirements.txt
python setup.py install
```

或者使用pip安装

```bash
pip install -u Saker
```

## 特性

### Web网站扫描

```python
>>> from saker.core.scaner import Saker
>>> s = Saker("http://127.0.0.1")
>>> s.scan(filename="index.php", ext="php")
```

或者使用命令行

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

### 生成模糊测试载荷

```python
>>> from saker.fuzzer.code import Code
>>> payload = Code.fuzzErrorUnicode(payload)
```

```python
>>> from saker.fuzzers.ssi import SSI
>>> payloads = SSI.test()
```

### 爆破密码等

```python
>>> from saker.brute.dir import DirBrute
>>> dirBrute = DirBrute("php", "index.php")
>>> paths = dirBrute.weakfiles()
```

目前支持http basic auth / ftp / MySQL / SSH 等的密码爆破。

### API调用

```python
>>> from saker.api.dnsdumper import DNSdumpster
>>> DNSdumpster("github.com")
```

### HTML处理

```python
>>> from saker.handler.htmlhandler import HTMLHandler
>>> h = HTMLHandler("<html><head><title>title</title></head><body></body></html>")
>>> print(h.title)
```

### 端口扫描

```python
>>> from saker.port.nmap import Nmap
>>> n = Nmap(domain)
>>> ret = n.run()
>>> print(n.ret)
```

## TODO

- FingerPrint
- AutoTest
