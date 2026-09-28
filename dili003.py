class Dili_user:
    def __init__(self, username, usertype):
        self.username = username
        self.usertype = usertype
        
    def watch(self):
        print("观看普通视频")
        
class Dili_vip(Dili_user):
    def __init__(self, username, usertype="Dili_vip"):
        super().__init__(username, usertype)   
        
    def watch(self):
        print("观看VIP视频")
        
def userwatch(user):
    user.watch()
    
user=[Dili_user("Lihua","Dili_user"), Dili_vip("Mike")]
for u in user:
    userwatch(u)