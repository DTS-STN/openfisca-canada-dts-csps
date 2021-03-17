from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class hours_worked__daily__city_motor_vehicle_operator(Variable):
    value_type = float
    entity = Person
    label = u"Placeholder"
    definition_period = DAY
    reference = u"TODO"