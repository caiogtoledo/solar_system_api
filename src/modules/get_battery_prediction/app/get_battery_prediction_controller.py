
from src.modules.get_battery_prediction.app.get_battery_prediction_usecase import GetBatteryPredictionUsecase
from src.modules.get_battery_prediction.app.get_battery_prediction_viewmodel import GetBatteryPredictionViewmodel
from src.modules.get_consumer_history.app.get_consumer_history_viewmodel import GetConsumerHistoryViewmodel
from src.shared.domain.entities.battery import Battery
from src.shared.domain.entities.consumer import Consumer
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetBatteryPredictionController:

    def __init__(self, usecase: GetBatteryPredictionUsecase):
        self.GetBatteryPredictionUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            battery_id = request.data.get('battery_id')
            if battery_id is None:
                raise MissingParameters('battery_id')

            validate = Battery.validate_battery_id(battery_id)
            if not validate:
                raise WrongTypeParameter(
                    "battery_id", "str", type(battery_id))

            battery_prediction = self.GetBatteryPredictionUsecase(
                battery_id=battery_id,
                k_records=request.data.get('k_records')
            )

            viewmodel = GetBatteryPredictionViewmodel(battery_prediction)

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
