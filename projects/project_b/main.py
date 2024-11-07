import sys
import os
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from projects.common.utils import load_json_file, calculate_statistics

def analyze_json_data(filename: str):
    try:
        # 假设json文件包含数值数据
        data = load_json_file(filename)
        if "values" in data:
            stats = calculate_statistics(data["values"])
            print(f"文件 {filename} 的统计结果:")
            for key, value in stats.items():
                print(f"{key}: {value:.2f}")
    except Exception as e:
        print(f"处理文件时出错: {str(e)}")

if __name__ == "__main__":
    # 示例用法
    sample_data = {
        "values": [10.5, 20.3, 30.7, 40.2, 50.1]
    }
    
    # 创建示例JSON文件
    with open("sample_data.json", "w") as f:
        json.dump(sample_data, f)
    
    analyze_json_data("sample_data.json") 