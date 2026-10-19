import streamlit as st

# Configuració de la pàgina
st.set_page_config(
    page_title="ETS EN CHESTER O EN MIKE?",
    page_icon="⚡",
    layout="centered"
)

# Carregar Google Fonts (Permanent Marker + Space Mono)
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    
    <style>
    /* Fons fosc estil industrial i font Space Mono general */
    .stApp {
        background-color: #0a0c0e !important;
        color: #ffffff !important;
        font-family: 'Space Mono', monospace !important;
    }
    
    /* Textos generals, paràgrafs i etiquetes */
    p, span, label, div {
        color: #f3f4f6 !important;
        font-family: 'Space Mono', monospace !important;
    }

    /* Targetes de preguntes i opcions dels radio buttons */
    div[role="radiogroup"] > label {
        background-color: #181c24 !important;
        padding: 14px !important;
        border-radius: 6px !important;
        border-left: 5px solid #ff3333 !important;
        border-top: 1px solid #2e3545 !important;
        border-right: 1px solid #2e3545 !important;
        border-bottom: 1px solid #2e3545 !important;
        margin-bottom: 10px !important;
        transition: all 0.2s ease;
    }

    /* Text de les opcions a dins del botó */
    div[role="radiogroup"] > label p {
        color: #ffffff !important;
        font-size: 15px !important;
        font-weight: 400 !important;
        font-family: 'Space Mono', monospace !important;
    }

    div[role="radiogroup"] > label:hover {
        border-left: 5px solid #4ade80 !important;
        background-color: #222834 !important;
    }

    /* Enunciats de les preguntes */
    .stRadio > label {
        font-size: 17px !important;
        font-weight: 700 !important;
        color: #fbbf24 !important;
        font-family: 'Space Mono', monospace !important;
        margin-bottom: 8px !important;
    }

    /* BOTÓ DEFINITIU: Fons vermell (#ff3333) coordinat amb el títol */
    div[data-testid="stFormSubmitButton"] > button,
    div[data-testid="stFormSubmitButton"] button {
        background-color: #ff3333 !important;
        background: #ff3333 !important;
        border: 2px solid #dc2626 !important;
        border-radius: 6px !important;
        padding: 12px 25px !important;
        box-shadow: 0px 0px 18px rgba(255, 51, 51, 0.7) !important;
        width: 100% !important;
        margin-top: 15px !important;
    }

    /* Lletres negres forçades amb Space Mono per al botó */
    div[data-testid="stFormSubmitButton"] button *,
    div[data-testid="stFormSubmitButton"] button p,
    div[data-testid="stFormSubmitButton"] button span {
        color: #000000 !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        font-family: 'Space Mono', monospace !important;
        letter-spacing: 1px !important;
    }

    /* Efecte en passar el ratolí */
    div[data-testid="stFormSubmitButton"] button:hover {
        background-color: #dc2626 !important;
        background: #dc2626 !important;
        box-shadow: 0px 0px 25px rgba(255, 51, 51, 1) !important;
    }

    /* Separador */
    hr {
        border-color: #2e3545 !important;
    }
    </style>
""", unsafe_allow_html=True)

# CAPÇALERA EN HTML PUR
st.markdown("""
    <h1 style="font-family: 'Permanent Marker', cursive, sans-serif; color: #ff3333; text-align: center; font-size: 42px; letter-spacing: 2px; text-shadow: 0px 0px 15px rgba(255, 51, 51, 0.8); margin-bottom: 0px;">
        ⚡ETS EN CHESTER O EN MIKE?⚡
    </h1>
    <h3 style="font-family: 'Space Mono', monospace; color: #4ade80; text-align: center; font-size: 18px; letter-spacing: 2px; font-weight: 700; margin-top: 10px; margin-bottom: 25px;">
        [ HYBRID THEORY // METEORA EDITION ]
    </h3>
""", unsafe_allow_html=True)

st.write("---")

# Formulari del test
with st.form("quiz_form"):

    q1 = st.radio(
        "1. Et peta el PC a mig projecte i no has desat res. Què fas?",
        [
            "A) Mètode volcànic: te cagues en tot, quasi rebentes el teclat i tens 5 minuts de col·lapse emocional.",
            "B) Mètode analític: fas una broma d'ironia fina, respires fons, et fas un cafè i et poses a refer-ho de zero."
        ]
    )

    q2 = st.radio(
        "2. Són les 4 de la matinada al garito i sona el temacle de la nit. Quina reacció tens?",
        [
            "A) Cantes a ple pulmó, t'enfiles a una cadira si fa falta i ho cremes tot fins a l'última gota d'energia.",
            "B) Te poses en mode dj mental, analitzes el temàs, fas quatre passos de ball marcant el ritme i xerradeta guapa amb una cervesa a la mà."
        ]
    )

    q3 = st.radio(
        "3. Quina és la teva muda de dia a dia un dia qualsevol?",
        [
            "A) Lo primer que trob a l'armari: camiseta de grup/fosca, texans i dessuadora/jaqueta de fa mil anys.",
            "B) Bambes guapes, pantalons amples, dessuadora/jaqueta ben polida i tot super ben pensat abans de sortir de casa."
        ]
    )

    q4 = st.radio(
        "4. Quan et toca posar-te en mode nerd davant la pantalla... quin és el teu terreny?",
        [
            "A) Mètode prova-error i força bruta: toc tots els botons, em cag en tot quan no va, cerc la solúció més directa i quan ho faig funcionar em sento el rei del món.",
            "B) Mètode arquitecte: m'encanta tenir-ho tot ordenat, trastejar amb codi/scripts, optimitzar processos i automatitzar fins i tot la meva vida si cal."
        ]
    )

    q5 = st.radio(
        "5. Quan hi ha algú que t'agrada i vols tirar la canya, quin és el teu estil?",
        [
            "A) Vaig de cara i amb tot: intensitat, mirada fixa i dir-ho directament abans no me pegui un atac de nervis.",
            "B) Joc de seducció calculat: faig bromes intel·ligents, mantinc el misteri, control el tempo de la conversa i deix que tot flueixi com si res."
        ]
    )

    submitted = st.form_submit_button("🔥 EXECUTAR DIAGNÒSTIC 🔥")

# Lògica i resultat
if submitted:
    chester_count = sum([
        q1.startswith("A"),
        q2.startswith("A"),
        q3.startswith("A"),
        q4.startswith("A"),
        q5.startswith("A")
    ])
    
    mike_count = 5 - chester_count

    st.write("---")
    
    if chester_count >= 3:
        st.balloons()
        st.error(f"PERFIL: CHESTER BENNINGTON ({chester_count}/5 A)")
        st.write("""
        **Pura passió, cor, visceralitat i intensitat sense filtres.** 
        Quan una cosa t'agrada o et fot, se't nota a la cara a tres cents quilòmetres. Et mous per impulsos, per intuïció i per emocions reals. No et van les coses a mitges ni la hipocresia: si cal anar amb tot, hi vas amb el cap per davant, i quan et fas valdre o et diverteixes, contagies a tothom que tens al voltant!
        """)
    else:
        st.snow()
        st.success(f"PERFIL: MIKE SHINODA ({mike_count}/5 B)")
        st.write("""
        **Estratègia, cervell, temple i control de la situació.** 
        Tens un talent natural per no perdre els nirvis quan les coses es tornen loques. Et mola tenir el teu espai, pensar les coses abans de fer-les i trobar la sol·lució intel·ligent a qualsevol moguda. Ets la persona que manté la calma, la que dona sentit al caos i la que sap gaudir dels detalls.
        """)