
## 升级依赖

``` shell
pip install --upgrade django django-simple-captcha django-registration-redux django-grappelli django-celery-beat django-bootstrap4 django-prometheus prometheus-client djangorestframework django-celery-beat celery flower django-debug-toolbar  django-python3-ldap ldap3 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

如果遇到版本问题，可以查看 requirements.django5.txt 文件中适用于 django 5.0 的 package 版本。

## 迁移 celery 数据库

``` shell
python manage.py migrate
```

## 更改 admin 用户密码（非必须）

python manage.py changepassword admin

## 更改 jobs/template/base.html 的内容

找到如下行的内容：

```html
<a href="/accounts/logout" style="text-decoration: none; color:#007bff">{% translate "Logout" %}</a>
```

替换成如下内容：

```html
    <form method="post" action="/accounts/logout/">
      {% csrf_token %}<button type="submit" style="background: none!important;border: none;padding: 0!important;color: #069;text-decoration: underline;cursor: pointer;margin-right: 10px;">{% translate "Logout" %}</button>
    </form>
```

## 启动服务

```shell
python3 ./manage.py runserver 127.0.0.1:8000 --settings=settings.local
```

## 系统的使用

候选人简历投递： http://127.0.0.1:8000/
管理员后台管理：http://127.0.0.1:8000/admin/

候选人注册之后可以提交简历。 
管理员（admin）在管理后台的简历列表中标记候选人进入流程之后，在应聘者列表中能够看到候选人。 
管理员可以分配面试官， 进入后续面试流程。