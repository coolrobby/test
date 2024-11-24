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

# 创建一个状态来保存每个卡片的选择状态
if 'selected' not in st.session_state:
    st.session_state.selected = {}

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
                # 点击卡片后，标记状态
                is_selected = st.session_state.selected.get(word, False)
                
                # 使用HTML和CSS为每个单词创建卡片，并根据选择状态显示“✔”
                st.markdown(
                    f"""
                    <div style="border: 1px solid #ddd; padding: 20px; margin: 10px; text-align: center;
                    border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); font-size:{font_size}px;
                    cursor: pointer;" onclick="window.parent.document.getElementById('{word}').click();">
                        <strong>{word} {'✔' if is_selected else ''}</strong>
                    </div>
                    <button id="{word}" style="display:none;" onclick="window.parent.document.getElementById('{word}').click();">
                    </button>
                    """, unsafe_allow_html=True

                )
                # 更新点击状态
                if st.button(f"选择{word}", key=f"select_{word}"):
                    st.session_state.selected[word] = not is_selected

    # “分数”按钮，点击后显示选中卡片的数量
    if st.sidebar.button("分数"):
        score = sum(1 for selected in st.session_state.selected.values() if selected)
        st.sidebar.write(f"已选择的卡片数量: {score}")

else:
    st.sidebar.write("请输入单词列表并点击右侧的按钮进行随机选择。")
