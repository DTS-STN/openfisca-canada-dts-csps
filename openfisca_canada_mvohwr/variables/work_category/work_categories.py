from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class work_category__is_bus_operator_only(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = ETERNITY
    default_value=False
    reference = u"TODO"
    def formula(persons, period, parameters):
        return (((persons("weekly_work_schedule__total_hours_bus_operator",period) > 0) *\
            (persons("weekly_work_schedule__total_hours_highway_operator",period) == 0) *\
            (persons("weekly_work_schedule__total_hours_city_operator",period) == 0) *\
            (persons("weekly_work_schedule__total_hours_other",period) == 0))) 


class work_category__is_city_operator_only(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = ETERNITY
    default_value=False
    reference = u"TODO"
    def formula(persons, period, parameters):
        return (((persons("weekly_work_schedule__total_hours_city_operator",period) > 0) *\
            (persons("weekly_work_schedule__total_hours_bus_operator",period) == 0) *\
            (persons("weekly_work_schedule__total_hours_highway_operator",period) == 0) *\
            (persons("weekly_work_schedule__total_hours_other",period) == 0))) 


class work_category__is_highway_operator_only(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = ETERNITY
    default_value=False
    reference = u"TODO"
    def formula(persons, period, parameters):
        return (((persons("weekly_work_schedule__total_hours_highway_operator",period) > 0) *\
            (persons("weekly_work_schedule__total_hours_bus_operator",period) == 0) *\
            (persons("weekly_work_schedule__total_hours_city_operator",period) == 0) *\
            (persons("weekly_work_schedule__total_hours_other",period) == 0)))

class work_category__is_other_only(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = ETERNITY
    default_value=False
    reference = u"TODO"
    def formula(persons, period, parameters):
        return (((persons("weekly_work_schedule__total_hours_other",period) > 0) *\
            (persons("weekly_work_schedule__total_hours_bus_operator",period) == 0) *\
            (persons("weekly_work_schedule__total_hours_city_operator",period) == 0) *\
            (persons("weekly_work_schedule__total_hours_highway_operator",period) == 0)))  

class work_category__daily_is_highway_operator_only(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = ETERNITY
    default_value=False
    reference = u"TODO"
    def formula(persons, period, parameters):
        return ((persons("daily_work_schedule__total_hours_highway_operator",period) > 0) *\
            (persons("daily_work_schedule__total_hours_bus_operator",period) == 0) *\
            (persons("daily_work_schedule__total_hours_city_operator",period) == 0) *\
            (persons("daily_work_schedule__total_hours_other",period) == 0))