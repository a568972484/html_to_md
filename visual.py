import json
import os
import time
from tkinter import *

import requests
from bs4 import BeautifulSoup
from lxml.html import etree

# 总窗口
root = Tk()
# 设置标题

root.title('博客园随笔转换')


# 设置大小

def count_url_lis_to_dict(func_1):
    def wrapper(*args, **kwargs):
        dic = dict()
        lis = func_1(*args, **kwargs)
        count = lis[0]
        url_lis = lis[1]
        dic['count'] = count
        name_xpath = '//*[@id="cb_post_title_url"]/text()'
        for url in url_lis:
            try:
                response = requests.get(url)
                response = response.text
                response_html = etree.HTML(response)
                name = response_html.xpath(name_xpath)[0]
                dic[name] = url
                show_windos(f'已经获取标题为{name},url为{url}')
            except:
                show_windos(f'链接{url}获取随笔失败')
                continue
        show_windos('全部读取完毕')
        show_windos(f'随笔总数{dic["count"]}')
        show_windos(f'保存的json文件中的内容{dic}')
        return dic

    return wrapper


@count_url_lis_to_dict
def get_count_url_lis(url):
    lis = []
    count = 1
    url = f'https://www.cnblogs.com/{url}'
    while True:
        count_1 = len(lis)
        response = requests.get(f'{url}default.html?page={count}')
        response = response.text
        data_1 = re.findall(' href="(.*?)"', response, re.S)
        for a in data_1:  # type:str
            if a.startswith('http'):
                if a.endswith('html'):
                    if 'archive' not in a:
                        lis.append(a)
        count += 1
        lis = set(lis)
        lis = list(lis)
        count_2 = len(lis)

        if count_1 == count_2:
            return count_2, lis  # 博客的数据量,博客里面随笔的url


@count_url_lis_to_dict
def get_category_url_lis(url_):
    """获取某个博客下的所有博客链接"""
    url = f'https://www.cnblogs.com/{url_}'
    response = requests.get(url)
    data = response.text

    category_url_lis = re.findall('class="entrylistItemTitle" href="(.*?)"', data)

    return len(category_url_lis), category_url_lis


# 保存爬取的字典成 json格式
def dump_json(dict, url):
    file_name = url.split('/')[-2]

    if not os.path.exists('博客园随笔'): os.mkdir('博客园随笔')  # 创建个放随笔的文件夹

    file_path = os.path.join('博客园随笔', f'{file_name}.json')
    with open(file_path, 'w', encoding='utf8') as fw:
        json.dump(dict, fw)
        show_windos('字典保存json文件成功')


# 读取字典且保存去除字典中count 这一栏
def read_dic(url):
    file_name = url.split('/')[-2]
    file_path = os.path.join('博客园随笔', f'{file_name}.json')
    try:
        with open(file_path, 'r', encoding='utf8') as fr:
            dic = json.load(fr)
            # 删除计数这一栏
            del dic["count"]

            # 去掉头
            dic_str = json.dumps(dic)
            dic_str = re.sub(r'https://www.cnblogs.com/', '', dic_str)

            # 变回字典
            dic = json.loads(dic_str)

            return dic
    except:
        show_windos('没有爬取下来链接')
        return False


# 输入随笔的url转md格式文件
def url_to_md_txt(url):
    try:
        url = f'https://www.cnblogs.com/{url}'
        response = requests.get(url)
        a = re.findall(
            '<div id="cnblogs_post_body" class="blogpost-body cnblogs-markdown">(.*?)</div><div id="MySignature"></div>',
            response.text, re.S)
        if not a:
            response_dome = BeautifulSoup(response.text, 'html.parser')
            response_dome_str = str(response_dome.div)
            a = re.findall('<div class="postBody">(.*?)</div><div id="MySignature"></div>', response_dome_str, re.S)
        a = a[0]
        # 标题
        a = re.sub('<h1>.*?\d*\. (?P<name>.*?)</h1>', '<h1>\g<name>\n\n</h1>', a)
        a = re.sub('<h1.*?>', '# ', a)
        a = re.sub('<h2>.*?\d*\.\d* (?P<name>.*?)</h2>', '<h2>\g<name>\n\n</h2>', a)
        a = re.sub('<h2.*?>', '## ', a)
        a = re.sub('<h3>.*?\d*\.\d*\.\d* (?P<name>.*?)</h3>', '<h3>\g<name>\n\n</h3>', a)
        a = re.sub('<h3.*?>', '### ', a)
        a = re.sub('<h4>.*?\d*\.\d*\.\d*\.\d* (?P<name>.*?)</h4>', '<h4>\g<name>\n\n</h4>', a)
        a = re.sub('<h4.*?>', '#### ', a)
        a = re.sub('<h5>.*?\d*\.\d*\.\d*\.\d*\.\d* (?P<name>.*?)</h5>', '<h5>\g<name>\n\n</h5>', a)
        a = re.sub('<h5.*?>', '##### ', a)
        a = re.sub('<h6>.*?\d*\.\d*\.\d*\.\d*\.\d*\.\d* (?P<name>.*?)</h6>', '<h6>\g<name>\n\n</h6>', a)
        a = re.sub('<h6.*?>', '###### ', a)
        a = re.sub('</h1>|</h2>|</h3>|</h4>|</h5>|</h6>|', "", a)

        # 三个点
        if '<pre class=' in a:
            a = re.sub('<pre class="', '```', a)
            a = re.sub('"><code>', '\n', a)
        if '</code></pre>' in a:
            a = re.sub('</code></pre>', '\n```', a)
        a = re.sub('<code.*?>|</code>', '```', a)
        a = re.sub('<div class="cnblogs_code".*?>', '```python', a)
        a = re.sub('</div>', '```', a)

        # 标签
        # 去掉开头的div标签
        a = re.sub('<div.*?>', '', a)

        # em标签
        a = re.sub('<em.*?>|</em>', ' ', a)

        # strong标签加粗
        a = re.sub('<strong>|</strong>', '**', a)

        # span标签
        a = re.sub('<span.*?>|</span>', '', a)

        # pre标签
        a = re.sub('<pre.*?>|</pre>', '', a)

        # p标签
        a = re.sub('<p.*?>|</p>', '', a)

        # br标签
        a = re.sub('<br/>', '\n', a)

        # 里面内容特殊变化
        # 双引号
        a = re.sub('&quot;', '"', a)
        # 单引号
        a = re.sub('&#39;', "'", a)
        # >符号
        a = re.sub('&gt', '>', a)
        # 符号
        a = re.sub('&lt', '<', a)

        # 上面全是转md
        return a

    # 可能博客不一样会存在见状性没有用我匹配的格式找到内容
    except:
        return False


# 保存文档
def text_to_file(name, text):
    # 创建文件夹
    if not os.path.exists('博客园随笔md格式'): os.mkdir('博客园随笔md格式')

    # 创建文件路径
    file_path = os.path.join('博客园随笔md格式', f'{name}.md')

    # 保存
    try:
        with open(file_path, 'w', encoding='utf8') as fw:
            fw.write(text)
            show_windos(f'{name}的markdown文件保存成功')
    except:
        show_windos(f'{name}的markdown文件保存失败')


# 展示窗口
windos_1 = Listbox(root)


def show_windos(*args, start_index='ywy'):
    if start_index == 'ywy':
        for data in args:
            windos_1.insert(END, data)
    elif start_index == 0:
        windos_1.delete(0, END)
        for data in args:
            windos_1.insert(END, data)


# 功能选择输入框标题
count_1 = Label(root, text='批量爬取博客园首页的所有随笔字典并保存json文件,且随笔全部转成md格式文件')
count_2 = Label(root, text='输入指定随笔url把随笔内容转成md并且保存')
count_3 = Label(root, text='爬取某个分类下的所有博客')

# 功能输入框输入框
# 存储内容
entry_1_data = StringVar()
entry_2_data = StringVar()
entry_3_data = StringVar()
# 输入框
entry_1 = Entry(root, state='normal', textvariable=entry_1_data)
entry_2 = Entry(root, state='normal', textvariable=entry_2_data)
entry_3 = Entry(root, state='normal', textvariable=entry_3_data)


# 按键传参设置
# 按键1
def b_1_dump(enter=entry_1):
    url = enter.get()
    show_windos(f'查找的URL:https://www.cnblogs.com/{url}',start_index=0)
    try:
        # 读取字典
        show_windos('爬取中请等待')
        dic = get_count_url_lis(url)
        # 保存字典
        dump_json(dic, url)
        # 读取字典title和url
        dic = read_dic(url)  # type:dict
        for name, name_url in dic.items():
            show_windos(name_url)
            text = url_to_md_txt(name_url)
            if text:
                text_to_file(name, text)
            else:
                show_windos(f'{name}随笔转md失败')
        show_windos('全部md转换完成')
    except:
        show_windos('输入url有误或者没有随笔')


# 记录文章默认名字序号
action_2_num = 0


def b_2_dump(enter=entry_2):
    url = enter.get()
    show_windos(f'查找的URL:https://www.cnblogs.com/{url}',start_index=0)
    global action_2_num
    name = f'第{action_2_num}篇'
    action_2_num += 1
    try:
        text = url_to_md_txt(url)
        text_to_file(name, text)
    except:
        show_windos('输入url有误或者没有随笔')


def b_3_dump(enter=entry_3):
    url = enter.get()
    show_windos(f'查找的URL:https://www.cnblogs.com/{url}',start_index=0)
    try:
        # 读取字典
        show_windos('爬取中请等待')
        dic = get_category_url_lis(url)
        # 保存字典
        dump_json(dic, url)
        # 读取字典title和url
        dic = read_dic(url)  # type:dict
        for name, name_url in dic.items():
            show_windos(name_url)
            text = url_to_md_txt(name_url)
            if text:
                text_to_file(name, text)
            else:
                show_windos(f'{name}随笔转md失败')
        show_windos('全部md转换完成')
    except:
        show_windos('输入url有误或者没有随笔')


# 功能对应3个按钮

b_1 = Button(root, text='确定输入', command=b_1_dump)
b_1.grid(row=0, column=2)

b_2 = Button(root, text='确定输入', command=b_2_dump)
b_2.grid(row=1, column=2)

b_3 = Button(root, text='确定输入', command=b_3_dump)
b_3.grid(row=2, column=2)

# 位置排版
# 功能一
count_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)

# 功能二
count_2.grid(row=1, column=0)
entry_2.grid(row=1, column=1)

# 功能三
count_3.grid(row=2, column=0)
entry_3.grid(row=2, column=1)

# 默认展示窗口
msg = '''
功能一输入首页url例如
https://www.cnblogs.com/pythonywy/
你只要输入pythonywy/即可
功能二输入首页url例如
https://www.cnblogs.com/pythonywy/p/11123051.html
你只要输入pythonywy/p/11123051.html即可
功能三输入首页url例如
例如 https://www.cnblogs.com/nickchen121/category/1379216.html
你只要输入nickchen121/category/1379216.html即可
消息展示面板'''

# 提示界面
msg_Label = Label(root, text=msg)
msg_Label.grid(row=3, column=0, sticky=N + S + E + W)


# 实时消息界面

windos_1.grid(row=4, column=0, sticky=N + S + W + E)
time.sleep(1)



# 展示
root.mainloop()
