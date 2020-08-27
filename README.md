## 项目说明

用做创业公司职位发布，简历投递，招聘管理的开源项目，基于高效的Django & Python开发。
这是使用Python Django花了1天时间开发出来，可以用于企业的招聘面试管理的Django项目。
优秀的产品经理，能够做好迭代版本规划，

### 运行的前提条件

机器上有安装有Python, Django. 参考:
https://docs.djangoproject.com/

### 如何运行
本地和生产环境分别运行如下命令:
python ./manage.py runserver 127.0.0.1:8000 --settings=settings.local
python ./manage.py runserver 127.0.0.1:8000 --settings=settings.production

然后可以通过访问如下两个页面 
* http://127.0.0.1:8000 首页
* http://127.0.0.1:8000/admin 管理后台

### 命令行导入候选人

python manage.py import_candidates --path /path/to/your/file.csv

### OpenLDAP/Active Directory集成
* 1.settings/base.py中配置LDAP相关的映射信息 （用户尝试登陆时自动创建账号，但创建的账号 is_staff = false,不能登陆系统）
* 2.运行 ./manage.py ldap_sync_users 来同步LDAP账号到 Django 账号库， 使用用户在 django 后台有账号。
* 3.admin登陆后台，编辑用户属性，设置为 is_staff （使得用户能登陆）, 同时添加到自己建的群组: interviewer （使得用户有权限做面试操作）

### 钉钉消息通知

在 settings/local.py 或者 settings/production.py 中配置群机器人的 WebHook ， 用来发送消息通知。
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=xsxxx"

### 功能列表
* 管理职位
* 浏览职位
* 投递职位 [TODO]
* 维护候选人信息
* 导入候选人信息
* 面试官录入面试反馈
* 域账号集成 
* 钉钉消息通知集成 
* 候选人列表筛选和查询 [TODO]
* 如何增加自定义按钮 （数据导出） [TODO]
* 替换Django admin的主题风格 [TODO]