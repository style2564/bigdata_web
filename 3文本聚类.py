import streamlit as st
from pathlib import Path
import base64
import pandas as pd
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans



def process_df(df):
    # 读取停用词表
    stopwords = set()
    with open('C:/Users/Administrator/Desktop/nlpforall/cn_text_classifier_master/static/dict.txt', 'r', encoding='utf-8') as f:
        for word in f:
            stopwords.add(word.strip())
    with open('C:/Users/Administrator/Desktop/nlpforall/cn_text_classifier_master/static/stop_words.txt', 'r', encoding='utf-8') as f:
        for word in f:
            stopwords.add(word.strip())
    with open('C:/Users/Administrator/Desktop/nlpforall/cn_text_classifier_master/static/stopwords.txt', 'r', encoding='utf-8') as f:
        for word in f:
            stopwords.add(word.strip())

    # 定义分词函数
    def tokenize(text):
        words = jieba.cut(text)
        return [word for word in words if word not in stopwords]

    # 对 content 列应用分词函数
    df['content'] = df['content'].apply(tokenize)

    return df

def merge_lists_to_string(df):
    ale = []
    for i in df['content']:
        ale.append(" ".join(i))
    df['content'] = ale
    return df

def process_plot(x,y):
    lis = []
    for i in range(len(x)):
        lis1 = []
        for j in range(len(x[i])):
            lis1.append([x[i][j],y[i][j]])
        lis.append(lis1)
    options = {
        "title": {"text": "聚类结果散点图"},
        "xAxis": {},
        "yAxis": {},
        "series": []
    }
    colors = ["#FFCC99", "#99CCFF", "#99FF99", "#FF99CC", "#CCCCFF", "#FFFF99", "#FF9999", "#99FFFF", "#CC99FF", "#CCFF99"]
    # 遍历 data_list 中的每个子列表，为每个子列表创建一个 series 并设置颜色
    for i, data in enumerate(lis):
        series = {
            "symbolSize": 20,
            "data": data,
            "type": "scatter",
            "itemStyle": {"color": colors[i]}  # 设置不同的颜色
        }
        options["series"].append(series)
    with tab4:
        stqdm(time.sleep(13.82))
        st_echarts(options=options, height="500px",width="900px")
    return lis

# 设置页面配置
st.set_page_config(
    page_title="NLP Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.example.com/help",
        "Report a bug": "https://www.example.com/bug",
        "About": "This is an **extremely** cool NLP app made by Streamlit. Source code: https://github.com/example/nlp-app",
    },
)

# 获取静态文件夹的路径
static_dir = Path(st.__path__[0]) / "static"

# 构造图片路径
image_path = static_dir / "image" / "cluser.svg"



# 定义 CSS 样式
css = """
<style>
    .container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background-color: #f0f0f0;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }

    .title {
        font-size: 36px;
        font-weight: bold;
        color: #333333;
        margin-right: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }

    .image {
        width: 50px;
        height: 50px;
        object-fit: contain;
    }
</style>
"""

# 构造 HTML 内容
html_content = f"""
{css}
<div class="container">
    <h1 class="title">NLP Agent demo3 - 文本聚类</h1>
    <img class="image" src="data:image/svg+xml;base64,{image_data}">
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)

st.divider()

st.sidebar.subheader("文本聚类 😚")
st.sidebar.info("这里是文本聚类功能的说明...")

st.sidebar.subheader("高级选项")
model = st.sidebar.radio("你想用什么行业模型进行该任务",[":rainbow[Kmeans] :large_orange_diamond:", "***DBSCAN*** :large_orange_diamond:", "Birch :large_orange_diamond:"])

# 上传CSV文件
uploaded_file = st.file_uploader("在这里上传CSV文件,每一行表示一个文本个体")
if uploaded_file:
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["原始表格", "处理后表格","聚类后表格", "聚类散点图","不同簇的主题词"])
    if model == ":rainbow[Kmeans] :large_orange_diamond:":
        number = int(st.sidebar.number_input("输入你想要的聚类簇数"))
        # 读取CSV文件并显示为DataFrame
        if number:
            with tab1:
                df = pd.read_csv(uploaded_file,encoding='gbk')
                st.dataframe(df,width=900)
            with tab2:
                process1_df =  process_df(df)
                st.dataframe(process1_df ,width=900)
            with tab3:
                process2_df = merge_lists_to_string(process1_df)
                cluster_result,x,y = Kmeans_Text_Classify(df, number)
                st.dataframe(cluster_result, width = 900)
            process_plot(x,y)
    elif model == "***DBSCAN*** :large_orange_diamond:":
        # 读取CSV文件并显示为DataFrame
        with tab1:
            df = pd.read_csv(uploaded_file,encoding='utf-8')
            st.dataframe(df,width=900)
        with tab2:
            process1_df =  process_df(df)
            st.dataframe(process1_df ,width=900)
        with tab3:
            process2_df = merge_lists_to_string(process1_df)
            cluster_result,x,y = DBSCAN_Text_Classify(df, 3)
            st.dataframe(cluster_result, width = 900)
        process_plot(x,y)
    else:
        number = int(st.sidebar.number_input("输入你想要的聚类簇数"))
        # 读取CSV文件并显示为DataFrame
        if number:
            with tab1:
                df = pd.read_csv(uploaded_file,encoding='gbk')
                st.dataframe(df,width=900)
            with tab2:
                process1_df =  process_df(df)
                st.dataframe(process1_df ,width=900)
            with tab3:
                process2_df = merge_lists_to_string(process1_df)
                cluster_result,x,y = Birch_Text_Classify(df, number)
                st.dataframe(cluster_result, width = 900)
            process_plot(x,y)
        