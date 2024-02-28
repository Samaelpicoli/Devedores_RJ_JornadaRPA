from botcity.web import WebBot, Browser, By, table_to_dict
from webdriver_manager.chrome import ChromeDriverManager
import login
import navegacao
import dados

#Inicializando o WebBot
bot = WebBot()
bot.headless = False
bot.browser = Browser.CHROME
bot.driver_path = ChromeDriverManager().install()

def main():

    #Dados que serão utilizados como parâmetros nas funções
    site = 'https://jornadarpa.com.br/alunos/desafios/dataextractioncrm/login.html'
    usuario = 'aluno'
    senha = 'desafiosrpa'
    timeout = 40000

    login.realizar_login(bot, By, timeout, site, usuario, senha)

    navegacao.primeira_navegacao(bot, By, timeout)

    primeiro_df = navegacao.extracao_tabelas(bot, By, timeout, table_to_dict, 'pagamentos')

    navegacao.segunda_navegacao(bot, By, timeout)

    segundo_df = navegacao.extracao_tabelas(bot, By, timeout, table_to_dict, 'clientes')

    dados.concatenar_e_filtrar_dados(primeiro_df, segundo_df)

    navegacao.encerra_browser(bot, By, timeout)

if __name__ == '__main__':
    main()
 









