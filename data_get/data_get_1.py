
import requests
import csv
import time



def get_nextwork(nowpage,n):
    cookies = {
        'partner': 'www_baidu_com',
        'seo_refer_info_2023': '%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3DgZ5UGvJmeLiwwZRt8rpf0DPJW6bvC462ZU_PNPWDEkm%26wd%3D%26eqid%3De4b930ae0000453200000003671f52ab%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D',
        'privacy': '1730106052',
        'guid': '98e03f0dcbc4b786c829197dab6cb9a0',
        'sajssdk_2015_cross_new_user': '1',
        'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
        'tfstk': 'f2cK9Wtbahxhu0bOBT9gE-DiiHYMib3FBDufZuqhFcntlme5dJMo28Et4k23OpuWwli3xUPQx_F-y0oud7xF8Aoml6cHL7f8T7PWmnADiwuUa7a9po-UYVgaP1LWHz0E877wmnADi2S8CYkew7i715abu7aQR0Z6WzalAT1IVF3_bzN7V0NWWVGWUBqP_of-UdojQvzUX_1RuyeQcIrON_GTJiqjRE55NfULpboqSId7KYg43X0kw1PnkAN_yb8feuexFXVsOhObQ8MSn8HGAemj2ViztfT5doMnx5GIHa1SWWESDfwfvhEjTVG41RAXkVGZx2ltraO7Smqs8XNJGEPLOkNT7bxNOuHsFX2UaMt84f3sOYIzZjcYJxs0DzXBWFBPUJaatgPKMpFTeNaTmFqOUTy9OPEDWFBPUJaaWoYGHTWzBB1..',
        'Hm_lvt_1370a11171bd6f2d9b1fe98951541941': '1730106054,1730110599',
        'Hm_lpvt_1370a11171bd6f2d9b1fe98951541941': '1730110599',
        'HMACCOUNT': 'C1F7B9F9F58DF83B',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2298e03f0dcbc4b786c829197dab6cb9a0%22%2C%22first_id%22%3A%22192d25b53630-0d19c68c9b5b178-26001151-1338645-192d25b53649df%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyZDI1YjUzNjMwLTBkMTljNjhjOWI1YjE3OC0yNjAwMTE1MS0xMzM4NjQ1LTE5MmQyNWI1MzY0OWRmIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiOThlMDNmMGRjYmM0Yjc4NmM4MjkxOTdkYWI2Y2I5YTAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2298e03f0dcbc4b786c829197dab6cb9a0%22%7D%2C%22%24device_id%22%3A%22192d25b53630-0d19c68c9b5b178-26001151-1338645-192d25b53649df%22%7D',
        'search': 'jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%CB%B9%A4%D6%C7%C4%DC%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%ED%BC%FE%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
        'JSESSIONID': '8FE2D3F2EAE0152CF0A7F0C6EB34F095',
        'ssxmod_itna': 'WqRxBDuDy7qiqxBPiKGdD7fuYYKPS+wM40KtvhELt4UtD/BK+DnqD=GFDK40EYC5KFE8RGdqKlRY+ttYhBaLm=Wlb2hHHR9o4GLDmKDyij2ieDx2q0rD74irDDxD3Db3QDSDWKD9D04CMnkNgDi3DbxiDmMdDILiexDLlGT6exYQDGuIXD7QKvM4D0M4bXGGuGDrDYSLeuwuMiiarGqDM7eGXKDydGquCyZ+VWaFrQlPcDB6mxBjZInttL7UDgui3CBpoCY+hQdotiGqqY0hdiGeUarxNtGGdQwDeKihuoO4uCOqHUDDAK2PCwq4D===',
        'ssxmod_itna2': 'WqRxBDuDy7qiqxBPiKGdD7fuYYKPS+wM40KtvhELt4tG9Co=WYDBwwme7P4px15hbWqxx1TIAqx4+KvBigm8NW+iovEVI7YSWtSB+i3q1MesdmtD6ljL5Lfo7F3xBwQRxmw8fdAwueVCKkHlyPF6esKr4+7EIaTlcOsx7HPIWilo+tPRhCY7D5KWutfhuacDpEK1FEvtg843ahI49Pe6KW5ieCT03Fk6I3AIy8CYd829cfKuPwbO8G56lYYUjqioonP69Clr46X4=xKOf4dkibjhYnIYjOQ2ILohGwkfIyI/PZM2Fbr+f56qD23Ahmwjmp6qaiXBZPq7mQZYtPiLWA+05dFP/Ct9jQwCrkQ2ri6V7G4xx/lX=aX8C2njDPWwVPRORw0YpZOGjhDbWqUDpoZX=SdpGfoA2op=mOpGReNePWr+uhqo2m1ze5iNjnGVAGKFqR1PWo5w93ACrEGDnSK9tE0inu6ckjX=p5OS2WWrGAwxBT9lPZr6qfK5mXfKLnfYUlY92vxe7eGQgpdPwXcWNdOQmPtSpTwE=k835LtbzKcg=BCUuidCfoQXQcPWAPBOMRUEg45kp=AYHb1ykwaI/PB58DHDG20rtmoorSPHLaF/WEd4hUqm/PRgpWGTTwvfqtzS/Szabw4WDDFqD+1xxD==',
        'acw_tc': 'ac11000117301126260616483e007182fb5294913e1f6db15edb8c7f2c223a',
        'acw_sc__v2': '671f6c721b3809863621c3af8c34cac1ae94d026',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN',
        'Connection': 'keep-alive',
        # 'Cookie': 'partner=www_baidu_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3DgZ5UGvJmeLiwwZRt8rpf0DPJW6bvC462ZU_PNPWDEkm%26wd%3D%26eqid%3De4b930ae0000453200000003671f52ab%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1730106052; guid=98e03f0dcbc4b786c829197dab6cb9a0; sajssdk_2015_cross_new_user=1; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; tfstk=f2cK9Wtbahxhu0bOBT9gE-DiiHYMib3FBDufZuqhFcntlme5dJMo28Et4k23OpuWwli3xUPQx_F-y0oud7xF8Aoml6cHL7f8T7PWmnADiwuUa7a9po-UYVgaP1LWHz0E877wmnADi2S8CYkew7i715abu7aQR0Z6WzalAT1IVF3_bzN7V0NWWVGWUBqP_of-UdojQvzUX_1RuyeQcIrON_GTJiqjRE55NfULpboqSId7KYg43X0kw1PnkAN_yb8feuexFXVsOhObQ8MSn8HGAemj2ViztfT5doMnx5GIHa1SWWESDfwfvhEjTVG41RAXkVGZx2ltraO7Smqs8XNJGEPLOkNT7bxNOuHsFX2UaMt84f3sOYIzZjcYJxs0DzXBWFBPUJaatgPKMpFTeNaTmFqOUTy9OPEDWFBPUJaaWoYGHTWzBB1..; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1730106054,1730110599; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1730110599; HMACCOUNT=C1F7B9F9F58DF83B; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2298e03f0dcbc4b786c829197dab6cb9a0%22%2C%22first_id%22%3A%22192d25b53630-0d19c68c9b5b178-26001151-1338645-192d25b53649df%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyZDI1YjUzNjMwLTBkMTljNjhjOWI1YjE3OC0yNjAwMTE1MS0xMzM4NjQ1LTE5MmQyNWI1MzY0OWRmIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiOThlMDNmMGRjYmM0Yjc4NmM4MjkxOTdkYWI2Y2I5YTAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2298e03f0dcbc4b786c829197dab6cb9a0%22%7D%2C%22%24device_id%22%3A%22192d25b53630-0d19c68c9b5b178-26001151-1338645-192d25b53649df%22%7D; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%CB%B9%A4%D6%C7%C4%DC%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%ED%BC%FE%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; JSESSIONID=8FE2D3F2EAE0152CF0A7F0C6EB34F095; ssxmod_itna=WqRxBDuDy7qiqxBPiKGdD7fuYYKPS+wM40KtvhELt4UtD/BK+DnqD=GFDK40EYC5KFE8RGdqKlRY+ttYhBaLm=Wlb2hHHR9o4GLDmKDyij2ieDx2q0rD74irDDxD3Db3QDSDWKD9D04CMnkNgDi3DbxiDmMdDILiexDLlGT6exYQDGuIXD7QKvM4D0M4bXGGuGDrDYSLeuwuMiiarGqDM7eGXKDydGquCyZ+VWaFrQlPcDB6mxBjZInttL7UDgui3CBpoCY+hQdotiGqqY0hdiGeUarxNtGGdQwDeKihuoO4uCOqHUDDAK2PCwq4D===; ssxmod_itna2=WqRxBDuDy7qiqxBPiKGdD7fuYYKPS+wM40KtvhELt4tG9Co=WYDBwwme7P4px15hbWqxx1TIAqx4+KvBigm8NW+iovEVI7YSWtSB+i3q1MesdmtD6ljL5Lfo7F3xBwQRxmw8fdAwueVCKkHlyPF6esKr4+7EIaTlcOsx7HPIWilo+tPRhCY7D5KWutfhuacDpEK1FEvtg843ahI49Pe6KW5ieCT03Fk6I3AIy8CYd829cfKuPwbO8G56lYYUjqioonP69Clr46X4=xKOf4dkibjhYnIYjOQ2ILohGwkfIyI/PZM2Fbr+f56qD23Ahmwjmp6qaiXBZPq7mQZYtPiLWA+05dFP/Ct9jQwCrkQ2ri6V7G4xx/lX=aX8C2njDPWwVPRORw0YpZOGjhDbWqUDpoZX=SdpGfoA2op=mOpGReNePWr+uhqo2m1ze5iNjnGVAGKFqR1PWo5w93ACrEGDnSK9tE0inu6ckjX=p5OS2WWrGAwxBT9lPZr6qfK5mXfKLnfYUlY92vxe7eGQgpdPwXcWNdOQmPtSpTwE=k835LtbzKcg=BCUuidCfoQXQcPWAPBOMRUEg45kp=AYHb1ykwaI/PB58DHDG20rtmoorSPHLaF/WEd4hUqm/PRgpWGTTwvfqtzS/Szabw4WDDFqD+1xxD==; acw_tc=ac11000117301126260616483e007182fb5294913e1f6db15edb8c7f2c223a; acw_sc__v2=671f6c721b3809863621c3af8c34cac1ae94d026',
        'From-Domain': '51job_web',
        'Referer': 'https://we.51job.com/pc/search?keyword=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%B7%A5%E7%A8%8B%E5%B8%88&searchType=2&sortType=0&metro=',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'account-id': '',
        'partner': 'www_baidu_com',
        'property': '%7B%22partner%22%3A%22www_baidu_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3Fkeyword%3D%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D',
        'sec-ch-ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sign': '50153e48513fb01a235f882a0bc34685cedeb3e18e4930153b211f84e3e5f368',
        'user-token': '',
        'uuid': '98e03f0dcbc4b786c829197dab6cb9a0',
    }

    params = {
        'api_key': '51job',
        'timestamp': '1730112624',
        'keyword': '人工智能工程师',
        'searchType': '2',
        'function': '',
        'industry': '',
        'jobArea': '000000',
        'jobArea2': '',
        'landmark': '',
        'metro': '',
        'salary': '',
        'workYear': '',
        'degree': '',
        'companyType': '',
        'companySize': '',
        'jobType': '',
        'issueDate': '',
        'sortType': '0',
        'pageNum': f'{nowpage+1}',
        'requestId': 'd4585713d9c9fa6eab8127b933358c45',
        'pageSize': '100',
        'source': '1',
        'accountId': '',
        'pageCode': 'sou|sou|soulb',
    }

    response = requests.get('https://we.51job.com/api/job/search-pc', params=params, cookies=cookies, headers=headers)
    response.encoding = 'utf-8'
    items = response.json()['resultbody']['job']['items']
    print(items)
    with open('medium.csv', 'a', newline='', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['职位', '公司', '薪资', '城市', '公司详情页'])
        csv_writer.writeheader()
        for item in items:
            dit = {
                '职位': item['jobName'],
                '公司': item['fullCompanyName'],
                '薪资': item['provideSalaryString'],
                '城市': item['jobAreaString'],
                '公司详情页': item['companyHref']
            }
            csv_writer.writerow(dit)
            n=n+1

    return n





if __name__ == '__main__':
    n=0
    total=0
    print("请输入你要爬取的页数:", end='')
    Numberpage = int(input())
    for nowpage in range(Numberpage):
        total = total+get_nextwork(nowpage,n)



    print(f"共爬取{total}条信息")
    print()

