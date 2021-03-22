from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class cmvo_daily_mvo_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.cmvo_daily_mvo_standard_hours_of_work


class cmvo_weekly_holiday_mvo_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.cmvo_weekly_holiday_mvo_standard_hours_of_work


class cmvo_weekly_mvo_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.cmvo_weekly_mvo_standard_hours_of_work


class hmvo_weekly_holiday_mvo_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.hmvo_weekly_holiday_mvo_standard_hours_of_work


class hmvo_weekly_mvo_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).mvo_standard_hours_of_work.hmvo_weekly_mvo_hours_of_work
