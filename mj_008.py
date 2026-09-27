#codex写的，但类和创造实例已经学过，但一些函数，装饰器是因为AI后去了解的，可能注释不是很全面
"""MJ-008 账号模板：把同一个账号的数据放在一起"""
import hashlib #初步去了解了一些，内置哈希算法库，我的理解是不可逆加密密码，生成摘要
from datetime import datetime #引进处理日期和时间的函数


class Account:
    """账号模板""" 

    def __init__(self, account_name, nickname, password, status="正常"):
        self.account_name = account_name                          # 账号名
        self.nickname = nickname                                  # 昵称
        self.password_digest = self._make_digest(password)        # 密码摘要（不存明文）
        self.status = status                                      # 账号状态
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 创建时间，datetimme.now,strftime()格式化时间,然后是年月日时分秒
        #hexdigest()是将摘要转换为十六进制字符串
    @staticmethod
    def _make_digest(password):
        """生成密码摘要"""
        return hashlib.sha256(password.encode("utf-8")).hexdigest()  #使用sha256算法生成密码摘要
    
    def check_password(self,password): 
        """校验密码：比较摘要，全程不碰明文"""
        return self._make_digest(password) == self.password_digest

    def show_info(self):
        """输出该账号的基本信息"""
        print("=" * 46)
        print("账号信息")
        print("=" * 46)
        print(f"账号名   : {self.account_name}")
        print(f"昵称     : {self.nickname}")
        print(f"密码摘要 : {self.password_digest}")
        print(f"账号状态 : {self.status}")
        print(f"创建时间 : {self.created_at}")
        print("=" * 46)


def main():
    # 小目标 2：创建一个账号实例
    account = Account(
        account_name="cxt0718",
        nickname="小陈同学",
        password="abc123456",
        status="正常",
    )

    # 输出基本信息
    account.show_info()

    # 小目标 3 演示：密码只用来校验，绝不打印明文
    if account.check_password("abc123456"):
        print("密码校验：正确（明文只出现这一次，用于验证，不保存不打印）")
    else:
        print("密码校验：错误")

    
if __name__ == "__main__":  #用来判断当前模块是否作为主程序运行，因为可能被其他脚本导入，如果值是模块名就不会执行下面  
    main()  