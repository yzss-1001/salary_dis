import re
import requests
page = 3
i = 1
for current_page in range(page):

    current = (current_page+1)*30

    cookies = {
        'BDqhfp': '%E9%B8%A1%E8%9B%8B%26%260-10-1undefined%26%260%26%261',
        'BAIDUID': '0A89A07C97C731F9DF4A64F21E775B87:FG=1',
        'BAIDUID_BFESS': '0A89A07C97C731F9DF4A64F21E775B87:FG=1',
        'Hm_lvt_246a5e7d3670cfba258184e42d902b31': '1728289959',
        'BIDUPSID': '0A89A07C97C731F9DF4A64F21E775B87',
        'indexPageSugList': '%5B%22%E9%B8%A1%E8%9B%8B%22%2C%22%E8%B4%9D%E5%85%8B%E5%8B%92%22%2C%22%E5%A4%A7%E8%BF%AB%E6%9D%B0%22%5D',
        'PSTM': '1728889997',
        'H_PS_PSSID': '60821_60853_60875',
        'ZFY': 'Ab:AiGgou7:AzATj5GTf9o4Gg5se2KjPXYQgK1BjitXDM:C',
        '__bid_n': '19298ef705c9216b2bad9f',
        'TF_ORIGIN_URL': 'https://easylearn.baidu.com/edu-page/throw-in/zuowenIm?query=%25E5%259B%25BD%25E5%25AE%25B6%25E5%258A%25A9%25E5%25AD%25A6%25E9%2587%2591%25E7%2594%25B3%25E8%25AF%25B7%25E8%25A1%25A8%25E7%2594%25B3%25E8%25AF%25B7%25E7%2590%2586%25E7%2594%25B1200%25E5%25AD%2597&fr=tf&tf_source=bd_zw&account=bdzw1390&tf_source=bd_zw&account=bdzw1390&rid=-1&bd_vid=13024586899457498960',
        'SEARCH_MARKET_URL': 'http%3A//wenku.baidu.com/ndlaunch/browse/chat%3Ffr%3Dlaunch_ad%26utm_source%3Dbdcl-WD%26utm_medium%3Dcpc%26keyword%3D%25E5%2585%258D%25E8%25B4%25B9ai%2520%25E5%2586%2599%25E4%25BD%259C%26utm_account%3DSS-bdtg1033%26e_creative%3D95016305960%26e_keywordid%3D806223207049%26bd_vid%3DnWDzrHfYrj64P1DdnWmYnHmsnNtkrj0kg17xnH0sg1wxrHRsnHm1njR4PW0',
        'BDUSS': 'jlZTWVjMFpCdWVnTFZtWVZLYXc3WDdDbjNHcnhCMW8wT3NyOHcwLX5CVnFMamhuSUFBQUFBJCQAAAAAAQAAAAEAAADxYZ0UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqhEGdqoRBnQ',
        'BDUSS_BFESS': 'jlZTWVjMFpCdWVnTFZtWVZLYXc3WDdDbjNHcnhCMW8wT3NyOHcwLX5CVnFMamhuSUFBQUFBJCQAAAAAAQAAAAEAAADxYZ0UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqhEGdqoRBnQ',
        'RT': '"z=1&dm=baidu.com&si=ec522a44-8a2d-4600-8b73-adf9fc123d57&ss=m2d1ifak&sl=3j&tt=kq70&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=29qg0"',
        'BDRCVFR[X_XKQks0S63]': 'mk3SLVN4HKm',
        'firstShowTip': '1',
        'BDRCVFR[dG2JNJb_ajR]': 'mk3SLVN4HKm',
        'userFrom': 'images.baidu.com',
        'ab_sr': '1.0.1_MGUzYjE0NzJjOTEwNjA0OWEzYmQzNDcwMTc4OTQ0YjllMjM5NGFmOTdkYWQyNDk1MjdhYzk1ZjY5YWUwMjYwMjg5NzY3MmRhYTJhYTFhNjAzODBmM2FkODAyYWY1YTA3ODcwOTcyMjNkNGVlMjM4NGFkODAwMDk3ZDE2YWI1YzFiMjllZmEzNDk2NWFlZDNlNjU3YWVkNmM5ZjhmNmRiZg==',
        'BDRCVFR[-pGxjrCMryR]': 'mk3SLVN4HKm',
    }

    headers = {
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'BDqhfp=%E9%B8%A1%E8%9B%8B%26%260-10-1undefined%26%260%26%261; BAIDUID=0A89A07C97C731F9DF4A64F21E775B87:FG=1; BAIDUID_BFESS=0A89A07C97C731F9DF4A64F21E775B87:FG=1; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1728289959; BIDUPSID=0A89A07C97C731F9DF4A64F21E775B87; indexPageSugList=%5B%22%E9%B8%A1%E8%9B%8B%22%2C%22%E8%B4%9D%E5%85%8B%E5%8B%92%22%2C%22%E5%A4%A7%E8%BF%AB%E6%9D%B0%22%5D; PSTM=1728889997; H_PS_PSSID=60821_60853_60875; ZFY=Ab:AiGgou7:AzATj5GTf9o4Gg5se2KjPXYQgK1BjitXDM:C; __bid_n=19298ef705c9216b2bad9f; TF_ORIGIN_URL=https://easylearn.baidu.com/edu-page/throw-in/zuowenIm?query=%25E5%259B%25BD%25E5%25AE%25B6%25E5%258A%25A9%25E5%25AD%25A6%25E9%2587%2591%25E7%2594%25B3%25E8%25AF%25B7%25E8%25A1%25A8%25E7%2594%25B3%25E8%25AF%25B7%25E7%2590%2586%25E7%2594%25B1200%25E5%25AD%2597&fr=tf&tf_source=bd_zw&account=bdzw1390&tf_source=bd_zw&account=bdzw1390&rid=-1&bd_vid=13024586899457498960; SEARCH_MARKET_URL=http%3A//wenku.baidu.com/ndlaunch/browse/chat%3Ffr%3Dlaunch_ad%26utm_source%3Dbdcl-WD%26utm_medium%3Dcpc%26keyword%3D%25E5%2585%258D%25E8%25B4%25B9ai%2520%25E5%2586%2599%25E4%25BD%259C%26utm_account%3DSS-bdtg1033%26e_creative%3D95016305960%26e_keywordid%3D806223207049%26bd_vid%3DnWDzrHfYrj64P1DdnWmYnHmsnNtkrj0kg17xnH0sg1wxrHRsnHm1njR4PW0; BDUSS=jlZTWVjMFpCdWVnTFZtWVZLYXc3WDdDbjNHcnhCMW8wT3NyOHcwLX5CVnFMamhuSUFBQUFBJCQAAAAAAQAAAAEAAADxYZ0UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqhEGdqoRBnQ; BDUSS_BFESS=jlZTWVjMFpCdWVnTFZtWVZLYXc3WDdDbjNHcnhCMW8wT3NyOHcwLX5CVnFMamhuSUFBQUFBJCQAAAAAAQAAAAEAAADxYZ0UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqhEGdqoRBnQ; RT="z=1&dm=baidu.com&si=ec522a44-8a2d-4600-8b73-adf9fc123d57&ss=m2d1ifak&sl=3j&tt=kq70&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=29qg0"; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=images.baidu.com; ab_sr=1.0.1_MGUzYjE0NzJjOTEwNjA0OWEzYmQzNDcwMTc4OTQ0YjllMjM5NGFmOTdkYWQyNDk1MjdhYzk1ZjY5YWUwMjYwMjg5NzY3MmRhYTJhYTFhNjAzODBmM2FkODAyYWY1YTA3ODcwOTcyMjNkNGVlMjM4NGFkODAwMDk3ZDE2YWI1YzFiMjllZmEzNDk2NWFlZDNlNjU3YWVkNmM5ZjhmNmRiZg==; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
        'Referer': 'https://images.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E9%B8%A1%E8%9B%8B',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'tn': 'resultjson_com',
        'logid': '10175657834706998738',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'fr': '',
        'word': '鸡蛋',
        'queryWord': '鸡蛋',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '0',
        'hd': '',
        'latest': '',
        'copyright': '',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'expermode': '',
        'nojc': '',
        'isAsync': '',
        'pn': f'{current}',
        'rn': '30',
        'gsm': '1e',
        '1729215604638': '',
    }

    response = requests.get('https://images.baidu.com/search/acjson', params=params, cookies=cookies, headers=headers)

    # print(response.text)
    html = response.text
    pattern = re.compile('"thumbURL":"(.*?)"',re.S)
    items = re.findall(pattern,html)
    # print(items)

    for item in items:
        img_save_path = f'../img_data/image{i}.jpg'
        response = requests.get(item)
        content = response.content
        print(content)
        with open(img_save_path,'wb')as file:
            file.write(content)
            i=i+1




# for item in items:


# def img_url():
#
#
#
# def get_data(url,headers):
#     response = requests.get(url,headers=headers)
#     if response.status_code==200:
#         return response.text
#     else:
#         print(response.status_code)
#
# def pare_img_url(html):
#     pattern = re.compile('"thumbURL:(.*?)"',re.s)
#     items = re.findall(pattern,html)
#     return items
#
#
# def get_img_content(url):
#     response = requests.get(url,headers=headers)
#     if response.status_code==200:
#         return response.content
#     else:
#         print(response.status_code)
#
# def parse_img_url():
#
#
#
#
#
# def main():
#     img_name = 0
#     url = config.img_url
#     headers = config().img_headers
#     data = get_data(url,headers)
#     img_url = parse_img_url(data)
#     for img in img_url:
#         img_content = get_img_content(img)
#         img_name  =config.img_file+str(img_name)+".jpg"
#         save_img(img_content,img_name)
#
# if __name__ == '__main__':


