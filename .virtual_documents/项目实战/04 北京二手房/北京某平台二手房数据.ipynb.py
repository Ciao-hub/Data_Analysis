import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Map


from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB


df = pd.read_csv('二手房数据.csv', encoding = 'gbk')  # https://docs.python.org/3/library/codecs.html#standard-encodings
df.head()


df.describe()


df.isna().sum()


df['电梯'].unique()    # unique 给出Series唯一值


df['电梯'].fillna('未知', inplace = True)


df.isna().sum()


df['电梯'].unique()


df['朝向'].unique()


df['朝向'] = df['朝向'].str.replace('南西','西南')
df['朝向'].unique()


g = df.groupby('市区')
df_region = g.count()['小区']
region = df_region.index.tolist()
count = df_region.values.tolist()
df_region.sort_values(ascending = False)


new = [x + '区' for x in region]   # 源文件里没有'区',无法和Map()里数据对应
m = (
    Map()
    .add('',[list(z) for z in zip(new,count)],'北京')
    .set_global_opts(
        title_opts = opts.TitleOpts(title = '北京各城区二手房分布'),
        visualmap_opts = opts.VisualMapOpts(max_ = 3000)
    )
)

m.load_javascript()


m.render_notebook()


df_price = g.mean()['价格(万元)']
df_price
