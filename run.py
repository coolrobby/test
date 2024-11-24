import random
import time

# 计数器
if 'count' not in st.session_state:
    st.session_state.count = 0

# 显示计数器
def increment_counter():
    st.session_state.count += 1

# 随机选择10个单词
def get_random_words(word_list):
    return random.sample(word_list, 10) if len(word_list) >= 10 else word_list

# 倒计时函数
def start_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        st.session_state.timer = f"{mins:02d}:{secs:02d}"
        time.sleep(1)
        seconds -= 1
        if seconds == 0:
            st.session_state.timer = "Time's up!"
            break

# 页面标题
st.title("单词随机选择与倒计时")

# 用户输入单词列表
input_words = st.text_area("请输入单词列表，一行一个单词:")

# 将输入的单词转成列表
word_list = input_words.splitlines()

# 显示随机选择的单词
if st.button("随机选择10个单词"):
    if word_list:
        random_words = get_random_words(word_list)
        st.write("随机选择的单词:", random_words)
    else:
        st.write("请先输入单词列表。")

# 显示计数器
st.write(f"计数器: {st.session_state.count}")

# 增加计数器
if st.button("增加计数器"):
    increment_counter()

# 倒计时功能
minutes = st.number_input("设置倒计时时长 (分钟):", min_value=1, step=1)

if st.button("开始倒计时"):
    st.session_state.timer = "00:00"
    start_timer(minutes)
    st.write("倒计时:", st.session_state.timer)
