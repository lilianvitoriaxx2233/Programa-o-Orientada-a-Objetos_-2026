import streamlit as st
import time
from service import Service

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")

        id_profissional = st.session_state["usuario_id"]
        horarios = Service.horario_listar_agendados_profissional(id_profissional)

        if len(horarios) == 0:
            st.write("Nenhum serviço aguardando confirmação")
            return

        opcoes = []
        for horario in horarios:
            cliente = Service.cliente_listar_id(horario.get_id_cliente())
            servico = Service.servico_listar_id(horario.get_id_servico())
            nome_cliente = cliente.get_nome() if cliente else "Não informado"
            descricao = servico.get_descricao() if servico else "Não informado"
            opcoes.append(f"{horario.get_data().strftime('%d/%m/%Y %H:%M')} - {nome_cliente} - {descricao}")

        indice = st.selectbox("Selecione o serviço", range(len(horarios)), format_func=lambda i: opcoes[i])
        horario = horarios[indice]

        if st.button("Confirmar Serviço"):
            Service.horario_confirmar(horario.get_id())
            st.success("Serviço confirmado com sucesso")
            time.sleep(1)
            st.rerun()
