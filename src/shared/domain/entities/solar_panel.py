import abc

from src.shared.helpers.errors.domain_errors import EntityError


class SolarPanel(abc.ABC):
    solar_panel_id: str
    instantly: float # W
    daily: float # KWh
    monthly: float # KWh

    def __init__(self, solar_panel_id: str, instantly: float, daily: float, monthly: float, temperature: float):
        if not self.validate_solar_panel_id(solar_panel_id):
            raise EntityError("solar_panel_id")
        self.solar_panel_id = solar_panel_id

        if not self.validate_instantly(instantly):
            raise EntityError("instantly")
        self.instantly = instantly

        if not self.validate_daily(daily):
            raise EntityError("daily")
        self.daily = daily

        if not self.validate_monthly(monthly):
            raise EntityError("monthly")
        self.monthly = monthly

    @staticmethod
    def validate_solar_panel_id(solar_panel_id: str) -> bool:
        return isinstance(solar_panel_id, str) and len(solar_panel_id) > 0

    @staticmethod
    def validate_instantly(daily: float) -> bool:
        return isinstance(daily, (int, float))

    @staticmethod
    def validate_daily(daily: float) -> bool:
        return isinstance(daily, (int, float))

    @staticmethod
    def validate_monthly(monthly: float) -> bool:
        return isinstance(monthly, (int, float))


    def __repr__(self):
        return (f"solar_panel(solar_panel_id={self.solar_panel_id}, instantly={self.instantly}, "
                f"daily={self.daily}, monthly={self.monthly}, "
        )