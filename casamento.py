import streamlit as st
import pandas as pd

st.title("💍 Planejamento Interativo do Casamento de Filipe & Yasmin")

# Informações Gerais
data = "Janeiro de 2026"
local = "Chácara Paraíso do Conde"
horario = "17h - Pôr do Sol"

tab1, tab2, tab3 = st.tabs(["📅 Informações", "💰 Orçamento", "⏳ Cronograma"])

with tab1:
    st.header("📅 Detalhes do Casamento")
    st.write(f"**Data:** {data}")
    st.write(f"**Local:** {local}")
    st.write(f"**Horário:** {horario}")
    st.write("**Estilo:** Rústico e vintage com toques de Evangelion e High School Musical")
    
    st.subheader("🎨 Paleta de Cores")
    cores = {
        "Verde Sage": "#7D8471",
        "Verde Eucalipto": "#44674D",
        "Rosa Antigo": "#D8A7B1",
        "Rosa Blush": "#F1CCCD",
        "Bege Champagne": "#F7E7CE",
        "Dourado Envelhecido": "#D4AF37"
    }
    for cor, hex in cores.items():
        st.markdown(f"<span style='background-color:{hex}; padding:5px 10px; border-radius:5px;'>{cor}</span>", unsafe_allow_html=True)
    
with tab2:
    st.header("💰 Orçamento Estimado")
    
    dados_orcamento = {
        "Categoria": ["Aluguel da Chácara", "Decoração", "Buffet", "Música", "Fotografia/Vídeo", "Vestuário", "Convites/Papelaria", "Lembranças", "Cerimonialista", "Transporte", "Acomodação"],
        "Valor (R$)": [7000, 8000, 5000, 2000, 6500, 5000, 1000, 1500, 3500, 2000, 500]
    }
    df_orcamento = pd.DataFrame(dados_orcamento)
    df_orcamento["Editar"] = [st.number_input(f"{cat}", value=valor) for cat, valor in zip(df_orcamento["Categoria"], df_orcamento["Valor (R$)"])]
    
    total = sum(df_orcamento["Editar"])
    st.write("**Total Estimado:** R$", total)
    st.dataframe(df_orcamento, use_container_width=True)

with tab3:
    st.header("⏳ Cronograma Detalhado")
    eventos = [
        ("08:00", "Chegada da equipe de decoração e montagem"),
        ("09:00", "Montagem das estruturas (arco, tendas, mesas)"),
        ("15:30", "Chegada dos convidados"),
        ("17:00", "Início da cerimônia"),
        ("19:00", "Abertura da recepção"),
        ("21:00", "Corte do bolo e brinde"),
        ("23:45", "Lançamento do buquê"),
        ("00:00", "Encerramento oficial")
    ]
    df_cronograma = pd.DataFrame(eventos, columns=["Horário", "Evento"])
    st.dataframe(df_cronograma, use_container_width=True)
    
st.write("📝 Este planejamento pode ser ajustado conforme novas necessidades surgirem.")
