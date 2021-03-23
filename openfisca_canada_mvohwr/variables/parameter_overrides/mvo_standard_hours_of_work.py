from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class cmvo_daily_mvo_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"CMVO daily standard hours based on the parameter"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.cmvo_daily_mvo_standard_hours_of_work


class cmvo_weekly_mvo_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"CMVO weekly standard hours based on the parameter"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.cmvo_weekly_mvo_standard_hours_of_work


class hmvo_daily_holiday_reduction_hours(Variable):
    value_type = float
    entity = Person
    label = u"HMVO daily reduction hours based on the parameter"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.hmvo_daily_holiday_reduction_hours



class hmvo_weekly_mvo_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"HMVO weekly hours based on the parameter"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.hmvo_weekly_mvo_hours_of_work
