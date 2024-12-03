import streamlit as st
from summari import summarizer  # Import fungsi dari summari.py
import base64

# Mengatur halaman dengan ikon emoji
st.set_page_config(page_title='🔗 Text Summarization')

# CSS tambahan untuk latar belakang dan elemen UI
st.markdown("""
    <style>
        .reportview-container {
            background: linear-gradient(to right, #00c6ff, #0072ff);
        }
        .css-ffhzg2 {
            padding-top: 20px;
        }
        .stTextInput>div>div>input {
            padding: 15px;
            border-radius: 10px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            font-size: 18px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk membuat file teks untuk diunduh
def create_download_link(text, filename="summary.txt"):
    """
    Mengembalikan link unduhan untuk file teks.
    """
    b64 = base64.b64encode(text.encode()).decode()  # Encode teks ke Base64
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">Klik di sini untuk mengunduh ringkasan</a>'
    return href

# Judul aplikasi
st.title("🔗 Text Summarization")
st.write("Input teks artikel yang ingin anda meringkasnya, dan aplikasi ini akan membuat ringkasannya.")

# Input teks dari pengguna
user_input = st.text_area("Masukkan teks di bawah ini:", height=200)

if st.button("Buat Ringkasan"):
    if user_input.strip():  # Validasi input
        # Panggil fungsi summarizer
        summary, original_length, summary_length = summarizer(user_input)

        # Menampilkan hasil ringkasan
        st.subheader("Ringkasan:")
        st.write(summary)

        # Statistik panjang teks
        st.subheader("Statistik:")
        st.write(f"- Panjang teks asli: {original_length} kata")
        st.write(f"- Panjang ringkasan: {summary_length} kata")

        # Tombol unduh hasil ringkasan
        st.markdown("### Unduh Ringkasan:")
        st.markdown(create_download_link(summary), unsafe_allow_html=True)
    else:
        st.error("Teks tidak boleh kosong. Masukkan teks untuk dirangkum.")
