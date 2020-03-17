# -*- coding: utf-8 -*-
from  email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
import smtplib
class Email:

    #初始化方法 smtp地址 用户名 密码  接收地址   标题 邮件内容 邮件附件
    def __init__(self,title,content=None,file=None):
        self.smtp_add = "smtp.163.com"
        self.username = "dyqwaszx@163.com"
        self.password = "dy1994522"
        self.recv = "dyqwaszx@163.com"
        self.title =title
        self.content =content
        self.file =file

    #发送邮件方法
    def send_mail(self):
        # 处理邮件信息的类
        msg = MIMEMultipart()
        # 插入邮件正文(邮件内容) 需要注意的是发送字符串内容要先转换成文本 设置指定的字符集
        msg.attach(MIMEText(self.content, _charset="utf-8"))
        # 设置邮件头信息
        msg["Subject"] = self.title
        # 设置用户名
        msg["From"] = self.username
        # 设置邮件内容
        msg["To"] = self.recv
        # 判断是否有附件
        if self.file:
            # 读取附件内容
            att = MIMEText(open(self.file).read())
            # 设置附件内容类型
            att["Content-Type"] = 'application/octet-stream'
            # att["Content-Type"] = 'application/octet-stream'
            # 设置附件头
            att["Content-Disposition"] = 'attachment;filename="{}"'.format(self.file)
            # 把内容加到邮件主题中
            msg.attach(att)

        # 登录邮件服务器
        self.smtp = smtplib.SMTP(self.smtp_add, port=25)
        self.smtp.login(self.username, self.password)
        # 发送邮件
        self.smtp.sendmail(self.username, self.recv, msg.as_string())

if __name__ == "__main__":
        email = Email( "我的邮件发送")
        email.send_mail()