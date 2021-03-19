from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class weekly_work_schedule__total_hours_bus_operator(Variable):
    value_type = float
    entity = Person
    label = u"Is total weekly hours for bus (clc)"
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

class weekly_work_schedule__total_hours_city_operator(Variable):
    value_type = float
    entity = Person
    label = u"Is total weekly hours for CMVO"
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

class weekly_work_schedule__total_hours_highway_operator(Variable):
    value_type = float
    entity = Person
    label = u"Is total weekly hours for HMVO"
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

class weekly_work_schedule__total_hours_other(Variable):
    value_type = float
    entity = Person
    label = u"Is total weekly hours for Other (clc) includes forklift and shunt drivers etc."
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

class weekly_work_schedule__total_holiday_days_in_period(Variable):
    value_type = float
    entity = Person
    label = u"Weekly holiday days in the week"
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197, https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont" 