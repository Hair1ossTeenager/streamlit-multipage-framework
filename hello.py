import os
import streamlit as st
from pkg.menu import menu

if __name__ == '__main__':
    st.session_state.root_path = os.path.dirname(os.path.abspath(__file__))

    sub_menus = {
        'subGroup1': 'subgroup1',
        'subGroup2': 'subgroup2',
    }
    for key in menu.dynamic_pages().keys():
        if key not in sub_menus.values():
            sub_menus[key] = key

    # 选择页面子目录
    sub_menu = st.selectbox(
        '传送门',
        sub_menus.keys(),
    )
    # 设置默认页面子目录
    if 'sub_menu' not in st.session_state:
        st.session_state.sub_menu = menu.default_sub_menu()

    if sub_menu in sub_menus and sub_menu != st.session_state.sub_menu:
        st.session_state.sub_menu = sub_menus[sub_menu]

    menu.show_menu()
