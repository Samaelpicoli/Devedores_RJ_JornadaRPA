from botcity.web import WebBot, Browser, By, table_to_dict
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class DesafioDevedores:

    """
    Essa classe contém as funcionalidades do RPA Devedores RJ.
    Mais informações: 
    https://jornadarpa.com.br/alunos/desafios/dataextractioncrm/
    """

    def __init__(self, url: str):
        """Inicializa a classe e seus atributos, bem como o 
        WebDriver utilizado.

        Args:
            url (str): url do site que o robô deverá acessar.
        """
        self._url = url
        self._bot = WebBot()
        self._bot.headless = False
        self._bot.browser = Browser.CHROME
        self._bot.driver_path = ChromeDriverManager().install()
        self._bot.browse(url)
        self._bot.maximize_window()
        self.timeout = 40000
        self.etapa_navegacao = 'inicial'

    def login(self, usuario, senha):
        """Realiza o login para acesso a página.

        Args:
            usuario (str): usuário para realizar o login.
            senha (str): senha para realizar o login.

        Raises:
            Exception: Erro durante a etapa de login.
        """
        try:
            elemento_usuario = self._bot.find_element(by=By.ID, 
                                                      selector='user', 
                                                      waiting_time=self.timeout
                                                      ,ensure_clickable=True)
            
            elemento_usuario.send_keys(usuario)

            elemento_senha = self._bot.find_element(selector='pass', 
                                                    by=By.ID,
                                                    waiting_time=self.timeout)
            
            elemento_senha.send_keys(senha)
            resultado = self._calculo_login()
            elemento_calculo = self._bot.find_element(selector='cap', 
                                                      by=By.ID)
            
            elemento_calculo.send_keys(str(resultado))

            seletor = 'button.btn.btn-primary.btn-block'
            botao_acessar = self._bot.find_element(selector=seletor, 
                                                   by=By.CSS_SELECTOR)
            
            botao_acessar.click()
        except Exception as error:
            print(f'Erro durante a realização do login: {error}')
            raise Exception('Erro durante a realização do login.')

    def _calculo_login(self):
        """Realiza um cálculo solicitado pelo login para conseguir 
        acessar o site.

        Returns:
            int resultado_soma: resultado do cálculo na etapa de login
        """
        calculo_label = self._bot.find_element(selector='lbltipAddedComment',
                                               by=By.ID).text
        
        calculo_label_split = calculo_label.split('+')
        primeiro_numero = calculo_label_split[0]
        segundo_numero = calculo_label_split[1]
        resultado_soma = int(primeiro_numero) + int(segundo_numero) 
        return resultado_soma
    
    def navegacao_inicial(self):
        """Esse método realiza a primeira navegação no site para acessar 
        a primeira tabela que o robô vai extrair.

        Raises:
            Exception: Erro durante a navegação inicial.
        """
        try:
            botao_faturamento = self._bot.find_element(
                selector='//*[@id="navcol-2"]/ul/li[2]/div/a', 
                by=By.XPATH, waiting_time=self.timeout, ensure_clickable=True)
            
            botao_faturamento.click()

            botao_pagamentos = self._bot.find_element(
                selector='//*[@id="navcol-2"]/ul/li[2]/div/div/a[1]', 
                by=By.XPATH, waiting_time=self.timeout, ensure_clickable=True)
            
            botao_pagamentos.click()
        except Exception as error:
            print(f'Erro durante a navegação inicial no site: {error}')
            raise Exception('Erro durante a navegação inicial no site.')
        
    def navegacao_final(self):
        """Esse método realiza a navegação final para acessar a 
        segunda tabela que o robô vai extrair.

        Raises:
            Exception: Erro durante a navegação finals.
        """
        try:
            self._bot.scroll_up(clicks=10)

            botao_cadastros = self._bot.find_element(
                '//*[@id="navcol-2"]/ul/li[1]/div/a', 
                By.XPATH, waiting_time=self.timeout, ensure_clickable=True)
            
            botao_cadastros.click()

            botao_clientes = self._bot.find_element(
                '//*[@id="navcol-2"]/ul/li[1]/div/div/a[1]', 
                By.XPATH, waiting_time=self.timeout, ensure_clickable=True)
            
            botao_clientes.click()
        except Exception as error:
            print(f'Erro durante a navegação no site: {error}')
            raise Exception('Erro durante a navegação no site.')
        
    def extracao_tabela(self, nome_df):
        """Essa função realiza a extração das tabelas, 
        realizando a paginação no site para extrair os dados, 
        utilizando o table_to_dict que faz a extração, e adiciono
        na lista_tabela, após isso através de um loop faço uma 
        outra conversão para uma nova lista que conterá os dicts
        e assim crio o DataFrame com o nome que quero passar, e retorno o DF.

        Args:
            nome_df (str): Nome do DataFrame que será armazenado no processo.
        Raises:
            Exception: Erro durante a extração das tabelas no site.

        Returns:
            nome_df (DataFrame): será retornado o DataFrame criado 
            durante a extração das tabelas.
        """
        try:
            botao_proximo = self._bot.find_element('datatable_next', By.ID, 
                                                   waiting_time=self.timeout,
                                                   ensure_clickable=True)
            
            lista_tabela = []
            botao_desabilitado = self._bot.find_element(
                'li#datatable_next.paginate_button.page-item.next.disabled', 
                By.CSS_SELECTOR, waiting_time=3000)
            
            while not botao_desabilitado:
                botao_desabilitado = self._bot.find_element(
                    'li#datatable_next.paginate_button.page-item.next.disabled', 
                    By.CSS_SELECTOR, waiting_time=3000)
                
                tabela = self._bot.find_element('datatable', By.ID, 
                                                ensure_visible=True)
                
                tabela_dict = table_to_dict(table=tabela)
                lista_tabela.append(tabela_dict)
                self._bot.scroll_down(clicks=10)
                botao_proximo = self._bot.find_element('datatable_next', 
                                                       By.ID, 
                                                       ensure_clickable=True)
                
                botao_proximo.click()

            # Cria uma lista vazia para armazenar todos os dicionários
            dados_concatenados = []
            # Itera sobre a lista de listas de dicionários e armazena cada 
            # dicionário na lista concatenada
            for lista in lista_tabela:
                for dicionario in lista:
                    dados_concatenados.append(dicionario)
    
            # Cria o DataFrame do pandas a partir da lista concatenada
            nome_df = pd.DataFrame(dados_concatenados)
            return nome_df
        
        except Exception as error:
            print(f'Erro durante a extração das tabelas no site: {error}')
            raise Exception('Erro durante a extração das tabelas no site.')
        
    def encerra_browser(self):
        """Esse método encerra o navegador e deleta a 
        instância do ChromeDriver.

        Raises:
            Exception: Erro durante a finalização do driver.
        """
        try:
            self._bot.browse(self._url)            
            self._bot.stop_browser()
        except Exception as error:
            print(f'Erro ao fechar o browser: {error}')
            raise Exception('Erro ao fechar o browser.')
   
    def processar_e_salvar_dados(self, df, df_2):
        """
        Realiza a concatenação e filtragem dos dados dos dataframes e 
        salva o resultado em um arquivo CSV.

        Args:
            df (DataFrame): Primeiro dataframe a ser concatenado.
            df_2 (DataFrame): Segundo dataframe a ser concatenado.
        """
        try:
            # Concatena os dataframes
            df_concatenado = pd.concat([df, df_2], axis=1)

            # Filtra os dados para pagamentos pendentes de clientes 
            # do Rio de Janeiro
            df_final = df_concatenado.loc[
                (df_concatenado['cidade'] == 'Rio de Janeiro') 
                & (df_concatenado['pago'] == 'N')
            ]

            # Salva o dataframe filtrado em um arquivo CSV
            df_final.to_csv('clientes_devedores_rj.csv', sep=',', 
                            encoding='utf-8', index=False)
            print(df_final)
            print("Dados processados e salvos com sucesso.")
        except (Exception, ValueError) as error:
            print(f'Erro durante a união e filtro dos dados gerados: {error}')
            raise Exception('Erro durante a união e filtro dos dados gerados')