from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class daily_clc_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"The daily standard CLC hours from the parameters"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        return parameters(period).clc_standard_hours_of_work.daily_clc_standard_hours_of_work


class overtime_clc_rate(Variable):
    value_type = float
    entity = Person
    label = u"The overtime rate for CLC from the parameters"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).clc_standard_hours_of_work.overtime_clc_rate


class weekly_clc_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"The weekly standard CLC hours from the parameters"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        return parameters(period).clc_standard_hours_of_work.weekly_clc_standard_hours_of_work
