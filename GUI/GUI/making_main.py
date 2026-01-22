from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import platform
import webbrowser

class GUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)
        # making the screen and infos :
        self.setGeometry(300,100,800,600)
        self.setFixedSize(900,650)
        self.setWindowTitle("WINbloke")
        self.setWindowIcon(QIcon('icon.png'))
        # chaging the top bar of the proggram
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)
        
        # i will use horizontal layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0) # this is for fitting the page => from the resize when the person is resizing


        # making the menu on the left of the proggram
        self.menu = QListWidget(self)
        self.menu.setIconSize(QSize(30,30))
        self.menu.setFont(QFont('Times', 10))
        self.menu.move(0,266)
        self.layout.addWidget(self.menu)

        # giving it to the function
        self.setUI()
        
    def setUI(self):
        # making the top left
        # putting the picutre 
        self.pic_label = QLabel(self)
        self.user_image = QPixmap("icon.png")
        self.pic_label.setPixmap(self.user_image)
        self.pic_label.move(30,0)
        self.pic_label.resize(200,200)
        self.pic_label.setStyleSheet("border-radius : 25px;")
        # winbloke name and logo
        self.user_name = platform.uname().node
        self.pic_text = QLabel(self.user_name,self)
        self.pic_text.move(10,185)
        self.pic_text.resize(230,60)
        self.pic_text.setStyleSheet("font-family: Courier; background: gold ; border-radius : 10px; font-size : 18px; border: 2px solid cyan; font : bold;")
        self.pic_text.setAlignment(Qt.AlignCenter)
        self.pic_text.setWordWrap(True)
 

        # making the scors unvisible
        self.menu.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.menu.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # continue

        self.menu.setFrameShape(QListWidget.NoFrame)
        self.menu.setSpacing(0)

        # making the proggram
        
        # the color of the theme with a bool
        self.dark_theme = False
        
        # proggram
        # page color 
        self.setStyleSheet("background-color : white;")
        
        # writing the stylesheet
        self.menu.setStyleSheet("QListWidget"
            "{"
            "min-width: 250px;" 
            "max-width: 250px;" 
            "min-height: 450px;" 
            "max-height: 450px;" 
            "color: black;" 
            "background: white;"
            "}"
            "QListView::item"
            "{"
            "color : black;"
            "background: white;"
            "border-bottom: 1px dashed grey;"
            "}"
            "QListView::item:selected"
            "{"
            "color : black;"
            "background: rgb(200,200,200);"
            "border-left: 3px solid #595959;"
            "padding-left: 10px;"
            "}"
            )
        
        # QListWidgetItems
        # home
        self.home = QListWidgetItem(QIcon('home_white.png'), str("Home"), self.menu)
        self.home.setSizeHint(QSize(250,55))
        self.home.setTextAlignment(Qt.AlignCenter)
        # direct-message
        self.direct_message = QListWidgetItem(QIcon('direct-message_white.png'), str("Direct Message"), self.menu)
        self.direct_message.setSizeHint(QSize(250,55))
        self.direct_message.setTextAlignment(Qt.AlignCenter)
        #social medias
        self.social_medias = QListWidgetItem(QIcon('social-medias_white.png'), str("Social Medias"), self.menu)
        self.social_medias.setSizeHint(QSize(250,55))
        self.social_medias.setTextAlignment(Qt.AlignCenter)
        #speech
        self.speech = QListWidgetItem(QIcon('speech_white.png'), str("Speech"), self.menu)
        self.speech.setSizeHint(QSize(250,55))
        self.speech.setTextAlignment(Qt.AlignCenter)
        #settings
        self.settings = QListWidgetItem(QIcon('settings_white.png'), str("Settings"), self.menu)
        self.settings.setSizeHint(QSize(250,55))
        self.settings.setTextAlignment(Qt.AlignCenter)
        # prosessor settings
        self.home = QListWidgetItem(QIcon('processor_white.png'), str("Processor"), self.menu)
        self.home.setSizeHint(QSize(250,55))
        self.home.setTextAlignment(Qt.AlignCenter)
        # help
        self.help = QListWidgetItem(QIcon('help_white.png'), str("Help"), self.menu)
        self.help.setSizeHint(QSize(250,55))
        self.help.setTextAlignment(Qt.AlignCenter)

        # signals
        self.menu.itemClicked.connect(self.clicking_func)
        self.menu.itemDoubleClicked.connect(self.clicking_func)
        
        # five buttons on the top right and the background
        # background
        self.background_frame = QLabel(self)
        self.background_frame.setStyleSheet("border-left : 5px solid grey ; background-color : white")
        self.background_frame.resize(650,650)
        self.background_frame.move(250,0)
        self.bg_photo = QPixmap("microphone-background_white.png")
        self.background_frame.setPixmap(self.bg_photo)
        # making the basic of the right part
        # adding the four buttons to it
        # info - button
        self.info_button = QPushButton(self)
        self.info_button.resize(40, 40)
        self.info_button.move(850,10)
        self.info_button.setStyleSheet("background-image: url('info_white.png'); background-repeat: no-repeat; background-position: center;")
        self.info_button_pixmap = QPixmap('info_white.png')
        self.info_button.setMask(self.info_button_pixmap.mask())
        self.info_button.clicked.connect(self.info_func)
        # mail - button 
        self.mail_button = QPushButton(self)
        self.mail_button.resize(40, 40)
        self.mail_button.move(850, 60)
        self.mail_button.setStyleSheet("background-image: url('mail_white.png'); background-repeat: no-repeat; background-position: center;")
        self.mail_button_pixmap = QPixmap('mail_white.png')
        self.mail_button.setMask(self.mail_button_pixmap.mask())
        self.mail_button.clicked.connect(self.mail_func)
        # donate - button
        self.donate_button = QPushButton(self)
        self.donate_button.resize(40, 40)
        self.donate_button.move(850, 110)
        self.donate_button.setStyleSheet("background-image: url('donate_white.png'); background-repeat: no-repeat; background-position: center;")
        self.donate_button_pixmap = QPixmap('donate_white.png')
        self.donate_button.setMask(self.donate_button_pixmap.mask())
        self.donate_button.clicked.connect(self.donate_func)
        # github - button
        self.github_button = QPushButton(self)
        self.github_button.resize(40, 40)
        self.github_button.move(850, 160)
        self.github_button.setStyleSheet("background-image: url('github_white.png'); background-repeat: no-repeat; background-position: center;")
        self.github_button_pixmap = QPixmap('github_white.png')
        self.github_button.setMask(self.github_button_pixmap.mask())
        self.github_button.clicked.connect(self.github_func)
        # dark and light theme
        self.dark_light_theme_button = QPushButton(self)
        self.dark_light_theme_button.resize(40, 40)
        self.dark_light_theme_button.move(850, 210)
        self.dark_light_theme_button.setStyleSheet("background-image: url('theme_white.png'); background-repeat: no-repeat; background-position: center;")
        self.dark_light_theme_button_pixmap = QPixmap('theme_white.png')
        self.dark_light_theme_button.setMask(self.dark_light_theme_button_pixmap.mask())
        self.dark_light_theme_button.clicked.connect(self.dark_light_theme_func)
        
        self.test_label = QLabel("this is home page",self)
        self.test_label.setStyleSheet("color : red;")
        
        # first frame
        self.home_func()
        self.last_selected_button = "home"
    
    # five buttons that we have and when they are clicked
    def info_func(self):
        webbrowser.open('https://iliya-aghazadeh.github.io/Small-Site-About-Me/')
    
    def mail_func(self):
        webbrowser.open('https://iliya-aghazadeh.github.io/Small-Site-About-Me/')
        
    def donate_func(self):
        webbrowser.open('https://iliya-aghazadeh.github.io/Small-Site-About-Me/')
        
    def github_func(self):
        webbrowser.open('https://iliya-aghazadeh.github.io/Small-Site-About-Me/')
    
    def dark_light_theme_func(self):
        self.dark_theme = False if self.dark_theme == True else True 
        if self.dark_theme : 
            self.dark_style_sheets()
        else : 
            self.white_style_sheets()
    
    def dark_style_sheets(self):
        # page color 
        self.setStyleSheet("")
        self.setStyleSheet("background-color : black;")
        
        # writing the stylesheet
        self.menu.setStyleSheet("")
        self.menu.setStyleSheet("QListWidget"
            "{"
            "min-width: 250px;" 
            "max-width: 250px;" 
            "min-height: 450px;" 
            "max-height: 450px;" 
            "color: white;" 
            "background: black;"
            "}"
            "QListView::item"
            "{"
            "color : white;"
            "background: black;"
            "border-bottom: 1px dashed grey;"
            "}"
            "QListView::item:selected"
            "{"
            "color : white;"
            "background: rgb(100,100,100);"
            "border-left: 3px solid #d1d1d1;"
            "padding-left: 10px;"
            "}"
            )
        self.menu.clear()
        # QListWidgetItems
        # home
        self.home = QListWidgetItem(QIcon('home_black.png'), str("Home"), self.menu)
        self.home.setSizeHint(QSize(250,55))
        self.home.setTextAlignment(Qt.AlignCenter)
        # direct-message
        self.direct_message = QListWidgetItem(QIcon('direct-message_black.png'), str("Direct Message"), self.menu)
        self.direct_message.setSizeHint(QSize(250,55))
        self.direct_message.setTextAlignment(Qt.AlignCenter)
        #social medias
        self.social_medias = QListWidgetItem(QIcon('social_medias_black.png'), str("Social Medias"), self.menu)
        self.social_medias.setSizeHint(QSize(250,55))
        self.social_medias.setTextAlignment(Qt.AlignCenter)
        #speech
        self.speech = QListWidgetItem(QIcon('speech_black.png'), str("Speech"), self.menu)
        self.speech.setSizeHint(QSize(250,55))
        self.speech.setTextAlignment(Qt.AlignCenter)
        #settings
        self.settings = QListWidgetItem(QIcon('settings_black.png'), str("Settings"), self.menu)
        self.settings.setSizeHint(QSize(250,55))
        self.settings.setTextAlignment(Qt.AlignCenter)
        # prosessor settings
        self.home = QListWidgetItem(QIcon('processor_black.png'), str("Processor"), self.menu)
        self.home.setSizeHint(QSize(250,55))
        self.home.setTextAlignment(Qt.AlignCenter)
        # help
        self.help = QListWidgetItem(QIcon('help_black.png'), str("Help"), self.menu)
        self.help.setSizeHint(QSize(250,55))
        self.help.setTextAlignment(Qt.AlignCenter)

        # signals
        self.menu.itemClicked.connect(self.clicking_func)
        self.menu.itemDoubleClicked.connect(self.clicking_func)
        
        # five buttons on the top right and the background
        # background
        self.background_frame.clear()
        self.background_frame.setStyleSheet("border-left : 5px solid grey ; background-color : black")
        self.background_frame.resize(650,650)
        self.background_frame.move(250,0)
        self.bg_photo = QPixmap("microphone-background_black.png")
        self.background_frame.setPixmap(self.bg_photo)
        # making the basic of the right part
        # adding the four buttons to it
        # info - button
        self.info_button = QPushButton(self)
        self.info_button.resize(40, 40)
        self.info_button.move(850,10)
        self.info_button.setStyleSheet("background-image: url('info_white.png'); background-repeat: no-repeat; background-position: center;")
        self.info_button_pixmap = QPixmap('info_white.png')
        self.info_button.setMask(self.info_button_pixmap.mask())
        self.info_button.clicked.connect(self.info_func)
        # mail - button 
        self.mail_button = QPushButton(self)
        self.mail_button.resize(40, 40)
        self.mail_button.move(850, 60)
        self.mail_button.setStyleSheet("background-image: url('mail_white.png'); background-repeat: no-repeat; background-position: center;")
        self.mail_button_pixmap = QPixmap('mail_white.png')
        self.mail_button.setMask(self.mail_button_pixmap.mask())
        self.mail_button.clicked.connect(self.mail_func)
        # donate - button
        self.donate_button = QPushButton(self)
        self.donate_button.resize(40, 40)
        self.donate_button.move(850, 110)
        self.donate_button.setStyleSheet("background-image: url('donate_white.png'); background-repeat: no-repeat; background-position: center;")
        self.donate_button_pixmap = QPixmap('donate_white.png')
        self.donate_button.setMask(self.donate_button_pixmap.mask())
        self.donate_button.clicked.connect(self.donate_func)
        # github - button
        self.github_button = QPushButton(self)
        self.github_button.resize(40, 40)
        self.github_button.move(850, 160)
        self.github_button.setStyleSheet("background-image: url('github_white.png'); background-repeat: no-repeat; background-position: center;")
        self.github_button_pixmap = QPixmap('github_white.png')
        self.github_button.setMask(self.github_button_pixmap.mask())
        self.github_button.clicked.connect(self.github_func)
        # dark and light theme
        self.dark_light_theme_button = QPushButton(self)
        self.dark_light_theme_button.resize(40, 40)
        self.dark_light_theme_button.move(850, 210)
        self.dark_light_theme_button.setStyleSheet("background-image: url('theme_white.png'); background-repeat: no-repeat; background-position: center;")
        self.dark_light_theme_button_pixmap = QPixmap('theme_white.png')
        self.dark_light_theme_button.setMask(self.dark_light_theme_button_pixmap.mask())
        self.dark_light_theme_button.clicked.connect(self.dark_light_theme_func)
        
        # writing the things inside each of the buttons
        
        self.test_label.setStyleSheet("")
        self.test_label.setStyleSheet("color : white; background-color : black")
        
    
    def white_style_sheets(self):
        # page color 
        self.setStyleSheet("")
        self.setStyleSheet("background-color : white;")
        
        # writing the stylesheet
        self.menu.setStyleSheet("")
        self.menu.setStyleSheet("QListWidget"
            "{"
            "min-width: 250px;" 
            "max-width: 250px;" 
            "min-height: 450px;" 
            "max-height: 450px;" 
            "color: black;" 
            "background: white;"
            "}"
            "QListView::item"
            "{"
            "color : black;"
            "background: white;"
            "border-bottom: 1px dashed grey;"
            "}"
            "QListView::item:selected"
            "{"
            "color : black;"
            "background: rgb(200,200,200);"
            "border-left: 3px solid #595959;"
            "padding-left: 10px;"
            "}"
            )
        self.menu.clear()
        # QListWidgetItems
        # home
        self.home = QListWidgetItem(QIcon('home_white.png'), str("Home"), self.menu)
        self.home.setSizeHint(QSize(250,55))
        self.home.setTextAlignment(Qt.AlignCenter)
        # direct-message
        self.direct_message = QListWidgetItem(QIcon('direct-message_white.png'), str("Direct Message"), self.menu)
        self.direct_message.setSizeHint(QSize(250,55))
        self.direct_message.setTextAlignment(Qt.AlignCenter)
        #social medias
        self.social_medias = QListWidgetItem(QIcon('social-medias_white.png'), str("Social Medias"), self.menu)
        self.social_medias.setSizeHint(QSize(250,55))
        self.social_medias.setTextAlignment(Qt.AlignCenter)
        #speech
        self.speech = QListWidgetItem(QIcon('speech_white.png'), str("Speech"), self.menu)
        self.speech.setSizeHint(QSize(250,55))
        self.speech.setTextAlignment(Qt.AlignCenter)
        #settings
        self.settings = QListWidgetItem(QIcon('settings_white.png'), str("Settings"), self.menu)
        self.settings.setSizeHint(QSize(250,55))
        self.settings.setTextAlignment(Qt.AlignCenter)
        # prosessor settings
        self.home = QListWidgetItem(QIcon('processor_white.png'), str("Processor"), self.menu)
        self.home.setSizeHint(QSize(250,55))
        self.home.setTextAlignment(Qt.AlignCenter)
        # help
        self.help = QListWidgetItem(QIcon('help_white.png'), str("Help"), self.menu)
        self.help.setSizeHint(QSize(250,55))
        self.help.setTextAlignment(Qt.AlignCenter)

        # signals
        self.menu.itemClicked.connect(self.clicking_func)
        self.menu.itemDoubleClicked.connect(self.clicking_func)
        
        # five buttons on the top right and the background
        # background
        self.background_frame = QLabel(self)
        self.background_frame.setStyleSheet("border-left : 5px solid grey ; background-color : white")
        self.background_frame.resize(650,650)
        self.background_frame.move(250,0)
        self.bg_photo = QPixmap("microphone-background_white.png")
        self.background_frame.setPixmap(self.bg_photo)
        # making the basic of the right part
        # adding the four buttons to it
        # info - button
        self.info_button = QPushButton(self)
        self.info_button.resize(40, 40)
        self.info_button.move(850,10)
        self.info_button.setStyleSheet("background-image: url('info_white.png'); background-repeat: no-repeat; background-position: center;")
        self.info_button_pixmap = QPixmap('info_white.png')
        self.info_button.setMask(self.info_button_pixmap.mask())
        self.info_button.clicked.connect(self.info_func)
        # mail - button 
        self.mail_button = QPushButton(self)
        self.mail_button.resize(40, 40)
        self.mail_button.move(850, 60)
        self.mail_button.setStyleSheet("background-image: url('mail_white.png'); background-repeat: no-repeat; background-position: center;")
        self.mail_button_pixmap = QPixmap('mail_white.png')
        self.mail_button.setMask(self.mail_button_pixmap.mask())
        self.mail_button.clicked.connect(self.mail_func)
        # donate - button
        self.donate_button = QPushButton(self)
        self.donate_button.resize(40, 40)
        self.donate_button.move(850, 110)
        self.donate_button.setStyleSheet("background-image: url('donate_white.png'); background-repeat: no-repeat; background-position: center;")
        self.donate_button_pixmap = QPixmap('donate_white.png')
        self.donate_button.setMask(self.donate_button_pixmap.mask())
        self.donate_button.clicked.connect(self.donate_func)
        # github - button
        self.github_button = QPushButton(self)
        self.github_button.resize(40, 40)
        self.github_button.move(850, 160)
        self.github_button.setStyleSheet("background-image: url('github_white.png'); background-repeat: no-repeat; background-position: center;")
        self.github_button_pixmap = QPixmap('github_white.png')
        self.github_button.setMask(self.github_button_pixmap.mask())
        self.github_button.clicked.connect(self.github_func)
        # dark and light theme
        self.dark_light_theme_button = QPushButton(self)
        self.dark_light_theme_button.resize(40, 40)
        self.dark_light_theme_button.move(850, 210)
        self.dark_light_theme_button.setStyleSheet("background-image: url('theme_white.png'); background-repeat: no-repeat; background-position: center;")
        self.dark_light_theme_button_pixmap = QPixmap('theme_white.png')
        self.dark_light_theme_button.setMask(self.dark_light_theme_button_pixmap.mask())
        self.dark_light_theme_button.clicked.connect(self.dark_light_theme_func)
        
        # writing the things inside each of the buttons
        
        self.test_label.setStyleSheet("")
        self.test_label.setStyleSheet("color : black; background-color : white")
        
        
    # qlistwidget each one click function
    def clicking_func(self):
        self.last_item_cleaner()
        # wrting the condistions for the button which is clicked
        self.what = self.menu.currentItem().text()
        if self.what == "Processor":
            self.processor_func()
        if self.what == "Home" : 
            self.home_func()
        elif self.what == "Direct Message":
            self.direct_message_func()
        elif self.what == "Social Medias":
            self.social_medias_func()
        elif self.what == "Speech" : 
            self.speech_func()
        elif self.what == "Settings" :
            self.settings_func()
        elif self.what == "Help" : 
            self.help_func()
            
    # cleaning the last item which was selected
    def last_item_cleaner(self):
        if self.last_selected_button == "home" : 
            self.test_label.hide()
        if self.last_selected_button == "direct_message" : 
            pass
        if self.last_selected_button == "social_media" : 
            pass
        if self.last_selected_button == "speech" :
            pass
        if self.last_selected_button == "setting" : 
            pass
        if self.last_selected_button == "processor" :
            pass
        if self.last_selected_button == "help" : 
            pass
 
    # the functions of QListWidgetItem       
    def home_func(self):
        self.last_selected_button = "home"
        self.test_label.move(500,500)
        self.test_label.show()
         
        
    def direct_message_func(self):
        self.last_selected_button = "direct_message"
 
        
    def social_medias_func(self):
        self.last_selected_button == "social_medias"
 
        
    def speech_func(self):
        self.last_selected_button == "speech"

        
    def settings_func(self):
        self.last_selected_button == "settings"

    
    def processor_func(self):
        self.last_selected_button == "processor"
        # connection function
        def Check_Network_Connection():
            import requests
            url = "http://www.google.com"
            try:
                requests.get(url, timeout=3)
                return True
            except (requests.ConnectionError, requests.Timeout):
                return False
        # having microphone
        def Number_Of_Microphone_Connected_Devices():
            import ctypes
            winmm = ctypes.windll.winmm.waveInGetNumDevs() 
            if winmm != 0:
                return True
            else:
                return False
        # having enough ram
        def Ram():
            import psutil

            if dict(psutil.virtual_memory()._asdict())["total"] >= 2857841664:
                return True
            else:
                return False
        # storage space 
        def Storage_Space():
            import shutil

            total, used, free = shutil.disk_usage("/")

            if free // (2**30) >= 1:
                return True
            else:
                return False
        # cheking the operating system         
        def Check_Operating_System():
            import platform
            if platform.system() != "Windows" or platform.machine() != "AMD64":
                return False
            return True
        
        # now cheking each of them 
    
        
        
        
    def help_func(self):
        self.last_selected_button == "help"

# end of the GUI
# setting the stylesheet
Stylesheet = """
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
"""

if  __name__=='__main__':
          app = QApplication(sys.argv)
          app.setStyleSheet(Stylesheet)
          ex=GUI()
          ex.show()
          sys.exit(app.exec_())
