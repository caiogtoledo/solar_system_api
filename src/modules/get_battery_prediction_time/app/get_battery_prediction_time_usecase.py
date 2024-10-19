from datetime import datetime, timedelta
from typing import Tuple
from src.shared.domain.entities.battery_prediction_time import BatteryPredictionTime
from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetBatteryPredictionTimeUsecase:
    def __init__(self,
                 producersConsumersRepo: IProducersConsumersRepository,
                 batteryRepo: IBatteryRepository
                 ):
        self.producersConsumersRepo = producersConsumersRepo
        self.batteryRepo = batteryRepo
        self.battery_capacity = 2000  # mAh

    def __call__(self, battery_id: str, k_records: int) -> Tuple[int, int]:
        last_measure_battery = self.batteryRepo.get_last_battery_measurement_by_id(
            battery_id=battery_id)

        if last_measure_battery is None:
            raise NoItemsFound(f"battery: {battery_id}")

        all_solar_panels = self.producersConsumersRepo.get_all_solar_panels_measurements(
            records=k_records)
        all_consumers = self.producersConsumersRepo.get_all_consumers_measurements(
            records=k_records)

        # Inicializa variáveis de simulação
        current_soc = last_measure_battery.soc
        current_voltage = last_measure_battery.voltage

        # Simulação de consumo e produção baseado nos dados históricos (médias)
        avg_production = sum(panel.instantly for panel in all_solar_panels) / \
            len(all_solar_panels) if all_solar_panels else 0
        avg_consumption = sum(consumer.instantly for consumer in all_consumers) / \
            len(all_consumers) if all_consumers else 0

        # Calcula a corrente líquida (produção menos consumo) em Watts
        net_power = avg_production - avg_consumption  # em Watts

        # Converte para corrente (A): P = V * I  => I = P / V
        net_current = net_power / current_voltage if current_voltage else 0  # em Amperes

        # Se a corrente líquida for zero, não há mudança no SoC
        if net_current == 0:
            raise ValueError(
                "A bateria não está carregando nem descarregando.")

        # Calcula a taxa de variação do SoC
        soc_delta_per_hour = (net_current * 1000) / \
            self.battery_capacity  # delta por hora

        # Calcula o tempo para chegar a 100% ou 0%
        is_charging = soc_delta_per_hour > 0
        if is_charging:  # Carregando
            hours_to_full = (1.0 - current_soc) / soc_delta_per_hour
            time_remaining = timedelta(hours=hours_to_full)
        else:  # Descarregando
            hours_to_empty = current_soc / abs(soc_delta_per_hour)
            time_remaining = timedelta(hours=hours_to_empty)

        # Extrai dias, horas e minutos do tempo restante
        total_seconds = int(time_remaining.total_seconds())
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60

        time_predict = BatteryPredictionTime(
            battery_id=battery_id,
            days=days,
            hours=hours,
            minutes=minutes,
            charging=is_charging
        )

        return time_predict
