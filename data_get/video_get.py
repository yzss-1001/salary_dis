import requests
import re

cookies = {
    'BAIDUID': '0A89A07C97C731F9DF4A64F21E775B87:FG=1',
    'BAIDUID_BFESS': '0A89A07C97C731F9DF4A64F21E775B87:FG=1',
    'Hm_lvt_246a5e7d3670cfba258184e42d902b31': '1728289959',
    'BIDUPSID': '0A89A07C97C731F9DF4A64F21E775B87',
    'PSTM': '1728889997',
    'H_PS_PSSID': '60821_60853_60875',
    'ZFY': 'Ab:AiGgou7:AzATj5GTf9o4Gg5se2KjPXYQgK1BjitXDM:C',
    '__bid_n': '19298ef705c9216b2bad9f',
    'BDUSS': 'jlZTWVjMFpCdWVnTFZtWVZLYXc3WDdDbjNHcnhCMW8wT3NyOHcwLX5CVnFMamhuSUFBQUFBJCQAAAAAAQAAAAEAAADxYZ0UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqhEGdqoRBnQ',
    'BDUSS_BFESS': 'jlZTWVjMFpCdWVnTFZtWVZLYXc3WDdDbjNHcnhCMW8wT3NyOHcwLX5CVnFMamhuSUFBQUFBJCQAAAAAAQAAAAEAAADxYZ0UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqhEGdqoRBnQ',
    'hkpcSearch': '%u5929%u9F99%u516B%u90E8',
    'PC_TAB_LOG': 'video_details_page',
    'COMMON_LID': '1f15418746337f029853a0f5bc5ad2a6',
    'Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5': '1729498755,1729514886,1729518859',
    'HMACCOUNT': 'AE0E7E0D236B65A4',
    'BAIDU_SSP_lcr': 'https://cn.bing.com/',
    'ppfuid': 'FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGkHJI5+HejCI+YBMRTRlDLcGEimjy3MrXEpSuItnI4KDwqEyLna1xawwcZqp5pcyx3gwNSQKKIDdXA6eDfuiw2FMn0Pe6/S6BiwnlgEX5luFeupSILuGSq59z+tUgI1O6PGgLbz7OSojK1zRbqBESR5Pdk2R9IA3lxxOVzA+Iw1TWLSgWjlFVG9Xmh1+20oPSbrzvDjYtVPmZ+9/6evcXmhcO1Y58MgLozKnaQIaLfWRPAn9I0uOqAMff6fuUeWcH3uP17MSwwfMB6PygUxkCDZ6PdkwAJKyudgfO/X6mWKMM5FjnYxYstXg/9EfB3EVmL9vtWLunkLhj7/Cf/HJLm+lV1Uhhp5FAe6gNJIUptp7EMAaXYKm11G+JVPszQFdp9AJLcm4YSsYUXkaPI2Tl66J246cmjWQDTahAOINR5rXR5r/7VVI1RMZ8gb40q7az7vCK56XLooKT5a+rsFrf5Zu0yyCiiagElhrTEOtNdBJJq8eHwEHuFBni9ahSwpC7lbKkUwaKH69tf0DFV7hJROiLETSFloIVkHdy3+I2JUr1LsplAz0hMkWt/tE4tXVUV7QcTDTZWS/2mCoS/GV3N9awQ6iM6hs/BWjlgnEa1+5sdRXsYpujkFc+s7Qmm7mA/ZcYZrBj1SLvHrhKBJfWmH5FKazXcZ/j40FJv+iLGBn3nkkgHlne61I8I7KhtQgIkmBMJIjPMkS/L051MeqdGScsKYTJuSucgI5c3+79eVH+y2TvbOTuuHv1uGxwXFb2Y4Fi0ocudki7TJZ2CEOH+MgDooXooe2fDtFPlvZZhrBIBvU6WqlsFUVZFhvETwAmJrGRChHnhPuJeIKACPXiVuli9ItRLEkdb1mLxNHAk3uJy88YX/Rf/sKUjR12zxRTDxxJNDJS+Dlsbqu3n4I65ujli/3rQ8Zk1MjmTOsz9+kTqOM4upsnQ6IWq/zeZTItMCgHpQhuhr4ip73honuzoJhfJJqPUSX01viD97GXfw7kf+R6as3JPAEXsdOdDsWEAgJn+ZMVrELI7pXz8Jko9Xv3uSDHo/C3kmFLrauvEYpUg3FbqEqM6JmRHqkwRhSJTRMi4kJJH/clk6pRO2hhO6zRszeYvFyXCPSuJ5oyoOgoCPKXE8fX73WOZ0mAlF1mc=',
    'Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5': '1729519905',
    'ab_sr': '1.0.1_ODE5MTgxMGJkYjZkYzg4NWY5ZWE5YjhlMDI3NzcyOGZiMWNiZWZmZTdkZjlhZWVhOGRiMzU1N2NmMThkNzM1MjI4MzA4NjYzNTQ1MWQ2ZDVjN2Q1YTRiZDY1NzEzYzUwYmYyNjI3ODU3YmVlMzdiOTVlMWNhMzYyMWI3YjQ0OTg1MTg1NGY3MDIwMDE2NTk2M2ZmNDI0YzA0NGZhZDlhYzc1NDQwYTk5ZWU2MDBiNGMxM2VkYWVjOTU5MzA4NjkyZjkyY2Q3NWVkNTMwN2YwNmZkMjIwOWNkOGZlMzc0OTY=',
    'reptileData': '%7B%22data%22%3A%22ca120856c73692a17a18f617e9fa49df0bd17534d0e29dd138471c852ec1c7a4e598847069659c484c6c2f629bd29021b30a8b9ac8cdb6537e236c17f785491ca5156d131becbf710afb149203fba73d90e246e4b6e647c6fa793dce476af75346893681e0d7fa382a41ff501942d9dae8505954de8c9cfc6d69f369536322d7%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%229b28a336%22%7D',
    'RT': '"z=1&dm=baidu.com&si=ec522a44-8a2d-4600-8b73-adf9fc123d57&ss=m2j2vahe&sl=k&tt=s1w&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=mmna&ul=mpy4&hd=mq72"',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'BAIDUID=0A89A07C97C731F9DF4A64F21E775B87:FG=1; BAIDUID_BFESS=0A89A07C97C731F9DF4A64F21E775B87:FG=1; Hm_lvt_246a5e7d3670cfba258184e42d902b31=1728289959; BIDUPSID=0A89A07C97C731F9DF4A64F21E775B87; PSTM=1728889997; H_PS_PSSID=60821_60853_60875; ZFY=Ab:AiGgou7:AzATj5GTf9o4Gg5se2KjPXYQgK1BjitXDM:C; __bid_n=19298ef705c9216b2bad9f; BDUSS=jlZTWVjMFpCdWVnTFZtWVZLYXc3WDdDbjNHcnhCMW8wT3NyOHcwLX5CVnFMamhuSUFBQUFBJCQAAAAAAQAAAAEAAADxYZ0UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqhEGdqoRBnQ; BDUSS_BFESS=jlZTWVjMFpCdWVnTFZtWVZLYXc3WDdDbjNHcnhCMW8wT3NyOHcwLX5CVnFMamhuSUFBQUFBJCQAAAAAAQAAAAEAAADxYZ0UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGqhEGdqoRBnQ; hkpcSearch=%u5929%u9F99%u516B%u90E8; PC_TAB_LOG=video_details_page; COMMON_LID=1f15418746337f029853a0f5bc5ad2a6; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1729498755,1729514886,1729518859; HMACCOUNT=AE0E7E0D236B65A4; BAIDU_SSP_lcr=https://cn.bing.com/; ppfuid=FOCoIC3q5fKa8fgJnwzbE67EJ49BGJeplOzf+4l4EOvDuu2RXBRv6R3A1AZMa49I27C0gDDLrJyxcIIeAeEhD8JYsoLTpBiaCXhLqvzbzmvy3SeAW17tKgNq/Xx+RgOdb8TWCFe62MVrDTY6lMf2GrfqL8c87KLF2qFER3obJGkHJI5+HejCI+YBMRTRlDLcGEimjy3MrXEpSuItnI4KDwqEyLna1xawwcZqp5pcyx3gwNSQKKIDdXA6eDfuiw2FMn0Pe6/S6BiwnlgEX5luFeupSILuGSq59z+tUgI1O6PGgLbz7OSojK1zRbqBESR5Pdk2R9IA3lxxOVzA+Iw1TWLSgWjlFVG9Xmh1+20oPSbrzvDjYtVPmZ+9/6evcXmhcO1Y58MgLozKnaQIaLfWRPAn9I0uOqAMff6fuUeWcH3uP17MSwwfMB6PygUxkCDZ6PdkwAJKyudgfO/X6mWKMM5FjnYxYstXg/9EfB3EVmL9vtWLunkLhj7/Cf/HJLm+lV1Uhhp5FAe6gNJIUptp7EMAaXYKm11G+JVPszQFdp9AJLcm4YSsYUXkaPI2Tl66J246cmjWQDTahAOINR5rXR5r/7VVI1RMZ8gb40q7az7vCK56XLooKT5a+rsFrf5Zu0yyCiiagElhrTEOtNdBJJq8eHwEHuFBni9ahSwpC7lbKkUwaKH69tf0DFV7hJROiLETSFloIVkHdy3+I2JUr1LsplAz0hMkWt/tE4tXVUV7QcTDTZWS/2mCoS/GV3N9awQ6iM6hs/BWjlgnEa1+5sdRXsYpujkFc+s7Qmm7mA/ZcYZrBj1SLvHrhKBJfWmH5FKazXcZ/j40FJv+iLGBn3nkkgHlne61I8I7KhtQgIkmBMJIjPMkS/L051MeqdGScsKYTJuSucgI5c3+79eVH+y2TvbOTuuHv1uGxwXFb2Y4Fi0ocudki7TJZ2CEOH+MgDooXooe2fDtFPlvZZhrBIBvU6WqlsFUVZFhvETwAmJrGRChHnhPuJeIKACPXiVuli9ItRLEkdb1mLxNHAk3uJy88YX/Rf/sKUjR12zxRTDxxJNDJS+Dlsbqu3n4I65ujli/3rQ8Zk1MjmTOsz9+kTqOM4upsnQ6IWq/zeZTItMCgHpQhuhr4ip73honuzoJhfJJqPUSX01viD97GXfw7kf+R6as3JPAEXsdOdDsWEAgJn+ZMVrELI7pXz8Jko9Xv3uSDHo/C3kmFLrauvEYpUg3FbqEqM6JmRHqkwRhSJTRMi4kJJH/clk6pRO2hhO6zRszeYvFyXCPSuJ5oyoOgoCPKXE8fX73WOZ0mAlF1mc=; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1729519905; ab_sr=1.0.1_ODE5MTgxMGJkYjZkYzg4NWY5ZWE5YjhlMDI3NzcyOGZiMWNiZWZmZTdkZjlhZWVhOGRiMzU1N2NmMThkNzM1MjI4MzA4NjYzNTQ1MWQ2ZDVjN2Q1YTRiZDY1NzEzYzUwYmYyNjI3ODU3YmVlMzdiOTVlMWNhMzYyMWI3YjQ0OTg1MTg1NGY3MDIwMDE2NTk2M2ZmNDI0YzA0NGZhZDlhYzc1NDQwYTk5ZWU2MDBiNGMxM2VkYWVjOTU5MzA4NjkyZjkyY2Q3NWVkNTMwN2YwNmZkMjIwOWNkOGZlMzc0OTY=; reptileData=%7B%22data%22%3A%22ca120856c73692a17a18f617e9fa49df0bd17534d0e29dd138471c852ec1c7a4e598847069659c484c6c2f629bd29021b30a8b9ac8cdb6537e236c17f785491ca5156d131becbf710afb149203fba73d90e246e4b6e647c6fa793dce476af75346893681e0d7fa382a41ff501942d9dae8505954de8c9cfc6d69f369536322d7%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%229b28a336%22%7D; RT="z=1&dm=baidu.com&si=ec522a44-8a2d-4600-8b73-adf9fc123d57&ss=m2j2vahe&sl=k&tt=s1w&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=mmna&ul=mpy4&hd=mq72"',
    'Referer': 'https://haokan.baidu.com/v?vid=14029366291294056886',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'title': '天龙八部：少室山下睥睨群雄，乔峰以一敌三，慕容复不是敌手',
    'vid': '14029366291294056886',
    'act': 'pcRec',
    'pd': 'pc',
    'rank': '',
    'rank_type': '',
    'hk_nonce': '7bddd34b0988545b3c38820d9ca67b2b',
    'hk_timestamp': '1729519912',
    'hk_sign': '044c13ab9412a06bcf66625a107e8758',
    'hk_token': 'FXMDdAVwdwNwAHAGfXt3C3t7fgA',
}

response = requests.get('https://haokan.baidu.com/haokan/ui-web/video/rec', params=params, cookies=cookies, headers=headers)

html = response.text
pattern = re.compile('"play_url":"(.*?)"',re.S)#正则表达式   #推荐'previewUrlHttp'视频较小 'play_url'视频较大
items = re.findall(pattern,html)
# print(items)
i=1
for item in items:
    img_save_path = f'../video_data/video{i}.mp4'
    response = requests.get(item)
    # print(response)
    content = response.content
    print(content)
    with open(img_save_path,'wb')as file:
        file.write(content)
        i=i+1