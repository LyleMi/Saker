<p align="center"><a href="" target="_blank" rel="noopener noreferrer"><img width="200" src="https://raw.githubusercontent.com/LyleMi/Saker/master/logo.jpg" alt="Saker logo"></a></p>

[![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](http://www.python.org/download/)
![](https://img.shields.io/github/issues/lylemi/saker.svg)
![](https://img.shields.io/github/forks/lylemi/saker.svg)
![](https://img.shields.io/github/stars/lylemi/saker.svg)
![](https://img.shields.io/github/license/lylemi/saker.svg)

[中文版本(Chinese version)](README.zh-cn.md)

Saker是一个辅助测试Web站点的工具，有信息收集、渗透测试、爆破路径等功能。

本工具仅供学习和交流使用，请勿在未授权的测试中使用。

## 目录

- [功能](#%E5%8A%9F%E8%83%BD)
- [安装](#%E5%AE%89%E8%A3%85)
- [用例](#%E7%94%A8%E4%BE%8B)

## 功能

- Web扫描
  - 信息搜集
  - 框架指纹
- Fuzz Web 请求
  - XSS
  - SQL injection
  - SSRF
  - XXE
  - ...
- 子域名搜集
- 端口扫描
- 爆破
  - Web 路径
  - 密码
  - 域名
- 辅助服务器
  - DNS重绑定
  - SSRF
  - XSS
- 三方API集成
  - censys
  - crtsh
  - fofa
  - github
  - shodan
  - sqlmap
  - threadcrowd
  - ...

## 安装

### 最新版本

```bash
pip install -U git+https://github.com/lylemi/saker
```

```bash
git clone https://github.com/LyleMi/Saker.git
pip install -r requirements.txt
python setup.py install
```

### 稳定版本

```bash
pip install Saker
```

### 开发测试版

将 /path/to/saker 加入 PYTHONPATH 中

```bash
export PYTHONPATH=/path/to/saker:$PYTHONPATH
```

## 用例

### Web网站扫描

```python
from saker.core.scaner import Scanner
s = Scanner("http://127.0.0.1")
s.scan(filename="index.php", ext="php")
```

或者使用命令行

```bash
python -m saker scan

usage: main.py [options]

Saker Scanner

optional arguments:
  -h, --help            show this help message and exit
  -s, --scan            run with list model
  -f file, --file file  scan specific file
  -e ext, --ext ext     scan specific ext
  -i, --info            get site info
  -u URL, --url URL     define specific url
  -p PROXY, --proxy PROXY
                        proxy url
  -t INTERVAL, --timeinterval INTERVAL
                        scan time interval, random sleep by default
```

### 测试网站

```python
from saker.core.mutator import Mutator
options = {
    "url": "http://127.0.0.1:7777/",
    "params": {
        "test": "test"
    }
}
m = Mutator(options)
m.fuzz('url')
m.fuzz('params', 'test')
```

命令行

```bash
python -m saker fuzz

usage: [options]

Saker Fuzzer

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     define specific url
  -m METHOD, --method METHOD
                        request method, use get as default
  -p PARAMS, --params PARAMS
                        request params, use empty string as default
  -d DATA, --data DATA  request data, use empty string as default
  -H HEADERS, --headers HEADERS
                        request headers, use empty string as default
  -c COOKIES, --cookies COOKIES
                        request cookies, use empty string as default
  -P PART, --part PART  fuzz part, could be url / params / data / ...
  -k KEY, --key KEY     key to be fuzzed
  -v VULN, --vuln VULN  Vulnarability type to be fuzzed
  -t INTERVAL, --timeinterval INTERVAL
                        scan time interval, random sleep by default
```

### 端口扫描

```bash
python -m saker port

usage: [options]

Saker Port Scanner

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        define scan target
  -b, --background      run port scanner in background with unix daemon, only
                        support unix platform
```

### 生成模糊测试载荷

#### Unicode Fuzz

```python
from saker.fuzzer.code import Code
payload = Code.fuzzErrorUnicode(payload)
```

#### Fuzz SSI

```python
from saker.fuzzers.ssi import SSI
payloads = [i for i in SSI.fuzz()]
```

### 爆破密码等

```python
from saker.brute.dir import DirBrute
dirBrute = DirBrute("php", "index.php")
paths = dirBrute.weakfiles()
```

目前支持http basic auth / ftp / MySQL / SSH 等的密码爆破。

### API调用

#### Crt.sh

```python
from saker.api.crtsh import crtsh
crtsh("github.com")
```

#### DNSDumper

```python
from saker.api.dnsdumper import DNSdumpster
DNSdumpster("github.com")
```

#### Github API

```python
from saker.api.githubapi import GithubAPI
g = GithubAPI()
g.gatherByEmail("@github.com")
```

#### SQLMap API

```python
from saker.api.sqlmap import SQLMap
options = {"url": "https://github.com"}
SQLMap().scan(options)
```
### HTML处理

```python
import requests
from saker.handler.htmlHandler import HTMLHandler
r = requests.get("https://github.com")
h = HTMLHandler(r.text)
print(h.title)
The world’s leading software development platform · GitHub
print(h.subdomains("github.com"))
['enterprise.github.com', 'resources.github.com', 'developer.github.com', 'partner.github.com', 'desktop.github.com', 'api.github.com', 'help.github.com', 'customer-stories-feed.github.com', 'live-stream.github.com', 'services.github.com', 'lab.github.com', 'shop.github.com', 'education.github.com']
```

### 启动特定功能服务器

```python
from saker.servers.socket.dnsrebinding import RebindingServer
values = {
    'result': ['8.8.8.8', '127.0.0.1'],
    'index': 0
}
dnsServer = RebindingServer(values)
dnsServer.serve_forever()
```

## 声明

项目仅供测试和实验目的，请勿测试任何未授权的系统。

## Contribution
---

如果有任何的问题、意见或者建议欢迎以[Issues](https://github.com/lylemi/saker/issues)或PR的形式提出，不胜感激。
