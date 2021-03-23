from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class mvo_max_distance_from_home_terminal(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).mvo_driver_classification.mvo_max_distance_from_home_terminal
