import streamlit as st
from pkg.menu import menu


def show_demo1():
    st.title("Demo1")


if __name__ == '__main__':
    menu.show_menu()
    show_demo1()