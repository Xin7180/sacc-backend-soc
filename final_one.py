#自己写的,有些不知道英文的变量我用拼音了,感觉都放一起好像太长了？但不在一个文件里还要导入
print("欢迎来到跳音流量观察台","\n当前身份: 后端组 SOC 实习生","\n负责人:yantz")
print("菜单选项: ",
        "\n1. 添加一条内容数据",
        "\n2. 查看所有内容数据",
        "\n3. 计算并展示流量等级",
        "\n4. 搜索指定标题或作者",
        "\n0. 退出系统")

def add_data():
    content=[]
    bianhao =1
    while True:
        title = input("请输入内容标题: ")
        author = input("请输入作者: ")
        pintai = input("请输入平台: ")
        bofangliang = int(input("请输入播放量: "))
        dianzanshu = int(input("请输入点赞数: "))
        pinglunshu = int(input("请输入评论数: "))
        zhuanfashu = int(input("请输入转发数: "))
        shoucangshu = int(input("请输入收藏数: "))
        biaoqian = input("请输入标签: ")
        item_one={"编号": bianhao, 
                    "标题": title, 
                    "作者": author, 
                    "平台": pintai, 
                    "播放量": bofangliang,
                    "点赞数": dianzanshu, 
                    "评论数": pinglunshu,
                    "转发数": zhuanfashu,
                    "收藏数": shoucangshu,
                    "标签": biaoqian}
        content.append(item_one)
        bianhao += 1
        if input("是否继续输入？(y/n): ") != 'y':
            break
        
def display_data(content):
    print("="*20,"已录入内容","="*20)
    if not content:
        print("当前还没有内容数据，运营同学还没开始发疯。")
    else:
        for item in content:
            print(f"\n编号: {item['编号']}",
              f"\n标题: {item['标题']}", 
              f"\n作者: {item['作者']}",
              f"\n平台: {item['平台']}",
              f"\n播放量: {item['播放量']}", 
              f"\n点赞数: {item['点赞数']}",
              f"\n评论数: {item['评论数']}",
              f"\n转发数: {item['转发数']}",
              f"\n收藏数: {item['收藏数']}",
              f"\n标签: {item['标签']}")
    print("="*45)

def calculate(content):
    TrafficScore=0
    if not content:
        print("当前还没有内容数据，无法计算流量等级。")
        return
    for item in content:
        TrafficScore= (item['播放量']*0.4 + item['点赞数']*2 + item['评论数']*3 +
                            item['转发数']*4 + item['收藏数']*5)
        if TrafficScore >= 200000:
            print(f"\n内容 {item['编号']}","的流量等级为: 爆款候选")
        elif 50000 <= TrafficScore < 200000:
            print(f"\n内容 {item['编号']}","的流量等级为: 大爆预备")
        elif 10000 <= TrafficScore < 50000:
            print(f"\n内容 {item['编号']}","的流量等级为: 小爆一下")
        elif 1000 <= TrafficScore < 10000:
            print(f"\n内容 {item['编号']}","的流量等级为: 有点水花")
        else:
            print(f"\n内容 {item['编号']}","的流量等级为: 无人问津")
        
def search(content):
    if not content:
        print("当前还没有内容数据，无法进行搜索。")
        return
    keyword = input("请输入要搜索的标题或作者关键字: ")
    while not keyword:
        print("关键字不能为空，请重新输入。")
        keyword = input("请输入要搜索的标题或作者关键字: ")
    found_items = [item for item in content if keyword in item['标题'] or keyword in item['作者']]
    if found_items:
        print(f"找到 {len(found_items)} 条匹配的内容:")
        for item in found_items:
            print(f" {item['编号']}",f" {item['标题']}",  f" {item['作者']}")
    else:
        print("未找到匹配的内容。")
        
while True:
    choice = input("请选择你要进行的操作： ")
    if choice == "1":
        add_data()
    elif choice == "2":
        display_data(content)
    elif choice == "3":
        calculate(content)
    elif choice == "4":
        search(content)
    elif choice == "0":
        print("退出系统，感谢使用！")
        break
    else:
        print("无效的选项，请重新输入。")
        
            