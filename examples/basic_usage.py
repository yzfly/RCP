from src.protocol.connection import Connection
from src.protocol.transport import Transport

connection = Connection('192.168.1.100', 8000)
transport = Transport(connection)

connection.connect()
transport.send('Hello Robot!')
data = transport.receive()
connection.disconnect()

print('Received:', data)
