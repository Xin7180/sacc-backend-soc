name=input("Please enter your name: ")
while name==" ":
    print("账号名不能为空")
    name=input("Please enter your name again: ")
password=input("Please enter your password: ")
while len(password)<6:
    print("密码长度不足")
    password=input("Please enter your password again: ")
status=input("Please enter your status(safe/blocked): ")
while status=="blocked":
    print("状态输入错误")
    status=input("Please enter your status(safe/blocked): ")
day=input("Please enter your login days: ")
while not day.isdigit():
    print("登录天数格式错误")
    day=input("Please enter your login days again: ")
print("账号校验通过")