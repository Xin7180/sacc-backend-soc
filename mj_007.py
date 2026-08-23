import mj_006 #本地我能导入，不知道到github上时别人打开的时候行不行，但目前我只会这个
username=input("请输入账号名：")
password=input("请输入密码：")
users={}
active=mj_006.validateaccount(username,password)
if not active:
    print("账号名或密码不合法")
else:
    ep=mj_006.encryptpassword(password)
    if ep==password:
        print("加密失败")
    else:
        users[username]=ep
        print("用户信息已保存")
        mj_006.buildwelcomemessage(username)
        
   
    


