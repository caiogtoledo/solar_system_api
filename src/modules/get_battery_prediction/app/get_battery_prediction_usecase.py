

from typing import List, Optional
from datetime import datetime, timedelta

from src.shared.domain.entities.battery import Battery
from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetBatteryPredictionUsecase:
    def __init__(self,
                 producersConsumersRepo: IProducersConsumersRepository,
                 batteryRepo: IBatteryRepository
                 ):
        self.producersConsumersRepo = producersConsumersRepo
        self.batteryRepo = batteryRepo
        self.battery_capacity = 2000  # mAh

    def __call__(self, battery_id: str, k_records: int) -> List[Battery]:
        # k_records é a quantidade de registros que vamos contabilizar
        # para a média do calculo para estimar a duração da bateria

        last_measure_battery = self.batteryRepo.get_last_battery_measurement_by_id(
            battery_id=battery_id)

        if last_measure_battery == None:
            raise NoItemsFound(f"battery: {battery_id}")

        all_solar_panels = self.producersConsumersRepo.get_all_solar_panels_measurements(
            records=k_records)
        all_consumers = self.producersConsumersRepo.get_all_consumers_measurements(
            records=k_records)

        # Inicializa variáveis de simulação
        current_soc = last_measure_battery.soc
        battery_projections = []
        current_time = datetime.now()

        # Definimos um intervalo de 1 hora para projeções futuras (pode ser ajustado)
        projection_interval = timedelta(hours=1)

        # Quantidade de horas que queremos projetar
        simulation_duration = 12
        # delta_time será 1 hora, mas pode ser ajustado
        delta_time = 1  # em horas

        for hour in range(int(simulation_duration/delta_time)):
            # Simula o tempo futuro em que a predição está ocorrendo
            future_timestamp = current_time + (projection_interval * hour)

            # Simulação de consumo e produção baseado nos dados históricos (médias)
            avg_production = sum(panel.instantly for panel in all_solar_panels) / \
                len(all_solar_panels) if all_solar_panels else 0
            avg_consumption = sum(consumer.instantly for consumer in all_consumers) / \
                len(all_consumers) if all_consumers else 0

            # Calcula a corrente líquida (produção menos consumo) em Watts
            net_power = avg_production - avg_consumption  # em Watts

            # Converte para corrente (A): P = V * I  => I = P / V
            net_current = net_power / \
                last_measure_battery.voltage if last_measure_battery.voltage else 0  # em Amperes

            # Atualiza o SoC com base na corrente líquida e capacidade da bateria
            # net_current está em A, então multiplicamos por 1000 para mA
            soc_delta = (net_current * 1000 * delta_time) / \
                self.battery_capacity
            current_soc += soc_delta

            # Garante que o SoC não ultrapasse os limites de 0% a 100%
            if current_soc > 1.0:
                current_soc = 1.0
            elif current_soc < 0.0:
                current_soc = 0.0

            battery_projection = Battery(
                battery_id=last_measure_battery.battery_id,
                soc=current_soc,  # SoC projetado
                voltage=last_measure_battery.voltage,
                current=net_current,
                temperature=last_measure_battery.temperature,
                timestamp=int(future_timestamp.timestamp() * 1000)
            )
            battery_projections.append(battery_projection)

        last_measure: Optional[Battery] = self.batteryRepo.get_all_battery_measurements(
            battery_id)

        if last_measure is None:
            raise NoItemsFound(": battery status")

        battery_projection_with_all_history = last_measure + battery_projections

        return battery_projection_with_all_history
