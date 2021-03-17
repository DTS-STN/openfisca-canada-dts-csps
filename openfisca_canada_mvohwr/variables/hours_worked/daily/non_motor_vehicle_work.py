from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class hours_worked__daily__non_motor_vehicle_work(Variable):
    value_type = float
    entity = Person
    label = u"Work for an employer that does not involve operating a vehicle"
    definition_period = DAY
    reference = u"TODO"