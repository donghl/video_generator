from datetime import datetime
from typing import Dict, Any

from projects.common.utils import format_datetime, calculate_statistics
from projects.common.config import ConfigManager

class DataProcessor:
    def __init__(self):
        self.config = ConfigManager()
        self.date_format = self.config.get("project_a", "date_format", "%Y-%m-%d %H:%M:%S")
        self.output_format = self.config.get("project_a", "output_format", "json")
    
    def process_data(self, data: list = None) -> Dict[str, Any]:
        """处理数据并返回结果"""
        current_time = datetime.now()
        formatted_time = format_datetime(current_time)
        
        if data is None:
            data = [1.5, 2.7, 3.2, 4.8, 5.1]  # 默认数据
            
        stats = calculate_statistics(data)
        
        result = {
            "timestamp": formatted_time,
            "statistics": stats,
            "data_length": len(data)
        }
        
        return result 