import streamlit as st
from datetime import datetime, time
from contrato import Venda
produtos = [
    "ZapFlow com ChatGPT",
    "ZapFlow com Llama",
    "ZapFlow com Gemini"
]

def main():
    st.title("Sistema CRM de vendas ZapFlow - Interface simples")
    email = st.text_input("Email do vendedor")
    data_venda = st.date_input("Data da venda:", datetime.now())
    horario_venda = st.time_input("Horario da venda", value=time(9,0))
    valor_venda = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade_produto = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto vendido", produtos)

    if st.button("Confirmar venda"):
        data_hora = datetime.combine(data_venda, horario_venda)
        try:
            venda = Venda(
                email = email,
                data_hora = data_hora,
                valor_venda = valor_venda,
                quantidade_produto = quantidade_produto,
                produto = produto
            )
            st.write("venda registrada")
        except Exception as e:
            st.write(f"Erro = {e}")
        st.write(f'detalhes do registro: ', venda.model_dump())

if __name__=="__main__":
    main()