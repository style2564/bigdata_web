import streamlit as st
from PIL import Image
import streamlit as st
import numpy as np

# 设置页面配置
st.set_page_config(page_title="NLP Demo", page_icon="🌐", layout="wide")

# 主页标题
st.title("欢迎使用 NLP Demo! 👋")

# 主体内容

# 定义一个函数来执行代码并返回结果
def run_code():
    # 创建一个随机的数组
    array = np.random.rand(3, 4)
    return array

# 展示代码块
code = '''
import numpy as np

# 创建一个随机的数组
array = np.random.rand(3, 4)
print(array)
'''

st.code(code, language='python')

# 在应用中添加一个按钮
if st.button('Run Code'):
    # 当按钮被点击时，执行代码并展示结果
    result = run_code()
    st.write('The result of the code execution is:')
    st.write(result)
    # st.session_state

import streamlit as st
import numpy as np

# 初始化session_state中的数据容器
if 'results' not in st.session_state:
    st.session_state['results'] = []

# 定义一个函数来添加结果到session_state
def add_result(result):
    st.session_state['results'].append(result)

# 第一个按钮和它的功能
if st.button('Run1 Code'):
    # 生成随机数组
    array1 = np.random.rand(3, 4)
    add_result(('Result of the first code execution:', array1))
for result in st.session_state['results']:
    st.write(result[0])
# 第二个按钮和它的功能
if st.button('Run2 Code'):
    # 生成随机数组
    array2 = np.random.rand(5, 6)
    add_result(('Result of the second code execution:', array2))
for result in st.session_state['results']:
    st.write(result[1])
import streamlit as st

# 假设你的HTML文件名为 'large_file.html'，并且它位于与Streamlit脚本相同的目录下
html_file_path = 'fig1.html'

# 创建一个超链接
st.markdown(f'<a href="{html_file_path}" target="_blank">打开大型HTML文件</a>', unsafe_allow_html=True)


