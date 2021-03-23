from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class calculate_overtime_daily__overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Calculate daily overtime"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        condition = persons("daily_work_schedule__is_holiday", period) + \
                    persons("work_category__daily_is_majority_highway_operator", period) + \
                    persons("work_category__daily_is_highway_operator_only", period)
        return where(condition,
                     0,  # General Holiday or highway only --> no OT
                     persons("calculate_overtime_daily__non_highway_worked_hours", period)
                     )


class calculate_overtime_daily__non_highway_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        ot_hours = persons("daily_summed_hours__non_highway_worked_hours", period) - persons("standard_hours__daily", period)
        return max_(0, ot_hours)
