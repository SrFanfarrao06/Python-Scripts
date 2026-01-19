total_tempo = 0

with open("alarmes.csv", "r") as arquivo:
    next(arquivo)

    for linha in arquivo:
        try:
            serial, site, tempo = linha.strip().split(",")
            tempo = int(tempo)
        except ValueError:
            # erro no valor do tempo
            continue
        except Exception:
            # erro estrutural inesperado
            continue

        total_tempo += tempo

print("Tempo total:", total_tempo)
