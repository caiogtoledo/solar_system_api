from src.modules.create_alert.app.alert_usecase import CreateAlertUsecase
from src.modules.create_alert.app.alert_viewmodel import AlertViewmodel
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, Created


class CreateAlertController:

    def __init__(self, usecase: CreateAlertUsecase):
        self.CreateAlertUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('alert_id') is None:
                raise MissingParameters('alert_id')
            if request.data.get('type') is None:
                raise MissingParameters('type')
            if request.data.get('message') is None:
                raise MissingParameters('message')

            measure = self.CreateAlertUsecase(
                alert_id=request.data.get('alert_id'),
                type=request.data.get('type'),
                message=request.data.get('message'),
                is_resolved=request.data.get('is_resolved'),
                timestamp_created_at=request.data.get('timestamp_created_at'),
            )

            viewmodel = AlertViewmodel(measure)

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
