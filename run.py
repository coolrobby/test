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

# 初始化单词卡状态
if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = {}

# 初始化抽取的单词列表
if 'random_words' not in st.session_state:
    st.session_state.random_words = []

# 随机抽取的单词显示区域（在主区域显示）
if input_words:
    word_list = input_words.splitlines()  # 将输入的单词列表转成列表

    # "随机抽取" 按钮在侧边栏
    if st.sidebar.button("随机抽取"):
        if len(word_list) >= 10:
            st.session_state.random_words = random.sample(word_list, 10)  # 从输入的单词中随机选择10个
        else:
            st.session_state.random_words = word_list  # 如果单词不足10个，则显示所有单词

    # 显示已抽取的单词
    if st.session_state.random_words:
        st.subheader("随机抽取的单词：")
        cols = st.columns(3)  # 每行显示3个卡片

        for i, word in enumerate(st.session_state.random_words):
            col = cols[i % 3]  # 循环选择每列
            with col:
                # 使用HTML和CSS为每个单词创建卡片
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ddd; padding: 20px; margin: 10px; text-align: center;
                    border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); font-size:{font_size}px;">
                        <strong>{word}</strong>
                        <div style="margin-top: 10px;">{st.session_state.correct_answers.get(i, '')}</div>
                    </div>
                    """, unsafe_allow_html=True
                )

                # 在同一行显示 "对" 和 "错" 按钮，并垂直居中
                col.button("对", key=f"correct_{i}", on_click=lambda i=i: mark_correct(i))
                col.button("错", key=f"wrong_{i}", on_click=lambda i=i: mark_wrong(i))

else:
    st.sidebar.write("请输入单词列表并点击右侧的按钮进行随机选择。")

# 处理“对”按钮点击
def mark_correct(index):
    st.session_state.correct_answers[index] = '✔'  # 标记为对

# 处理“错”按钮点击
def mark_wrong(index):
    st.session_state.correct_answers[index] = 'X'  # 标记为错
