import csv


def solicitar_dados():
    print("===== RENTSMART =====")

    tipo = input(
        "Tipo de imóvel (apartamento/casa/estúdio): "
    ).strip().lower()

    quartos = int(input("Quantidade de quartos: "))
    vagas = int(input("Quantidade de vagas/garagem: "))

    criancas = input(
        "Possui crianças? (sim/não): "
    ).strip().lower()

    parcelas = int(
        input("Quantidade de parcelas da taxa (1 a 5): ")
    )

    return tipo, quartos, vagas, criancas, parcelas


def validar_dados(tipo, quartos, vagas, criancas, parcelas):

    if tipo not in ["apartamento", "casa", "estúdio", "estudio"]:
        return False

    if quartos < 0:
        return False

    if vagas < 0:
        return False

    if criancas not in ["sim", "não", "nao"]:
        return False

    if parcelas < 1 or parcelas > 5:
        return False

    return True


def calcular_aluguel(tipo, quartos, vagas, criancas):

    # =====================================
    # APARTAMENTO
    # =====================================
    if tipo == "apartamento":

        aluguel = 700

        # A partir de 2 quartos: + R$ 200
        if quartos >= 2:
            aluguel += 200

        # Possui garagem: + R$ 300
        if vagas >= 1:
            aluguel += 300

        # Sem crianças: desconto de 5%
        if criancas in ["não", "nao"]:
            aluguel *= 0.95

    # =====================================
    # CASA
    # =====================================
    elif tipo == "casa":

        aluguel = 900

        # A partir de 2 quartos: + R$ 250
        if quartos >= 2:
            aluguel += 250

        # Possui garagem: + R$ 300
        if vagas >= 1:
            aluguel += 300

    # =====================================
    # ESTÚDIO
    # =====================================
    elif tipo in ["estúdio", "estudio"]:

        aluguel = 1200

        # Até 2 vagas: + R$ 250
        if vagas >= 2:
            aluguel += 250

        # Cada vaga adicional: + R$ 60
        if vagas > 2:
            aluguel += (vagas - 2) * 60

    return aluguel


def calcular_taxa(parcelas):

    taxa = 2000
    valor_parcela = taxa / parcelas

    return taxa, valor_parcela


def exibir_orcamento(aluguel, taxa, valor_parcela, parcelas):

    print("\n================================")
    print("        ORÇAMENTO RENTSMART")
    print("================================")

    print(f"Aluguel mensal: R$ {aluguel:.2f}")
    print(f"Taxa contratual: R$ {taxa:.2f}")
    print(
        f"Taxa: {parcelas}x de "
        f"R$ {valor_parcela:.2f}"
    )

    print("================================")


def gerar_csv(aluguel, valor_parcela, parcelas):

    nome_arquivo = "projecao_12_meses.csv"

    with open(
        nome_arquivo,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([
            "Mês",
            "Aluguel",
            "Taxa",
            "Total"
        ])

        for mes in range(1, 13):

            if mes <= parcelas:
                taxa_mes = valor_parcela
            else:
                taxa_mes = 0

            total = aluguel + taxa_mes

            escritor.writerow([
                mes,
                f"{aluguel:.2f}",
                f"{taxa_mes:.2f}",
                f"{total:.2f}"
            ])

    print(
        f"\nArquivo '{nome_arquivo}' "
        "gerado com sucesso!"
    )


def main():

    # =====================================
    # ENTRADA E VALIDAÇÃO
    # =====================================

    while True:

        try:

            (
                tipo,
                quartos,
                vagas,
                criancas,
                parcelas
            ) = solicitar_dados()

            if validar_dados(
                tipo,
                quartos,
                vagas,
                criancas,
                parcelas
            ):
                break

            print("\nDados inválidos.")
            print("Digite os dados novamente.\n")

        except ValueError:

            print(
                "\nErro: quartos, vagas e parcelas "
                "devem ser números.\n"
            )

    # =====================================
    # CALCULAR ALUGUEL
    # =====================================

    aluguel = calcular_aluguel(
        tipo,
        quartos,
        vagas,
        criancas
    )

    # =====================================
    # CALCULAR TAXA CONTRATUAL
    # =====================================

    taxa, valor_parcela = calcular_taxa(
        parcelas
    )

    # =====================================
    # EXIBIR ORÇAMENTO
    # =====================================

    exibir_orcamento(
        aluguel,
        taxa,
        valor_parcela,
        parcelas
    )

    # =====================================
    # GERAR CSV
    # =====================================

    gerar_csv(
        aluguel,
        valor_parcela,
        parcelas
    )


# =========================================
# INÍCIO DO PROGRAMA
# =========================================

if __name__ == "__main__":
    main()