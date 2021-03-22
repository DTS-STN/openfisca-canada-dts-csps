from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class daily_summed_hours__clc_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("daily_work_schedule__total_hours_bus_operator",period) + \
            persons("daily_work_schedule__total_hours_other",period)


class daily_summed_hours__non_highway_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("daily_work_schedule__total_hours_bus_operator",period) + \
            persons("daily_work_schedule__total_hours_other",period) +\
                persons("daily_work_schedule__total_hours_city_operator",period)
