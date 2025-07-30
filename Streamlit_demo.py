import streamlit as st
import datetime
import pandas as pd
import numpy as np

# 页面设置
st.set_page_config(page_title="Streamlit组件演示", layout="wide")
st.title("📊 Streamlit 组件演示大全")

# 生成示例文件内容
def generate_sample_file():
    df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
    return df.to_csv(index=False).encode("utf-8")

# 页面布局
col1, col2 = st.columns(2)

with col1:
    # ========== 按钮组件 ==========
    st.header("🕹️ 按钮组件")
    
    # 普通按钮
    if st.button("点击触发操作"):
        st.success("按钮点击成功！")
    
    # 下载按钮
    csv_data = generate_sample_file()
    st.download_button(
        label="下载示例CSV文件",
        data=csv_data,
        file_name="sample_data.csv",
        mime="text/csv"
    )

# with col2:
with col2:
    # ========== 文件上传组件 ==========
    st.header("📤 文件上传组件")
    uploaded_file = st.file_uploader("请选择CSV文件", type=["csv"])
    if uploaded_file:
        st.write(f"已上传文件：`{uploaded_file.name}`")
        st.write(f"文件大小：{uploaded_file.size // 1024} KB")

# ========== 选择组件 ==========
st.header("✅ 选择组件")
col3, col4 = st.columns(2)

with col3:
    # 复选框
    checkbox_val = st.checkbox("启用高级选项")
    if checkbox_val:
        st.write("🔧 高级功能已启用")

    # 单选框
    radio_val = st.radio(
        "选择数据源",
        options=["数据库", "API接口", "本地文件"],
        index=0
    )
    st.write(f"当前选择的数据源：**{radio_val}**")

with col4:
    # 多选框
    multiselect_val = st.multiselect(
        "选择分析维度",
        options=["时间", "地域", "用户类型", "产品类别"],
        default=["时间"]
    )
    st.write("已选维度：", multiselect_val)

    # 滑动条
    slider_val = st.slider(
        "选择价格区间",
        min_value=0, max_value=1000,
        value=(200, 800)
    )
    st.write(f"价格过滤区间：`{slider_val[0]} - {slider_val[1]}`")

# ========== 输入组件 ==========
st.header("⌨️ 输入组件")
col5, col6 = st.columns(2)

with col5:
    # 文本输入
    text_input_val = st.text_input("请输入用户名", placeholder="例如：user_123")
    if text_input_val:
        st.write(f"当前用户：`{text_input_val}`")

    # 数值输入
    number_input_val = st.number_input(
        "输入年龄",
        min_value=0, max_value=150,
        value=25, step=1
    )
    st.write(f"年龄验证通过：{number_input_val} 岁")

with col6:
    # 日期选择
    date_val = st.date_input(
        "选择预约日期",
        value=datetime.date.today(),
        min_value=datetime.date(2023, 1, 1)
    )
    st.write(f"预约日期：{date_val.strftime('%Y/%m/%d')}")

    # 时间选择
    time_val = st.time_input("选择预约时间")
    st.write(f"预约时间：{time_val.strftime('%H:%M')}")

# ========== 颜色选择组件 ==========
st.header("🎨 颜色选择组件")
selected_color = st.color_picker("选择主题色", "#00FF00")
st.write(f"当前颜色代码：{selected_color}")
st.write(f'<div style="height:50px; background:{selected_color}; border-radius:5px"></div>', 
        unsafe_allow_html=True)

# ========== 特殊选择器 ==========
st.header("🔍 特殊选择器")
select_slider_val = st.select_slider(
    "选择质量评级",
    options=["极差", "差", "一般", "良好", "优秀"],
    value="良好"
)
st.write(f"当前质量评级：⭐ {select_slider_val}")

# 下拉选择框
selectbox_val = st.selectbox(
    "选择数据格式",
    options=["CSV", "JSON", "Excel"],
    index=0
)
st.write(f"将导出为 **{selectbox_val}** 格式")

# ========== 监控组件 ==========
st.header("🎨 监控组件")
col7, col8, col9 = st.columns(3)
col7.metric("Temperature", "70 °F", "1.2 °F")
col8.metric("Wind", "9 mph", "-8%")
col9.metric("Humidity", "86%", "4%")


# 隐藏分隔线
st.markdown("---")
st.caption("© 2023 Streamlit组件演示 - 建议在本地运行查看完整交互")
