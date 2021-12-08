from unittest.mock import Mock

import pytest

from libpythonbruno import github_api


@pytest.fixture
def avatar_url():
    url = github_api.buscar_avatar('brunoccalmeida')
    resposta_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/45464845?v=4'
    resposta_mock.json.return_value = {'login': 'brunoccalmeida',
                                       'id': 45464845, 'node_id': 'MDQ6VXNlcjQ1NDY0ODQ1',
                                       'avatar_url': url}
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resposta_mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('brunoccalmeida')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('brunoccalmeida')
    assert 'https://avatars.githubusercontent.com/u/45464845?v=4' == url
