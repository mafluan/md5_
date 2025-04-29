import streamlit as st
import hashlib

st.set_page_config(page_title="MD5 Hashing Interface", page_icon="🔐", layout="centered")

st.title("🔐 MD5 Hashing Interface")

st.markdown("""
This educational interface helps you understand how the *MD5 hashing algorithm* works.
You can enter your own text, see the MD5 hash result, and explore each part of the process in a simple and visual way.
""")

with st.expander("What is MD5?", expanded=False):
    st.markdown("""
    <div style='background-color:#f5f0ff; padding:10px; border-radius:10px'>
    MD5 stands for Message Digest 5. It is a cryptographic hash function that takes any input and converts it into a fixed 128-bit (32-character hexadecimal) string.
    
    It is commonly used to:
    - Verify file integrity
    - Create unique IDs
    - Learn hashing concepts in education
    </div>
    """, unsafe_allow_html=True)

with st.expander("Main Properties", expanded=False):
    st.markdown("""
    <div style='background-color:#f5f0ff; padding:10px; border-radius:10px'>
    - *Deterministic*: Same input always gives the same output.
    - *Fast*: Works quickly on any input size.
    - *Fixed-length*: Always outputs 128-bit hash.
    - *Avalanche Effect*: Small changes in input cause big changes in output.
    - *Non-reversible*: You can't go backwards to get the original input.
    </div>
    """, unsafe_allow_html=True)

with st.expander("Where is MD5 Used?", expanded=False):
    st.markdown("""
    <div style='background-color:#f5f0ff; padding:10px; border-radius:10px'>
    Despite its known security weaknesses, MD5 is still used in:
    
    - *Checksums for downloaded files*
    - *Digital forensics*
    - *Legacy password systems (not recommended)*
    - *Database record IDs*
    - *Learning cryptography and algorithms*
    </div>
    """, unsafe_allow_html=True)

with st.expander("Step-by-Step Example: 'hello'", expanded=False):
    st.markdown("""
    <div style='background-color:#f5f0ff; padding:10px; border-radius:10px'>
    Let’s take the input *"hello"* and see how MD5 processes it:

    1. *Convert to binary*: "hello" becomes a binary stream via UTF-8.
    2. *Padding*: Adds bits so the length becomes a multiple of 512.
    3. *Append original length*: Adds 64-bit representation of original message length.
    4. *Initialize buffers*: Four 32-bit words (A, B, C, D) are set.
    5. *Process through 64 operations*: Non-linear functions and bitwise shifts.
    6. *Final hash*: Produces this digest:

    
    Input:  hello
    MD5 Hash: 5d41402abc4b2a76b9719d911017c592
    

    This result is unique to "hello". Even "Hello" (with capital H) produces a completely different hash.
    </div>
    """, unsafe_allow_html=True)

# Input field
user_input = st.text_area("Enter text to generate MD5 hash:", height=100, placeholder="e.g., hello")

if st.button("Generate MD5 Hash"):
    if user_input:
        md5_hash = hashlib.md5(user_input.encode()).hexdigest()
        st.success(f"✅ Resulting MD5 Hash:\n`{md5_hash}`")

        with st.expander("How MD5 Works Internally", expanded=False):
            st.markdown("""
            <div style='background-color:#f5f0ff; padding:10px; border-radius:10px'>
            Internally, MD5 goes through multiple stages:

            - Input is first converted to binary using UTF-8.
            - Message is padded with a 1-bit and then 0-bits to reach 448 mod 512 bits.
            - Original message length is appended in 64 bits.
            - MD5 initializes four buffers: A, B, C, D with predefined constants.
            - The binary message is divided into 512-bit blocks.
            - Each block is processed in 64 rounds using non-linear functions and bitwise operations.
            - The final output is a combination of the four buffers (A, B, C, D) converted to hexadecimal.

            This creates a digital "fingerprint" that is nearly impossible to reverse.
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please enter text to hash.")

# Visual explanation diagram
st.markdown("### MD5 Hashing Process Diagram:")
st.image("https://www.comparitech.com/wp-content/uploads/2022/12/md5-algorithm-example-diagram.png", caption="Source: Comparitech.com")

st.markdown("---")
st.caption("Created with Streamlit | MD5 visualization tool for educational use.")