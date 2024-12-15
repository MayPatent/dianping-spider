"""
店铺列表爬虫
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from config import HEADERS, SHOP_LIST_URL, SHOP_LIST_FILE, REQUEST_DELAY
import os

def get_shop_list(page_num):
    """获取指定页码的店铺列表"""
    url = SHOP_LIST_URL.format(page_num)
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        shop_list = soup.find_all('a', onclick="LXAnalytics('moduleClick', 'shoppic')")
        
        shops = []
        for shop in shop_list:
            shop_name = shop.find('img')['alt']
            shop_id = shop['href'].split('/')[-1]
            shops.append({'店铺名称': shop_name, '店铺ID': shop_id})
        
        return shops
    return []

def crawl_all_shops(start_page=1, end_page=50):
    """爬取所有店铺信息"""
    all_shops = []
    
    for page in range(start_page, end_page + 1):
        try:
            shops = get_shop_list(page)
            all_shops.extend(shops)
            print(f"成功爬取第{page}页")
            time.sleep(REQUEST_DELAY)
        except Exception as e:
            print(f"爬取第{page}页时出错: {e}")
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(SHOP_LIST_FILE), exist_ok=True)
    
    # 保存数据
    df = pd.DataFrame(all_shops)
    df.to_excel(SHOP_LIST_FILE, index=False)
    print(f"店铺数据已保存到 {SHOP_LIST_FILE}")