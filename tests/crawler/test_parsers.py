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

        actual = parsers.process(process.html)
        assert expected_keys == list(actual.keys())

    def test_parser_process_not_found_and_return_empty_values(
        self, process_not_found
    ):
        expected = {'Dados do processo': {}, 'Partes do processo': [],
                    'Movimentações': []}

        actual = parsers.process(process_not_found.html)
        assert expected == actual


class TestSecondGradeProcess:
    def test_parser_movements_return_correct_list(self, second_movements):
        expected = [
            {'data': '28/05/2019',
             'movimento': ('Certidão Emitida\nCERTIDÃO Certifico que foi '
                           'interposto Agravo em Recurso Especial da decisão '
                           'de fls. 433-437. Certifico, ainda, que esse '
                           'Agravo, foi recebido, no carimbo, em 27/05/2019, '
                           'devido a problemas no saj/protocolo. Maceió, 28 '
                           'de maio de 2019 Eleonora Paes Cerqueira de França '
                           'Diretora Adjunta Especial de Assuntos Judiciários '
                           'Fernanda Luiza de Albuquerque Brasil Lins Técnica '
                           'Judiciária')},
            {'data': '28/05/2019',
             'movimento': 'Juntada de Petição de\nAgravo'},
            {'data': '28/05/2019',
             'movimento': 'Incidente Cadastrado\nSeq.: 50 - Agravo'},
            {'data': '03/05/2019',
             'movimento': ('Certidão Emitida\nCERTIFICO que foi '
                           'disponibilizada no Diário da Justiça Eletrônico '
                           'do Tribunal de Justiça de Alagoas em 03/05/2019 '
                           'a decisão de fls. 433-437 e considerada publicada '
                           'em 06/05/2019, nos termos do Artigo 4º, § 3º, da '
                           'Lei nº 11.419/2006. Maceió, 03 de maio de 2019 '
                           'Eleonora Paes Cerqueira de França Diretora '
                           'Adjunta Especial de Assuntos Judiciários Fernanda '
                           'Luiza de Albuquerque Brasil Lins Técnica '
                           'Judiciária')},
            {'data': '03/05/2019',
             'movimento': 'Publicado\nDisponibilizado no DJE de 03/05/2019.'}]
        assert expected == parsers.movements(second_movements)

    def test_parser_process_parts_return_correct_list(self, second_parts):
        expected = [
            [{'Apelante': 'Importadora Auto Peças Ltda'},
             {'Advogada': 'Roberta Eulália V. Lyra'},
             {'Advogado': 'Andréa Lyra Maranhão'},
             {'Advogado': 'Leonardo Mafra Costa'},
             {'Advogado': 'Marina Vilela de Castro Loyola Caju'},
             {'Advogado': 'Pedro Henrique Pedrosa Nogueira'},
             {'Advogada': 'Daniela Nobre de Melo Nogueira'},
             {'Advogado': 'Rolland Marques de Meira'},
             {'Advogado': 'Antônio Jakson M. S. Cavalcanti'},
             {'Advogada': 'Flávia Nobre de Melo'},
             {'Advogada': 'Daniella Mafra Barbosa'},
             {'Advogado': 'Carlos Pedrosa Mauricio da Rocha'}],
            [{'Apelado': 'Manuel Francisco Gonzaga Filho'},
             {'Advogado': 'Petrúcio Pereira Guedes'},
             {'Advogada': 'Priscila Araújo Guedes'},
             {'Advogado': 'Rodrigo Fireman Barros'}]
        ]

        assert expected == parsers.parts(second_parts)

    def test_parser_general_data_return_correct_dict(self,
                                                     second_general_data):
        expected = {'Classe': 'Apelação', 'Área ': 'Cível',
                    'Assunto': 'Perdas e Danos',
                    'Distribuição': 'Vice-Presidência',
                    'Relator': 'DES. SEBASTIÃO COSTA FILHO',
                    'Valor da ação': '380,00'}

        assert expected == parsers.general_data(second_general_data)
