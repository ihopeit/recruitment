## 项目说明

用做创业公司职位发布，简历投递，招聘管理的开源项目，基于高效的Django & Python开发。
这是使用Python Django花了1天时间开发出来，可以用于企业的招聘面试管理的Django项目。
优秀的产品经理，能够做好迭代版本规划，

### 运行的前提条件

机器上有安装有Python, Django. 参考:
https://docs.djangoproject.com/

### 如何运行
python ./manage.py runserver 127.0.0.1:8000
然后可以通过访问如下两个页面 
* http://127.0.0.1:8000 首页
* http://127.0.0.1:8000/admin 管理后台

### 功能列表
* 管理职位
* 浏览职位
* 投递职位 [TODO]
* 维护候选人信息
* 导入候选人信息
* 面试官录入面试反馈
* 域账号集成 [TODO]
* 邮件通知集成 [TODO]
* 候选人列表筛选和查询 [TODO]
* 如何增加自定义按钮 （数据导出） [TODO]
* 替换Django admin的主题风格 [TODO]