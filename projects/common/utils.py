from datetime import datetime
from typing import List, Dict, Any
import json

def format_datetime(dt: datetime) -> str:
    """格式化日期时间"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def load_json_file(filepath: str) -> Dict[str, Any]:
    """加载JSON文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_statistics(numbers: List[float]) -> Dict[str, float]:
    """计算基本统计数据"""
    if not numbers:
        return {"mean": 0, "sum": 0, "min": 0, "max": 0}
    
    return {
        "mean": sum(numbers) / len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers)
    } 