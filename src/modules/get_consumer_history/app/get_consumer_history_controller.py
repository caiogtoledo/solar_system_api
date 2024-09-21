
from src.modules.get_consumer_history.app.get_consumer_history_usecase import GetConsumerHistoryUsecase
from src.modules.get_consumer_history.app.get_consumer_history_viewmodel import GetConsumerHistoryViewmodel
from src.modules.get_status_battery_history.app.get_battery_status_history_viewmodel import GetBatteryStatusHistoryViewmodel
from src.shared.domain.entities.consumer import Consumer
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetConsumerHistoryController:

    def __init__(self, usecase: GetConsumerHistoryUsecase):
        self.GetConsumerHistoryUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            consumer_id = request.data.get('consumer_id')
            if consumer_id is None:
                raise MissingParameters('consumer_id')

            validate = Consumer.validate_consumer_id(consumer_id)
            if not validate:
                raise WrongTypeParameter(
                    "consumer_id", "str", type(consumer_id))

            measure = self.GetConsumerHistoryUsecase(
                consumer_id=consumer_id,
            )

            viewmodel = GetConsumerHistoryViewmodel(measure)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
