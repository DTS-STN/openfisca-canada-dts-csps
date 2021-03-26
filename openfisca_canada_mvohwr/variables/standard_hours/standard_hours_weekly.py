from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class standard_hours__weekly_clc(Variable):
    value_type = float
    entity = Person
    label = u"Is weekly CLC (bus + other) taking account of holidays in week if any"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

    def formula(persons, period, parameters):
        clc_weekly_hours = persons("weekly_clc_standard_hours_of_work", period)
        clc_daily_hours = persons("daily_clc_standard_hours_of_work", period)

        nb_holidays = persons("weekly_work_schedule__total_holiday_days_in_period", period)
        clc_holiday_adjusted_hours = clc_weekly_hours - (clc_daily_hours * nb_holidays)

        return where(clc_holiday_adjusted_hours < 0, 0, clc_holiday_adjusted_hours)


class standard_hours__weekly_cmvo(Variable):
    value_type = float
    entity = Person
    label = u"Is weekly hours for CMVO taking account of holidays if any in week"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        cmvo_weekly_hours = persons("cmvo_weekly_mvo_standard_hours_of_work", period)
        cmvo_daily_hours = persons("cmvo_daily_mvo_standard_hours_of_work", period)

        nb_holidays = persons("weekly_work_schedule__total_holiday_days_in_period", period)
        adjusted_holiday_hours = cmvo_weekly_hours - (cmvo_daily_hours * nb_holidays)

        return where(adjusted_holiday_hours < 0, 0, adjusted_holiday_hours)


class standard_hours__weekly_hmvo(Variable):
    value_type = float
    entity = Person
    label = u"Is weekly hours for HMVO taking account of exemption and holidays"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
        hmvo_weekly_hours = persons("hmvo_weekly_mvo_hours_of_work", period)
        hmvo_daily_hours = persons("hmvo_daily_holiday_reduction_hours", period)  

        nb_holidays = persons("weekly_work_schedule__total_holiday_days_in_period", period)
        adjusted_holiday_hours = hmvo_weekly_hours - (hmvo_daily_hours * nb_holidays)

        return select(
            [
                persons("standard_hours__has_authorized_exemption", period),
                not_(persons("standard_hours__has_authorized_exemption", period))
            ],
            [
                persons("standard_hours__weekly_alternative", period),
                where(adjusted_holiday_hours < 0, 0, adjusted_holiday_hours)
            ]
        )


class standard_hours__has_authorized_exemption(Variable):
    value_type = bool
    entity = Person
    label = u"HMVO has authorized exemption to deviate from standard weekly hours"
    definition_period = DAY
    default_value = False
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#docCont"

    def formula(persons, period, parameters):
         return ((persons("standard_hours__weekly_alternative", period) > 0) &
                persons("standard_hours__is_hmvo_weekly_only", period))


class standard_hours__weekly_alternative(Variable):
    value_type = float
    entity = Person
    label = u"Is weekly alternative hours applicable to HMVO only"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#h-604501"


class standard_hours__is_weekly_clc_standard_hours_of_work(Variable):
    value_type = bool
    entity = Person
    label = u"Is Other (forklift or shunt etc.) (not CMVO or HMVO) with standard hours of work"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

    def formula(persons, period, parameters):
        return not_(persons("work_category__is_highway_operator_only", period)) & \
               not_(persons("work_category__is_city_operator_only", period))


class standard_hours__is_cmvo_weekly_mvo_standard_hours_of_work(Variable):
    value_type = bool
    entity = Person
    label = u"Is CMVO only (not HMVO) with standard hours of work per week"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#h-604495"

    def formula(persons, period, parameters):
        return not_(persons("work_category__is_highway_operator_only", period)) & \
               (persons("work_category__is_city_operator_only", period))


class standard_hours__is_hmvo_weekly_only(Variable):
    value_type = bool
    entity = Person
    label = u"Is HMVO only (not CMVO) with standard hours of work per week"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html#h-604501"

    def formula(persons, period, parameters):
        return persons("work_category__is_highway_operator_only", period)

