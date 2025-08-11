import streamlit as st
import time
from datetime import datetime

# 初始化记录列表
if 'records' not in st.session_state:
    st.session_state.records = []
    
# 设置页面布局
st.set_page_config(layout="wide")

# 创建两列：左侧时间显示，右侧操作按钮
col1, col2 = st.columns([3, 1])

# 左侧时间显示区域
with col1:
    # 创建时间显示容器
    time_placeholder = st.empty()
    
    # 获取当前时间并显示
    current_time = datetime.now().strftime("%H:%M:%S")
    time_placeholder.markdown(f"<h1 style='text-align: center; font-size: 120px;'>{current_time}</h1>", 
                             unsafe_allow_html=True)

# 右侧操作按钮区域
with col2:
    st.header("喂食操作")
    
    # 四个喂食按钮
    if st.button("🍼 喂奶180ml", use_container_width=True):
        new_record = {
            'type': '喂奶',
            'amount': '180ml',
            'time': datetime.now().strftime("%H:%M:%S"),
            'timestamp': datetime.now().timestamp()
        }
        st.session_state.records.append(new_record)
        st.success("已记录喂奶180ml")
    
    if st.button("🥣 辅食20ml", use_container_width=True):
        new_record = {
            'type': '辅食',
            'amount': '20ml',
            'time': datetime.now().strftime("%H:%M:%S"),
            'timestamp': datetime.now().timestamp()
        }
        st.session_state.records.append(new_record)
        st.success("已记录辅食20ml")
    
    if st.button("💧 喂水30ml", use_container_width=True):
        new_record = {
            'type': '喂水',
            'amount': '30ml',
            'time': datetime.now().strftime("%H:%M:%S"),
            'timestamp': datetime.now().timestamp()
        }
        st.session_state.records.append(new_record)
        st.success("已记录喂水30ml")
    
    if st.button("🍪 小零食", use_container_width=True):
        new_record = {
            'type': '小零食',
            'amount': '少量',
            'time': datetime.now().strftime("%H:%M:%S"),
            'timestamp': datetime.now().timestamp()
        }
        st.session_state.records.append(new_record)
        st.success("已记录小零食")

# 记录显示区域
st.divider()
st.header("喂食记录")

# 按时间倒序显示记录
if not st.session_state.records:
    st.info("暂无记录，请添加喂食记录")
else:
    # 显示记录表格
    for i, record in enumerate(reversed(st.session_state.records)):
        cols = st.columns([1, 2, 2, 1])
        
        # 显示记录信息
        cols[0].markdown(f"**{len(st.session_state.records)-i}**")
        cols[1].write(f"**{record['type']}**")
        cols[2].write(f"{record['amount']} - {record['time']}")
        
        # 删除按钮
        if cols[3].button("删除", key=f"del_{i}"):
            # 计算实际索引（因为显示是倒序）
            actual_index = len(st.session_state.records) - i - 1
            del st.session_state.records[actual_index]
            st.rerun()
    
    # 添加清空按钮
    if st.button("清空所有记录", type="primary"):
        st.session_state.records = []
        st.success("所有记录已清空")
        time.sleep(0.5)
        st.rerun()

# 添加使用说明
st.divider()
st.markdown("### 使用说明")
st.info("""
1. 中央大字体显示当前时间（每秒自动更新）
2. 右侧按钮用于记录不同类型的喂食
3. 下方表格显示所有喂食记录（最新记录在最上方）
4. 每条记录右侧的删除按钮可删除该记录
5. 底部按钮可清空所有记录
""")

# 自动刷新时间显示
def refresh_time():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        time_placeholder.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{current_time}</h1>", 
                                 unsafe_allow_html=True)
        time.sleep(1)

# 使用Streamlit的自动刷新机制
if 'refresher' not in st.session_state:
    st.session_state.refresher = st.empty()

# 在Streamlit主线程中更新时间
if st.session_state.refresher:
    st.session_state.refresher.empty()
    st.experimental_rerun = False
    refresh_time()
