from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class calculate_overtime__overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      #take the better of daily vs weekly
      daily_ot = persons("calculate_overtime_daily__overtime_worked_hours",period)
      weekly_ot = persons("calculate_overtime_weekly__overtime_worked_hours",period)
      return where(daily_ot > weekly_ot, daily_ot, weekly_ot)