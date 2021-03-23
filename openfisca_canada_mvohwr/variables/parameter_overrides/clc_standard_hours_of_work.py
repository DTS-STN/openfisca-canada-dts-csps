from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class daily_clc_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).clc_standard_hours_of_work.daily_clc_standard_hours_of_work


class overtime_clc_rate(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).clc_standard_hours_of_work.overtime_clc_rate


class weekly_clc_standard_hours_of_work(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return parameters(period).clc_standard_hours_of_work.weekly_clc_standard_hours_of_work
