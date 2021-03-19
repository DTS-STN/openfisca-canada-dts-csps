from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class summed_hours__clc_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Is weekly total hours for Bus(clc) + Other(clc) operator"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        return persons("weekly_work_schedule__total_hours_bus_operator",period) + \
            persons("weekly_work_schedule__total_hours_other",period)

class summed_hours__clc_cmvo_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Is weekly total hours for sum of (bus + other clc) and CMVO"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        return persons("summed_hours__clc_worked_hours",period) + \
            persons("weekly_work_schedule__total_hours_city_operator",period)

class summed_hours__clc_hmvo_cmvo_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Is weekly total hours for sum of (bus + other clc) and CMVO and HMVO"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        return persons("summed_hours__clc_worked_hours",period) + \
            persons("weekly_work_schedule__total_hours_city_operator",period) + \
            persons("weekly_work_schedule__total_hours_highway_operator",period)