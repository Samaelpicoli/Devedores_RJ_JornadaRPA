import pandas as pd

def primeira_navegacao(bot, By, timeout):

    #Essa função realiza a primeira navegação no site
    #para acessar a primeira tabela que o robô vai extrair.
    try:
        botao_faturamento = bot.find_element(selector='//*[@id="navcol-2"]/ul/li[2]/div/a', by=By.XPATH, waiting_time=timeout, ensure_clickable=True)
        botao_faturamento.click()
        botao_pagamentos = bot.find_element(selector='//*[@id="navcol-2"]/ul/li[2]/div/div/a[1]', by=By.XPATH, waiting_time=timeout, ensure_clickable=True)
        botao_pagamentos.click()
    
    except Exception as error:
        print(f'Erro durante a navegação inicial no site: {error}')
        raise Exception('Erro durante a navegação inicial no site.')

def extracao_tabelas(bot, By, timeout, table_to_dict, nome_df):

    #Essa função realiza a extração das tabelas, realizando a paginação no site
    #para extrair os dados, utilizando o table_to_dict que faz a extração, e adiciono
    #na lista_tabela, após isso faço uma outra conversão para uma outra lista
    #e assim crio o DataFrame com o nome que quero passar, e retorno o DF.
    try:
        botao_proximo = bot.find_element('datatable_next', By.ID, waiting_time=timeout ,ensure_clickable=True)
        lista_tabela = []
        botao_desabilitado = bot.find_element('li#datatable_next.paginate_button.page-item.next.disabled', By.CSS_SELECTOR, waiting_time=3000)
        while not botao_desabilitado:

                botao_desabilitado = bot.find_element('li#datatable_next.paginate_button.page-item.next.disabled', By.CSS_SELECTOR, waiting_time=3000)
                tabela = bot.find_element('datatable', By.ID, ensure_visible=True)
                tabela_dict = table_to_dict(table=tabela)
                lista_tabela.append(tabela_dict)
                bot.scroll_down(clicks=10)
                botao_proximo = bot.find_element('datatable_next', By.ID, ensure_clickable=True)
                botao_proximo.click()

        # Cria uma lista vazia para armazenar todos os dicionários
        dados_concatenados = []
        # Itera sobre a lista de listas de dicionários e armazena cada dicionário na lista concatenada
        for lista in lista_tabela:
            for dicionario in lista:
                dados_concatenados.append(dicionario)

        # Cria o DataFrame do pandas a partir da lista concatenada
        nome_df = pd.DataFrame(dados_concatenados)
        return nome_df
    
    except Exception as error:
        print(f'Erro durante a extração das tabelas no site: {error}')
        raise Exception('Erro durante a extração das tabelas no site.')

def segunda_navegacao(bot, By, timeout):
    
    #Essa funçaõ realiza a segunda navegação no site para extrair a segunda tabela.
    try:
        bot.scroll_up(clicks=10)
        botao_cadastros = bot.find_element('//*[@id="navcol-2"]/ul/li[1]/div/a', By.XPATH, waiting_time=timeout, ensure_clickable=True)
        botao_cadastros.click()
        botao_clientes = bot.find_element('//*[@id="navcol-2"]/ul/li[1]/div/div/a[1]', By.XPATH, waiting_time=timeout, ensure_clickable=True)
        botao_clientes.click()

    except Exception as error:
        print(f'Erro durante a navegação no site: {error}')
        raise Exception('Erro durante a navegação no site.')

def encerra_browser(bot, By, timeout):
    
    #Essa função fecha o browser.
    try:
        bot.browse('https://jornadarpa.com.br/alunos/desafios/dataextractioncrm/desafio_crm_menu.html')
        botao_faturamento = bot.find_element(selector='//*[@id="navcol-2"]/ul/li[2]/div/a', by=By.XPATH, waiting_time=timeout, ensure_clickable=True)
        bot.stop_browser()
    except Exception as error:
        print(f'Erro ao fechar o browser: {error}')
        raise Exception('Erro ao fechar o browser.')