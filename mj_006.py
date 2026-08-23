def validateaccount(name,password):
    """检查账号名和密码是否合法"""
    if  name!="" and len(password) >= 6:
        return True
    return False

def encryptpassword(password):
    """对密码进行加密"""
    encryptedP="" 
    for char in password: #原密码每个字节
        encryptedP+=chr(ord(char)+1)#初始字节向后移动一位
    return encryptedP

def buildwelcomemessage(username):
    """构建欢迎信息"""
    print("Hello World!","账号",username,"诞生了")
    
active=validateaccount("lihua","123456")
encryptpassword("123456")
buildwelcomemessage("lihua")
