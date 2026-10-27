import streamlit as st
import pandas as pd
from service import Service

class ListarHorariosNaoConfirmadosHojeUI:
    @staticmethod
    def main():
        st.header("Horários não confirmados de hoje")

        horarios = Service.horario_listar_nao_confirmados_hoje()
        horarios = sorted(horarios, key=lambda horario: horario.get_data())

        if len(horarios) == 0:
            st.write("Nenhum horário não confirmado para hoje.")
            return

        dados = []
        for horario in horarios:
            cliente = Service.cliente_listar_id(horario.get_id_cliente())
            servico = Service.servico_listar_id(horario.get_id_servico())
            profissional = Service.profissional_listar_id(horario.get_id_profissional())

            nome_cliente = cliente.get_nome() if cliente != None else "Não informado"
            descricao_servico = servico.get_descricao() if servico != None else "Não informado"
            nome_profissional = profissional.get_nome() if profissional != None else "Não informado"

            dados.append({
                "id": horario.get_id(),
                "data e hora": horario.get_data().strftime("%d/%m/%Y %H:%M"),
                "cliente": nome_cliente,
                "serviço": descricao_servico,
                "profissional": nome_profissional
            })

        df = pd.DataFrame(dados)
        st.dataframe(df, hide_index=True, use_container_width=True)