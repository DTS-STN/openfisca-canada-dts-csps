from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class hours_worked__daily__overtime_hours(Variable):
    value_type = float
    entity = Person
    label = u"Work for an employer that does not involve operating a vehicle"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("hours_worked__daily__bus_operator",period)