from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from .measure_solar_panel_usecase import MeasureSolarPanelUsecase
from .measure_solar_panel_viewmodel import MeasureSolarPanelViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Created


class MeasureSolarPanelController:

    def __init__(self, usecase: MeasureSolarPanelUsecase):
        self.MeasureSolarPanelUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('solar_panel_id') is None:
                raise MissingParameters('solar_panel_id')
            if request.data.get('instantly') is None:
                raise MissingParameters('instantly')

            measure = self.MeasureSolarPanelUsecase(
                solar_panel_id=request.data.get('solar_panel_id'),
                instantly=request.data.get('instantly'),
                timestamp=request.data.get('timestamp'),
            )

            viewmodel = MeasureSolarPanelViewmodel(measure)

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
