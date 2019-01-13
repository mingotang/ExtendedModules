
# see: https://www.jianshu.com/p/0e7be22577ca


from PyQt5.QtWidgets import QDialog, QSystemTrayIcon, QMenu ,QAction,QApplication,QListWidgetItem,QListWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
import sys
import conf#<====导入conf

class main(QDialog):
    def __init__(self):
        super().__init__()
        self.loadMenu()
        self.initUI()

    def loadMenu(self): 
        conf.menuItems.append({"text": "启动", "icon": "./icons/set.png", "event": self.show, "hot": "D"})
        conf.menuItems.append({"text": "退出", "icon": "./icons/close.png", "event": self.close, "hot": "Q"})
        self.trayIconMenu = QMenu(self)# 创建菜单
        #遍历绑定 显示的文字、图标、热键和点击事件
        #热键可能是无效的 我这里只是为了显示效果而已
        for i in conf.menuItems: 
            tmp = QAction(QIcon(i["icon"]), i["text"],self, triggered=i["event"])
            tmp.setShortcut(self.tr(i["hot"]))
            self.trayIconMenu.addAction(tmp) 
    def loadList(self):
        lv = QListWidget()
        for i in range(len(conf.menuItems)):
            itm = conf.menuItems[i]
            if not 'icon' in itm.keys():
                itm["icon"] = None
            if not 'event' in itm.keys():
                itm["event"] = self.show
            if not 'hot' in itm.keys():
                itm["hot"] = 'None' 
            qlv = QListWidgetItem(QIcon(itm["icon"]), self.tr(itm["text"]+"  ("+itm["hot"]+")"))
            qlv.event = itm["event"] 
            # qlv.clicked.connect(self.close)
            lv.insertItem(i + 1, qlv)
        lv.itemDoubleClicked.connect(self.dbclickItem)
        self.layout.addWidget(lv)

    def dbclickItem(self, item):
        item.event()

    def initUI(self):
        self.trayIcon = QSystemTrayIcon(self)  # <===创建通知栏托盘图标
        self.trayIcon.setIcon(QIcon("./icons/menu2.png"))#<===设置托盘图标
        self.trayIcon.setContextMenu(self.trayIconMenu)#<===创建右键连接菜单
        self.trayIcon.show()#<====显示托盘
        self.layout = QVBoxLayout()
        self.loadList()
        self.setLayout(self.layout)
        self.setWindowIcon(QIcon("./icons/menu2.png"))  #<===设置窗体图标
        self.setGeometry(300, 300, 180, 300)  # <===设置窗体打开位置与宽高
        self.setWindowTitle('窗体标题')
        # self.show()#<====显示窗体
        # self.hide()#<====隐藏窗体
        # 默认不显示窗体        

    # 重写窗体关闭事件,让其点击关闭时隐藏
    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())