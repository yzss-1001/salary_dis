import requests
import csv
import time
import xlwt



def get_nextwork(nowpage,n):
    cookies = {
        'guid': '98e03f0dcbc4b786c829197dab6cb9a0',
        'nsearch': 'jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D',
        'search': 'jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%CB%B9%A4%D6%C7%C4%DC%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%ED%BC%FE%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21',
        'tfstk': 'fkxt9Zc50XcM5ueLJrghoa4AgVknqnpaJCJ7msfglBdpFQQb5NTDMZCpg1bGfVJjD6OGsxS1soIvHIRc5icaQeRkFlxi7iqAbiSjZbmoqRJN0i1dD7qc_p9FhkHjytvwQiyEZbmoqdPARKCsDiOfAM65Ui61GIZIpt601rZ6GvpCTtsfGIsjppGWLcf4Y_qvu2PNIdLN9oZYUOQ1N05LcotdB7fWCYrbcHBOWnRyK0nfSE9PzhvmDkSMeesCHnk7ksQJlhjBfXi58ZTXrZL31AAWMpOVjHMb5_TMsMt6y-ZXpGCXwH_76XCWbptPAwmSeptesd-pn-ifKQfBQhsxVYSOf1sdLncUfsLBlhbN05GAgHpBfEIyx3xRBUNlwt4spvU4uN6FjSS92VIdkJ6dZvfLur7Kf9CopvU4uN6Fp_D3yrzVJc1..',
        'partner': 'www_baidu_com',
        'seo_refer_info_2023': '%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3DrTkW7BAJXxJy5xKCYJ73VY64xoS0HODWi1DvIfO87wO%26wd%3D%26eqid%3Daa94590c000b808900000003672868f1%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D',
        'privacy': '1730701568',
        'Hm_lvt_1370a11171bd6f2d9b1fe98951541941': '1730106054,1730110599,1730701570',
        'Hm_lpvt_1370a11171bd6f2d9b1fe98951541941': '1730701570',
        'HMACCOUNT': 'C1F7B9F9F58DF83B',
        'acw_tc': 'ac11000117307015744637335e009145cd2624b03358bb44efcfc60a98b603',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2298e03f0dcbc4b786c829197dab6cb9a0%22%2C%22first_id%22%3A%22192d25b53630-0d19c68c9b5b178-26001151-1338645-192d25b53649df%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyZDI1YjUzNjMwLTBkMTljNjhjOWI1YjE3OC0yNjAwMTE1MS0xMzM4NjQ1LTE5MmQyNWI1MzY0OWRmIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiOThlMDNmMGRjYmM0Yjc4NmM4MjkxOTdkYWI2Y2I5YTAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2298e03f0dcbc4b786c829197dab6cb9a0%22%7D%2C%22%24device_id%22%3A%22192d25b53630-0d19c68c9b5b178-26001151-1338645-192d25b53649df%22%7D',
        'acw_sc__v2': '67286909a6bfdbd13cdcef6624359aa0a78adf22',
        'JSESSIONID': 'A41D407D8E39A67A810599050D65902B',
        'ssxmod_itna': 'QqfOBKiIeAxRogDzpDUDGEImG7twLwdt45KDkYBSSDBwW4iNDnD8x7YDvmfOD0g4pdoYChDhFP5nxcGFtYcR5hq6tB0HLd8OxB3DEx06xkloxiigDCeDIDWeDiDG4Gm4qGtDpxG=DjDytZ9TtDm4GWDeDg/4Gg3erD03NBWdrD4qDBIgdDKw2gUDDlUGndCBj5ieD+/32lBlUxWpqtGqDM7eGXYYydGqT1gZ+VWaF8=jPcDB=pxBjZInttL7UDgui37ApKmYAeQqotKGqsQg+xthxht0qjCB4uCADriVkF48pdDDfG0HD===',
        'ssxmod_itna2': 'QqfOBKiIeAxRogDzpDUDGEImG7twLwdt45KDkYBSD8wZ4GNFG2+xFqijdx==',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN',
        'Connection': 'keep-alive',
        # 'Cookie': 'guid=98e03f0dcbc4b786c829197dab6cb9a0; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%CB%B9%A4%D6%C7%C4%DC%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%C8%ED%BC%FE%CB%E3%B7%A8%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; tfstk=fkxt9Zc50XcM5ueLJrghoa4AgVknqnpaJCJ7msfglBdpFQQb5NTDMZCpg1bGfVJjD6OGsxS1soIvHIRc5icaQeRkFlxi7iqAbiSjZbmoqRJN0i1dD7qc_p9FhkHjytvwQiyEZbmoqdPARKCsDiOfAM65Ui61GIZIpt601rZ6GvpCTtsfGIsjppGWLcf4Y_qvu2PNIdLN9oZYUOQ1N05LcotdB7fWCYrbcHBOWnRyK0nfSE9PzhvmDkSMeesCHnk7ksQJlhjBfXi58ZTXrZL31AAWMpOVjHMb5_TMsMt6y-ZXpGCXwH_76XCWbptPAwmSeptesd-pn-ifKQfBQhsxVYSOf1sdLncUfsLBlhbN05GAgHpBfEIyx3xRBUNlwt4spvU4uN6FjSS92VIdkJ6dZvfLur7Kf9CopvU4uN6Fp_D3yrzVJc1..; partner=www_baidu_com; seo_refer_info_2023=%7B%22referUrl%22%3A%22https%3A%5C%2F%5C%2Fwww.baidu.com%5C%2Flink%3Furl%3DrTkW7BAJXxJy5xKCYJ73VY64xoS0HODWi1DvIfO87wO%26wd%3D%26eqid%3Daa94590c000b808900000003672868f1%22%2C%22referHost%22%3A%22www.baidu.com%22%2C%22landUrl%22%3A%22%5C%2F%22%2C%22landHost%22%3A%22www.51job.com%22%2C%22partner%22%3Anull%7D; privacy=1730701568; Hm_lvt_1370a11171bd6f2d9b1fe98951541941=1730106054,1730110599,1730701570; Hm_lpvt_1370a11171bd6f2d9b1fe98951541941=1730701570; HMACCOUNT=C1F7B9F9F58DF83B; acw_tc=ac11000117307015744637335e009145cd2624b03358bb44efcfc60a98b603; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2298e03f0dcbc4b786c829197dab6cb9a0%22%2C%22first_id%22%3A%22192d25b53630-0d19c68c9b5b178-26001151-1338645-192d25b53649df%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyZDI1YjUzNjMwLTBkMTljNjhjOWI1YjE3OC0yNjAwMTE1MS0xMzM4NjQ1LTE5MmQyNWI1MzY0OWRmIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiOThlMDNmMGRjYmM0Yjc4NmM4MjkxOTdkYWI2Y2I5YTAifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2298e03f0dcbc4b786c829197dab6cb9a0%22%7D%2C%22%24device_id%22%3A%22192d25b53630-0d19c68c9b5b178-26001151-1338645-192d25b53649df%22%7D; acw_sc__v2=67286909a6bfdbd13cdcef6624359aa0a78adf22; JSESSIONID=A41D407D8E39A67A810599050D65902B; ssxmod_itna=QqfOBKiIeAxRogDzpDUDGEImG7twLwdt45KDkYBSSDBwW4iNDnD8x7YDvmfOD0g4pdoYChDhFP5nxcGFtYcR5hq6tB0HLd8OxB3DEx06xkloxiigDCeDIDWeDiDG4Gm4qGtDpxG=DjDytZ9TtDm4GWDeDg/4Gg3erD03NBWdrD4qDBIgdDKw2gUDDlUGndCBj5ieD+/32lBlUxWpqtGqDM7eGXYYydGqT1gZ+VWaF8=jPcDB=pxBjZInttL7UDgui37ApKmYAeQqotKGqsQg+xthxht0qjCB4uCADriVkF48pdDDfG0HD===; ssxmod_itna2=QqfOBKiIeAxRogDzpDUDGEImG7twLwdt45KDkYBSD8wZ4GNFG2+xFqijdx==',
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
        'sign': '7999a332eb2ff27e70ae886c2399b87a876f61e8ae8edd85bea0eee094ca052f',
        'user-token': '',
        'uuid': '98e03f0dcbc4b786c829197dab6cb9a0',
    }

    params = {
        'api_key': '51job',
        'timestamp': '1730701595',
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
        'requestId': '',
        'pageSize': '100',
        'source': '1',
        'accountId': '',
        'pageCode': 'sou|sou|soulb',
    }
    time.sleep(2.5)
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

