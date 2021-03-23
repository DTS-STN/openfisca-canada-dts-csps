from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class mvo_max_distance_from_home_terminal(Variable):
    value_type = float
    entity = Person
    label = u"calculate the max distance based on the parameter"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        return parameters(period).mvo_driver_classification.mvo_max_distance_from_home_terminal
