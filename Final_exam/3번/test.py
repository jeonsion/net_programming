

#원격 시스템에서 연속적으로 명령어 실행하기
#ssh 서버에 접속하여 학번을 이름으로 하는 폴더를 1개 생성한다.
#해당폴더 내에서 cat /proc/meminfo > mem.txt 파일을 생성한다.
#본인학번 폴더 전체를 '학번.zip'으로 압축한다
#해당 파일을 sftp를 이용하여 (프로그램이 실해되고 있는) 현재 폴더로 가져온다.
#가져온 파일을 이메일의 첨부파일로 daeheekim@sch.ac.kr로 전송한다. 단, 이메일의 제목과 첨부 파일의 이름은 "학번.zip" 이어야한다

import getpass
import paramiko
import time

import smtplib
from email.message import EmailMessage
import filetype

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'a24349663@gmail.com'
recipient = '20191545@sch.ac.kr'
password = 'rrnawehylcrwrtau'


buffsize = 65536

transport = paramiko.Transport(('114.71.220.5', 22))

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input("Username: ")
pwd = getpass.getpass("Password: ")
transport.connect(username=user, password=pwd)
cli.connect('114.71.220.5', username=user, password=pwd)

ssh.connect('114.71.220.5', 22, username = user, password = pwd)


channel = cli.invoke_shell()
channel.send('mkdir 20191545\n')
time.sleep(0.5)

channel.send('cd 20191545\n')
time.sleep(0.5)

channel.send('cat /proc/meminfo > mem.txt\n')
time.sleep(0.5)

channel.send('cd ..\n')
time.sleep(0.5)

filename = '20191545.zip'
dirnam = '20191545'
CMD = 'zip -r ' + filename + ' ' + dirnam

stdin, stdout, stderr = ssh.exec_command(CMD)
sftp = ssh.open_sftp()
sftp.get(filename, filename)
ssh.close()

friends = ["daeheekim@sch.ac.kr", "ninanooo@gmail.com"]

msg = EmailMessage()
msg['Subject'] = '네트워크 프로그래밍 기말고사'
msg['From'] = sender
msg['To'] = ', '.join(friends)
msg.set_content('네트워크 프로그래밍 기말고사 답안 제출합니다.')

with open('20191545.zip', 'rb') as f:
    file_data = f.read()
msg.add_attachment(file_data, maintype='application', subtype=filetype.guess_mime(file_data), filename='20191545.zip')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
    