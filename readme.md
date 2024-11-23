# [dzx0217.github.io](https://dzx0217.github.io/)

## 目录结构

- 目录结构：
    - index.html：主页
		- onshow.html：主页具体内容
    - ppt_menu.html：PPT菜单
		- ppt_list.html：PPT列表
    - resume_menu.html：简历菜单
		- resume_list.html：简历列表
	- weekly_menu.html：周报菜单
		- weekly_list.html：周报列表
		- blog_menu.html：博客菜单

	- ppt：ppt文件夹
	- resume：简历文件夹
	- weekly：周报文件夹
    - statics：静态文件文件
		- icons: 图标文件夹
		- images: 图片文件夹
		- provement: 证明文件夹


## 日常流程

1. 在文件夹内添加新的PPT或简历或周报文件；
2. 在对应的list.html中添加新的条目(倒序添加在最新项)；
3. 提交到Github；

## 添加菜单

1. 添加菜单目录：新建一个add_menu.html(内容可以复制index.html的代码)
	- 修改对应代码部分：
	```html
	<!-- 侧边栏 -->
		<div class="sidebar" id="sidebar">
			<div class="sidebar-content">
				<!-- 侧边栏内容 -->
				<a href="index.html">/</a>
				<a href="ppt_menu.html">ppt</a>
				<a href="resume_menu.html">resume</a>
				<a href="weekly_menu.html">weekly</a>
				
				<a href="add_menu.html">添加菜单</a>
			
			</div>
		</div>
	```

	```html
	<!-- 主内容 -->
		<div class="content">
			<iframe src="add_list.html" frameborder="0" class="iframe-content"></iframe>
		</div>
	```
2. 添加列表：新建一个add_list.html，用于表示新加菜单的主要内容(内容可以复制ppt_list.html的代码)

3. 修改index.html、ppt_menu.html、resume_menu.html、weekly_menu.html
	- 对应代码部分：添加了某个菜单就添加某个菜单列表
	```html
	<!-- 侧边栏 -->
		<div class="sidebar" id="sidebar">
			<div class="sidebar-content">
				<!-- 侧边栏内容 -->
				<a href="index.html">/</a>
				<a href="ppt_menu.html">ppt</a>
				<a href="resume_menu.html">resume</a>
				<a href="weekly_menu.html">weekly</a>
				
				<a href="add_menu.html">添加菜单</a>
			
			</div>
		</div>
	```
4. 参照[日常流程](#日常流程)

5. 提交到Github；

## resume：[GPT协助写简历](https://chat.openai.com/share/02bf7548-77f1-4c1d-a1e1-4e3dd8ee494e)

