import streamlit as st
from utils import load_data_step3, reset_progress
import time

def show_step_3():
    st.header("Final: Teka-Teki Poneglyph Terakhir")
    st.markdown("Selamat datang di **Laugh Tale**! Untuk menemukan One Piece, Anda harus menerjemahkan pesan terakhir yang terukir di sini.")
    st.divider()

    # DESKRIPSI PUZZLE
    st.subheader("Deskripsi Puzzle")
    st.info("""
    Poneglyph terakhir ini tidak berisi tulisan biasa, melainkan sebuah teka-teki "Tebak Gambar".
    
    Tugas Anda adalah menemukan **frasa kunci rahasia** yang tersembunyi. Gunakan petunjuk dan contoh di bawah ini untuk memecahkan teka-teki terakhir.
    """)
    st.divider()

    # DATASET
    st.subheader("Catatan Kuno")
    
    st.success("""
    **Petunjuk Penting:** Untuk menemukan emoji di setiap `Label`, carilah emoji yang **unik/anomali**. Translasi emoji yang kamu temukan [disini.](https://unicode.org/emoji/charts/full-emoji-list.html) 
    """)
    
    placeholder_df = load_data_step3()
    if not placeholder_df.empty:
        st.dataframe(placeholder_df)
    st.divider()

    # CONTOH JAWABAN
    st.subheader("Contoh Cara Menjawab (Ini Bukan Jawaban Sebenarnya)")
    st.markdown("Bayangkan Anda telah menemukan dan menyusun emoji berikut:")
    
    col1, col2, col3 = st.columns(3)
    col1.markdown("<h2 style='text-align: center;'>🍊</h2>", unsafe_allow_html=True)
    col2.markdown("<h2 style='text-align: center;'>🚬</h2>", unsafe_allow_html=True)
    col3.markdown("<h2 style='text-align: center;'>🤥</h2>", unsafe_allow_html=True)

    st.warning(
    "Setelah emoji tersusun, terjemahkan menjadi kata-kata (misal: **'tangerine cigarette lying face'**). Frasa inilah yang dimasukkan sebagai jawaban."
    )
    st.divider()
    
    # INPUT JAWABAN
    st.subheader("Kunci Final One Piece")
    st.markdown("**Masukkan frasa rahasia yang sudah Anda pecahkan:**")
    user_answer = st.text_input("Frasa Kunci Rahasia").lower()

    if st.button("Tebak"):
        CORRECT_PHRASE = "smiling face with hearts money-mouth face hot face confused face weary cat" # JAWABAN BENAR
        
        # LOGIKA JAWABAN BENAR/SALAH
        if user_answer.strip() == CORRECT_PHRASE:
            st.balloons()
            st.success("SELAMAT! Kunci yang Anda masukkan benar!")
            st.markdown("## 🎉 Anda Telah Menemukan One Piece! 🎉") # MASUKKAN LINK UNTUK MASUK KE NEXT ENDGAME DIVISI LAIN [BIKIN PAGE BARU AE KLO MAU, BIAR LEBIH IMMERSIVE HAHAHAH]
            st.session_state.step3_final_puzzle_solved = True
            st.session_state.stage = 5
            st.rerun()
        else:
            st.error("Frasa yang Anda masukkan salah! Poneglyph mereset dirinya dan Anda terlempar kembali ke awal.")
            time.sleep(3)
            reset_progress()
            st.rerun()
    
    # if st.session_state.get("step3_final_puzzle_solved", False):
    #     if st.button("Mulai Petualangan Baru 🗺️"):
    #         st.session_state.stage = 5
    #         st.rerun()