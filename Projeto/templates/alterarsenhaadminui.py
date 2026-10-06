import streamlit as st
import time
from service import Service

class AlterarSenhaAdminUI:
    def main():
        st.header("Alterar Senha")

        admin = Service.cliente_listar_id(st.session_state["usuario_id"])
        if admin is None:
            st.error("Administrador não encontrado")
            return

        st.write("E-mail do administrador:", admin.get_email())
        st.caption("O e-mail do administrador não pode ser alterado.")

        senha_atual = st.text_input("Senha atual", type="password")
        nova_senha = st.text_input("Nova senha", type="password")
        confirmar = st.text_input("Confirmar nova senha", type="password")

        if st.button("Alterar Senha"):
            if senha_atual != admin.get_senha():
                st.error("Senha atual incorreta")
            elif nova_senha == "":
                st.error("Informe a nova senha")
            elif nova_senha != confirmar:
                st.error("As senhas não são iguais")
            else:
                Service.cliente_alterar_senha(admin.get_id(), nova_senha)
                st.success("Senha alterada com sucesso")
                time.sleep(1)
                st.rerun()
