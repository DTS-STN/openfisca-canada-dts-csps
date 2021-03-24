from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class daily_summed_hours__clc_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Is total daily hours for bus (CLC) operator and Other(CLC)"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        return persons("daily_work_schedule__total_hours_bus_operator",period) + \
            persons("daily_work_schedule__total_hours_other",period)


class daily_summed_hours__non_highway_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Is total daily hours for Bus (CLC), Other (CLC) and City Operators"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        return persons("daily_work_schedule__total_hours_bus_operator",period) + \
            persons("daily_work_schedule__total_hours_other",period) +\
                persons("daily_work_schedule__total_hours_city_operator",period)
