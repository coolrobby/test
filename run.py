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

# 初始化 session_state 来存储已选择的单词的状态
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = {}

# 随机抽取的单词显示区域（在主区域显示）
if input_words:
    word_list = input_words.splitlines()  # 将输入的单词列表转成列表

    # "随机抽取" 按钮在侧边栏
    if st.sidebar.button("随机抽取"):
        if len(word_list) >= 10:
            random_words = random.sample(word_list, 10)  # 从输入的单词中随机选择10个
        else:
            random_words = word_list  # 如果单词不足10个，则显示所有单词

        # 在主区域显示卡片布局，每行显示3张卡片
        st.subheader("随机抽取的单词：")
        cols = st.columns(3)  # 每行显示3个卡片

        for i, word in enumerate(random_words):
            col = cols[i % 3]  # 循环选择每列
            with col:
                # 判断当前单词是否被选中，若选中则显示“✔”
                is_selected = st.session_state.selected_words.get(word, False)

                # 显示单词卡片
                if is_selected:
                    icon = "✔"
                else:
                    icon = ""

                # 使用HTML和CSS为每个单词创建卡片，并添加点击事件来切换状态
                if st.button(f"{word} {icon}", key=f"word_{i}"):
                    # 切换单词的选择状态
                    st.session_state.selected_words[word] = not is_selected

    # 显示“分数”按钮
    if st.sidebar.button("查看分数"):
        # 计算已选中的单词数量
        selected_count = sum(st.session_state.selected_words.values())
        st.sidebar.write(f"已选中的卡片数量：{selected_count}")
else:
    st.sidebar.write("请输入单词列表并点击右侧的按钮进行随机选择。")
