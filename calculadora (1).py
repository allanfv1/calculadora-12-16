import datetime

def verificar_dia_trabalho():
    hoje = datetime.date.today()
    dia_do_mes = hoje.day

    while True:
        resposta = input("Você trabalhou hoje? (sim/não): ").strip().lower()
        if resposta in ["sim", "não"]:
            trabalhou_hoje = resposta == "sim"
            break
        print("Resposta inválida. Digite 'sim' ou 'não'.")

    while True:
        try:
            dia_calculado = int(input("Qual dia deseja calcular? (1-31): ").strip())
            if 1 <= dia_calculado <= 31:
                break
            print("Por favor, insira um número entre 1 e 31.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    while True:
        try:
            mes_calculado = int(input("Qual mês deseja calcular? (1-12): ").strip())
            if 1 <= mes_calculado <= 12:
                break
            print("Por favor, insira um número entre 1 e 12.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    while True:
        try:
            ano_calculado = int(input("Qual ano deseja calcular? (ex: 2025): ").strip())
            if ano_calculado >= 1:
                break
            print("Por favor, insira um ano válido.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    par_ou_impar = "par" if dia_calculado % 2 == 0 else "ímpar"

    # Ajuste na lógica para alternar corretamente trabalho e folga
    diferenca_dias = (dia_calculado - dia_do_mes) % 2
    trabalha_no_dia = (trabalhou_hoje and diferenca_dias == 0) or (not trabalhou_hoje and diferenca_dias == 1)

    status_trabalho = "Trabalho" if trabalha_no_dia else "Folga"

    # Determinar o dia da semana em português
    dias_da_semana = {
        "Monday": "Segunda-feira",
        "Tuesday": "Terça-feira",
        "Wednesday": "Quarta-feira",
        "Thursday": "Quinta-feira",
        "Friday": "Sexta-feira",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }

    data_calculada = datetime.date(ano_calculado, mes_calculado, dia_calculado)
    dia_semana = data_calculada.strftime("%A")
    dia_semana_portugues = dias_da_semana[dia_semana]

    print(f"O dia {dia_calculado}/{mes_calculado}/{ano_calculado} ({dia_semana_portugues}) é um dia {par_ou_impar}.")
    print(f"No dia {dia_calculado}/{mes_calculado}/{ano_calculado}, você terá: {status_trabalho}.")

    if trabalha_no_dia:
        print("Bom trabalho!")
    else:
        print("Boa folga!")

if __name__ == "__main__":
    verificar_dia_trabalho()

