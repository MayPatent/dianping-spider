"""
推荐菜品爬虫
"""
import requests
import pandas as pd
import json
import time
import os
from config import HEADERS, DISH_INFO_URL, SHOP_LIST_FILE, DISH_DATA_FILE, REQUEST_DELAY

def get_shop_dishes(shop_id):
    """获取指定店铺的推荐菜品信息"""
    params = {
        'shopId': shop_id,
        'cityId': '1', # 本代码以上海的面包烘培菜品为例
        'power': '5',
        'mainCategoryId': '34245',
        'shopType': '10',
        'shopCityId': '1'
    }
    
    response = requests.get(DISH_INFO_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data.get("dishesWithPicVO", [])
    return []

def crawl_all_dishes():
    """爬取所有店铺的推荐菜品"""
    # 读取店铺数据
    shop_data = pd.read_excel(SHOP_LIST_FILE)
    recommendations = []
    
    for index, row in shop_data.iterrows():
        shop_name = row['店铺名称']
        shop_id = row['店铺ID']
        
        try:
            dishes = get_shop_dishes(shop_id)
            for dish in dishes:
                recommendations.append({
                    '店铺名称': shop_name,
                    '店铺ID': shop_id,
                    '推荐菜名称': dish.get('dishTagName', 'N/A'),
                    '图片链接': dish.get('defaultPicURL', 'N/A')
                })
            print(f"成功爬取店铺: {shop_name} (ID: {shop_id})")
        except Exception as e:
            print(f"爬取店铺 {shop_name} (ID: {shop_id}) 时出错: {e}")
        
        time.sleep(REQUEST_DELAY)
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(DISH_DATA_FILE), exist_ok=True)
    
    # 保存数据
    df = pd.DataFrame(recommendations)
    df.to_excel(DISH_DATA_FILE, index=False)
    print(f"推荐菜数据已保存到 {DISH_DATA_FILE}")