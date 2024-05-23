from desafio import DesafioDevedores
from config import site, usuario, senha, loop, state


while loop == 'ON':

    match state:
        
        case 'INITIALIZATION':
            bot = DesafioDevedores(site)
            bot.login(usuario, senha)
            state = 'GET'
            continue

        case 'GET':
            if bot.etapa_navegacao == 'inicial':
                bot.navegacao_inicial()
                state = 'PROCESS'
                continue
            elif bot.etapa_navegacao == 'final':
                bot.navegacao_final()
                state = 'PROCESS'
                continue
            else:
                state = 'END'
                continue
        
        case 'PROCESS':
            if bot.etapa_navegacao == 'inicial':
                pagamentos_pendentes = bot.extracao_tabela('pagamentos')
                state = 'GET'
                bot.etapa_navegacao = 'final'
                continue
            
            elif bot.etapa_navegacao == 'final':
                estado = bot.extracao_tabela('estados')
                state = 'GET'
                bot.etapa_navegacao = None
                continue    

        case 'END':
            bot.processar_e_salvar_dados(pagamentos_pendentes, estado)
            bot.encerra_browser()
            loop = 'OFF'
        
print('FIM')



 









