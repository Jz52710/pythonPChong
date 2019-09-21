from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread

with open('data.txt',encoding='utf-8') as f:
    data = f.read()

nezha =imread('nz.png')
imgcolor =ImageColorGenerator(nezha)

nz = WordCloud(font_path="./STXINGKA.TTF",scale=6,mode="RGBA",background_color=None,mask=nezha,color_func=imgcolor)

nz.generate(data)

nz.to_file('哪吒.png')

#numpy爬
# from PIL import Image
# from numpy as np
# nezha = np.array(Image.open('nz.png'))
# imgcolor =ImageColorGenerator(nezha)
#
# nz = WordCloud(font_path="./STXINGKA.TTF",scale=6,mode="RGBA",background_color=None,mask=nezha,color_func=imgcolor)
#
# nz.generate(data)
#
# nz.to_file('哪吒.png')
