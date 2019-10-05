class XSXT:

    #主页面开始
    def __init__(self):
        self.all = []
        while True:
            self.Decktop()#显示菜单
            number = input("请输入选项：")
            if number == '1':#输入
                self.all = self.addHj()

            elif number == '2':#修改
                try:
                    student = self.modX(self.all)
                except Exception as e:
                    print(e)#学生信息不符合
                else:
                    self.all.remove(self.delX(self.all,delname=student.get('name')))#删除旧信息
                    self.all.append(student)#添加新信息

            elif number == '3':#删除
                try:
                    self.all.remove(self.delX(self.all))
                except Exception as e:
                    print(e)

            elif number == '4':#查询户籍
                self.queryH(self.all)

            elif number == '5':#查询学籍
                self.queryX(self.all)

            elif number == '6':#查询
                self.query(self.all)

            elif number == '7':#打印
                self.save(self.all)

            elif number == '0':
                break
            else:
                break
            input("按下回车显示菜单")

    #界面
    def Decktop(self):
        biao = """
                *-----------------------------------*
                *----------学生信息管理系统----------*
                *---------1.添加学生基本信息---------*
                *---------2.修改学生所有信息---------*
                *---------3.删除学生所有信息---------*
                *---------4.查询学生户籍信息---------*
                *---------5.查询学生学籍信息---------*
                *---------6.查询学生基本信息---------*
                *---------7.打印学生基本信息---------*
                *---------0.退出学生信息系统---------*
                *-----------------------------------*
                """
        print(biao)

    #添加学生基本信息
    def addHj(self):
        hj = []
        while True:
            name = input("请输入名字：")
            if not name:
                break
            age = input("请输入年龄：")
            idCard = input("请输入身份证号：")
            date = input("请输入出生年月：")
            address = input("请输入住址：")
            sID = input('请输入学号：')
            coll = input("请输入所属学院：")
            major = input("请输入专业：")
            classnamme = input("请输入班级：")
            info ={'name':name,'age':age,'idCard':idCard,'data':date,'address':address,'sID':sID,'coll':coll,'major':major,'classname':classnamme}
            hj.append(info)
        print("学生户籍信息添加成功！")
        return hj

    #修改学生信息
    def modX(self,mod):
        modName = input('请输入需要修改的学生姓名：')
        for info in mod:
            if modName == info.get('name'):
                modAge = input('请输入年龄：')
                modIDcard = input('请输入身份证号：')
                modDate = input('请输入出生年月：')
                modAddress = input('请输入住址：')
                modSid = input('请输入学号：')
                modColl = input('请输入所属学院：')
                modMajor = input('请输入专业：')
                modClassname = input('请输入班级：')
                info = {'name':modName,'age':modAge,'idCard':modIDcard,'data':modDate,'address':modAddress,'sID':modSid,'coll':modColl,'major':modMajor,'classname':modClassname}
                return info
        raise IndexError("无%s学生信息" % modName)

    #删除学生信息
    def delX(self,all,delname =''):
        if not delname:
            delname = input("请输入需要删除学生的姓名：")
        for info in all:
            if delname == info.get('name'):
                return info
        raise IndexError("无%s学生的信息" % delname)

    #查询学生户籍信息
    def queryH(self,HJ,Hjname =''):
        if not Hjname:
            Hjname = input("请输入查询学生户籍姓名")
        for info in HJ:
            if Hjname == info.get('name'):
                print("姓名".center(8), "身份证号码".center(12), "出生年月".center(8), "住址".center(2))
                print(info.get('name').center(8),info.get('idCard').center(2),info.get('data').center(8),info.get('address').center(6))

    #查询学生学籍信息
    def queryX(self,XJ,Xjname = ''):
        if not Xjname:
            Xjname = input("请输入查询学生学号：")
        for info in XJ:
            if Xjname == info.get('sID'):
                print("学号".center(8), "身份证号码".center(18), "所属学院".center(6), "专业".center(6),"班级".center(6))
                print(info.get('sID').center(8), info.get('idCard').center(2), info.get('coll').center(8),info.get('major').center(4),info.get('classname').center(4))

    #查询学生基本信息
    def query(self,xjinfo):
        if not xjinfo:
            print("无信息")
            return
        print("学号".center(12),"姓名".center(2),"年龄".center(2),'所属学院'.center(5),'班级'.center(4))
        for info in xjinfo:
            print(info.get('sID').center(2),info.get('name').center(4),info.get('age').center(4),info.get('coll').center(5),info.get('classname').center(4))

    #打印学生信息
    def save(self,xjinfo):
        import xlwt
        book = xlwt.Workbook()
        mysheel = book.add_sheet('学生信息表')
        lists = ['sID','name','age','coll','classname']
        for i in range(0,len(lists)):
            mysheel.write(0,i,lists[i])
        for i in range(0,len(xjinfo)):
            try:
                mysheel.write(i+1,0,xjinfo[i]['sID'])
                mysheel.write(i+1,1,xjinfo[i]['name'])
                mysheel.write(i+1,2,xjinfo[i]['age'])
                mysheel.write(i+1,3,xjinfo[i]['coll'])
                mysheel.write(i+1,4,xjinfo[i]['classname'])
            except:
                print('kong')
        book.save('学生基本信息表.xls')






XSXT()