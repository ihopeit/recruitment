## MySQL 依赖包安装说明

### 安装 MySQLdb 模块

### pip 安装 mysql connect 和 客户端：
* pip install mysql-connector-python-rf mysqlclient

以上命令如果安装出错，  安装相关依赖：
debian 下面需要先安装 libmysqlclient: 
* apt-get install default-libmysqlclient-dev

centos/redhat 下面安装 mysql-devel : 
* yum install mysql-devel gcc gcc-devel python-devel