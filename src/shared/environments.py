from enum import Enum
import os

from src.shared.domain.repositories.alerts_repository_interface import IAlertsRepository
from src.shared.domain.repositories.battery_repository_interface import IBatteryRepository
from src.shared.domain.repositories.measurements_repository_interface import IMeasurementsRepository
from src.shared.domain.repositories.producers_consumers_repository_interface import IProducersConsumersRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    HOMOLOG = "HOMOLOG"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE
    mongo_uri: str
    mongo_db_name: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["ENV"] = os.environ.get("ENV") or STAGE.DOTENV.value

    def load_envs(self):
        if "ENV" not in os.environ or os.environ["ENV"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("ENV")]
        self.mongo_uri = os.environ.get("MONGO_URI")
        self.mongo_db_name = os.environ.get("DB_NAME")

    @staticmethod
    def get_alerts_repo() -> IAlertsRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.alerts_repository_mock import AlertsRepositoryMock
            return AlertsRepositoryMock
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.mongodb.alerts_repository_mongodb import AlertsRepositoryMongoDB
            return AlertsRepositoryMongoDB
        else:
            raise Exception("No repository found for this stage")

    @staticmethod
    def get_battery_repo() -> IBatteryRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.battery_repository_mock import BatteryRepositoryMock
            return BatteryRepositoryMock
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.mongodb.battery_repository_mongodb import BatteryRepositoryMongoDB
            return BatteryRepositoryMongoDB
        else:
            raise Exception("No repository found for this stage")

    @staticmethod
    def get_measurements_repo() -> IMeasurementsRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.measurements_repository_mock import MeasurementsRepositoryMock
            return MeasurementsRepositoryMock
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.mongodb.measurements_repository_mongodb import MeasurementsRepositoryMongoDB
            return MeasurementsRepositoryMongoDB
        else:
            raise Exception("No repository found for this stage")

    @staticmethod
    def get_producers_consumers_repo() -> IProducersConsumersRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock
            return ProducersConsumersRepositoryMock
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.HOMOLOG, STAGE.PROD]:
            from src.shared.infra.repositories.mongodb.producers_consumers_repository_mongodb import ProducersConsumersRepositoryMongoDB
            return ProducersConsumersRepositoryMongoDB
        else:
            raise Exception("No repository found for this stage")

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__
