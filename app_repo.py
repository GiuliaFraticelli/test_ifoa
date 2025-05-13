import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as plt
import io
import matplotlib.image as mpimg
from PIL import Image
import soundfile as sf

def show_title():
    st.markdown("""
    <style>
    .gradient-text {
        text-align: center;
        font-size: 27px;
        font-weight: bold;
        background: linear-gradient(to right, #00008B, #0000CD, #4169E1, #1E90FF, #87CEEB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    
    <h1 class="gradient-text">💙 SELEZIONA IL TUO STATO D'ANIMO 💙 </h1>
    """, unsafe_allow_html=True)
    
    # st.markdown("*Streamlit* is **really** ***cool***.")
    # st.markdown('''
    # :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    # :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
    # st.markdown("Here's a bouquet &mdash;\
    #         :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

def main():
    show_title()
    

    if "test_avviato" not in st.session_state:
        st.session_state.test_avviato = False
    
    if "risultato_mostrato" not in st.session_state:
        st.session_state.risultato_mostrato = False

    if st.button("Inizia il test"):
        st.session_state.test_avviato = True
        st.session_state.risultato_mostrato = False
    # if st.session_state.test_avviato and st.button("🔄 Rifai il test"):
    #     st.session_state.test_avviato = False  
    #     st.session_state.risultato_mostrato = False  
    #     st.rerun()

    punteggi = [0, 0, 0, 0, 0]

    if st.session_state.test_avviato:
        arrabbiato = st.slider("🤬 Arrabbiato", 0, 100, 0, step=1)
        assonnato = st.slider("😪 Assonnato", 0, 100, 0, step=1)
        affamato = st.slider("🍕 Affamato", 0, 100, 0, step=1)
        stressato = st.slider("😵‍💫 Stressato", 0, 100, 0, step=1)
        triste = st.slider("😭 Triste", 0, 100, 0, step=1)

        if st.button("✅ Mostra risultato"):
            punteggi =  [arrabbiato, assonnato, affamato, stressato, triste]
            valori_maggiori_zero = sum(1 for p in punteggi if p >0)
            valori_uguali_zero = punteggi.count(0)

            if valori_uguali_zero <= 1 and valori_maggiori_zero >= 4:
                st.session_state.risultato_mostrato = True

        if st.session_state.risultato_mostrato:        
                
            somma_punti = sum(punteggi)
            st.markdown(f"<h2 style='color: black;'>Totale: {somma_punti}</h2>", unsafe_allow_html=True)

            if 4 <=somma_punti <= 99:
                st.subheader("Sei un Maestro Zen")
                st.image("giphy.gif")
            elif 100 <= somma_punti <= 199:
                st.subheader("Te la cavi bene")
                st.image("spongebob.gif")
            elif 200 <= somma_punti <= 299:
                st.subheader("Ti vedo un po' agitato")
                st.image("everythings-fine-im-fine.gif")
            elif 300 <= somma_punti <= 399:
                st.subheader("Amo, così non va bene!!!")
                st.image("sheldon_stressed.gif")            
            elif 400 <= somma_punti <= 499:
                st.subheader("Se vai avanti così esplodi ")
                st.image("Hades_exploding.gif")
            elif somma_punti == 500:
                st.subheader("Andrà meglio nella prossima vita... ☠️")
                st.image("gravestone.gif")
        else:
            st.info("⚠️ Per ottenere il risultato, seleziona almeno 4 valori!")
    
    if st.session_state.test_avviato and st.button("🔄 Rifai il test"):
        st.session_state.test_avviato = False  
        st.session_state.risultato_mostrato = False  
        st.rerun()      

# st.write(f"**Arrabbiato:** {arrabbiato}")
# st.write(f"**Assonnato:** {assonnato}")
# st.write(f"**Affamato:** {affamato}")
# st.write(f"**Stressato:** {stressato}")
# st.write(f"**Triste:** {triste}")


if __name__ =='__main__':
    main()