import pytest

from libpythonbruno.spam.enviador_de_email import Enviador
from libpythonbruno.spam.main import EnviadorDeSpam
from libpythonbruno.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Bruno', email='brunothetav@hotmail.com'),
            Usuario(nome='Luciano', email='brunothetav@hotmail.com')
        ],
        [
            Usuario(nome='Bruno', email='brunothetav@hotmail.com')
        ]
    ]

)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('brunoccalmeida@hotmail.com',
                                   'Curso Python Pro',
                                   'Confira os módulos fantásticos')
    assert len(usuarios) == enviador.qde_email_enviados
