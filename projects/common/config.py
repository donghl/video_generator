import os
import toml
from typing import Dict, Any
from pprint import pprint

class ConfigManager:
    _instance = None
    _config = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._config is None:
            self.load_config()
    
    def load_config(self, config_path: str = None):
        """加载配置文件"""
        if config_path is None:
            # 默认在项目根目录查找config.toml
            root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            config_path = os.path.join(root_dir, 'config.toml')
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                self._config = toml.load(f)
        except FileNotFoundError:
            self._config = self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """获取默认配置"""
        return {
            "common": {
                "temp_dir": "temp",
                "data_dir": "data",
                "log_level": "INFO"
            },
            "project_a": {
                "output_format": "json",
                "date_format": "%Y-%m-%d %H:%M:%S"
            },
            "project_b": {
                "analysis_mode": "basic",
                "save_results": True
            },
            "external_app": {
                "report_format": "detailed",
                "save_history": True,
                "history_file": "reports.json"
            }
        }
    
    def get(self, section: str, key: str, default: Any = None) -> Any:
        """获取配置值"""
        try:
            return self._config[section][key]
        except KeyError:
            return default
    
    def get_section(self, section: str) -> Dict[str, Any]:
        """获取整个配置区段"""
        return self._config.get(section, {})
    
    def get_all_config(self) -> Dict[str, Any]:
        """获取所有配置"""
        return self._config

def print_config_section(section_name: str, section_data: Dict[str, Any], indent: int = 0):
    """格式化打印配置区段"""
    print("  " * indent + f"[{section_name}]")
    for key, value in section_data.items():
        if isinstance(value, dict):
            print_config_section(key, value, indent + 1)
        else:
            print("  " * (indent + 1) + f"{key} = {value}")

def main():
    """主函数：读取并显示所有配置"""
    config_manager = ConfigManager()
    all_config = config_manager.get_all_config()
    
    print("\n配置文件内容:")
    print("=" * 50)
    
    # 按区段打印配置
    for section_name, section_data in all_config.items():
        print_config_section(section_name, section_data)
        print()
    
    print("=" * 50)
    print("\n配置详细信息:")
    print("-" * 50)
    
    # 获取并显示特定配置示例
    print(f"临时目录: {config_manager.get('common', 'temp_dir')}")
    print(f"日志级别: {config_manager.get('common', 'log_level')}")
    print(f"Project A 输出格式: {config_manager.get('project_a', 'output_format')}")
    print(f"Project B 分析模式: {config_manager.get('project_b', 'analysis_mode')}")
    
    # 显示完整的配置（使用pprint格式化输出）
    print("\n完整配置（字典格式）:")
    print("-" * 50)
    pprint(all_config, indent=2)

if __name__ == "__main__":
    main()