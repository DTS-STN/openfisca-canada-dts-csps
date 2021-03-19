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
                    persons("work_category__daily_is_majority_highway_operator",period) * not_(persons("standard_hours__has_autherized_exemption",period)), 
                    persons("work_category__daily_is_majority_highway_operator",period) * persons("standard_hours__has_autherized_exemption",period),
                    persons("work_category__daily_is_majority_city_operator",period)
                ],
                [
                    0,
                    persons("standard_hours__daily_alternative",period),
                    parameters(period).mvo_standard_hours_of_work.cmvo_daily_mvo_standard_hours_of_work
                ],
                parameters(period).clc_standard_hours_of_work.daily_clc_standard_hours_of_work
            )

class standard_hours__daily_alternative(Variable):
    value_type = float
    entity = Person
    label = u""
    definition_period = DAY
    reference = u"TODO"
    # def formula(persons, period, parameters):
    #     return where(True, parameters(period).mvo_standard_hours_of_work.hmvo_daily_holiday_reduction_hours,\
    #         parameters(period).mvo_standard_hours_of_work.hmvo_daily_holiday_reduction_hours)
  