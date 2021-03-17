from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class employment__is_there_an_employment_relationship(Variable):
    value_type = bool
    entity = Person
    label = u"Is there an employment relationship?"
    definition_period = DAY
    reference = u"TODO"