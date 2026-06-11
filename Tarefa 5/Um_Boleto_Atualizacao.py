"""2. Um Boleto
Escreva a classe Boleto e a enumeração Pagamento de acordo com o diagrama UML apresentado abaixo.
• A classe deve ter como atributos os dados de um boleto com informações sobre código de barras, datas, valores
e situação de pagamento;
• O construtor da classe recebe os dados iniciais de um boleto;
• O método Pagar registra o valor pago para o boleto que pode ser menor ou igual ao valor do boleto;
• O método Situacao retorna a situação de pagamento do boleto que pode ser: Em Aberto, quando o pagamento
ainda não foi realizado; Pago Parcial, quando o valor pago for menor que o valor do boleto; ou Pago, quando o
valor do pagamento corresponder ao valor do boleto;
• O método ToString deve retornar um texto com os atributos do objeto;
• A enumeração Pagamento é usada para listar os possíveis valores das situações de pagamento de um boleto.
• Inclua métodos de acesso na classe para permitir alterar e recuperar os dados de um boleto (não apresentados
no diagrama.

Escreva a classe BoletoUI, de acordo com o diagrama, para manter uma lista de boletos e realizar as operações:
• Main inicia a aplicação mostrando um menu de opções em loop, até que a opção
“Sair” seja selecionada;
• Menu deve mostrar as opções do usuário: inserir, listar, atualizar, excluir, boletos
em aberto, boletos pagos, boletos a vencer, boletos vencidos, pagar boleto e
sair;
• Inserir solicita os dados de um boleto e insere na lista;
• Listar mostra todos os boletos cadastrados;
• Atualizar atualiza os dados de um boleto;
• Excluir remove um boleto da lista;
• BoletosEmAberto mostra os boletos não pagos;
• BoletosPagos mostra os boletos pagos parcial e totalmente;
• BoletosAVencer mostra os boletos não pagos que não venceram ainda;
• BoletosVencidos mostra os boletos não pagos que já venceram;
• PagarBoleto permite informar o pagamento de um bolero em aberto."""


from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, codigo, emissao, vencimento, valor):
        self.codBarras = codigo
        self.dateEmissao = emissao
        self.dataVencimento = vencimento
        self.dataPago = None
        self.valorBoleto = valor
        self.situacao = Pagamento.EmAberto
    def Pagar(self, valor):
        if self.situacao == Pagamento.Pago:
            print("Boleto já foi pago.")
            return
        if valor <= 0:
            print("Valor de pagamento deve ser positivo.")
            return
        if valor > self.valorBoleto:
            print("Valor de pagamento ultrapassa o valor atual do boleto")
            return
        self.valorBoleto -= valor
        self.dataPago = datetime.now()