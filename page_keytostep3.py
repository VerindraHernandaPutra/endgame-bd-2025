import streamlit as st
from utils import load_data_keytostep3, PONEGLYPH_2, reset_progress
import time

# --- Definisi Dialog Intro ---
@st.dialog("Mengungkap Pesan", width="large")
def intro_dialog_1():
    st.image("assets/images/pagekeyto3_awal_part1.png", use_container_width=True)
    if st.button("Baca Tulisannya..."):
        st.session_state.keytostep3_intro_slide = 2
        st.rerun()

@st.dialog("Petunjuk Kedua", width="large")
def intro_dialog_2():
    st.image("assets/images/pagekeyto3_awal_part2.png", use_container_width=True)
    if st.button("Mulai Terjemahkan Petunjuk"):
        st.session_state.keytostep3_intro_slide = 0  # Selesaikan intro
        st.rerun()

# --- Definisi Dialog Outro ---
@st.dialog("Tebakan Benar!", width="large")
def outro_dialog_1():
    st.image("assets/images/pagekeyto3_akhir_part1.png", use_container_width=True)
    if st.button("Lanjutkan... #1"):
        st.session_state.keytostep3_outro_slide = 2
        st.rerun()

@st.dialog("Pulau Terakhir", width="large")
def outro_dialog_2():
    st.image("assets/images/pagekeyto3_akhir_part2.png", use_container_width=True)
    if st.button("Lanjutkan... #2"):
        st.session_state.keytostep3_outro_slide = 3
        st.rerun()

@st.dialog("Laugh Tale", width="large")
def outro_dialog_3():
    st.image("assets/images/pagekeyto3_akhir_part3.png", use_container_width=True)
    if st.button("Lanjutkan... #3"):
        st.session_state.keytostep3_outro_slide = 4
        st.rerun()
        
@st.dialog("Harta Karun di Depan Mata", width="large")
def outro_dialog_4():
    st.image("assets/images/pagekeyto3_akhir_part4.png", use_container_width=True)
    if st.button("Berlayar ke Stage Terakhir"):
        st.session_state.keytostep3_outro_slide = 0 # Selesaikan outro
        st.session_state.stage = 4                   # Lanjut ke stage puzzle berikutnya
        st.rerun()

# --- Fungsi Utama Halaman ---
def show_key_to_step3():
    # Page Guard: Pastikan puzzle sebelumnya selesai
    if not st.session_state.get("step2_pixel_puzzle_solved", False):
        st.error("Anda harus menyelesaikan Puzzle Piksel di Step 2 terlebih dahulu.")
        return

    # Router internal untuk menampilkan dialog atau puzzle
    intro_slide = st.session_state.get("keytostep3_intro_slide", 1)
    outro_slide = st.session_state.get("keytostep3_outro_slide", 0)

    if intro_slide == 1:
        intro_dialog_1()
    elif intro_slide == 2:
        intro_dialog_2()
    elif outro_slide == 1:
        outro_dialog_1()
    elif outro_slide == 2:
        outro_dialog_2()
    elif outro_slide == 3:
        outro_dialog_3()
    elif outro_slide == 4:
        st.balloons()
        outro_dialog_4()
    else:
        # --- Konten Puzzle Utama ---
        st.header("Step 2 (lanjutan): Mengungkap Pesan Poneglyph Kedua")
        st.markdown("Dengan kunci yang kau dapatkan, Poneglyph Kedua akhirnya terbuka! Perhatikan setiap ukiran di dalamnya baik-baik. Ukiran kuno ini sulit dipahami, namun sebuah [arahan](https://docs.google.com/document/d/e/2PACX-1vTd-TtoEGN1Z1WoUtNSFGKe8dl7LyT5tgQ2pFYGZZs0aCl6k_NJykFYXy2ZB08wY2nhJEXLnLlzcvv6/pub) dapat menuntunmu untuk menyingkap makna yang tersembunyi.", unsafe_allow_html=True)
        st.divider()

        st.subheader("Poneglyph Kedua Terbuka!")
        st.info(PONEGLYPH_2)

        islands_df = load_data_keytostep3()
        if not islands_df.empty:
            st.subheader("Island Database Reference:")
            st.dataframe(islands_df)

        st.subheader("Tebak nama pulau yang digambarkan oleh Poneglyph Kedua:")
        user_guess_2 = st.text_input("Nama Pulau Selanjutnya").lower()

        if st.button("Tebak Pulau Kedua"):
            if 'laugh tale' in user_guess_2:
                st.session_state.step2_island_guess_correct = True
                st.session_state.keytostep3_outro_slide = 1 # Memulai sekuens outro
                st.rerun()
            else:
                st.error("Tebakanmu salah. Kamu salah berlayar dan harus mengulang perjalanan.")
                time.sleep(2)
                reset_progress()
                st.rerun()