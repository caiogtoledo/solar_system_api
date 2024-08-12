from src.modules.get_actual_status_battery.app.get_actual_status_battery_usecase import GetActualStatusBatteryUsecase
from src.modules.get_actual_status_battery.app.get_actual_status_battery_viewmodel import GetActualStatusBatteryViewmodel
from src.shared.domain.entities.battery import Battery
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetActualStatusBatteryController:

    def __init__(self, usecase: GetActualStatusBatteryUsecase):
        self.GetActualStatusBatteryUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            battery_id = request.data.get('battery_id')
            if battery_id is None:
                raise MissingParameters('battery_id')

            validate = Battery.validate_battery_id(battery_id)
            if not validate:
                raise WrongTypeParameter(
                    "battery_id", "str", type(battery_id))

            measure = self.GetActualStatusBatteryUsecase(
                battery_id=battery_id,
            )

            viewmodel = GetActualStatusBatteryViewmodel(measure)

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
