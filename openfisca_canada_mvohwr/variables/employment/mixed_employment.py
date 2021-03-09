from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class employment__is_mixed_employment(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person eligible for the EI Workshare?"
    definition_period = DAY
    reference = u"TODO"
    
    def formula(persons, period, parameters):
        return persons("employment__is_warehouse_worker",period) & persons("employment__is_driver",period)

class employment__is_driver(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person eligible for the EI Workshare?"
    definition_period = DAY
    reference = u"TODO"

class employment__is_warehouse_worker(Variable):
    value_type = bool
    entity = Person
    label = u"Is this person eligible for the EI Workshare?"
    definition_period = DAY
    reference = u"TODO"