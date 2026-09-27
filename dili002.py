day=0
views_total=0
while day<7:
    day+=1
    views=int(input("请输入今天的播放量: "))
    views_total+=views
    if day==7:
        print(f"累计播放量: {views_total}")
        
