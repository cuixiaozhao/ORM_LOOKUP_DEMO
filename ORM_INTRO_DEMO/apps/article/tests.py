import sys
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

mail_server = "smtp.163.com"  # 此处为163邮箱服务器地址；
send_username = 'tqtl911@163.com'  # 163邮箱用户名；
send_password = '19930911cXS'  # 163邮箱密码：需要使用163授权码；

recv_username = '290799238@qq.com'  # 收件人，多个收件人用逗号分隔开；


def send_trouble_mail(happen_time, order_number, ipv4, touble_desc):
    """
    发送告警邮件;
    :param happen_time:
    :param order_number:
    :param ipv4:
    :param touble_desc:
    :return:
    """
    mail_content = """
    尊敬的用户您好：
        xxx实例，于%s发生告警，故障单号为:%s,实例IP地址为:%s,故障描述如下:%s
    """ % (happen_time, order_number, ipv4, touble_desc)

    # 传入的邮件内容：
    mail = MIMEText(mail_content)

    mail['Subject'] = '此处填写邮件主题，比如：监控宝告警邮件'  # 邮件主题；

    mail['From'] = send_username  # 邮件发送人；

    mail['To'] = recv_username  # 收件人；

    smtp = smtplib.SMTP(mail_server, port=25)  # 连接邮箱服务器，smtp的端口号是25；
    smtp.login(send_username, send_password)  # 登录邮箱；
    smtp.sendmail(send_username, recv_username, mail.as_string())  # 参数分别是发件人，收件人，第三个参数是发送邮件的内容变成字符串；
    smtp.quit()  # 发送完毕后，退出smtp；
    print('你好，邮件已发送成功！')


if __name__ == '__main__':
    send_trouble_mail(datetime.now(), '20181123321321', '123.456.78.90', '这是一封来自监控宝的告警邮件！')
