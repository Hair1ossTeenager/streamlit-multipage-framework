import os.path
import time

import streamlit as st


def dynamic_pages():
    if 'dynamic_pages' not in st.session_state:
        st.session_state.dynamic_pages = _dynamic_pages()
        time.sleep(1)
    return st.session_state.dynamic_pages


def _dynamic_pages():
    root_path = st.session_state.root_path
    source_files_path = os.path.join(root_path, 'src')
    dest_files_path = os.path.join(root_path, 'pages')

    # 生成软链接，动态生成子目录
    pages = dict()
    for dir in os.listdir(source_files_path):
        if not os.path.isdir(os.path.join(source_files_path, dir)):
            continue
        pages[dir] = []
        for file in os.listdir(os.path.join(source_files_path, dir)):
            if not os.path.isfile(os.path.join(source_files_path, dir, file)):
                continue
            if file.lower() == '.keep':
                continue
            pages[dir].append(file)
            if not os.path.islink(os.path.join(dest_files_path, file)):
                os.symlink(os.path.join(source_files_path, dir, file), os.path.join(dest_files_path, file))
    return pages


def default_sub_menu():
    return 'subgroup1'


def show_menu():
    # 展示不同的页面子目录
    sub_menu = default_sub_menu()
    if 'sub_menu' in st.session_state and st.session_state.sub_menu is not None:
        sub_menu = st.session_state.sub_menu
    link_pages(dynamic_pages()[sub_menu])


def link_pages(pages):
    pages.sort()
    st.sidebar.page_link('hello.py', label='home')
    for page in pages:
        st.sidebar.page_link('pages/' + page)


def menu_redirect():
    if "sub_menu" not in st.session_state or st.session_state.sub_menu is None:
        st.switch_page('hello.py')
    show_menu()
