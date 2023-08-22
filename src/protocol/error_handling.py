class ErrorHandling:
    def __init__(self):
        # 定义可能的错误代码及其描述
        self.error_codes = {
            0: "Success",
            1: "Connection Error",
            2: "Authentication Failed",
            3: "Invalid Data Format",
            4: "Permission Denied",
            5: "Resource Unavailable",
            6: "Internal Server Error",
            # 更多自定义错误可以在此添加
        }

    def handle_error(self, error_code):
        # 获取错误描述
        description = self.error_codes.get(error_code, "Unknown Error")
        print(f"Error {error_code}: {description}")
        # 根据错误代码执行特定逻辑
        # 例如，可以尝试重新连接、发送错误报告、关闭资源等
        if error_code == 1:
            print("Attempting to reconnect...")
        elif error_code == 6:
            print("Please contact support.")
        # 其他错误处理逻辑


if __name__ == "__main__":
    error_handler = ErrorHandling()

    # 模拟一些错误
    error_handler.handle_error(1)
    error_handler.handle_error(5)
    error_handler.handle_error(999) # 未知错误
