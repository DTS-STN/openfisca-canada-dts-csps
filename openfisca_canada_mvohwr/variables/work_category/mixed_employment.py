from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class work_category__is_majority_highway_operator(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    default_value=False
    reference = u"TODO"
    def formula(persons, period, parameters):
        return (persons("weekly_work_schedule__total_hours_highway_operator",period) >= persons("weekly_work_schedule__total_hours_bus_operator",period) *\
          persons("weekly_work_schedule__total_hours_highway_operator",period) >= persons("weekly_work_schedule__total_hours_city_operator",period) *\
          persons("weekly_work_schedule__total_hours_highway_operator",period) >= persons("weekly_work_schedule__total_hours_other",period))