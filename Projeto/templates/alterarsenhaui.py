import streamlit as st
from service import Service
import time

class AlterarSenhaUI:

    @staticmethod
    def main():

        st.header("Alterar Senha")

        admin = Service.cliente_listar_id(
            st.session_state["usuario_id"]
        )

        st.write("E-mail:", admin.get_email())

        senha = st.text_input(
            "Nova senha",
            type="password"
        )

        confirmar = st.text_input(
            "Confirmar nova senha",
            type="password"
        )

        if st.button("Alterar Senha"):

            if senha == "":
                st.error("Informe a nova senha")
                return

            if senha != confirmar:
                st.error("As senhas não são iguais")
                return

            Service.cliente_atualizar(
                admin.get_id(),
                admin.get_nome(),
                admin.get_email(),
                admin.get_fone(),
                senha
            )

            st.success(
                "Senha alterada com sucesso!"
            )

            time.sleep(1)
            st.rerun()