import streamlit as st

st.set_page_config(page_title="Coração do Adauto", page_icon="💖")

# 💓 CSS do coração batendo
st.markdown("""
<style>
.heart {
    font-size: 80px;
    animation: pulse 1s infinite;
    text-align: center;
}

@keyframes pulse {
    0% { transform: scale(1); }
    25% { transform: scale(1.2); }
    50% { transform: scale(1); }
    75% { transform: scale(1.2); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

st.title("💖 Coração do Adauto 💖")

nome = st.text_input("Qual o seu nome?")

if nome:

    if nome.lower().strip() == "julia":

        senha = st.text_input("Digite a senha secreta:", type="password")

        if senha:

            if senha == "281193":
                st.success("Acesso liberado ❤️")

                comida = st.text_input("Qual sua comida favorita?")
                idade = st.number_input("Qual sua idade?", step=1, min_value=0)

                if comida and idade:
                    st.markdown("## 💌 RESULTADO 💌")
                    st.write("**Nome:**", nome)
                    st.write("**Idade:**", idade)

                    if comida.lower().strip() == "lasanha":
                        st.success("A gente combina 😍🍕")
                    else:
                        st.info("Prefiro lasanha com você 😄")

                    st.markdown("### ❤️ Amor da vida do Adauto ❤️ TE AMO INFINITO")

                    # 💓 Coração animado
                    st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)

                    # 📸 Foto
                    st.image("foto.jpg", caption="Nosso momento ❤️", use_column_width=True)

                    # 🎈 Animação extra
                    st.balloons()

            else:
                st.error("Senha incorreta!")

    else:
        st.error("Acesso negado 🚫")
