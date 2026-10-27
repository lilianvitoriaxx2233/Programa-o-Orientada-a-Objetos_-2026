import streamlit as st
import pandas as pd
from service import Service

class ListarAgendaClienteUI:
    @staticmethod
    def main():
        st.header("Listar agenda do cliente")

        clientes = Service.cliente_listar()
        clientes = [cliente for cliente in clientes if cliente.get_nome().casefold() != "admin"]

        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado.")
            return

        cliente = st.selectbox(
            "Selecione o cliente",
            clientes,
            format_func=lambda cliente: cliente.get_nome(),
        )

        horarios = sorted(
            Service.horario_listar_cliente(cliente.get_id()),
            key=lambda horario: horario.get_data(),
        )

        if len(horarios) == 0:
            st.write("Esse cliente não possui horários na agenda.")
            return

        dados = []
        for horario in horarios:
            profissional = Service.profissional_listar_id(horario.get_id_profissional())
            servico = Service.servico_listar_id(horario.get_id_servico())

            nome_profissional = profissional.get_nome() if profissional != None else "Não informado"
            descricao_servico = servico.get_descricao() if servico != None else "Não informado"

            dados.append({
                "ID": horario.get_id(),
                "Data e hora": horario.get_data().strftime("%d/%m/%Y %H:%M"),
                "profissional": nome_profissional,
                "serviço": descricao_servico,
            })

        df = pd.DataFrame(dados)
        st.dataframe(df, hide_index=True, use_container_width=True)
