import streamlit as st
import time
from PIL import Image
# Baca file PNG
image = Image.open("assets/images/berhasil menebak.png")

def show_final_page():
    """
    Menampilkan halaman kemenangan setelah pemain menemukan One Piece.
    """

    # 1. Memicu animasi perayaan secara otomatis
    st.balloons()

    # 2. Judul utama halaman
    st.title("🎉 SELAMAT, PETUALANG! 🎉")
    st.markdown("---")

    # 3. Pesan kemenangan yang epik
    st.header("Anda Telah Menemukan Harta Karun Legendaris...")
    st.header("ONE PIECE!")
    
    st.info("Jerih payahmu terbayar sudah! Namamu akan terukir dalam sejarah sebagai Raja Bajak Laut yang baru!", icon="👑")
    
    # 4. Menampilkan "Harta Karun" (bisa berupa gambar atau teks)
    # Anda bisa mengganti link gambar di bawah ini dengan gambar Anda sendiri.
    # Cukup unggah gambar ke folder yang sama dengan script dan ganti linknya. 
    st.image(image, use_container_width =True)

    st.markdown("---")

    # 5. Memberi pesan tambahan dan tombol untuk bermain lagi
    st.subheader("Perjalananmu mungkin telah berakhir, tapi legendamu akan abadi.")

    st.markdown("👉 Lanjutkan ke game berikutnya [di sini](https://www.google.com/)🗺️", unsafe_allow_html=True)
