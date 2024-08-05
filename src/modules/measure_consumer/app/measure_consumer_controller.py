from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from .measure_consumer_usecase import MeasureConsumerUsecase
from .measure_consumer_viewmodel import MeasureConsumerViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Created


class MeasureConsumerController:

    def __init__(self, usecase: MeasureConsumerUsecase):
        self.MeasureConsumerUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('consumer_id') is None:
                raise MissingParameters('consumer_id')
            if request.data.get('instantly') is None:
                raise MissingParameters('instantly')

            measure = self.MeasureConsumerUsecase(
                consumer_id=request.data.get('consumer_id'),
                instantly=request.data.get('instantly'),
                timestamp=request.data.get('timestamp'),
            )

            viewmodel = MeasureConsumerViewmodel(measure)

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
