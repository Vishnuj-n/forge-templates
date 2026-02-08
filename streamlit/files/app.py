#!/usr/bin/env python3
"""
Main Streamlit application.
"""
import streamlit as st


def main():
    """Main function for the Streamlit app."""
    st.set_page_config(page_title="My App", layout="centered")
    
    st.title("Welcome to Streamlit")
    
    st.write("This is a simple Streamlit application template.")
    
    # Example interactive widget
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}!")
    
    # Example button
    if st.button("Click me"):
        st.write("Button clicked!")


if __name__ == "__main__":
    main()
