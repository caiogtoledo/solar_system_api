from src.modules.get_solar_panel_production.app.get_solar_panel_production_usecase import GetSolarPanelProductionUsecase
from src.modules.get_solar_panel_production.app.get_solar_panel_production_viewmodel import GetSolarPanelProductionViewmodel
from src.shared.domain.entities.solar_panel import SolarPanel
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Created


class GetSolarPanelProductionController:

    def __init__(self, usecase: GetSolarPanelProductionUsecase):
        self.GetSolarPanelProductionUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            solar_panel_id = request.data.get('solar_panel_id')
            if solar_panel_id is None:
                raise MissingParameters('solar_panel_id')

            validate = SolarPanel.validate_solar_panel_id(solar_panel_id)
            if not validate:
                raise WrongTypeParameter(
                    "solar_panel_id", "str", type(solar_panel_id))

            measure = self.GetSolarPanelProductionUsecase(
                solar_panel_id=solar_panel_id,
            )

            viewmodel = GetSolarPanelProductionViewmodel(measure)

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
