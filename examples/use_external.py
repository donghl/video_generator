from external_app import generate_report

def main():
    # 准备数据
    test_data = {
        "values": [100.5, 200.3, -50.7, 0.0, 158.8],
        "metadata": {
            "source": "sensor_data",
            "type": "temperature"
        }
    }
    
    # 生成报告
    report = generate_report(test_data)
    
    # 使用报告数据
    print("数据分析报告")
    print("=" * 30)
    print(f"生成时间: {report['timestamp']}")
    
    # 显示统计结果
    if "extended_statistics" in report["analysis"]:
        stats = report["analysis"]["extended_statistics"]
        print("\n基础统计:")
        print(f"平均值: {stats['mean']:.2f}")
        print(f"总和: {stats['sum']:.2f}")
        print(f"最小值: {stats['min']:.2f}")
        print(f"最大值: {stats['max']:.2f}")
    
    # 显示其他分析结果
    print("\n数据特征:")
    print(f"数据点数量: {report['analysis']['data_points']}")
    print(f"包含负值: {report['analysis']['has_negative']}")
    print(f"包含零值: {report['analysis']['has_zero']}")

if __name__ == "__main__":
    main() 