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
    default_value = WorkCategory.OTHER
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        weekly_highway_hours = persons("weekly_work_schedule__total_hours_highway_operator", period)
        weekly_city_hours = persons("weekly_work_schedule__total_hours_city_operator", period)
        weekly_clc_hours = persons("weekly_work_schedule__total_hours_bus_operator", period) + persons("weekly_work_schedule__total_hours_other", period)

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


class work_category__daily_is_majority_city_operator(Variable):
    value_type = bool
    entity = Person
    label = u"on a given day, majority cmvo hours"
    definition_period = DAY
    default_value = False
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#h-604495"

    def formula(persons, period, parameters):
        return (persons("daily_work_schedule__total_hours_city_operator", period) > persons("daily_summed_hours__clc_worked_hours", period))


class work_category__daily_is_majority_highway_operator(Variable):
    value_type = bool
    entity = Person
    label = u"on a given day, majoity highway operator hours"
    definition_period = DAY
    default_value = False
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#h-604501"

    def formula(persons, period, parameters):
        return (persons("daily_work_schedule__total_hours_highway_operator", period) > persons("daily_summed_hours__non_highway_worked_hours", period))
