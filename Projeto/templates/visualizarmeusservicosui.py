import streamlit as st
import pandas as pd
from service import Service

class VisualizarMeusServicosUI:

    @staticmethod
    def main():

        st.header("Visualizar Meus Serviços")

        id_cliente = st.session_state["usuario_id"]

        horarios = Service.horario_listar_cliente(
            id_cliente
        )

        if len(horarios) == 0:
            st.write("Nenhum serviço agendado.")
            return

        for horario in horarios:

            st.write("----------------------------------")

            st.write(
                "Data:",
                horario.get_data().strftime(
                    "%d/%m/%Y %H:%M"
                )
            )

            profissional = Service.profissional_listar_id(
                horario.get_id_profissional()
            )

            if profissional != None:
                st.write(
                    "Profissional:",
                    profissional.get_nome()
                )

            servico = Service.servico_listar_id(
                horario.get_id_servico()
            )

            if servico != None:
                st.write(
                    "Serviço:",
                    servico.get_descricao()
                )

            if horario.get_confirmado():
                st.write(
                    "Situação: Serviço confirmado"
                )
            else:
                st.write(
                    "Situação: Aguardando confirmação"
                )