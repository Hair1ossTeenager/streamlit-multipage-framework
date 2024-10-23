# streamlit multipage framework

- [streamlit](#streamlit)
  - [项目结构](#项目结构)
  - [增加子页面步骤](#增加子页面步骤)
  - [删除或重命名子页面步骤](#删除或重命名子页面步骤)
  - [常见问题](#常见问题)

### 项目结构
```
|- README.md
|- requirements.txt      // python 依赖包，所有页面依赖包需要添加到此文件
|- hello.py              // streamlit 首页
|- pages                 // streamlit 子目录，子页面动态生成，不要提交任何代码在此目录
|- pkg                   // 非页面代码
|  |-- menu              // 页面目录相关，公共
|- src                   // 开发目录，各组子页面放到此目录下的子目录中
|  |-- subgroup1         // 页面子目录1
|  |-- subgroup2         // 页面子目录2
```

- 启动 streamlit
> streamlit run hello.py

### 增加子页面步骤
1. 在 `src` 目录下新建目录 `default`， 在 `src/default` 目录下新建一个 `.py` 文件，如 `test.py`，在主程中引用 `menu_redirect()` 方法
```python
import streamlit as st
from pkg.menu import menu


def test():
    st.title('测试')


if __name__ == '__main__':
    menu.menu_redirect()
    test()
```

### 删除或重命名子页面步骤
1. 删除 `pages` 目录下所有的 python 文件
2. 删除 `src` 目录下不需要的文件，例如 `src/default/test.py` 或将 `src/default/test.py` 文件重命名

### 常见问题
1. 启动后页面一直空白，命令行一直报错，该如何解决？
> 删除 `pages` 下所有 `.py` 结尾的文件
