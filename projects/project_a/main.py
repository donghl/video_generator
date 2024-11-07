from datetime import datetime
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from projects.common.utils import format_datetime, calculate_statistics

def process_data():
    current_time = datetime.now()
    formatted_time = format_datetime(current_time)
    print(f"当前时间: {formatted_time}")
    
    # 使用公共模块的统计功能
    data = [1.5, 2.7, 3.2, 4.8, 5.1]
    stats = calculate_statistics(data)
    print("数据统计结果:")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    process_data() 