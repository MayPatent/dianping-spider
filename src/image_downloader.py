"""
图片下载器
"""
import os
import requests
import pandas as pd
from config import DISH_DATA_FILE, IMAGES_FOLDER

def download_images():
    """下载所有菜品图片"""
    # 创建输出文件夹
    os.makedirs(IMAGES_FOLDER, exist_ok=True)
    
    # 读取菜品数据
    data = pd.read_excel(DISH_DATA_FILE)
    
    for index, row in data.iterrows():
        dish_name = row['推荐菜名称']
        image_url = row['图片链接']
        
        if pd.isna(image_url) or image_url == 'N/A':
            print(f"跳过无效图片链接: {dish_name}")
            continue
            
        try:
            # 生成文件名
            sanitized_dish_name = "".join(c for c in dish_name if c.isalnum() or c in " _-")
            file_name = f"{sanitized_dish_name}.jpg"
            file_path = os.path.join(IMAGES_FOLDER, file_name)
            
            # 下载图片
            response = requests.get(image_url, stream=True, timeout=10)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"成功下载图片: {dish_name}")
        except Exception as e:
            print(f"下载图片 {dish_name} 时出错: {e}")