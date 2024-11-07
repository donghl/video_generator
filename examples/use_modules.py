from projects.project_a.processor import DataProcessor
from projects.project_b.analyzer import DataAnalyzer

def main():
    # 创建处理器和分析器实例
    processor = DataProcessor()
    analyzer = DataAnalyzer()
    
    # 准备测试数据
    test_data = {
        "values": [10.5, 20.3, -5.7, 0.0, 15.8],
        "metadata": {
            "source": "test",
            "type": "temperature"
        }
    }
    
    # 使用处理器处理数据
    process_result = processor.process_data(test_data["values"])
    print("\n处理结果:")
    print(process_result)
    
    # 使用分析器分析数据
    analysis_result = analyzer.analyze_data(test_data)
    print("\n分析结果:")
    print(analysis_result)

if __name__ == "__main__":
    main() 