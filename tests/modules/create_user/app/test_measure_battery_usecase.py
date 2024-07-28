import pytest

from src.modules.measure_battery.app.measure_battery_usecase import MeasureBatteryUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock


class Test_CreateUserUsecase:

    def test_create_battery_measurement(self):
        repo = BatteryRepositoryMock()
        usecase = MeasureBatteryUsecase(repo)

        battery_measurement = usecase(
            battery_id="2",
            soc=0.50,
            voltage=0.5,
            current=0.5,
            temperature=30.0
        )

        assert repo.battery_measurements[-1] == battery_measurement

    # def test_create_user_invalid_name(self):
    #     repo = BatteryRepositoryMock()
    #     usecase = MeasureBatteryUsecase(repo)

    #     with pytest.raises(EntityError):
    #         user = usecase(name="V", email="branco@branco.branco")

    # def test_create_user_invalid_email(self):
    #     repo = UserRepositoryMock()
    #     usecase = CreateUserUsecase(repo)

    #     with pytest.raises(EntityError):
    #         user = usecase(name="Vitor Choueri", email="branco@brancobranco")


