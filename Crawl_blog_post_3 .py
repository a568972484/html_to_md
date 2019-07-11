import re
import requests
from lxml.html import etree
import json
import  os




#通过博客首页获取所有随笔以及对随笔计数的一个字典
#对于链接和标题的一个整合
def count_url_lis_to_dict(func_1):
    def wrapper(*args,**kwargs):
        dic = dict()
        lis = func_1(*args,**kwargs)
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
                print(f'已经获取标题为{name},url为{url}')
            except:
                continue
        print('全部读取完毕')
        print(f'随笔总数{dic["count"]}')
        print(f'保存的json文件中的内容{dic}')
        return dic
    return wrapper

@count_url_lis_to_dict
def get_count_url_lis(url):
    lis = []
    count = 1
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
        count +=1
        lis = set(lis)
        lis = list(lis)
        count_2 = len(lis)

        if count_1 == count_2:
            return count_2,lis  #博客的数据量,博客里面随笔的url


#保存爬取的字典成 json格式
def dump_json(dict,url):
    file_name = url.split('/')[-2]

    if not os.path.exists('博客园随笔'):os.mkdir('博客园随笔') #创建个放随笔的文件夹

    file_path = os.path.join('博客园随笔', f'{file_name}.json')
    with open(file_path,'w',encoding='utf8') as fw:
        json.dump(dict,fw)
        print('字典保存json文件成功')


#读取字典且保存去除字典中count 这一栏
def read_dic(url):
    file_name = url.split('/')[-2]
    file_path = os.path.join('博客园随笔', f'{file_name}.json')
    try:
        with open(file_path, 'r', encoding='utf8') as fr:
            dic =json.load(fr)
            #删除计数这一栏
            del dic["count"]
            return dic
    except:
        print('没有爬取下来链接')
        return False

#输入随笔的url转md格式文件
def url_to_md_txt(url):
    try:
        response = requests.get(url)
        a = re.findall('<div id="cnblogs_post_body" class="blogpost-body cnblogs-markdown">(.*?)</div><div id="MySignature"></div>',response.text, re.S)[0]
        a = re.sub('<h1.*?>', '# ', a)
        a = re.sub('<h2.*?>', '## ', a)
        a = re.sub('<h3.*?>', '### ', a)
        a = re.sub('<h4.*?>', '#### ', a)
        a = re.sub('<h5.*?>', '##### ', a)
        a = re.sub('<h6.*?>', '###### ', a)
        a = re.sub('<strong>|</strong>', '**', a)
        if '<pre class=' in a:
            a = re.sub('<pre class="', '```', a)
            a = re.sub('"><code>', '\n', a)
        if '</code></pre>' in a:
            a = re.sub('</code></pre>', '\n```', a)
        a = re.sub('<code>|</code>', '```', a)
        a = re.sub('<div class="cnblogs_code".*?>', '```python', a)
        a = re.sub('</div>', '```', a)
        a = re.sub('<li>', '- ', a)
        a = re.sub('<em>|</em>', ' ', a)
        a = re.sub('<td.*?>|</td>\n', '|', a)
        a = re.sub('<th.*?>|</th>\n', '|', a)
        a = re.sub('<tr.*?>|</tr>\n', '', a)
        a = re.sub('</tbody>|</table>|<table>|<tbody>', '', a)
        a = re.sub('\|\|', '|', a)
        a = re.sub('&quot;', '"', a)
        a = re.sub('&#39;', "'", a)
        a = re.sub('<br/>', '\n', a)
        a = re.sub('<p.*?>', '', a)
        a = re.sub('<span.*?>', '', a)
        # a = re.sub('</.*?>', '', a) 这个先不去掉,为了后面表格时候弄
        a = re.sub('<pre>', '', a)
        a = re.sub('<ul>', '', a)
        a = re.sub('<ol>', '', a)
        a = re.sub('<div.*?>', '', a)
        a = re.sub('<em id="__mceDel">', '', a)
        a = re.sub('<a.*?>', '', a)
        a = re.sub('<em id="__mceDel">', '', a)
        a = re.sub('&gt', '>', a)
        lis_a = a.split('\n')
        text = ''
        for data in lis_a:
            if not data:
                continue
            if data == '|':
                data = '\n'
            if '</thead>' in data:
                lis_x_count = data.count('|') - 1
                data_txt = data[:-8]
                lis_format = '|:-:' * lis_x_count
                data = f'{data_txt}\n{lis_format}|'
            text += f'{data}\n'
        text = re.sub('</.*?>', '', text)
        lis = text.split('\n')
        for index in range(len(lis)):
            if 'href=' in lis[index]:
                lis[index] = f'{lis[index]}</a>'
        new_text = ''
        for aaaa in lis:
            aaaa = re.sub('&lt;', "<", aaaa)
            new_text += f'{aaaa}\n'


        #上面全是转md
        return new_text

    #可能博客不一样会存在见状性没有用我匹配的格式找到内容
    except :
        return False

#保存文档
def text_to_file(name,text):

    #创建文件夹
    if not os.path.exists('博客园随笔md格式'): os.mkdir('博客园随笔md格式')

    #创建文件路径
    file_path = os.path.join('博客园随笔md格式', f'{name}.md')

    #保存
    try:
        with open(file_path,'w',encoding='utf8') as fw:
            fw.write(text)
            print(f'{name}的markdown文件保存成功')
    except:
        print(f'{name}的markdown文件保存失败')



#可视化窗口写:
action_msg ='''
输入1.批量爬取博客园首页的所有随笔字典并保存json文件,且随笔全部转成md格式文件
输入2.输入指定随笔url把随笔内容转成md并且保存
输入Q.退出脚本
'''

#功能1
def action_1():
    print('输入博客园首页的格式为\n'
          '例如https://www.cnblogs.com/pythonywy/')
    url = input('请输入')
    try:
        #读取字典
        print('爬取中请等待')
        dic = get_count_url_lis(url)
        #保存字典
        dump_json(dic,url)
        #读取字典title和url
        dic = read_dic(url) #type:dict
        for name,name_url in dic.items():
            print(name_url)
            text = url_to_md_txt(name_url)
            if text :
                text_to_file(name,text)
            else:
                print(f'{name}随笔转md失败')
        print('全部md转换完成')
    except:
        print('输入url有误或者没有随笔')


#功能二
def action_2():
    print('输入url\n'
          '例如https://www.cnblogs.com/pythonywy/p/11123051.html\n'
          '温馨提示,你若填写置顶随笔url将不会转md成功')
    url = input('请输入')
    name = input('请输入,你要保存的md文件的文件名称')
    try:
        text = url_to_md_txt(url)
        text_to_file(name, text)
    except:
        print('输入url有误或者没有随笔')


#主界面:
def run():
    while True:
        print(action_msg)
        action_msg_chiose = input('请选择功能')

        if action_msg_chiose == 'Q':print('退出');break
        elif action_msg_chiose not in ('1','2') :print('请好好输入');continue
        elif action_msg_chiose =='1':action_1()
        elif action_msg_chiose =='2':action_2()


