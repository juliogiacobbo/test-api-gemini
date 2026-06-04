from unittest.mock import MagicMock


def test_perguntar_retorna_texto_da_resposta(terminal02, mocker):
    """perguntar_ao_gemini() deve retornar o texto que veio da API."""
    mock_resposta = MagicMock()
    mock_resposta.text = "Paris"
    mocker.patch.object(terminal02.cliente.models, "generate_content", return_value=mock_resposta)

    resultado = terminal02.perguntar_ao_gemini("Qual a capital da França?")

    assert resultado == "Paris"


def test_loop_encerra_ao_digitar_sair(terminal02, mocker):
    """main() deve encerrar quando o usuário digitar 'sair'."""
    mocker.patch("builtins.input", side_effect=["sair"])
    mocker.patch("builtins.print")

    terminal02.main()  # se o loop não encerrar, o teste vai travar aqui
