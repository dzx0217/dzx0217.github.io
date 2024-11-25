# [dzx0217.github.io](https://dzx0217.github.io/)

## 目录结构

- index.html：主页, 侧边栏的基本框架；
- onshow.html：主页展示的主内容；
- contents：主内容；
	- ppt：ppt文件夹；
	  - RevealJS：在线展示ppt，以html的形式；
	  - Template：ppt文件模板；
	- resume：简历文件夹；
	- weekly：周报文件夹；
- index: 索引文件夹；
	- ppt_list.html：ppt列表；
	- resume_list.html：简历列表；
	- weekly_list.html：周报列表；
- statics:静态文件；
    - icon：图标文件夹；
	- image：图片文件夹；
	- provement: 证明文件；


## 日常流程

1. 更新内容：在contents文件夹内添加新的PPT或简历或周报文件；
2. 更新索引：在index文件夹内的对应list.html中添加新的条目(倒序添加在最新项)；
3. 提交：提交到Github；

## 添加菜单

1. 在index.html中的侧边栏添加新的菜单按钮：
```html
<!-- 侧边栏 -->
		<div class="sidebar" id="sidebar">
			<div class="sidebar-content">
				<!-- 侧边栏内容 -->
				<button class="sidebar_btn" title="home" onclick="changeContent('onshow.html')"><img
						src="statics/icons/home.png" alt="home"></button>
				<button class="sidebar_btn" title="ppt" onclick="changeContent('index/ppt_list.html')"><img
						src="statics/icons/ppt.png" alt="ppt"></button>
				<button class="sidebar_btn" title="resume" onclick="changeContent('index/resume_list.html')"><img
						src="statics/icons/resume.png" alt="resume"></button>
				<button class="sidebar_btn" title="weekly" onclick="changeContent('index/weekly_list.html')"><img
						src="statics/icons/weekly.png" alt="weekly"></button>
			</div>
		</div>
```

添加菜单按钮
```html
<button class="sidebar_btn" title="weekly" onclick="changeContent('index/add_list.html')"><img
						src="statics/icons/add.png" alt="add"></button>
```

2. 在[https://www.iconfont.cn/](https://www.iconfont.cn/)下载对应新添加菜单的icon图片，保存在statics/icons下
3. 在index文件夹内添加新的add_list.html文件；
4. 参照[日常流程](#日常流程)

5. 提交到Github；

## resume：[GPT协助写简历](https://chat.openai.com/share/02bf7548-77f1-4c1d-a1e1-4e3dd8ee494e)