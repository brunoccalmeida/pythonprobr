from libpythonbruno.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Bruno', email='brunothetav@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Bruno', email='brunothetav@hotmail.com'),
                Usuario(nome='Luciano', email='brunothetav@hotmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
