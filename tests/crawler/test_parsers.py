from crawler import parsers


class TestFirstGradeProcess:
    def test_parser_movements_return_correct_list(self, movements):
        expected = [
            {'data': '25/11/2018',
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

    def test_parser_process_parts_return_correct_list(self, parts):
        expected = [
            [{'Autora': 'Leidi Silva Ormond Galvão'},
             {'Advogada': 'Adriana Catelan Skowronski'},
             {'Advogada': 'Ana Silvia Pessoa Salgado de Moura'}],
            [{'Autora': 'Melissa Chaves Miranda'},
             {'Advogada': 'Adriana Catelan Skowronski'},
             {'Advogada': 'Ana Silvia Pessoa Salgado de Moura'}],
            [{'Autora': 'Ruzymar Campos de Oliveira'},
             {'Advogada': 'Adriana Catelan Skowronski'},
             {'Advogada': 'Ana Silvia Pessoa Salgado de Moura'}],
            [{'Réu': 'Estado de Mato Grosso do Sul'},
             {'RepreLeg': 'Procuradoria Geral do Estado de Mato Grosso do Sul'}
             ]
        ]
        assert expected == parsers.parts(parts)

    def test_parser_general_data_return_correct_dict(self, general_data):
        expected = {'Classe': 'Procedimento Comum Cível', 'Área': 'Cível',
                    'Assunto': 'Enquadramento',
                    'Distribuição': '30/07/2018 às 12:39 - Automática',
                    'Juiz': 'Zidiel Infantino Coutinho',
                    'Valor da ação': 'R$ 10.000,00'}
        assert expected == parsers.general_data(general_data)

    def test_parser_return_correct_keys(self, process):
        expected_keys = ['Dados do processo', 'Partes do processo',
                         'Movimentações']

        actual = parsers.process(process)
        assert expected_keys == list(actual.keys())

    def test_parser_process_not_found_and_return_empty_values(
        self, process_not_found
    ):
        expected = {'Dados do processo': {}, 'Partes do processo': [],
                    'Movimentações': []}

        actual = parsers.process(process_not_found)
        assert expected == actual
