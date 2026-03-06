import streamlit as st
from datetime import datetime, time
import contrato

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
        st.write("**Dados da venda**")
        st.write(f'Email do vendedor: {email}')
        st.write(f'data e hora da venda: {data_hora}')
        st.write(f'valor da venda: {valor_venda:.2f}')
        st.write(f'Quantidade de produtos vendidos: {quantidade_produto}')
        st.write(f'produto: {produto}')

if __name__=="__main__":
    main()