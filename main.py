from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
 
authorizer = DummyAuthorizer()
# 如果需要登录
# authorizer.add_user("username", "password", "dir", perm='elradfmw')
# 如果匿名登录
authorizer.add_anonymous('dir', perm='elradfmw')
 
handler = FTPHandler
handler.authorizer = authorizer

handler.passive_ports = range(60000, 60010)
 
server = FTPServer(('0.0.0.0', 6789), handler)
server.serve_forever()