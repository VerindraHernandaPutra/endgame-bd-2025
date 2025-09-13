import streamlit as st
from utils import load_data_keytostep3, PONEGLYPH_2, reset_progress
import time

def show_key_to_step3():
    if not st.session_state.get("step2_pixel_puzzle_solved", False):
        st.error("You must complete the Pixel Puzzle in Step 2 first.")
        return

    st.header("Step 2 (continued): Mengungkap Pesan Poneglyph Kedua")
    st.markdown("Dengan kunci yang kau dapatkan, Poneglyph Kedua akhirnya terbuka! Perhatikan setiap ukiran di dalamnya baik-baik. Ukiran kuno ini sulit dipahami, namun sebuah [arahan](https://docs.google.com/document/d/e/2PACX-1vTd-TtoEGN1Z1WoUtNSFGKe8dl7LyT5tgQ2pFYGZZs0aCl6k_NJykFYXy2ZB08wY2nhJEXLnLlzcvv6/pub)  dapat menuntunmu untuk menyingkap makna yang tersembunyi.", unsafe_allow_html=True)
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
            st.success("Tepat! Frasa 'jalan tersembunyi menuju harta terbesar' merujuk pada Laugh Tale!")
            st.session_state.step2_island_guess_correct = True
        else:
            st.error("Tebakanmu salah. Kamu salah berlayar dan harus mengulang perjalanan.")
            time.sleep(2)
            reset_progress()
            st.rerun()

    if st.session_state.get("step2_island_guess_correct", False):
        if st.button("Lanjut ke Laugh Tale (Final Step)"):
            st.session_state.stage = 4
            st.rerun()
