import pytest

from libpythonbruno.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario',
                         ['brunoccalmeida@hotmail.com', 'foo@bar.com.br'])


def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(destinatario,
                                'luciano@python.pro.br',
                                'Cursos Python Pro',
                                'Primeira turma Guido Von Rossum aberta.')
    assert destinatario in resultado
