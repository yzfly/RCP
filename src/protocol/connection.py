import socket

class Connection:
    def __init__(self, address, port, timeout=5):
        self.address = address
        self.port = port
        self.timeout = timeout
        self.socket = None

    def connect(self):
        try:
            # 创建一个TCP套接字
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 设置连接超时时间
            self.socket.settimeout(self.timeout)
            # 连接到指定的地址和端口
            self.socket.connect((self.address, self.port))
            print(f"Connected to {self.address}:{self.port}")
        except (socket.timeout, ConnectionError) as e:
            print(f"Failed to connect to {self.address}:{self.port} - {str(e)}")
            self.disconnect()

    def disconnect(self):
        if self.socket:
            # 关闭套接字
            self.socket.close()
            self.socket = None
            print(f"Disconnected from {self.address}:{self.port}")

    def send_data(self, data):
        if self.socket:
            try:
                # 将数据发送到连接的套接字
                self.socket.sendall(data.encode())
            except ConnectionError as e:
                print(f"Failed to send data to {self.address}:{self.port} - {str(e)}")
                self.disconnect()

    def receive_data(self, buffer_size=1024):
        if self.socket:
            try:
                # 从连接的套接字接收数据
                return self.socket.recv(buffer_size).decode()
            except ConnectionError as e:
                print(f"Failed to receive data from {self.address}:{self.port} - {str(e)}")
                self.disconnect()
        return None

if __name__ == '__main__':
    connection = Connection('192.168.1.100', 8000)
    connection.connect()
    connection.send_data('Hello Robot!')
    data = connection.receive_data()
    print('Received:', data)
    connection.disconnect()
