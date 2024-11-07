#!/bin/bash

# 检查是否安装了pyenv
if ! command -v pyenv &> /dev/null; then
    echo "正在安装pyenv..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install pyenv
    else
        # Linux
        curl https://pyenv.run | bash
    fi
fi

# 安装指定版本的Python
echo "安装Python 3.8.10..."
pyenv install 3.8.10 --skip-existing

# 设置本地Python版本
pyenv local 3.8.10

# 安装poetry
if ! command -v poetry &> /dev/null; then
    echo "安装poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# 创建虚拟环境并安装依赖
echo "安装项目依赖..."
poetry env use $(pyenv which python)
poetry install

echo "环境设置完成！" 