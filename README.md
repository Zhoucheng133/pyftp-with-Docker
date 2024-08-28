# Pyftpdlib Docker部署

1. 根据你的需要修改`main.py`
   ```python
   如果需要登录，你的代码应该是这样
   # ...
   authorizer.add_user("username", "password", "dir", perm='elradfmw')
   # authorizer.add_anonymous('dir', perm='elradfmw')
   handler = FTPHandler
   handler.authorizer = authorizer
   # ...

   #如果允许匿名登录，你的代码应该是这样
   # ...
   # authorizer.add_user("username", "password", "dir", perm='elradfmw')
   authorizer.add_anonymous('dir', perm='elradfmw')
   handler = FTPHandler
   handler.authorizer = authorizer
   # ...
   ```
2. 将本项目复制到服务器
3. 使用下面的命令来创建镜像，镜像名称随意
   ```bash
   docker build -t <镜像名称> <本项目在服务器中的位置>
   ```
4. 使用下面的命令创建容器，容器名称随意，镜像名称为上一步的名称
   ```bash
   sudo docker run -d --restart always -v <服务器中FTP映射路径>:/app/dir -p 6789:6789 -p 60000-60010:60000-60010 --name <容器名称> <镜像名称>
   ```