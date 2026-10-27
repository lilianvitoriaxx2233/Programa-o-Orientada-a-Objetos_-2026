import streamlit as st
from service import Service
import time

class ConfirmarServicoUI:

    @staticmethod
    def main():

        st.header("Confirmar Serviço")

        id_profissional = st.session_state["usuario_id"]

        horarios = Service.horario_listar_pendentes(
            id_profissional
        )

        if len(horarios) == 0:
            st.write(
                "Não existem serviços aguardando confirmação."
            )
            return

        for horario in horarios:

            st.write("----------------------------------")

            st.write(
                "Data:",
                horario.get_data().strftime(
                    "%d/%m/%Y %H:%M"
                )
            )

            cliente = Service.cliente_listar_id(
                horario.get_id_cliente()
            )

            if cliente != None:
                st.write(
                    "Cliente:",
                    cliente.get_nome()
                )

            servico = Service.servico_listar_id(
                horario.get_id_servico()
            )

            if servico != None:
                st.write(
                    "Serviço:",
                    servico.get_descricao()
                )

            if st.button(
                "Confirmar",
                key="confirmar_" + str(horario.get_id())
            ):

                Service.horario_confirmar(
                    horario.get_id()
                )

                st.success("Serviço confirmado com sucesso!")