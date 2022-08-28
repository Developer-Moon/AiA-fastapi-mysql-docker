import pandas as pd
from bs4 import BeautifulSoup
import requests


class BugsMusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = []
    title_ls = []
    artist_ls = []
    dict = {}
    df = None

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='p', attrs=({"class":self.class_name[1]}))
        ls2 = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls1:
            self.title_ls.append(i.find("a").text)
        for i in ls2:
            self.artist_ls.append(i.find("a").text)


# 딕셔너리에 담을려면 ??

    def insert_dict(self):
                                                             # i가 있는 위치에 따라
        # 방법 1. range                                      # 객체  
        for i in range(0, len(self.title_ls)):               # 파라미터               이터레이터는 커서가 움직인다?
            self.dict[self.title_ls[i]] = self.artist_ls[i]  # 오브젝트  
        # 방법 2. zip 둘 다 넣고싶을때
        for i, j in zip(self.title_ls, self.artist_ls):
            self.dict[i] = j
        # 방법 3. enumerate [열거]                          
        for i, j in enumerate(self.title_ls):
            self.dict[j] = self.artist_ls[i]

        print(dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')



    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = input('0-exit, 1-input time\n, '
                         '2-output\n, '
                         '3-print dict\n '
                         '4-dict to dataframe\n'
                         '5-df to csv')
            if menu == '0':
                break
            elif menu == '1':
                bugs.set_url('wl_ref=M_contents_03_01')
            elif menu == '2':
                bugs.class_name.append("artist")
                bugs.class_name.append("title")
                bugs.get_ranking()
            elif menu == '3':
                bugs.insert_dict()

            elif menu == '4':
                bugs.dict_to_dataframe()

            elif menu == '5':
                bugs.df_to_csv()

            else:
                print('Wrong Number')
                continue

BugsMusic.main()