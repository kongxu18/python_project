from  reportlab.graphics.shapes import Drawing, String, colors
from reportlab.graphics import renderPDF
from  reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

'''--- 添加中文支持 ---'''
# pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttf'))  # 注册要使用的字体
# pdfmetrics.registerFont(TTFont('g', 'futurama.ttf'))
pdfmetrics.registerFont(TTFont('song', 'SimSun.ttf'))  #注册字体  STHeiti Medium.ttc
'''--- 创建画布 ---'''
d = Drawing(300, 200)  # 创建画布并设置画布尺寸

'''--- 创建文本内容并设置样式与位置 ---'''
s1 = String(150, 100, '这是中文文字测试')  # 创建字符串并设置坐标、内容
s1.fontName = 'song'  # 设置字体
s1.fontSize = 14  # 设置字号
s1.fillColor = colors.red  # 设置字体颜色
s1.textAnchor = 'middle'  # 设置锚点为中心（即位置坐标为文本中心点坐标）

s2 = String(150, 120, '汉子！',fontName='song', fontSize=16, fillColor=colors.red, textAnchor='middle')
# 另一种设置方式

'''--- 添加内容到画布并生成PDF文件 ---'''
d.add(s1)  # 将字符串添加到画布
d.add(s2)

renderPDF.drawToFile(d, 'myPDF.pdf', '231231')  # 生成PDF文件并设置文件名称与文档描述