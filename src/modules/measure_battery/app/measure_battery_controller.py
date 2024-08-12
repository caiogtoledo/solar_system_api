from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from .measure_battery_usecase import MeasureBatteryUsecase
from .measure_battery_viewmodel import MeasureBatteryViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Created


class MeasureBatteryController:

    def __init__(self, usecase: MeasureBatteryUsecase):
        self.MeasureBatteryUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('battery_id') is None:
                raise MissingParameters('battery_id')
            if request.data.get('soc') is None:
                raise MissingParameters('soc')
            if request.data.get('voltage') is None:
                raise MissingParameters('voltage')
            if request.data.get('current') is None:
                raise MissingParameters('current')
            if request.data.get('temperature') is None:
                raise MissingParameters('temperature')

            measure = self.MeasureBatteryUsecase(
                battery_id=request.data.get('battery_id'),
                soc=request.data.get('soc'),
                voltage=request.data.get('voltage'),
                current=request.data.get('current'),
                temperature=request.data.get('temperature'),
                timestamp=request.data.get('timestamp'),
            )

            viewmodel = MeasureBatteryViewmodel(measure)

            return Created(viewmodel.to_dict())

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
