from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class weekly_work_schedule__total_hours_bus_operator(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    default_value=0
    reference = u"TODO"

class weekly_work_schedule__total_hours_city_operator(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    default_value=0
    reference = u"TODO"

class weekly_work_schedule__total_hours_highway_operator(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    default_value=0
    reference = u"TODO"

class weekly_work_schedule__total_hours_other(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    default_value=0
    reference = u"TODO"

class weekly_work_schedule__has_holiday_days_in_period(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("weekly_work_schedule__total_holiday_days_in_period",period) > 0

class weekly_work_schedule__total_holiday_days_in_period(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    default_value=0
    reference = u"TODO" 