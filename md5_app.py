import streamlit as st
import hashlib

st.set_page_config(page_title="MD5 Hasher", page_icon="🔐", layout="centered")

st.title("🔐 MD5 Hasher & Explainer")
st.write("This app takes your text, generates an MD5 hash, and explains how it works in a beginner-friendly way.")

st.markdown("### What is MD5?")
st.info("""
MD5 (Message-Digest Algorithm 5) is a *cryptographic hash function*.
It converts any input text into a *128-bit (32-character hexadecimal)* string.

Main properties:
- One-way function: You cannot reverse it.
- Same input = same output.
- A tiny change in input gives a totally different hash.

Used in:
- Data integrity checks
- Password storage
- File verification
""")

user_input = st.text_input("Enter text to hash", placeholder="e.g., hello world")

if st.button("Generate MD5"):
    if user_input:
        # Step-by-step explanation
        st.subheader("1. Convert to bytes")
        byte_data = user_input.encode()
        st.code(byte_data, language="python")

        st.subheader("2. Apply MD5 algorithm")
        md5_result = hashlib.md5(byte_data)

        st.subheader("3. Get the hexadecimal digest")
        hex_digest = md5_result.hexdigest()
        st.code(hex_digest, language="python")

        st.success(f"✅ MD5 Hash: {hex_digest}")

        st.markdown("---")
        st.subheader("How MD5 works (Simplified)")
        st.markdown("""
1. Converts your text into binary (bytes).
2. Splits the input into 512-bit blocks.
3. Applies *64 rounds* of bitwise operations (AND, OR, XOR, etc.).
4. Outputs a *128-bit digest*, which is shown as 32 hex characters.
        """)
    else:
        st.warning("Please enter some text to hash.")

st.markdown("---")
st.caption("Made with Streamlit for educational purposes.")