# Analisador Sintático com Inteligência Artificial

Este projeto implementa um **analisador sintático** utilizando conceitos de **Inteligência Artificial** para processar sentenças e identificar sua estrutura gramatical. O código foi desenvolvido como parte do curso **CS50 - Introduction to Artificial Intelligence with Python**, oferecido pela **Harvard University**.

## Tecnologias Utilizadas  
- **Linguagem**: Python 3.11  
- **Bibliotecas**: NLTK 
- **Ferramentas**: Git
- **Conceitos de IA**: CFG (Gramática Livre de Contexto), Tokenização, Árvores de Análise Sintática 

## Estrutura do Projeto

A pasta contém os seguintes arquivos:

- **`parser.py`**: Implementação do analisador sintático, capaz de identificar a estrutura hierárquica de uma sentença.
- **`sentences`**: Conjunto de sentenças de exemplo usadas para testar o analisador.

## Features  
- Tokenização personalizada de sentenças.  
- Reconhecimento de estruturas gramaticais complexas (frases nominais, verbais).  
- Geração de árvores sintáticas.

## Minha Contribuição

A implementação do **analisador sintático** foi desenvolvida no arquivo `parser.py`, incluindo a identificação de substantivos, verbos e suas relações dentro da frase.

## Como Funciona o Analisador

O projeto utiliza um modelo baseado em **gramática livre de contexto (CFG)** para interpretar sentenças. O analisador segue os seguintes passos:

1. **Tokenização**: Divide a frase em palavras individuais.
2. **Identificação de classes gramaticais**: Reconhece substantivos, verbos e outras categorias.
3. **Geração da árvore sintática**: Organiza as palavras de acordo com sua função na frase.

## Instalação e Execução

1. Clone o repositório:  
   ```bash  
   git clone https://github.com/Alvaro-Sena/analisador_sintatico.git  
   ```
2. Navegue até a pasta do repositório:
   ```bash  
   cd analisador_sintatico
   ``` 
3. Instale as dependências:  
   ```bash  
   pip install -r requirements.txt  
   ```  
4. Execute o analisador:  
   ```bash  
   python parser.py  
   ```  

Em seguida, use como parametro para "Sentence:" uma frase presente na pasta sentences.

Certifique-se de que possui **Python 3** instalado no seu ambiente.

## Contato
Caso tenha dúvidas ou sugestões, entre em contato através do meu [LinkedIn](www.linkedin.com/in/alvaro-sena), [GitHub](https://github.com/Alvaro-Sena) ou [WhatsApp](https://wa.me/447356040385).
