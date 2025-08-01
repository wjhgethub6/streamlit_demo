import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import time
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="高级Streamlit模板",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
def inject_custom_css():
    custom_css = """
    <style>
        /* 整体页面样式 */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f6;
        }
        
        /* 主容器 */
        .main {
            background: linear-gradient(145deg, #ffffff, #f0f7ff);
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            padding: 2rem;
            margin: 1rem;
        }
        
        /* 标题样式 */
        h1 {
            color: #2563eb;
            border-bottom: 3px solid #3b82f6;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            font-weight: 700;
        }
        
        h2 {
            color: #1e40af;
            margin-top: 1.8rem;
            margin-bottom: 1rem;
            font-weight: 600;
        }
        
        h3 {
            color: #3b82f6;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
            font-weight: 500;
        }
        
        /* 卡片样式 */
        .card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        }
        
        /* 按钮样式 */
        .stButton>button {
            background: linear-gradient(to right, #4f46e5, #7c3aed);
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.5rem 1.5rem;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .stButton>button:hover {
            background: linear-gradient(to right, #4338ca, #6d28d9);
            transform: scale(1.05);
        }
        
        /* 输入框样式 */
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #d1d5db;
            padding: 0.75rem;
        }
        
        /* 滑块样式 */
        .stSlider .thumb {
            background: #4f46e5 !important;
        }
        
        .stSlider .track {
            background: #c7d2fe !important;
        }
        
        /* 选择框样式 */
        .stSelectbox>div>div>div {
            border-radius: 8px;
            border: 1px solid #d1d5db;
        }
        
        /* 数据表格样式 */
        .stDataFrame {
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        /* 进度条样式 */
        .stProgress>div>div>div {
            background: linear-gradient(to right, #60a5fa, #3b82f6);
        }
        
        /* 侧边栏样式 */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e293b, #0f172a);
            color: white;
            border-radius: 0 15px 15px 0;
            padding: 1.5rem;
            box-shadow: 5px 0 15px rgba(0,0,0,0.1);
        }
        
        [data-testid="stSidebar"] .stMarkdown {
            color: #e2e8f0;
        }
        
        [data-testid="stSidebar"] .stMarkdown h1 {
            color: #93c5fd;
            border-bottom: 2px solid #3b82f6;
        }
        
        /* 标签页样式 */
        [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        [data-baseweb="tab"] {
            background: #e0f2fe !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            margin: 0 5px !important;
            transition: all 0.3s !important;
        }
        
        [data-baseweb="tab"]:hover {
            background: #bae6fd !important;
        }
        
        [aria-selected="true"] {
            background: #38bdf8 !important;
            color: white !important;
            font-weight: bold;
        }
        
        /* 页脚样式 */
        .footer {
            text-align: center;
            padding: 1.5rem;
            color: #64748b;
            font-size: 0.9rem;
            margin-top: 2rem;
            border-top: 1px solid #e2e8f0;
        }
        
        /* 响应式调整 */
        @media (max-width: 768px) {
            .main {
                padding: 1rem;
                margin: 0.5rem;
            }
            
            [data-testid="stSidebar"] {
                padding: 1rem;
            }
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# 注入自定义CSS
inject_custom_css()

# 侧边栏
with st.sidebar:
    st.title("控制面板")
    st.subheader("应用设置")
    
    theme = st.selectbox("选择主题", ["Light", "Dark", "System"])
    animation = st.checkbox("启用动画", True)
    
    st.divider()
    
    st.subheader("用户设置")
    username = st.text_input("用户名", "streamlit_user")
    email = st.text_input("邮箱", "user@example.com")
    
    st.divider()
    
    st.subheader("关于")
    st.info("这是一个高级Streamlit模板，展示了各种组件和自定义样式。")
    st.caption("© 2023 Streamlit高级模板 | 版本 1.0.0")

# 主内容区
st.title("🚀 Streamlit高级样式模板")
st.subheader("包含各种常用组件的现代化UI设计")

# 标签页
tab1, tab2, tab3, tab4 = st.tabs(["仪表盘", "数据可视化", "表单组件", "高级功能"])

with tab1:
    st.header("应用仪表盘")
    
    # 指标卡片
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="card">
            <h3>用户总数</h3>
            <h1>1,248</h1>
            <p style="color: #10b981;">↑ 12.5% 本月增长</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>活跃用户</h3>
            <h1>842</h1>
            <p style="color: #10b981;">↑ 8.3% 本月增长</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>留存率</h3>
            <h1>78.2%</h1>
            <p style="color: #ef4444;">↓ 2.1% 本月下降</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="card">
            <h3>平均使用时长</h3>
            <h1>12.7 min</h1>
            <p style="color: #10b981;">↑ 3.4% 本月增长</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 图表区域
    st.subheader("用户增长趋势")
    chart_col1, chart_col2 = st.columns([3, 1])
    
    with chart_col1:
        # 生成示例数据
        dates = pd.date_range(start="2023-01-01", end="2023-06-30", freq='D')
        values = np.random.randn(len(dates)).cumsum() + 50
        
        # 使用Plotly创建交互式图表
        fig = px.line(
            x=dates,
            y=values,
            labels={'x': '日期', 'y': '用户数'},
            title='2023年上半年用户增长趋势'
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='#f0f0f0'),
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with chart_col2:
        # 饼图
        st.subheader("用户分布")
        data = pd.DataFrame({
            'Category': ['移动端', '桌面端', '平板'],
            'Value': [65, 25, 10]
        })
        fig = px.pie(
            data, 
            names='Category', 
            values='Value',
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        fig.update_layout(showlegend=False, height=250, margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, use_container_width=True)

# 数据可视化标签页
with tab2:
    st.header("数据可视化")
    
    # 生成示例数据
    np.random.seed(42)
    data = pd.DataFrame({
        '日期': pd.date_range('2023-01-01', periods=100),
        '销售额': np.random.randint(100, 1000, size=100).cumsum(),
        '利润': np.random.randint(50, 500, size=100).cumsum(),
        '类别': np.random.choice(['A', 'B', 'C', 'D'], 100),
        '地区': np.random.choice(['东部', '西部', '北部', '南部'], 100)
    })
    
    # 数据筛选器
    col1, col2 = st.columns(2)
    with col1:
        category = st.multiselect("选择类别", options=data['类别'].unique(), default=data['类别'].unique())
    with col2:
        region = st.multiselect("选择地区", options=data['地区'].unique(), default=data['地区'].unique())
    
    # 应用筛选
    filtered_data = data[
        (data['类别'].isin(category)) & 
        (data['地区'].isin(region))
    ]
    
    # 显示数据表格
    st.subheader("数据表格")
    st.dataframe(filtered_data.style.highlight_max(axis=0, color='#d1fae5'), height=250)
    
    # 图表展示
    st.subheader("数据图表")
    
    chart_type = st.radio("选择图表类型", 
                         ["柱状图", "折线图", "散点图", "面积图"], 
                         horizontal=True)
    
    if chart_type == "柱状图":
        fig = px.bar(
            filtered_data, 
            x='日期', 
            y='销售额',
            color='类别',
            barmode='group',
            title='销售额按类别分布'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "折线图":
        fig = px.line(
            filtered_data, 
            x='日期', 
            y=['销售额', '利润'],
            title='销售额与利润趋势'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "散点图":
        fig = px.scatter(
            filtered_data, 
            x='销售额', 
            y='利润',
            color='类别',
            size='销售额',
            hover_name='地区',
            title='销售额与利润关系'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    elif chart_type == "面积图":
        fig = px.area(
            filtered_data, 
            x='日期', 
            y='销售额',
            color='地区',
            title='按地区划分的销售额'
        )
        st.plotly_chart(fig, use_container_width=True)

# 表单组件标签页
with tab3:
    st.header("表单组件示例")
    
    with st.form("user_form"):
        st.subheader("用户信息")
        
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("名字", placeholder="请输入您的名字")
        with col2:
            last_name = st.text_input("姓氏", placeholder="请输入您的姓氏")
        
        email = st.text_input("电子邮箱", placeholder="example@domain.com")
        
        col3, col4 = st.columns(2)
        with col3:
            age = st.slider("年龄", min_value=18, max_value=100, value=30)
        with col4:
            gender = st.radio("性别", ["男", "女", "其他"])
        
        occupation = st.selectbox("职业", [
            "学生", "工程师", "设计师", "产品经理", "数据分析师", "其他"
        ])
        
        interests = st.multiselect("兴趣爱好", [
            "编程", "阅读", "旅行", "运动", "音乐", "美食", "电影"
        ])
        
        bio = st.text_area("个人简介", placeholder="简单介绍一下自己...", height=100)
        
        agreement = st.checkbox("我同意条款和条件", value=False)
        
        submitted = st.form_submit_button("提交信息")
        
        if submitted:
            if not first_name or not last_name or not email:
                st.error("请填写必填字段！")
            elif not agreement:
                st.warning("请同意条款和条件")
            else:
                st.success("表单提交成功！")
                st.balloons()
                
                # 显示提交的数据
                st.subheader("提交的信息:")
                user_data = {
                    "姓名": f"{first_name} {last_name}",
                    "邮箱": email,
                    "年龄": age,
                    "性别": gender,
                    "职业": occupation,
                    "兴趣爱好": ", ".join(interests),
                    "个人简介": bio
                }
                st.json(user_data)

# 高级功能标签页
with tab4:
    st.header("高级功能示例")
    
    # 文件上传
    st.subheader("文件上传")
    uploaded_file = st.file_uploader("上传CSV文件", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"成功上传文件: {uploaded_file.name}")
        st.write("数据预览:")
        st.dataframe(df.head())
    
    st.divider()
    
    # 进度条和状态
    st.subheader("进度指示器")
    if st.button("启动处理"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(1, 101):
            progress_bar.progress(i)
            status_text.text(f"处理中... {i}%")
            time.sleep(0.03)
        
        status_text.text("处理完成！")
        st.success("任务已成功完成")
    
    st.divider()
    
    # 日期时间选择器
    st.subheader("日期时间选择")
    col1, col2 = st.columns(2)
    with col1:
        appointment_date = st.date_input("预约日期", datetime.today())
    with col2:
        appointment_time = st.time_input("预约时间", datetime.now().time())
    
    st.info(f"您预约的时间是: {appointment_date} {appointment_time.strftime('%H:%M')}")
    
    st.divider()
    
    # 可扩展区域
    st.subheader("可扩展内容")
    with st.expander("点击查看详细信息"):
        st.write("这里是隐藏的详细信息。")
        st.image("https://via.placeholder.com/600x200?text=详细信息图像", use_column_width=True)
        st.write("""
        - 项目1: 描述内容...
        - 项目2: 描述内容...
        - 项目3: 描述内容...
        """)
    
    # 工具提示
    st.divider()
    st.subheader("工具提示示例")
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("按钮 A", help="这是按钮A的工具提示")
        with col2:
            st.button("按钮 B", help="这是按钮B的工具提示")
        with col3:
            st.button("按钮 C", help="这是按钮C的工具提示")

# 页脚
st.markdown("""
<div class="footer">
    <p>高级Streamlit模板 | 使用Python和Streamlit构建 | © 2023</p>
</div>
""", unsafe_allow_html=True)