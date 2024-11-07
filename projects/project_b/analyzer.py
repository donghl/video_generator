from typing import Dict, Any
import json
import os

from projects.common.utils import load_json_file, calculate_statistics
from projects.common.config import ConfigManager

class DataAnalyzer:
    def __init__(self):
        self.config = ConfigManager()
        self.analysis_mode = self.config.get("project_b", "analysis_mode", "basic")
        self.save_results = self.config.get("project_b", "save_results", True)
    
    def analyze_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """直接分析数据字典"""
        try:
            if "values" in data:
                stats = calculate_statistics(data["values"])
                return {
                    "status": "success",
                    "statistics": stats,
                    "metadata": data.get("metadata", {})
                }
            else:
                return {
                    "status": "error",
                    "message": "No values found in data"
                }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    
    def analyze_json_file(self, filename: str) -> Dict[str, Any]:
        """分析JSON文件"""
        try:
            data = load_json_file(filename)
            return self.analyze_data(data)
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error processing file: {str(e)}"
            } 