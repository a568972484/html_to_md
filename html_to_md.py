import re
import requests
from bs4 import BeautifulSoup


headers = {}
def url_to_md_txt(url):
    try:
        url = f'https://www.cnblogs.com/{url}'
        response = requests.get(url)
        a = re.findall('<div id="cnblogs_post_body" class="blogpost-body cnblogs-markdown">(.*?)</div><div id="MySignature"></div>',response.text, re.S)
        if not a:
            response_dome = BeautifulSoup(response.text, 'html.parser')
            response_dome_str = str(response_dome.div)
            a = re.findall('<div class="postBody">(.*?)</div><div id="MySignature"></div>', response_dome_str, re.S)
        a = a[0]
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
        a = re.sub('<pre>', '', a)
        a = re.sub('<ul>', '', a)
        a = re.sub('<ol>', '', a)
        a = re.sub('<div.*?>', '', a)
        a = re.sub('<em id="__mceDel">', '', a)
        # a = re.sub('<a.*?>', '', a)
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
        return new_text
    #可能博客不一样会存在见状性没有用我匹配的格式找到内容
    except :
        return False

if __name__ == '__main__':
    url = input('\033[31;m请输入你的要爬取网页的的url\n'
                '例如https://www.cnblogs.com/pythonywy/p/11146937.html\n'
                '你只要输入pythonywy/p/11146937.html即可\n'
                '请输入')
    print('内容如下,复制绿色内容即可')
    print(f'\033[32;m{url_to_md_txt(url)}')
