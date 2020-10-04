## 这是集成已有系统数据库的例子

### 场景
* 提供功能，对已有数据库指定表进行浏览操作
* 禁用数据的修改，新增，删除操作

### 使用方法

#### 注册应用 settings/local.py

INSTALLED_APPS = [
    'running',
 ] + INSTALLED_APPS

#### 配置数据库和数据库路由 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'running': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'running',                    
            'USER': 'recruitment',                      
            'PASSWORD': 'recruitment',                  
            'HOST': '127.0.0.1',                      
            'PORT': '3306',
    },
}

DATABASE_ROUTERS = ['settings.router.DatabaseRouter']

#### 为已有系统数据库生成 model
python manage.py inspectdb --database=running --settings=settings.local  area city  country  province >> running/models.py
