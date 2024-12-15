"""
主程序入口
"""
from shop_spider import crawl_all_shops
from dish_spider import crawl_all_dishes
from image_downloader import download_images

def main():
    # 爬取店铺列表
    print("开始爬取店铺列表...")
    crawl_all_shops()
    
    # 爬取推荐菜品
    print("\n开始爬取推荐菜品...")
    crawl_all_dishes()
    
    # 下载图片
    print("\n开始下载图片...")
    download_images()
    
    print("\n所有数据爬取完成!")

if __name__ == "__main__":
    main()