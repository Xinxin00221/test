'''
JSON 是纯文本
JSON 具有"自我描述性"（人类可读）
JSON 具有层级结构（值中存在值）
JSON 可通过 JavaScript 进行解析
JSON 数据可使用 AJAX 进行传输
'''

# json 示例

{
    "sites":[
        {"name": "菜鸟教程", "url": "www.runood.com"},
        {"name": "google", "url": "www.google.com"},
        {"name": "微博", "url": "www.weibo.com"}
    ]
}

'''
json数据格式：主要由对象 { } 和数组 [ ] 组成:
其中对象包括键值对（属性:属性值）{key： value}，value 可为 str，num，list，obj。取值使用 objcet.key
{key: value, key2:value2，} 键：值用冒号分开，对间用，连接
数组包含元素：num，str，list，objcet 都可以，利用索引访问 [index]，用 . 连接各个值
可嵌套json
delete可删除对象，并不是彻底删除元素，而是删除它的值，但仍会保留空间
可以使用 JSON.parse() 方法将数据转换为 JavaScript 对象
可以使用 JSON.stringify() 方法将 JavaScript 对象转换为字符串
'''
