from unittest.mock import Mock

import pytest

from libpythonbruno.spam.enviador_de_email import Enviador
from libpythonbruno.spam.main import EnviadorDeSpam
from libpythonbruno.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Bruno', email='brunothetav@hotmail.com'),
            Usuario(nome='Luciano', email='luciano@python.pro.br')
        ],
        [
            Usuario(nome='Bruno', email='brunothetav@hotmail.com')
        ]
    ]

)
def test_qte_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('brunoccalmeida@hotmail.com',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Bruno', email='brunoccalmeida@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('luciano@python.pro.br',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos')
    enviador.enviar.assert_called_once_with('luciano@python.pro.br',
                                            'brunoccalmeida@hotmail.com',
                                            'Curso Python Pro',
                                            'Confira os módulos fantásticos')
