class pack():
    dic = {}
    def __init__(self):
        self.dic={}
    def set(self, value, key):
        self.dic[key] =value
    def get(self):
        clear()
        return self.dic
    def clear(self):
        self.dic={}



img=[]
title=[]
goodsphoto=[]
content=[]
price=[]
loc=[]
flag=[]
usr=[]
def clear():
    global  img,content,loc,flag,usr,goodsphoto,price,title
    img = []
    content = []
    loc = []
    flag = []
    usr = []
    goodsphoto = []
    price=[]
    title=[]

pack=pack()

def query(model,n,m,fla):
    global pack ,img ,content,loc,usr,flag
    ob=model.objects.filter(flag=fla)[n:m]
    number=ob.count()
    for i in range(0, number):
        img.append(ob[i].img)
        content.append(ob[i].content)
        usr.append(ob[i].usr.usr)
    for i in range(number,m):
        img.append("#")
        content.append("无数据")
        usr.append("空")
    pack.clear()
    pack.set(img, "img")
    pack.set(content, "content")
    pack.set(usr, "usr")
    return pack


def querygoods(model,n,m,fla):
    global goodsphoto,img, content,price,title
    ob=model.objects.filter(flag=fla)[n:m]
    number=ob.count()
    for i in range(0,number):
        goodsphoto.append(ob[i].goodsphoto)
        img.append(ob[i].img)
        title.append(ob[i].title)
        content.append(ob[i].content)
        price.append(ob[i].price)
    for i in range(number,m):
        goodsphoto.append("#")
        img.append("#")
        title.append("无数据")
        content.append("无数据")
        price.append("无数据")
    pack.clear()
    pack.set(goodsphoto,"goodsphoto")
    pack.set(img,"img")
    pack.set(title,"title")
    pack.set(content,"content")
    pack.set(price,"price")
    return pack






