from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class standard_hours__daily(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return select(
                [
                    persons("work_category__daily_is_majority_highway_operator",period),
                    persons("work_category__daily_is_majority_city_operator",period)
                ],
                [
                    0,
                    parameters(period).mvo_standard_hours_of_work.cmvo_daily_mvo_standard_hours_of_work
                ],
                parameters(period).clc_standard_hours_of_work.daily_clc_standard_hours_of_work
            )

