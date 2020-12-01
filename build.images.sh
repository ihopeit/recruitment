 docker build  -t ihopeit/recruitment-base:0.8 .
 docker tag ihopeit/recruitment-base:0.8 ihopeit/django-recruitment:0.8

 ## or just docker pull already built image from docker hub:
 # docker pull ihopeit/django-recruitment:0.8

## 构建包含 local.py 文件的 0.9 版本镜像：
cp settings/local.py settings/local-setting.py
docker build -f Dockerfile-local-setting -t ihopeit/django-recruitment:0.9 .
rm settings/local-setting.py

sudo docker tag ihopeit/django-recruitment:0.9 registry.cn-beijing.aliyuncs.com/ihopeit/django-recruitment:0.9