import streamlit as st
import time

# Define your rag function here
def rag(query):
    # Simulate a long-running process
    time.sleep(3)  # Remove this line and add your actual logic
    return f"Result for: {query}"

def main():
    # Streamlit app
    st.title("RAG Function Interface")

    # Input box
    query = st.text_input("Enter your query:")

    # Ask button
    if st.button("Ask"):
        # Show a loading spinner
        with st.spinner('Processing...'):
            # Call the rag function with the input query
            result = rag(query)
            # Display the result
            st.success(result)

if __name__ == "__main__":
    main()
