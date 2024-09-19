import datetime
from src.modules.measure_consumer.app.measure_consumer_controller import MeasureConsumerController
from src.modules.measure_consumer.app.measure_consumer_usecase import MeasureConsumerUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.producers_consumers_repository_mock import ProducersConsumersRepositoryMock


class Test_MeasureConsumerControler:
    def test_measurement_measure_consumer_controller(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureConsumerUsecase(repo=repo)
        controller = MeasureConsumerController(usecase=usecase)

        request = HttpRequest(body={
            'consumer_id': '1',
            'instantly': 0.5,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['consumer_id'] == repo.consumer_measurements[-1].consumer_id
        assert response.body['instantly'] == repo.consumer_measurements[-1].instantly
        assert response.body['timestamp'] == repo.consumer_measurements[-1].timestamp
        assert isinstance(response.body['timestamp'], int)
        assert response.body['timestamp'] == int(
            datetime.datetime.now().timestamp())*1000
        assert isinstance(response.body['daily'], float)
        assert isinstance(response.body['monthly'], float)
        assert response.body['daily'] <= response.body['monthly']
        assert response.body['message'] == "the measure was created successfully"

    def test_create_consumer_controller_missing_consumer_id(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureConsumerUsecase(repo=repo)
        controller = MeasureConsumerController(usecase=usecase)

        request = HttpRequest(body={
            # 'consumer_id': '1',
            'instantly': 0.5,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field consumer_id is missing"

    def test_create_consumer_controller_missing_instantly(self):
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureConsumerUsecase(repo=repo)
        controller = MeasureConsumerController(usecase=usecase)

        request = HttpRequest(body={
            'consumer_id': '1',
            # 'instantly': 0.5,
            'timestamp': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field instantly is missing"

    def test_create_consumer_controller_missing_timestamp(self):
        # Mesmo faltando timestamp, o caso de uso gerará um timestamp
        repo = ProducersConsumersRepositoryMock()
        usecase = MeasureConsumerUsecase(repo=repo)
        controller = MeasureConsumerController(usecase=usecase)

        request = HttpRequest(body={
            'consumer_id': '1',
            'instantly': 0.5,
            # 'timestamp': int(datetime.datetime.now().timestamp())*1000,
        })

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['consumer_id'] == repo.consumer_measurements[-1].consumer_id
        assert response.body['instantly'] == repo.consumer_measurements[-1].instantly
        assert isinstance(response.body['timestamp'], int)
        assert response.body['timestamp'] == int(
            datetime.datetime.now().timestamp())*1000
        assert isinstance(response.body['daily'], float)
        assert isinstance(response.body['monthly'], float)
        assert response.body['daily'] <= response.body['monthly']

        assert response.body['message'] == "the measure was created successfully"
