import bcrypt

class Authentication:
    def __init__(self):
        # 此处硬编码用户名和bcrypt哈希后的密码，实际应用中应从安全的数据源获取
        self.users = {
            'robot1': b'$2b$12$Wc4F2BJsd.KKKgpGpb/YWeed2Q3/YJKzjCJSmYQnIlgv5qnPEBQqW', # password: 'password'
        }

    def authenticate(self, username, password):
        # 获取存储的哈希
        password_hash = self.users.get(username)
        if password_hash:
            # 使用bcrypt来验证密码与存储的哈希是否匹配
            return bcrypt.checkpw(password.encode(), password_hash)
        return False

if __name__ == '__main__':
    auth = Authentication()
    username = 'robot1'
    password = 'password'
    if auth.authenticate(username, password):
        print('Authentication successful')
    else:
        print('Authentication failed')
