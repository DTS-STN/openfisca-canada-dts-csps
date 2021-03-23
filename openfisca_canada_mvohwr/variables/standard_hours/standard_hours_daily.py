from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class standard_hours__daily(Variable):
    value_type = float
    entity = Person
    label = u"gets the standard hours based on the type of work done"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        return select(
                [
                    persons("work_category__daily_is_majority_highway_operator",period),
                    persons("work_category__daily_is_majority_city_operator",period)
                ],
                [
                    0,
                    persons("cmvo_daily_mvo_standard_hours_of_work", period)
                ],
                persons("daily_clc_standard_hours_of_work", period)
            )

