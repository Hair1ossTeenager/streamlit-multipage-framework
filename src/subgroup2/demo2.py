import streamlit as st
from pkg.menu import menu


def show_demo2():
    st.title("Demo2")


if __name__ == '__main__':
    menu.show_menu()
    show_demo2()