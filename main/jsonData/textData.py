import requests
from datetime import datetime
from bs4 import BeautifulSoup
from requests.exceptions import InvalidURL,TooManyRedirects,MissingSchema
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError

class TextRetriever():

    def __init__(self):
        self.switch = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }

    def get_date(self, date):
        day = date.day
        year = date.year
        temp = date.month
        month = self.switch[temp]

        date_new = {'Day' : day, 'Month' : month, 'Year' : year}
        return date_new
        

    def get_link(self, date):
        url = f'https://www.valueline.com/Markets/Daily_Updates/Stock_Market_Today__{date["Month"]}_{date["Day"]},_{date["Year"]}.aspx'
        return url

    def get_text(self, url):

        cookies = {
            'ecm': 'user_id=0&isMembershipUser=0&site_id=&username=&new_site=/&unique_id=0&site_preview=0&langvalue=0&DefaultLanguage=1033&NavLanguage=1033&LastValidLanguageID=1033&DefaultCurrency=840&SiteCurrency=840&ContType=&UserCulture=1033&dm=www.valueline.com&SiteLanguage=1033',
            'EktGUID': '383e1754-381a-4352-a168-b0b9aeebdba9',
            'EkAnalytics': 'newuser',
            'ASP.NET_SessionId': '3xvotfjotn1al4rdvydz5tvu',
            '_ga': 'GA1.2.1025002423.1588929468',
            '_gid': 'GA1.2.1679466556.1588929468',
            '__utma': '47602208.1025002423.1588929468.1588929468.1588929468.1',
            '__utmc': '47602208',
            '__utmz': '47602208.1588929468.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
            'MGX_P': 'ff0a7604-ea2e-41b6-8a65-0b5ed4e29d73',
            'MGX_U': 'fd0f9e45-f8fb-42b2-adfb-65c9363692a2',
            'MGX_PX': '1e736b6f-8426-4309-89e8-788900d362fd',
            'MGX_CID': '90500e94-0154-4b21-a730-4558bda5eecc',
            'MGX_EID': 'bnNfc2VnXzAwMA==',
            '__hstc': '94504963.194b99fcfe0159281db1e0f885c3b030.1588929527976.1588929527976.1588929527976.1',
            'hubspotutk': '194b99fcfe0159281db1e0f885c3b030',
            '__hssrc': '1',
            'MGX_VS': '28',
            '__utmb': '47602208.28.10.1588929468',
            '__atuvc': '9%7C19',
            '__atuvs': '5eb523e7ee19a4d5008',
            '__hssc': '94504963.27.1588929527979',
        }
        
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.valueline.com/Markets/DailyUpdates.aspx',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        
        try:

            response = requests.get(url, headers=headers, cookies=cookies, timeout=20)

            html_doc = response.text
            tag = 'ArticleContent'

            soup = BeautifulSoup(html_doc, 'html.parser')

            try:

                val = soup.find_all('div', { 'id' : 'ArticleContent' })

                soup_text = BeautifulSoup(str(val[0]), 'html.parser')

                text = soup_text.getText(strip=True)

                return text

            except:
                
                return "NULL"

        except(ConnectTimeout, HTTPError, TooManyRedirects, ReadTimeout, Timeout, MissingSchema, InvalidURL, ConnectionError, Exception):
            
            return "NULL"

    def textData(self, date):
        
        _, _, text_data = self.get_text(self.get_link(self.get_date(date))).partition('Before The Bell - ')

        if text_data == '':
            text_data = 'NULL'

        return text_data