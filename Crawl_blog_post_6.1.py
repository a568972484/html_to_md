import json
import os
import re

import requests
from bs4 import BeautifulSoup
from lxml.html import etree


# 通过博客首页获取所有随笔以及对随笔计数的一个字典
# 对于链接和标题的一个整合
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
                print(f'\033[32;m已经获取标题为{name},url为{url}\033[0m')
            except:
                try:
                    name_xpath='//*[@id="topics"]/div/h1/text()[0]'
                    response = requests.get(url)
                    response = response.text
                    response_html = etree.HTML(response)
                    name = response_html.xpath(name_xpath)[0]
                    dic[name] = url
                    print(f'\033[32;m已经获取标题为{name},url为{url}\033[0m')
                except:
                    print(f'\033[31;m链接{url}获取随笔失败\033[0m')
                    continue
        print('\033[36;m全部读取完毕')
        print(f'随笔总数{dic["count"]}')
        print(f'保存的json文件中的内容{dic}\033[0m')
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
        print('\033[41;m字典保存json文件成功\033[0m')


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
        print('没有爬取下来链接')
        return False


# 输入随笔的url转md格式文件
def url_to_md_txt(url):
    try:
        url = f'https://www.cnblogs.com/{url}'
        response = requests.get(url)
        # print(response.text)
        a = re.findall(
            '<div id="cnblogs_post_body" class="blogpost-body.*?">(.*?)<div id="MySignature"></div>',
            response.text, re.S)
        if not a:
            response_dome = BeautifulSoup(response.text, 'html.parser')
            response_dome_str = str(response_dome.div)
            a = re.findall('<div class="postBody">(.*?)<div id="MySignature"></div>', response_dome_str, re.S)
        a = a[0]

        #去除a头尾的空格
        a = a.strip()

        #去除末尾的div
        a = a[:-6]

        #再去除一次宫格
        a = a.strip()

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
        # print(a)


        # 三个点
        if '<pre class=' in a:
            a = re.sub('<pre class="', '```', a)
            a = re.sub('"><code>', '\n', a)
        a = re.sub('<pre><code.*?>','```\n',a)
        a = re.sub('</code></pre>', '\n```', a)

        #另外一个写法的a
        a = re.sub('<div class="cnblogs_code".*?>', '```python', a)
        a = re.sub('</div>', '```', a)

        #一个点
        a = re.sub('<code.*?>|</code>', '`', a)



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

        #ul与li
        a = re.sub('<ul.*?>|</ul>|</li>','',a)
        a = re.sub('<li.*?>','- ',a)

        #html标签修正
        print(a)
        a = re.sub('<;', '<', a)
        a = re.sub('>;', '>', a)
        a = re.sub(';/', '/', a)

        # 上面全是转md
        return a

    # 可能博客不一样会存在见状性没有用我匹配的格式找到内容
    except:
        print('on')
        return False

# 输入随笔的url转hexo支持解析的md格式文件添加标题
def url_to_md_txt_hexo(url,tap):
    try:
        url = f'https://www.cnblogs.com/{url}'
        response = requests.get(url)
        # print(response.text)
        a = re.findall(
            '<div id="cnblogs_post_body" class="blogpost-body.*?">(.*?)<div id="MySignature"></div>',
            response.text, re.S)
        if not a:
            response_dome = BeautifulSoup(response.text, 'html.parser')
            response_dome_str = str(response_dome.div)
            a = re.findall('<div class="postBody">(.*?)<div id="MySignature"></div>', response_dome_str, re.S)
        a = a[0]

        #去除a头尾的空格
        a = a.strip()

        #去除末尾的div
        a = a[:-6]

        #再去除一次宫格
        a = a.strip()

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
        # print(a)


        # 三个点
        if '<pre class=' in a:
            a = re.sub('<pre class="', '```', a)
            a = re.sub('"><code>', '\n', a)
        a = re.sub('<pre><code.*?>','```\n',a)
        a = re.sub('</code></pre>', '\n```', a)

        #另外一个写法的a
        a = re.sub('<div class="cnblogs_code".*?>', '```python', a)
        a = re.sub('</div>', '```', a)

        #一个点
        a = re.sub('<code.*?>|</code>', '`', a)



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

        #ul与li
        a = re.sub('<ul.*?>|</ul>|</li>','',a)
        a = re.sub('<li.*?>','- ',a)

        #html标签修正
        print(a)
        a = re.sub('<;', '<', a)
        a = re.sub('>;', '>', a)
        a = re.sub(';/', '/', a)

        # 上面全是转md

        # 上面全是转md
        #添加头
        title_xpath = '//a[@id="cb_post_title_url"]/text()'
        response_html = etree.HTML(response.text)
        title = response_html.xpath(title_xpath)[0]
        data_xpath = '//*[@id="post-date"]/text()'
        data = response_html.xpath(data_xpath)[0]
        data_header = f'---\ntitle: {title} \ndate: {data} \ntags: {tap} \n\n\n---\n'
        a = data_header + a
        return a

    # 可能博客不一样会存在见状性没有用我匹配的格式找到内容
    except:
        print('on')
        return False

# 保存文档
def text_to_file(name, text,files_name='博客园随笔md格式'):
    # 创建文件夹
    if not os.path.exists(files_name): os.mkdir(files_name)

    # 创建文件路径
    file_path = os.path.join(files_name, f'{name}.md')

    # 保存
    try:
        with open(file_path, 'w', encoding='utf8') as fw:
            fw.write(text)
            print(f'\033[32;m{name}的markdown文件保存成功\033[0m')
    except:
        print(f'\033[31;m{name}的markdown文件保存失败\033[0m')


# 可视化窗口写:
action_msg = '''
输入1：批量爬取博客园首页的所有随笔字典并保存json文件,且随笔全部转成md格式文件
输入2：输入指定随笔url把随笔内容转成md并且保存
输入3：爬取某个分类下的所有博客
输入4：爬取某个分类下的所有博客,并保存自定义标签,标题以及创建日期,便捷hexo个人博客随笔上传
输入Q：退出脚本
'''


# 功能1
def action_1():
    print('\033[31;m输入博客园首页的格式为\n'
          '例如https://www.cnblogs.com/pythonywy/\n'
          '你只要输入 pythonywy/ 即可\n'
          '')
    url = input('请输入\033[0m')
    try:
        # 读取字典
        print('爬取中请等待')
        dic = get_count_url_lis(url)
        # 保存字典
        dump_json(dic, url)
        # 读取字典title和url
        dic = read_dic(url)  # type:dict
        for name, name_url in dic.items():
            print(name_url)
            text = url_to_md_txt(name_url)
            if text:
                text_to_file(name, text)
            else:
                print(f'{name}随笔转md失败')
        print('全部md转换完成')
    except:
        print('输入url有误或者没有随笔')


# 功能二
def action_2():
    print('\033[31;m输入url\n'
          '例如https://www.cnblogs.com/pythonywy/p/11123051.html\n'
          '你只要输入pythonywy/p/11146937.html即可\n')
    url = input('请输入\033[0m')
    name = input('请输入,你要保存的md文件的文件名称')
    try:
        text = url_to_md_txt(url)
        text_to_file(name, text)
    except:
        print('输入url有误或者没有随笔')

def action_3():
    """按照分类爬取分类下所有博客"""
    print('\033[31;m输入博客园首页的格式为\n'
          '例如 https://www.cnblogs.com/nickchen121/category/1379216.html \n'
          '你只要输入 nickchen121/category/1379216.html 即可\n'
          '')
    url = input('请输入\033[0m')

    try:
        # 读取字典
        print('爬取中请等待')
        dic = get_category_url_lis(url)
        # 保存字典
        dump_json(dic, url)
        # 读取字典title和url
        dic = read_dic(url)  # type:dict
        for name, name_url in dic.items():
            print(name_url)
            text = url_to_md_txt(name_url)
            if text:
                text_to_file(name, text)
            else:
                print(f'{name}随笔转md失败')
        print('全部md转换完成')
    except:
        print('输入url有误或者没有随笔')

def action_4():
    """按照分类爬取分类下所有博客,内容添加hexo传输内容包括标题,日期"""
    print('\033[31;m输入博客园首页的格式为\n'
          '例如 https://www.cnblogs.com/nickchen121/category/1379216.html \n'
          '你只要输入 nickchen121/category/1379216.html 即可\n'
          '')
    url = input('请输入\033[0m')
    files_name = input('请输入分类名称\033[0m')

    try:
        # 读取字典
        print('爬取中请等待')
        dic = get_category_url_lis(url)
        # 保存字典
        dump_json(dic, url)
        # 读取字典title和url
        dic = read_dic(url)  # type:dict
        for name, name_url in dic.items():
            print(name_url)
            text = url_to_md_txt_hexo(name_url,files_name)
            if text:
                text_to_file(name, text,files_name)
            else:
                print(f'{name}随笔转md失败')
        print('全部md转换完成')
    except:
        print('输入url有误或者没有随笔')


# 主界面:
def run():
    while True:
        print(f'\033[36;m{action_msg}')
        action_msg_chiose = input('请选择功能')

        if action_msg_chiose == 'Q':
            print('退出')
            break
        elif action_msg_chiose not in ('1', '2', '3','4'):
            print('请好好输入')
            continue
        elif action_msg_chiose == '1':
            action_1()
        elif action_msg_chiose == '2':
            action_2()
        elif action_msg_chiose == '3':
            action_3()
        elif action_msg_chiose == '4':
            action_4()


if __name__ == '__main__':
    run()
