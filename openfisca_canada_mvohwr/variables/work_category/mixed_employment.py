from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class WorkCategory(Enum):
  CMVO = u"City motor vehicle operator"
  HMVO = u"Highway motor vehicle operator"
  OTHER = u"Any other type of motor vehicle operator (bus operator, shunt driver, etc)"

class work_category_majority_type(Variable):
  value_type = Enum
  possible_values = WorkCategory
  entity = Person
  label = u"Calculate the majority hours to determine the winning category to calculate overtime"
  definition_period = DAY
  default_value=WorkCategory.OTHER
  reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

  def formula(persons, period, parameters):
      weekly_highway_hours = persons("weekly_work_schedule__total_hours_highway_operator",period)
      weekly_city_hours = persons("weekly_work_schedule__total_hours_city_operator",period)
      weekly_clc_hours = persons("weekly_work_schedule__total_hours_bus_operator",period) + persons("weekly_work_schedule__total_hours_other",period)

      return select(
        [
          (weekly_highway_hours > weekly_city_hours) * (weekly_highway_hours > weekly_clc_hours),
          (weekly_city_hours > weekly_highway_hours) * (weekly_city_hours > weekly_clc_hours),
          (weekly_clc_hours > weekly_highway_hours) * (weekly_clc_hours > weekly_city_hours)
        ],
        [
          WorkCategory.HMVO,
          WorkCategory.CMVO,
          WorkCategory.OTHER,
        ],
        WorkCategory.OTHER
      )
