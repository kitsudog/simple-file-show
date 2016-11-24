#!/bin/bash
set -euo pipefail
pip2.7 install -r requirements.txt --trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple
python2.7 app.py
