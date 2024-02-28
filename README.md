# Desafio Devedores RJ - JornadaRPA

# Sobre o projeto

Projeto realizado com base no exercício 'Desafio Devedores RJ' proposto no site: https://jornadarpa.com.br/alunos/desafios/dataextractioncrm/.

O site é uma aplicação web para treinamento de RPA, onde deve ser realizado o login, navegação e a extração de duas tabelas utilizando a paginação para mais páginas com daodos que devem ser extraídos, que deverão ser concatenadas e assim realizar um filtro nos dados para verificar clientes do Rio de Janeiro que estão com o pagamento pendente. 

Ao final da extração e tratamento dos dados, o robô irá transformar o DataFrame em um arquivo CSV que ficará salvo na pasta do projeto.

## Layout da web
![Web 1](https://github.com/Samaelpicoli/Devedores_RJ_JornadaRPA/blob/main/assets/login.PNG)

![Web 2](https://github.com/Samaelpicoli/Devedores_RJ_JornadaRPA/blob/main/assets/exemplo_tabela.PNG)


# Tecnologias Utilizadas

Python
BotCity

## Bibliotecas Utilizadas

Estão listadas no arquivo requirements.txt.

## Sobre o código

O projeto foi dividido em módulos, onde um arquivo faz o login no site inserindo usuário, senha e o cálculo que está definido em uma label (login.py), o arquivo navegacao.py realiza a navegação e a extração de ambas as tabelas e encerra o browser, 

e o arquivo dados.py é onde ele pega os DataFrames que a função de extração de tabelas irá retornar (ela é chamada 2 vezes para extrair diferentes tabelas), unirá os 2 DataFrames e fará o filtro dos dados excluindo as linhas que a coluna Pagamento está como SIM e a cidade do cliente é diferente de Rio de Janeiro, ao fim ele salvará esse novo DataFrame em um arquivo CSV na pasta do projeto.

Os arquivos são chamados dentro do arquivo main que os executa.


# Como executar o projeto
Pré-requisitos: Python 3.11+

```bash
#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
pip install -r requirements.txt
```

# Executar o projeto
python main.py

## Observações:

Por ser uma automação web baseada no código fonte do site e utilizando Xpaths, Ids e Class, pode ser que em 
algum momento a automação pare de funcionar caso o site mude.

# Autor
Samael Muniz Picoli

