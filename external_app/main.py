import json
from datetime import datetime
from typing import Dict, Any
import os
import sys

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from projects.common.config import ConfigManager
from projects.project_a.processor import DataProcessor
from projects.project_b.analyzer import DataAnalyzer
from projects.common.utils import format_datetime

def generate_report(data: Dict[str, Any]) -> Dict[str, Any]:
    """生成综合报告，使用A和B模块的功能"""
    config = ConfigManager()
    current_time = datetime.now()
    
    # 初始化处理器和分析器
    processor = DataProcessor()
    analyzer = DataAnalyzer()
    
    report = {
        "timestamp": format_datetime(current_time),
        "raw_data": data,
        "analysis": {}
    }
    
    # 使用配置
    report_format = config.get("external_app", "report_format", "basic")
    save_history = config.get("external_app", "save_history", False)
    
    # 使用项目A的功能处理数据
    if "values" in data:
        process_result = processor.process_data(data["values"])
        report["process_result"] = process_result
    
    # 使用项目B的功能分析数据
    analysis_result = analyzer.analyze_data(data)
    report["analysis"] = analysis_result
    
    # 如果需要保存历史
    if save_history:
        history_file = config.get("external_app", "history_file", "reports.json")
        _save_to_history(report, history_file)
    
    return report

def _save_to_history(report: Dict[str, Any], history_file: str):
    """保存报告到历史文件"""
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    
    history.append(report)
    
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=2)

def main():
    """主函数"""
    # 示例数据
    test_data = {
        "values": [15.5, -2.3, 0.0, 42.1, 23.8, 17.9],
        "metadata": {
            "source": "external_app",
            "type": "test_data"
        }
    }
    
    print("开始生成综合报告...")
    print("-" * 50)
    
    report = generate_report(test_data)
    
    print("\n最终报告:")
    print("-" * 50)
    print(f"生成时间: {report['timestamp']}")
    print("\n分析结果:")
    for key, value in report["analysis"].items():
        if isinstance(value, dict):
            print(f"\n{key}:")
            for k, v in value.items():
                print(f"  {k}: {v}")
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    main() 