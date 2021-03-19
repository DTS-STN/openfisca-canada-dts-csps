from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class standard_hours__weekly_clc(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    
    def formula(persons, period, parameters):
        clc_weekly_hours = parameters(period).clc_standard_hours_of_work.weekly_clc_standard_hours_of_work
        clc_daily_hours = parameters(period).clc_standard_hours_of_work.daily_clc_standard_hours_of_work
        
        nb_holidays = persons("weekly_work_schedule__total_holiday_days_in_period",period)
        clc_holiday_adjusted_hours = clc_weekly_hours - (clc_daily_hours * nb_holidays)
        
        return where(clc_holiday_adjusted_hours < 0, 0, clc_holiday_adjusted_hours)

class standard_hours__weekly_cmvo(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        cmvo_weekly_hours = parameters(period).mvo_standard_hours_of_work.cmvo_weekly_mvo_standard_hours_of_work
        cmvo_daily_hours = parameters(period).mvo_standard_hours_of_work.cmvo_daily_mvo_standard_hours_of_work

        nb_holidays = persons("weekly_work_schedule__total_holiday_days_in_period",period)
        adjusted_holiday_hours = cmvo_weekly_hours - (cmvo_daily_hours * nb_holidays)

        return where(adjusted_holiday_hours < 0, 0, adjusted_holiday_hours)


class standard_hours__weekly_hmvo(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        hmvo_weekly_hours = parameters(period).mvo_standard_hours_of_work.hmvo_weekly_mvo_hours_of_work
        hmvo_daily_hours = 10 # maybe? does anyone really know?

        nb_holidays = persons("weekly_work_schedule__total_holiday_days_in_period",period)
        adjusted_holiday_hours = hmvo_weekly_hours - (hmvo_daily_hours * nb_holidays)

        return select(
                [
                    persons("standard_hours__has_autherized_exemption",period),
                    not_(persons("standard_hours__has_autherized_exemption",period))
                ],
                [
                    persons("standard_hours__weekly_alternative",period),
                    where(adjusted_holiday_hours < 0, 0, adjusted_holiday_hours)
                ]
            )

class standard_hours__has_autherized_exemption(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    default_value=False
    reference = u"TODO"
    def formula(persons, period, parameters):
         return ((persons("standard_hours__weekly_alternative",period) > 0) &\
           (persons("standard_hours__is_hmvo_weekly_only", period) +\
           persons("standard_hours__is_hmvo_daily_only", period)))

class standard_hours__weekly_alternative(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

class standard_hours__is_weekly_clc_standard_hours_of_work(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return not_(persons("work_category__is_highway_operator_only",period)) &\
            not_(persons("work_category__is_city_operator_only",period))

class standard_hours__is_cmvo_weekly_mvo_standard_hours_of_work(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return not_(persons("work_category__is_highway_operator_only",period)) &\
            (persons("work_category__is_city_operator_only",period))

class standard_hours__is_hmvo_weekly_only(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return persons("work_category__is_highway_operator_only",period) 

class standard_hours__is_hmvo_daily_only(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return persons("work_category__daily_is_highway_operator_only",period) 