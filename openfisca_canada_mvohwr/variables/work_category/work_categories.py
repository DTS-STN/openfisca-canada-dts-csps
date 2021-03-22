from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class work_category__is_bus_operator_only(Variable):
    value_type = bool
    entity = Person
    label = u"person who operates a bus only - CLC"
    definition_period = ETERNITY
    default_value = False
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        return (((persons("weekly_work_schedule__total_hours_bus_operator", period) > 0) * \
                 (persons("weekly_work_schedule__total_hours_highway_operator", period) == 0) * \
                 (persons("weekly_work_schedule__total_hours_city_operator", period) == 0) * \
                 (persons("weekly_work_schedule__total_hours_other", period) == 0)))


class work_category__is_city_operator_only(Variable):
    value_type = bool
    entity = Person
    label = u"person who operates exclusively within a 10-mile radius of his home terminal - CMVO"
    definition_period = ETERNITY
    default_value = False
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        return (persons("weekly_work_schedule__total_hours_city_operator", period) > 0) * \
               (persons("weekly_work_schedule__total_hours_bus_operator", period) == 0) * \
               (persons("weekly_work_schedule__total_hours_highway_operator", period) == 0) * \
               (persons("weekly_work_schedule__total_hours_other", period) == 0)


class work_category__is_highway_operator_only(Variable):
    value_type = bool
    entity = Person
    label = u"person who is not a bus operator or a CMVO - highway only - HMVO"
    definition_period = ETERNITY
    default_value = False
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        return (persons("weekly_work_schedule__total_hours_highway_operator", period) > 0) * \
               (persons("weekly_work_schedule__total_hours_bus_operator", period) == 0) * \
               (persons("weekly_work_schedule__total_hours_city_operator", period) == 0) * \
               (persons("weekly_work_schedule__total_hours_other", period) == 0)


class work_category__is_other_only(Variable):
    value_type = bool
    entity = Person
    label = u"person who is only a forklift or shunt driver for eg. - Other"
    definition_period = ETERNITY
    default_value = False
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

    def formula(persons, period, parameters):
        return (persons("weekly_work_schedule__total_hours_other", period) > 0) * \
               (persons("weekly_work_schedule__total_hours_bus_operator", period) == 0) * \
               (persons("weekly_work_schedule__total_hours_city_operator", period) == 0) * \
               (persons("weekly_work_schedule__total_hours_highway_operator", period) == 0)


class work_category__daily_is_highway_operator_only(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = ETERNITY
    default_value = False
    reference = u"TODO"

    def formula(persons, period, parameters):
        return (persons("daily_work_schedule__total_hours_highway_operator", period) > 0) * \
               (persons("daily_work_schedule__total_hours_bus_operator", period) == 0) * \
               (persons("daily_work_schedule__total_hours_city_operator", period) == 0) * \
               (persons("daily_work_schedule__total_hours_other", period) == 0)
