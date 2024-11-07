import os
from typing import List, Dict
import toml
import inspect
import importlib
import sys

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def get_project_structure() -> str:
    """获取项目结构"""
    structure = []
    for root, dirs, files in os.walk('.'):
        # 跳过隐藏目录和虚拟环境
        if '/.' in root or '/.venv' in root or '/__pycache__' in root:
            continue
            
        level = root.count(os.sep)
        indent = '│   ' * level
        structure.append(f'{indent}├── {os.path.basename(root)}/')
        
        for file in sorted(files):
            if file.startswith('.') or file.endswith('.pyc'):
                continue
            indent = '│   ' * (level + 1)
            structure.append(f'{indent}├── {file}')
    
    return '\n'.join(structure)

def get_module_info(module_path: str) -> Dict:
    """获取模块信息"""
    try:
        module = importlib.import_module(module_path)
        doc = module.__doc__ or "No description available"
        classes = inspect.getmembers(module, inspect.isclass)
        functions = inspect.getmembers(module, inspect.isfunction)
        return {
            "doc": doc,
            "classes": classes,
            "functions": functions
        }
    except Exception as e:
        return {"error": str(e)}

def generate_readme() -> str:
    """生成README.md内容"""
    # 读取pyproject.toml获取项目信息
    with open('pyproject.toml', 'r') as f:
        project_info = toml.load(f)

    # 读取配置文件
    with open('config.toml', 'r') as f:
        config = toml.load(f)

    readme_content = f"""# {project_info['tool']['poetry']['name']}

{project_info['tool']['poetry']['description']}

## 项目结构

{get_project_structure()} 