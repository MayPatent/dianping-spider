# dianping-spider
# 大众点评美食数据爬虫

这是一个基于Python的爬虫项目,用于从大众点评网站爬取（此处以上海地区为例的）人气美食店铺、推荐菜品以及对应的图片数据。

## 项目结构

```
.
├── config.py               # 配置文件
├── shop_spider.py          # 店铺列表爬虫
├── dish_spider.py          # 推荐菜品爬虫 
├── image_downloader.py     # 图片下载器
├── main.py                 # 主程序入口
└── data
    ├── shop_data_shanghai.xlsx    # 爬取的店铺数据
    ├── dishes_shanghai.xlsx       # 爬取的菜品数据
    └── dish_images/               # 下载的图片数据
        └── ...
```

## 依赖库

- requests
- beautifulsoup4
- pandas
- openpyxl

可以通过以下命令安装所需的Python库:

```
pip install requests beautifulsoup4 pandas openpyxl
```

## 使用说明

1. 安装依赖: `pip install requests beautifulsoup4 pandas openpyxl`
2. 配置参数: 在 `config.py` 文件中配置请求头、URL和输出路径等信息。  
3. 运行主程序: `python main.py`
    - 也可以单独运行 `shop_spider.py`、`dish_spider.py` 和 `image_downloader.py` 来执行子任务
4. 查看数据: 爬取的数据将保存在 `data/` 文件夹下。
    - `shop_data_shanghai.xlsx`: 包含店铺名称和ID
    - `dishes_shanghai.xlsx`: 包含店铺的推荐菜品信息
    - `dish_images/`: 菜品图片

## 注意事项

- 爬虫过程中有适当的延迟设置,请勿频繁请求,以免对目标网站造成压力。
- 仅供学习和研究使用,切勿用于任何商业用途。爬取他人数据请遵守相关法律法规。 
- 因网络环境、目标网站结构变化等因素,爬虫可能会失效。如遇问题,请及时查看相关文档进行调试。

## 欢迎贡献

如果你有任何改进意见或建议,欢迎提交Pull Request或Issue。让我们一起努力,创造更好的数据爬取方案！
