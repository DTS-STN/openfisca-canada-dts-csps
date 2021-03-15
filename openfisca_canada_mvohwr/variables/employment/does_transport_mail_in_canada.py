from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class employment__does_transport_mail_in_canada(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"