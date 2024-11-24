import streamlit as st
import random

# 设置页面标题
st.title("单词随机选择器")

# 配置侧边栏
st.sidebar.title("操作面板")

# 输入框放在侧边栏
input_words = st.sidebar.text_area("请输入单词列表，一行一个单词:", height=300)

# 字体大小调节：使用 Slider 控件
font_size = st.sidebar.slider("选择显示字体大小", min_value=10, max_value=50, value=20, step=1)

# 随机抽取的单词显示区域（在主区域显示）
if input_words:
    word_list = input_words.splitlines()  # 将输入的单词列表转成列表

    # "随机抽取" 按钮在侧边栏
    if st.sidebar.button("随机抽取"):
        if len(word_list) >= 10:
            random_words = random.sample(word_list, 10)  # 从输入的单词中随机选择10个
        else:
            random_words = word_list  # 如果单词不足10个，则显示所有单词

        # 在主区域显示有序列表（从1开始），字体大小通过 Markdown 设置
        st.subheader("随机抽取的单词：")
        st.write("有序列表：")
        for i, word in enumerate(random_words, 1):
            # 使用 Markdown 和 HTML 设置动态字体大小
            st.markdown(f"<p style='font-size:{font_size}px'>{i}. {word}</p>", unsafe_allow_html=True)
else:
    st.sidebar.write("请输入单词列表并点击右侧的按钮进行随机选择。")
