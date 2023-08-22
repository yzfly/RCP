class EnergyManagement:
    def __init__(self):
        # 定义可能的能源模式
        self.modes = {
            'high': "High Performance",
            'medium': "Balanced Power and Performance",
            'low': "Low Power Consumption",
        }
        self.current_mode = 'medium'

    def set_power_mode(self, mode):
        # 检查模式是否有效
        if mode not in self.modes:
            print(f"Error: Invalid power mode '{mode}'")
            return False

        # 设置新的能源模式
        self.current_mode = mode
        description = self.modes[mode]
        print(f"Power mode set to '{description}'")

        # 这里可以添加实际调整硬件或系统设置的代码
        # 例如调整处理器频率、关闭非必要的设备等

        return True

    def get_power_mode(self):
        return self.current_mode, self.modes[self.current_mode]

    def get_available_modes(self):
        return self.modes

if __name__ == "__main__":
    energy_management = EnergyManagement()

    # 设置高性能模式
    energy_management.set_power_mode('high')

    # 获取当前模式
    mode, description = energy_management.get_power_mode()
    print(f"Current power mode: {description}")

    # 设置无效的模式
    energy_management.set_power_mode('ultra-low')
