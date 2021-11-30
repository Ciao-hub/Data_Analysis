import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Map


from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB


df = pd.read_csv('���ַ�����.csv', encoding = 'gbk')  # https://docs.python.org/3/library/codecs.html#standard-encodings
df.head()


df.describe()


df.isna().sum()


df['����'].unique()    # unique ����SeriesΨһֵ


df['����'].fillna('δ֪', inplace = True)


df.isna().sum()


df['����'].unique()


df['����'].unique()


df['����'] = df['����'].str.replace('����','����')
df['����'].unique()


g = df.groupby('����')
df_region = g.count()['С��']
region = df_region.index.tolist()
count = df_region.values.tolist()
df_region.sort_values(ascending = False)


new = [x + '��' for x in region]   # Դ�ļ���û��'��',�޷���Map()�����ݶ�Ӧ
m = (
    Map()
    .add('',[list(z) for z in zip(new,count)],'����')
    .set_global_opts(
        title_opts = opts.TitleOpts(title = '�������������ַ��ֲ�'),
        visualmap_opts = opts.VisualMapOpts(max_ = 3000)
    )
)

m.load_javascript()


m.render_notebook()


df_price = g.mean()['�۸�(��Ԫ)']
df_price
