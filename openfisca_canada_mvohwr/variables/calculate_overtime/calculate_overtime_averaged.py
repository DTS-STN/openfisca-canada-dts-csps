from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class calculate_overtime__averaged(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      ot_hours = persons("calculate_overtime__total_clc_hours", period) - (persons("calculate_overtime__number_of_averaging_scheduled_clc_weeks", period) * persons("weekly_clc_standard_hours_of_work", period))
      return max_(0, ot_hours)

class calculate_overtime__total_clc_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

class calculate_overtime__number_of_averaging_scheduled_clc_weeks(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"