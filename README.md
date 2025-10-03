Sistema Bancário em Python
Status: Concluído ✔️

📝 Sobre o Projeto
Este projeto foi desenvolvido como parte de um desafio de código da Digital Innovation One (DIO). O objetivo era construir um sistema bancário funcional via linha de comando, aplicando conceitos de desenvolvimento em Python em diferentes níveis de complexidade.

O projeto evoluiu em três etapas principais, demonstrando uma progressão de um script simples para um pacote Python estruturado:

Versão 1: Sistema Procedural: A primeira versão foi construída com lógica procedural, utilizando funções e dicionários para gerenciar as operações de depósito, saque e extrato.

Versão 2: Refatoração para POO: O sistema foi completamente refatorado para o paradigma de Programação Orientada a Objetos (POO). Seguindo um diagrama UML, foram criadas classes para modelar as entidades do sistema (Cliente, Conta, Transacao, etc.), aplicando conceitos como herança, encapsulamento e polimorfismo.

Versão 3: Empacotamento do Projeto: A versão POO foi estruturada como um pacote Python distribuível, utilizando setuptools para criar um arquivo setup.py e permitir a geração de distribuições (sdist e wheel).

✨ Funcionalidades
O sistema permite as seguintes operações bancárias:

[x] Depositar: Adicionar valores à conta.

[x] Sacar: Realizar saques com validação de saldo, limite de valor e número de saques diários.

[x] Exibir Extrato: Listar todas as transações realizadas e o saldo atual.

[x] Criar Usuário: Cadastrar novos clientes.

[x] Criar Conta Corrente: Vincular novas contas a usuários existentes.

[x] Listar Contas: Exibir todas as contas cadastradas.

🚀 Conceitos e Tecnologias Aplicadas
Programação Orientada a Objetos
Abstração e Encapsulamento: Modelagem das entidades do sistema em classes para representar o domínio do problema de forma coesa e segura.

Herança: Utilização de classes base e derivadas (PessoaFisica herda de Cliente, ContaCorrente herda de Conta) para reaproveitar código e especializar comportamentos.

Polimorfismo: Sobrescrita de métodos para adaptar funcionalidades, como as regras de negócio específicas do saque em ContaCorrente.

Empacotamento em Python
Estrutura de Pacotes: Organização do código em uma estrutura de diretórios padrão, com o uso do arquivo __init__.py.

Setuptools: Criação de um script setup.py para definir os metadados do pacote (versão, autor, dependências) e gerenciar a construção.

Tecnologias
Python 3

Git e GitHub para controle de versão.

🔧 Instalação e Uso
Pré-requisitos
Python 3.8 ou superior

Git

Passos para Execução
Clone o repositório:

Bash

git clone https://github.com/douglaspolicarpo/dio-sistema-bancario-python.git
Navegue até o diretório do projeto:

Bash

cd dio-sistema-bancario-python
(Opcional, mas recomendado) Crie e ative um ambiente virtual:

Bash

# Criar o ambiente
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate

# Ativar no Linux/Mac
source venv/bin/activate
Execute o sistema:
O arquivo principal está dentro da pasta do pacote. Para executá-lo, use o comando:

Bash

python sistema_bancario/sistema_bancario_com_python_POO.py
O menu interativo do sistema bancário será exibido no seu terminal.

👨‍💻 Autor
Douglas Policarpo

GitHub: @douglaspolicarpo

📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
