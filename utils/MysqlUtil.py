import pymysql
from  utils.LoginUtil import my_log
class Mysql:
    #初始化连接数据库不用yaml进行配置了 直连了
    def __init__(self):
        self.log = my_log("数据库日志")
        self.conn = pymysql.connect(
            host = "211.103.136.242",
            user = "test",
            password = "test123456",
            database = "meiduo",
            charset = "utf8",
            port = 7090
            )


    #单个查询方法
    def execute(self,sql):
        #获取执行的光标,把查的结果以字典形式 否则是地址值
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            #执行sql
            self.cursor.execute(sql)
            #查询一条数据
            res = self.cursor.fetchone()
        except:
            self.log.error("单个数据查询失败")
        return res


    #多个查询
    def execute_all(self, sql):
        # 获取执行的光标,把查的结果以字典形式 否则是地址值
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 执行sql
            self.cursor.execute(sql)
            # 查询一条数据
            res = self.cursor.fetchall()
        except:
            self.log.error("多个数据查询失败")
        return res

    #关闭连接
    def __del__(self):
        #判断执行完代码后如果时连接状态 就关闭连接
        if self.cursor is not None:
            self.cursor.close()
        # 判断执行完代码后如果时连接状态 就关闭数据库
        if self.conn is not None:
            self.conn.close()


if __name__ == '__main__':
    mysql = Mysql()
    ex = mysql.execute("select username,password from tb_users")
    print(ex)