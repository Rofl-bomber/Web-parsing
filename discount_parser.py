from bs4 import BeautifulSoup
import requests
import json
import pandas
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.shops = ['М.Видео', 'Ламода', 'Яндекс Маркет', 'Мегамаркет', 'Эльдорадо', 'Алиэкспресс']
        self.selected_shops = [False]*len(self.shops)

        self.ui.parser_button.clicked.connect(self.clicked_parse)
        self.ui.button_1.stateChanged.connect(self.clicked_shop)
        self.ui.button_2.stateChanged.connect(self.clicked_shop)
        self.ui.button_3.stateChanged.connect(self.clicked_shop)
        self.ui.button_4.stateChanged.connect(self.clicked_shop)
        self.ui.button_5.stateChanged.connect(self.clicked_shop)
        self.ui.button_6.stateChanged.connect(self.clicked_shop)
        self.ui.open_button.clicked.connect(self.clicked_open)
    def clicked_parse(self):
        create_table({self.shops[i]: data_handler(i) for i in range(len(self.shops)) if self.selected_shops[i]})

        self.ui.open_button.setEnabled(True)
    def clicked_shop(self):
        sender = self.sender()
        self.selected_shops[int(sender.objectName()[-1]) - 1] = sender.isChecked()

    def clicked_open(self):
        subprocess.Popen('Скидки.xlsx', shell=True)
        
def create_table(shops):
    with pandas.ExcelWriter('Скидки.xlsx') as writer:
        for shop, coupon in shops.items():
            df = pandas.DataFrame(coupon, columns=['title', 'promoCode','url'])
            df.columns = ['Название', 'Промокод', 'Ссылка']
            df.to_excel(writer,sheet_name=shop, index=False)
            writer.sheets[shop].autofit()

def data_handler(shop):
    shops = [
        'https://promokod.pikabu.ru/shops/mvideo',
        'https://promokod.pikabu.ru/shops/lamoda',
        'https://promokod.pikabu.ru/shops/market-yandex',
        'https://promokod.pikabu.ru/shops/megamarket',
        'https://promokod.pikabu.ru/shops/eldorado',
        'https://promokod.pikabu.ru/shops/aliexpress'
    ]
    bs = BeautifulSoup(requests.get(shops[shop]).text, 'lxml')
    content = json.loads(*bs.find('script', id='vike_pageContext').contents)
    return map(lambda coupon: {'promoCode': coupon['promoCode'], 'title': coupon['title'], 'url': 'https://promokod.pikabu.ru'+coupon['url']}, content['data']['coupons']['active'])

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
main()