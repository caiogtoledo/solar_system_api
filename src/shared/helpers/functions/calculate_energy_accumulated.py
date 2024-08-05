import datetime


def calculate_energy_accumulated(prev_energy, instantly_power, prev_timestamp, current_timestamp):
    """
    A energia acumulada (E) é a integral da potência (P) ao longo do tempo (t). 
    Para simplificar, você pode aproximar a integral somando a potência instantânea 
    multiplicada pelo intervalo de tempo (Δt) entre as leituras.

    VERIFICAR CASOS DE DESLIGAMENTO E LIGAMENTO DO PAINEL SOLAR E OUTROS EQUIPAMENTOS CONSUMIDORES
    """
    try:
        prev_time = datetime.datetime.fromtimestamp(prev_timestamp)
        current_time = datetime.datetime.fromtimestamp(current_timestamp)

        time_diff = (current_time - prev_time).total_seconds() / 3600.0

        energy_accumulated = prev_energy + (instantly_power * time_diff)

        return energy_accumulated
    except Exception as e:
        raise e
