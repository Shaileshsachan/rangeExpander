import streamlit as st
from src.expand_ranges import expand_ranges

st.set_page_config(page_title="Range Expander", page_icon="🔢")

st.title("Range Expander Utility (Stages 1–7)")

# User input
input_str = st.text_input("Enter range string:", "1-3, 5*2, 10..6")

col1, col2 = st.columns(2)

with col1:
    dedup = st.checkbox("Enable Deduplication", value=True)

with col2:
    output_format = st.selectbox("Output Format", ["list", "csv", "set"])

step_delimiter = st.text_input("Step Delimiter (e.g. ':')", ":")

range_delimiters = st.multiselect(
    "Range Delimiters",
    options=["-", "..", "to", "~"],
    default=["-", "..", "to", "~"]
)

if st.button("Expand Ranges"):
    try:
        result = expand_ranges(
            input_str=input_str,
            unique_sorted_output=dedup,
            range_delimiters=range_delimiters,
            step_delimiter=step_delimiter,
            output_format=output_format
        )

        st.success("Expansion Successful")
        st.code(result, language="python")

        with st.expander("Configuration"):
            st.write("**Input:**", input_str)
            st.write("**Delimiters:**", range_delimiters)
            st.write("**Step Delimiter:**", step_delimiter)
            st.write("**Deduplication:**", dedup)
            st.write("**Output Format:**", output_format)

    except Exception as e:
        st.error(f"Error: {str(e)}")
