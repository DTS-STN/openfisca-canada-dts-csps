from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class calculate_overtime_weekly__overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      return where(
        persons("work_category__is_majority_highway_operator",period), 
        persons("calculate_overtime_weekly__hmvo_overtime_worked_hours",period), 
        persons("calculate_overtime_weekly__clc_or_cmvo_overtime_worked_hours",period)
      )

class calculate_overtime_weekly__clc_or_cmvo_overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      ot_hours = persons("summed_hours__clc_cmvo_worked_hours",period) - persons("standard_hours__weekly",period)
      return where(
        ot_hours < 0, 
        0, 
        ot_hours
      )

class calculate_overtime_weekly__hmvo_overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      ot_hours = persons("summed_hours__clc_hmvo_cmvo_worked_hours",period) - persons("standard_hours__weekly",period)
      return where(
        ot_hours < 0, 
        0, 
        ot_hours
      )