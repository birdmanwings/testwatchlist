# testwatchlist
一个基于flask的watchlist   

## 安装
```
$ git clone https://github.com/birdmanwings/testwatchlist.git
$ cd testwatchlist
$ pipenv install --dev
$ pipenv shell
$ flask initdb --drop (初始化数据库)
$ flask forge (生成虚拟数据)  
$ flask admin (生成管理员账户)
* Username:你的用户名
* Password:设置的密码
* Repeat for confirmation:重复的密码
$ flask run
* Running on http://127.0.0.1:5000/
```
## 效果
![image](https://github.com/birdmanwings/testwatchlist/raw/master/images/test.png)
