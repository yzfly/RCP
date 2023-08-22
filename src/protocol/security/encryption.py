from cryptography.hazmat.primitives import algorithms, modes, padding
from cryptography.hazmat.backends import default_backend
import os

class Encryption:
    def __init__(self, key=None):
        self.backend = default_backend()
        # 使用给定的密钥或生成一个新的随机密钥
        self.key = key if key else os.urandom(32) # 256-bit key
        self.iv = os.urandom(16) # 128-bit IV

    def encrypt(self, data):
        # 创建加密对象
        cipher = self._create_cipher()
        encryptor = cipher.encryptor()
        # 添加PKCS7填充
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()
        # 加密填充的数据
        ct = encryptor.update(padded_data) + encryptor.finalize()
        return ct

    def decrypt(self, ciphertext):
        # 创建解密对象
        cipher = self._create_cipher()
        decryptor = cipher.decryptor()
        # 解密密文
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        # 删除PKCS7填充
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        return data.decode()

    def _create_cipher(self):
        # 创建AES加密对象
        algorithm = algorithms.AES(self.key)
        mode = modes.CBC(self.iv)
        return self.backend.create_symmetric_encryption_ctx(algorithm, mode)

if __name__ == "__main__":
    encryption = Encryption()
    data = "Hello Robot!"
    ciphertext = encryption.encrypt(data)
    print("Ciphertext:", ciphertext)
    plaintext = encryption.decrypt(ciphertext)
    print("Plaintext:", plaintext)
