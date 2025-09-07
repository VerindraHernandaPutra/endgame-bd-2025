import streamlit as st
import markovify
from utils import load_markov_model, decode_rot13

def show_step_3():
    st.header("Final: The Secret of Laugh Tale")
    st.markdown("Selamat datang di **Laugh Tale**! One Piece ada di sini, tapi terkunci di balik teka-teki terakhir!")
    st.divider()

    # LOAD DATASET | NANTI GANTI DATASET SI DAVAAA
    markov_model = load_markov_model()

    # LAGI MENTAHAN
    st.subheader("Langkah 1: Dekode Teks")
    st.markdown("Teks di bawah ini terenkripsi. Dekode untuk menemukan petunjuk!")
    encoded_text = "Gur oebja ebbfr fubjf bayl oernxvat tbyq, gubhtu gur jbeqf ner sver va gurfr qrnyf. Rirel jnl gur yvarf qbja, gurer vf bayl gubhtu pbairagvbaf. Gur jnl vf vaibyirq va gur nzbhag bs pbzznaqf, ohg gurer vf ab fcrpvny fbyhgvba. Vg nyjnlf frrzf yvxr gur yvar vf n ybg bs fbzrguvat arprffnel. Naq gurer vf na rknpg yvar gung fnlf: gurnger vf ba gur sebag qrngu zbhag. Gur erfg vf bayl bevtvany naq abguvat vf vagb fznyr."
    st.code(encoded_text, language='text')

    if st.button("Dekode Teks"):
        st.session_state.step3_decoded_text = decode_rot13(encoded_text)

    if st.session_state.step3_decoded_text:
        st.subheader("Hasil Dekode Teks:")
        st.code(st.session_state.step3_decoded_text, language='text')
        st.divider()