
from src.modules.get_producer_history.app.get_producer_history_usecase import GetProducerHistoryUsecase
from src.modules.get_producer_history.app.get_producer_history_viewmodel import GetProducerHistoryViewmodel
from src.shared.domain.entities.solar_panel import SolarPanel
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetProducerHistoryController:

    def __init__(self, usecase: GetProducerHistoryUsecase):
        self.GetProducerHistoryUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            producer_id = request.data.get('producer_id')
            if producer_id is None:
                raise MissingParameters('producer_id')

            validate = SolarPanel.validate_solar_panel_id(producer_id)
            if not validate:
                raise WrongTypeParameter(
                    "producer_id", "str", type(producer_id))

            measure = self.GetProducerHistoryUsecase(
                producer_id=producer_id,
            )

            viewmodel = GetProducerHistoryViewmodel(measure)

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
