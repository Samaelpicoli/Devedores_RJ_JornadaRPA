def realizar_login(bot, By ,timeout, site, usuario, senha):
    
    #Essa função realiza o login no site, inserindo usuário e senha
    #e realiza o cálculo que esta no escopo do projeto e o insere 
    #para assim acessar o sistema.
    try:
        bot.browse(site)
        bot.maximize_window()
        input_usuario = bot.find_element(by=By.ID, selector='user', waiting_time=timeout, ensure_clickable=True)
        input_usuario.send_keys(usuario)
        input_senha = bot.find_element(selector='pass', by=By.ID, waiting_time=timeout)
        input_senha.send_keys(senha)
        calculo_label = bot.find_element(selector='lbltipAddedComment', by=By.ID).text
        calculo_label_split = calculo_label.split('+')
        primeiro_numero = calculo_label_split[0]
        segundo_numero = calculo_label_split[1]
        resultado_soma = int(primeiro_numero) + int(segundo_numero)
        input_calculo = bot.find_element(selector='cap', by=By.ID)
        input_calculo.send_keys(str(resultado_soma))
        botao_acessar = bot.find_element(selector='button.btn.btn-primary.btn-block', by=By.CSS_SELECTOR)
        botao_acessar.click()

    except Exception as error:
        print(f'Erro durante a realização do login: {error}')
        raise Exception('Erro durante a realização do login.')







