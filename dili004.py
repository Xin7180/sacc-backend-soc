class Videos:
    def __init__(self, title, author, views=0, likes=0):
        self.title = title
        self.author = author
        self.views = views
        self.likes = likes

    def information(self):
        print(f"视频标题: {self.title}")
        print(f"up主: {self.author}")
        print(f"播放量: {self.views}")
        print(f"点赞量: {self.likes}")
        
    def like(self):
        self.likes += 1
        print(f"点赞成功!\n当前点赞量为: {self.likes}")
        