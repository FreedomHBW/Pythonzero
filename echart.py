'''
coder:Zero Net
date:2019/3/23
'''
from pyecharts import Bar, Line, Grid,Pie,Page,Overlap

attr1 = ['甲','乙','丙','丁','戊']
v1 = [ 0.303,0.311,0.366,0.320,0.312]
bar3 = Bar("团队与回购率分布",title_pos='17%')
bar3.add("", attr1, v1, xaxis_interval=0,)


attr = ['2018年1月', '2018年2月', '2018年3月', '2018年4月']
v3 = [15258820, 16482007, 18620273, 16341094]
v4 = ['', 8.02, 12.97, -12.24]
bar1 = Bar("主营收入统计",title_pos="46%")
bar1.add("总主营收入", attr, v3, legend_top='10%')
line1 = Line()
line1.add("月环比增长率", attr, v4,line_color='#eee', legend_top='10%')

overlap = Overlap()
overlap.add(bar1)
overlap.add(line1,is_add_yaxis=True ,yaxis_index=1, )


attr = [ 'A','B', 'C', 'D', 'E']
v2 = [0.29825, 0.315454545, 0.36025,0.2925,0.340625]


line1 = Line("产品回购率情况",title_pos="75%",title_top='2%')
line1.add("回购率", attr, v2, legend_top='15%',line_width=3,line_color='#50a3ba',legend_pos='77%',is_visualmap=True,visual_range=[400000,4000000],visual_range_color=['#eac763', '#d94e5d'],visual_pos='35%')



attr = ['A','B','C','D','E']
v1 = [13335837,14640323,12448656,14978269,11299109]
pie = Pie("产品销售额分布图", title_pos="75%",title_text_size=20)
pie.add(
    "",
    attr,
    v1,
    radius=[45, 65],
    center=[75, 60],
    legend_pos="81%",
    legend_top='30%',
    legend_text_size=5,
    legend_orient="vertical"

)


from pyecharts import Gauge
page = Page()
gauge = Gauge("KPI完成率",title_pos='17%')
gauge.add("业务指标", "完成率", 26.7,radius= ['110%'],angle_range=[200, -20],
    scale_range=[0, 100],
    is_legend_show=False,
    center=[19, 70])



from pyecharts import Map

value = [3854501, 3296547, 3235630, 3120583, 3063284, 2965055, 2913890,2786551,2742750,2706805,2551132,2380781,2085868,2061841,1991714,1977841,1918235,1864635,1815421,1683391,1602487,1560296,1555506,1429737,1365970,1362162,1174981,1142008,1092921,1047053,990888,865084,496646]
attr = [
    "云南","宁夏","江西","安徽","青海","浙江","广东","陕西","山东","河南","甘肃","海南","四川","湖南","上海","福建","新疆","吉林","黑龙江","河北","内蒙古","西藏","山西","江苏","香港","辽宁","贵州","重庆","广西","澳门","天津","湖北","北京"
    ]
map = Map("主营收入地域分布", width=1200, height=600,title_pos='45%')
map.add(
    "主营收入",
    attr,
    value,
    maptype="china",
    visual_range=[400000,4000000],
    visual_text_color="#000",visual_pos='60%',is_legend_show=False,is_visualmap=True)



attr = ['甲','乙','丙','丁','戊']
v1 = [14266931,16213786,9622845,19596171,7002461]
pie4 = Pie("团队贡献率", title_pos='47%', width=900)
pie4.add(
    "商品B",
    attr,
    v1,
    center=[50, 50],
    is_random=True,
    radius=[30, 75],
    rosetype="area",
    is_legend_show=False,
    is_label_show=True,
)



pie6 = Pie("主营收入", title_pos='15%', width=900,title_text_size=35,title_top='25%')
pie7= Pie("66.70 百万", title_pos='11%', width=900,title_text_size=55,title_top='50%',title_color='#50a3ba')
pie8 = Pie("阿宝可视化数据", title_pos='75%', width=900,title_text_size=55,title_top='35%',title_color='#50a3ba')
grid1 = Grid(height=260, width=1900)
grid1.add(overlap,grid_left="60%", grid_right="60%",grid_top='30%',grid_bottom='10%')
grid1.add(pie6,  grid_right="70%")
grid1.add(pie7,  grid_right="70%")
grid1.add(pie)
grid1.use_theme('dark')

grid2 = Grid(height=300, width=1900)
grid2.add(line1,grid_left="70%",grid_top='30%',grid_bottom='10%')
grid2.add(gauge,grid_left="75%", grid_right="10%")
grid2.add(map, grid_right="70%")
grid2.use_theme('dark')

grid3 = Grid(height=300, width=1900)
grid3.add(bar3,grid_left="7%", grid_right="69%")
grid3.add(pie4,grid_left="60%", grid_right="60%")
grid3.add(pie8)
grid3.use_theme('dark')

page.add(grid1)
page.add(grid2)
page.add(grid3)

page.render()