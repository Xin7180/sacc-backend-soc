names=["lihua01","lihua02","lihua03","lihua04","lihua05"," ","lihua06"]
number=0
for name in names:
    if name==" ":
        continue
    elif name=="risk_user":
        break
    else:
        print("正在创建账号:",name)
        number+=1
print("总共创建了",number,"个账号")
