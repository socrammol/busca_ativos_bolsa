# API PARA BUSCA DE ATIVOS NA BOLSA


### Tecnologias

- Python 3.9
- Django




### Funcionalidades

#### Carregando a aplicação 
Necessario ter o docker instaldo na maquina , na raiz do projeto , rodar o comando docker-compose up , se nao quiser acompanhar os logs colocar sufixo -d

#### Carga de dados na aplicação
Apos o termino da carga do docker , acessar o link http://127.0.0.1:8000/ 
o mesmo tem uma nterface basica , 
onde sera solicitado para criar um usuario, 
este possui os dados de configuração onde que :
#
Username e o nome do usuario, 
Ticker e o ticker que se deseja buscar na bolsa de valores, 
Tempomonitoramento e referente ao tempo (a partir do dia atual) 
em que se deseja pegar o inicio dos dados,
Terminomonitoramentoemdias  e referente ao tempo 
(a partir do dia atual) em que se deseja pegar o termino dos dados, Iniciomonitoramentoemdias e o tempo em minutos que o scheduler ira rodar , para pegar os dados da bolsa,Email e o email informado para recebimento e envio dos dados
Valormenor seria o menor valor aceitavel de um ativo,
Valormaior seria o maior valor aceitavel de um ativo 

