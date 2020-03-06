import pdfkit
pdfkit.from_url('https://www.cnblogs.com/shengulong/p/7994082.html','out.pdf')

# pdfkit.from_file('test.html','out.pdf')
#
# pdfkit.from_string('Hello!','out.pdf')

pdfkit.from_url(['google.com','yandex.ru','engadget.com'],'out.pdf')
pdfkit.from_file(['file1.html','file2.html'],'out.pdf')

# withopen('file.html')asf:
#     pdfkit.from_file(f,'out.pdf')

options={
    'page-size':'Letter',
    'margin-top':'0.75in',
    'margin-right':'0.75in',
    'margin-bottom':'0.75in',
    'margin-left':'0.75in',
    'encoding':"UTF-8",
    'no-outline':None
}
pdfkit.from_url('http://google.com','out.pdf', options=options)

# 当你转换文件、或字符串的时候，你可以通过css选项指定扩展的 CSS 文件。

# 单个 CSS 文件
css='example.css'pdfkit.from_file('file.html', options=options, css=css)
# Multiple CSS
filescss=['example.css','example2.css']
pdfkit.from_file('file.html', options=options, css=css)

# 你也可以通过你的HTML中的meta tags传递任意选项：

body = """  <html>  <head>  <meta name="pdfkit-page-size" content="Legal"/>  <meta name="pdfkit-orientation" content="Landscape"/>  </head>  Hello World!  </html>  """
pdfkit.from_string(body,'out.pdf')#with --page-size=Legal and --orientation=Landscape