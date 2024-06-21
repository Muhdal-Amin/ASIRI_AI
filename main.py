import streamlit as st # type: ignore

# main - Code entry point
def main():
    # Creating Graphical User Interface.

    # Setting Page Configs.
    st.set_page_config(page_title="ASIRI AI", page_icon=":sparkles:")

    st.header("Welcome To ASIRI AI :sparkles:")
    st.markdown("***")
    st.subheader("How Can I Help you Today?")
    st.text("")
    st.text_input("Ask a question :")

    # Creating a Side Bar
    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your PDF files here")
        st.button("Run")
    


if __name__ == "__main__":
    main()