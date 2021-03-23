from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class calculate_overtime__overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Calculate overtime hours take the best of daily, 60 or weekly rule"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
      #take the better of daily vs weekly
      daily_ot = persons("calculate_overtime_daily__overtime_worked_hours",period)
      weekly_ot = persons("calculate_overtime_weekly__overtime_worked_hours",period)
      sixty_hour_ot = persons("calculate_overtime_weekly__hmvo_overtime_worked_hours", period)
      return max(daily_ot, weekly_ot, sixty_hour_ot)