import jieba
import pickle

with open('哪吒影评.txt','rb') as f:
    data0 = pickle.load(f)

data1 = []

def qie(data):
    return [i for i in jieba.cut(data,cut_all=False) if i not in [',','，','。','!','！','...','…','“','”','：','？','你','】','【','-','（', '）','、','2','；','《','》','我','他','看','这','了''｜','~',' ','\n','也','说','就','给','在','B','1','/','X','🎨','3','4','5','.....']]

for data in data0:
    data1+=qie(data)
# print(data1)
with open('data.txt','w',encoding='utf-8') as f:
    f.write(' '.join(data1))