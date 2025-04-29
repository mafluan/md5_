import streamlit as st
import hashlib

st.set_page_config(page_title="MD5 Hashing Interface", page_icon="🔐", layout="centered")

# Кастомные стили (цвет фона раскрывающихся блоков и текста)
st.markdown("""
    <style>
    .st-expander {
        background-color: #f5f0ff !important;  /* нежно-сиреневый фон */
        border-radius: 10px;
        padding: 8px;
    }
    .st-expander > summary {
        color: #4B0082 !important;  /* фиолетовый заголовок */
        font-weight: bold;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Заголовок и вводное
st.title("🔐 MD5 Hashing Interface")
st.write("""
This tool demonstrates how the MD5 algorithm works. 
You can enter any text, get its MD5 hash, and explore how the process works behind the scenes.

It is designed to be easy to understand, even for those unfamiliar with cryptography.
""")

# Теория — блоки
with st.expander("What is MD5?"):
    st.write("""
MD5 is a cryptographic hash function developed in the early 1990s.
Its main job is to transform any input (text, file, etc.) into a short, fixed-length "fingerprint".

Although MD5 is no longer secure for cryptographic purposes, it remains widely used in education and file verification.
""")

with st.expander("Main Properties"):
    st.markdown("""
- *Irreversible*: You cannot "unhash" an MD5 result.
- *Fixed length*: Always returns 32 hexadecimal characters.
- *Sensitive to change*: A small input change creates a very different output.
- *Deterministic*: Same input → same output.
""")

with st.expander("Used In"):
    st.markdown("""
- Verifying file downloads
- Storing passwords (legacy systems)
- Detecting data changes
- Teaching and learning about hash functions
""")

# Ввод текста
user_input = st.text_area("Enter text to hash:", height=100, placeholder="Type something here...")

if st.button("Generate MD5 Hash"):
    if user_input:
        md5_hash = hashlib.md5(user_input.encode()).hexdigest()
        st.success(f"✅ MD5 Hash: {md5_hash}")

        with st.expander("How does MD5 work?"):
            st.markdown("""
MD5 is a bit like a *digital blender* — it takes your input and mixes it up until it becomes a 128-bit output.

Here’s how it works under the hood:

1. *Preprocessing*: The text is converted to binary. Padding is added to make the total length a multiple of 512 bits.
2. *Chunking*: The binary data is split into 512-bit blocks.
3. *Initialization*: Four fixed variables (A, B, C, D) are set as starting values.
4. *64 Operations*: For each block, MD5 performs a series of 64 complex bit-level operations (XOR, shifts, modulo adds) on the data.
5. *Output*: The final result is a unique 128-bit number, shown as a 32-digit hex string.

Even if your input changes just a little, the output becomes totally different.

That’s why MD5 is useful for spotting differences and verifying file integrity.
""")
    else:
        st.warning("Please enter text to generate a hash.")

st.markdown("---")
st.caption("Created with Streamlit | Suitable for educational use and teacher demonstration.")