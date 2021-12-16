import os

x = input('>> 输入博客文件名称(e.g. first_blog):')
name = f'{x}.md'
hugo_path = os.path.abspath('./tools/hugo.exe')
os.system(f'{hugo_path} new posts/{name}')
print('\n>> 博客创建成功啦，请在 content/posts 文件下编辑{}'.format(
    name
))