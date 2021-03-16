from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class standard_hours__weekly(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return select(
            [
                persons("standard_hours__is_weekly_clc_standard_hours_of_work",period),
                persons("standard_hours__is_cmvo_weekly_mvo_standard_hours_of_work",period),
                persons("standard_hours__is_hmvo_weekly_mvo_hours_of_work",period),
                persons("standard_hours__has_autherized_exemption",period)
            ],
            [
                parameters(period).clc_standard_hours_of_work.weekly_clc_standard_hours_of_work,
                parameters(period).mvo_standard_hours_of_work.cmvo_weekly_mvo_standard_hours_of_work,
                parameters(period).mvo_standard_hours_of_work.hmvo_weekly_mvo_hours_of_work,
                persons("standard_hours__weekly_alternative",period)
            ],
        )

class standard_hours__holiday(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

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
    def formula(persons, period, parameters):
        return persons("standard_hours__weekly_alternative",period) > 0

class standard_hours__weekly_alternative(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

class standard_hours__daily_alternative(Variable):
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

class standard_hours__is_hmvo_weekly_mvo_hours_of_work(Variable):
    value_type = bool
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"
    def formula(persons, period, parameters):
        return persons("work_category__is_highway_operator_only",period) &\
            not_(persons("standard_hours__has_autherized_exemption",period))