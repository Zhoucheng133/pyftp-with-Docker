FROM python:3.12.5
WORKDIR /app
COPY . /app
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN python -m pip install --upgrade pip
ENV TZ=Asia/Shanghai
RUN pip install pyftpdlib
EXPOSE 6789
CMD ["python", "main.py"]