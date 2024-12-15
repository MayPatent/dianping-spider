"""
配置文件，存储常量和配置项
"""
# HTTP请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',    
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "connection": "keep-alive",
    "cookie": "your_cookie",
    "host": "www.dianping.com",
    "referer": "https://www.dianping.com/shop/iypt41IpBzGiMhAV",
    "x-requested-with": "XMLHttpRequest"
}

# URL配置
SHOP_LIST_URL = 'https://www.dianping.com/shanghai/ch10/g34245p{}'  # {} 将被页码替换
DISH_INFO_URL = 'https://www.dianping.com/ajax/json/shopDynamic/shopTabs'

# 文件路径配置
SHOP_LIST_FILE = 'data/shop_data_shanghai.xlsx'
DISH_DATA_FILE = 'data/dishes_shanghai.xlsx'
IMAGES_FOLDER = 'data/dish_images'

# 爬虫配置
REQUEST_DELAY = 2  # 请求延迟(秒)
MAX_RETRIES = 3   # 最大重试次数