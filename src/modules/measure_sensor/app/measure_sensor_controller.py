from src.modules.measure_sensor.app.measure_sensor_viewmodel import MeasureSensorViewmodel
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from .measure_sensor_usecase import MeasureSensorUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Created


class MeasureSensorController:

    def __init__(self, usecase: MeasureSensorUsecase):
        self.MeasureConsumerUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('measurement_id') is None:
                raise MissingParameters('measurement_id')
            if request.data.get('value') is None:
                raise MissingParameters('value')
            if request.data.get('unit') is None:
                raise MissingParameters('unit')

            measure = self.MeasureConsumerUsecase(
                measurement_id=request.data.get('measurement_id'),
                value=request.data.get('value'),
                type=request.data.get('type'),
                unit=request.data.get('unit'),
                timestamp=request.data.get('timestamp'),
            )

            viewmodel = MeasureSensorViewmodel(measure)

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
