import streamlit as st
from utils import initialize_state
from page_step1 import show_step_1
from page_step2 import show_step_2
from page_keytostep3 import show_key_to_step3
from page_step3 import show_step_3
from page_finished import show_final_page

# JUDUL HALAMAN
st.set_page_config(
    page_title="Journey of the Poneglyphs",
    layout="wide",
)

initialize_state()
current_stage = st.session_state.get('stage', 0)

# URUTAN ALUR APLIKASI BERDASARKAN STAGE
if current_stage == 0:
    st.title("🗺️ Journey of the Poneglyphs")
    st.markdown("Selamat datang, jiwa petualang. Banyak yang telah mencoba, namun hanya yang terpilih yang sampai di titik ini. Rahasia harta karun terakhir menantimu di ujung perjalanan.")
    st.subheader("Beranikah kau memulainya?")
    st.image("assets/images/start.png", width=1080)
    st.markdown("Di setiap langkah perjalananmu, akan ada sebuah [arahan](https://docs.google.com/document/d/e/2PACX-1vTia45O2JX9iigTKPsc1XcZOZLwp2xK0jzWykgQBjZoPE_9p-xkOoFuAdvgWN7Q9XrwPVIYYgebYfi_/pub) yang akan menuntunmu menuju harta karun legendaris.", unsafe_allow_html=True)
    if st.button("Start Adventure"):
        st.session_state.stage = 1
        st.rerun()

elif current_stage == 1:
    show_step_1()

elif current_stage == 2:
    show_step_2()

elif current_stage == 3: 
    show_key_to_step3()

elif current_stage == 4:
    show_step_3() 

elif current_stage == 5:
    show_final_page()