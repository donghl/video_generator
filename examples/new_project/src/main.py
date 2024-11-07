from external_app import generate_report
from datetime import datetime
import json

class DataAnalyzer:
    def __init__(self):
        self.report_history = []
    
    def analyze_batch_data(self, data_list):
        """分析多批数据"""
        results = []
        for data in data_list:
            report = generate_report(data)
            results.append(report)
            self.report_history.append({
                "timestamp": datetime.now().isoformat(),
                "report": report
            })
        return results
    
    def save_reports(self, filename="reports.json"):
        """保存所有报告历史"""
        with open(filename, 'w') as f:
            json.dump(self.report_history, f, indent=2)

def main():
    analyzer = DataAnalyzer()
    
    # 示例数据批次
    test_batches = [
        {
            "values": [10.5, 20.3, 30.7],
            "metadata": {"batch": "1", "type": "test"}
        },
        {
            "values": [-5.2, 0.0, 15.8],
            "metadata": {"batch": "2", "type": "test"}
        }
    ]
    
    # 分析数据
    results = analyzer.analyze_batch_data(test_batches)
    
    # 保存报告
    analyzer.save_reports()
    
    # 显示结果
    for i, result in enumerate(results, 1):
        print(f"\n批次 {i} 分析结果:")
        print("-" * 30)
        print(f"时间戳: {result['timestamp']}")
        print("统计数据:", result['analysis']['extended_statistics'])

if __name__ == "__main__":
    main() 