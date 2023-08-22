from src.protocol.connection import Connection

class Transport:
    def __init__(self, address, port):
        self.connection = Connection(address, port)

    def send(self, data):
        # 连接到远程地址
        self.connection.connect()
        # 发送数据
        self.connection.send_data(data)
        # 断开连接
        self.connection.disconnect()

    def receive(self, buffer_size=1024):
        # 连接到远程地址
        self.connection.connect()
        # 接收数据
        data = self.connection.receive_data(buffer_size)
        # 断开连接
        self.connection.disconnect()
        return data

if __name__ == '__main__':
    transport = Transport('192.168.1.100', 8000)
    transport.send('Hello Robot!')
    data = transport.receive()
    print('Received:', data)
