from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class calculate_overtime_weekly__overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      work_category_majority_type = persons("work_category_majority_type",period)
      WorkCategory = work_category_majority_type.possible_values
      return select(
        [
          work_category_majority_type == WorkCategory.OTHER,
          work_category_majority_type == WorkCategory.CMVO,
          work_category_majority_type == WorkCategory.HMVO
        ],
        [
          persons("calculate_overtime_weekly__clc_overtime_worked_hours",period),
          max_(persons("calculate_overtime_weekly__cmvo_overtime_worked_hours",period), persons("calculate_overtime_weekly__hmvo_overtime_worked_hours",period)),
          persons("calculate_overtime_weekly__hmvo_overtime_worked_hours",period),
        ],
        persons("calculate_overtime_weekly__clc_overtime_worked_hours",period)
      )

class calculate_overtime_weekly__clc_overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      ot_hours = persons("summed_hours__clc_cmvo_worked_hours",period) - persons("standard_hours__weekly_clc",period)
      return where(
        ot_hours < 0, 
        0, 
        ot_hours
      )

class calculate_overtime_weekly__cmvo_overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      ot_hours = persons("summed_hours__clc_cmvo_worked_hours",period) - persons("standard_hours__weekly_cmvo",period)
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
      ot_hours = persons("summed_hours__clc_hmvo_cmvo_worked_hours",period) - persons("standard_hours__weekly_hmvo",period)
      return where(
        ot_hours < 0, 
        0, 
        ot_hours
      )