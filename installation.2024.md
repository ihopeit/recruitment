
## 环境准备
pyenv virtualenv 3.10 recruitment

pyenv activate recruitment

pip install -r requirements.txt

pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

## 本地启动 redis 服务

redis-server

## 更改 admin 用户密码

python manage.py changepassword admin

## 启动服务
python3 ./manage.py runserver 127.0.0.1:8000 --settings=settings.local

使用 admin 登录.