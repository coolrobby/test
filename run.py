import streamlit as st
import random

# 页面标题
st.title("单词随机选择器")

# 布局：左侧为输入框，右侧为显示随机单词区域
col1, col2 = st.columns([1, 2])  # 设置两个列，比例1:2，输入框在左，显示区域在右

# 在左侧列显示输入框
with col1:
    input_words = st.text_area("请输入单词列表，一行一个单词:", height=300)

# 随机选择的单词显示区域（右侧列）
with col2:
    if input_words:
        word_list = input_words.splitlines()  # 将输入的单词列表转成列表
        if st.button("随机选择10个单词"):
            if len(word_list) >= 10:
                random_words = random.sample(word_list, 10)  # 从输入的单词中随机选择10个
            else:
                random_words = word_list  # 如果单词不足10个，则显示所有单词
            # 显示随机选择的单词，使用大字号
            st.write(f"### 随机选择的单词：")
            st.markdown(f"<h1 style='text-align: center;'>{', '.join(random_words)}</h1>", unsafe_allow_html=True)
    else:
        st.write("请输入单词列表并点击按钮进行随机选择。")
