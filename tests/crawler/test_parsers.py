from crawler import parsers


def test_parser_movements(movements):
    expected = [{'data': '25/11/2018',
                 'movimento': ('Informação do Sistema\nPJMS - Certidão de '
                               'realização de consulta de repetiçaõ de ação')},
                {'data': '25/11/2018',
                 'movimento': ('Realizada pesquisa de suspeita de repetição '
                               'de ação\nNenhum processo localizado')},
                {'data': '22/10/2018',
                 'movimento': ('Em Cartório-p/ Escrivão/Diretor preparar '
                               'Conclusão')},
                {'data': '10/10/2018',
                 'movimento': ('Juntada de Petição Intermediária '
                               'Realizada\nNº Protocolo: WCGR.18.08405509-7 '
                               'Tipo da Petição: Manifestação do Autor '
                               'Data: 09/10/2018 14:59')},
                {'data': '05/10/2018',
                 'movimento': ('Publicado ato publicado em data da '
                               'publicação.\nRelação :0273/2018 Data da '
                               'Publicação: 08/10/2018 Número do Diário: 4126')
                 }]
    assert expected == parsers.movements(movements)
