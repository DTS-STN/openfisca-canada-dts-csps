from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class standard_hours__weekly(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        if(persons("work_category__is_highway_operator_only",period) *\
            persons("weekly_work_schedule__total_holiday_days_in_period)",period) == 0) 
            return parameters(period).mvo_standard_hours_of_work.hmvo_weekly_mvo_hours_of_work
        elif (persons("work_category__is_highway_operator_only",period) *\
            persons("weekly_work_schedule__total_holiday_days_in_period)",period) > 0)
            return parameters(period).mvo_standard_hours_of_work.hmvo_weekly_holiday_mvo_standard_hours_of_work
        elif (!persons("work_category__is_highway_operator_only",period) * persons("work_category__is_city_operator_only",period) *\
                persons("weekly_work_schedule__total_holiday_days_in_period)",period) == 0)
            return parameters(period).mvo_standard_hours_of_work.cmvo_weekly_mvo_hours_of_work
        elif (!persons("work_category__is_highway_operator_only",period) * persons("work_category__is_city_operator_only",period) *\
                persons("weekly_work_schedule__total_holiday_days_in_period)",period) > 0)
            return parameters(period).mvo_standard_hours_of_work.cmvo_weekly_holiday_mvo_standard_hours_of_work
        elif (!persons("work_category__is_highway_operator_only",period) * !persons("work_category__is_city_operator_only",period) *\
            persons("weekly_work_schedule__total_holiday_days_in_period)",period) > 0)
            



            return parameters(period).clc_standard_hours_of_work.weekly_clc_standard_hours_of_work
        


class standard_hours__daily(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return persons("employment__does_transport_goods_or_passangers_by_motor_vehicle",period)


class standard_hours__has_autherized_exemption(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    default_value=False
    reference = u"TODO"

class standard_hours__weekly_alternate(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

class standard_hours__daily_alternate(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"