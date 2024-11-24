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

            # 将“对”和“错”按钮放在同一行，确保按钮居中
            col1, col2 = col.columns([1, 1])  # 创建两个子列，宽度相等
            with col1:
                col1_button = st.button("对", key=f"correct_{i}", on_click=lambda i=i: mark_correct(i))
            with col2:
                col2_button = st.button("错", key=f"wrong_{i}", on_click=lambda i=i: mark_wrong(i))

else:
    st.sidebar.write("请输入单词列表并点击右侧的按钮进行随机选择。")
