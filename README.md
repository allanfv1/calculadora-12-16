Aqui está o README para o código `calculadora.py`:

---

# Calculadora de Jornada de Trabalho 12/36

Este é um script Python que ajuda a calcular se uma pessoa estará **trabalhando** ou **de folga** em uma data específica, com base na jornada de trabalho alternada **12/36**. O código verifica se a pessoa trabalhou no dia atual e, com base nisso, calcula se ela estará de folga ou trabalhando em uma data informada pelo usuário.

## Funcionalidade

O script faz o seguinte:

1. Pergunta ao usuário se ele trabalhou no dia atual (hoje).
2. Permite ao usuário calcular se estará de **trabalho** ou de **folga** em um dia específico do mês, considerando que o ciclo de trabalho é **12 horas de trabalho seguidas de 36 horas de descanso**.
3. Informa se o dia informado é **par** ou **ímpar**.
4. Mostra o dia da semana correspondente à data informada.
5. Informa se o usuário estará trabalhando ou de folga nesse dia.

## Como Funciona

1. **Entrada de dados**:
    - O usuário informa se trabalhou no dia atual (sim/não).
    - O usuário escolhe a data (dia, mês e ano) para a qual deseja calcular se está de trabalho ou folga.
   
2. **Cálculo do dia**:
    - O script verifica a diferença entre o dia atual e o dia informado, usando a jornada **12/36**.
    - Dependendo dessa diferença e se o usuário trabalhou no dia atual, o script determina se será um **dia de trabalho** ou **folga** no dia escolhido.
   
3. **Saída**:
    - O script exibe o dia da semana em português (Segunda-feira, Terça-feira, etc.).
    - O status do dia escolhido é informado como **"Trabalho"** ou **"Folga"**.
    - O script também informa se o dia é **par** ou **ímpar**.

## Exemplo de Uso

Ao rodar o script, ele solicitará que o usuário insira se trabalhou no dia atual e pedirá para informar a data que deseja calcular.

Exemplo de interação:

```plaintext
Você trabalhou hoje? (sim/não): sim
Qual dia deseja calcular? (1-31): 15
Qual mês deseja calcular? (1-12): 5
Qual ano deseja calcular? (ex: 2025): 2025

O dia 15/5/2025 (Sexta-feira) é um dia ímpar.
No dia 15/5/2025, você terá: Trabalho.
Bom trabalho!
```

## Instalação

1. Certifique-se de ter o Python 3.x instalado em sua máquina.
2. Clone ou baixe este repositório.
3. Execute o arquivo `calculadora.py`:

```bash
python calculadora.py
```

## Contribuições

Sinta-se à vontade para melhorar o código ou sugerir novas funcionalidades. Se encontrar algum erro ou tiver sugestões, fique à vontade para abrir uma issue ou enviar um pull request.

---

Esse README fornece uma visão geral do funcionamento do código. Caso precise de mais informações ou ajustes, só avisar!
