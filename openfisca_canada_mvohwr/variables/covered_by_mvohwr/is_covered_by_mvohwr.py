from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class employment__is_covered_by_mvohwr(Variable):
    value_type = bool
    entity = Person
    label = u"Are you covered by mvohwr?"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("employment__does_transport_goods_or_passangers_by_motor_vehicle",period) +\
            persons("employment__does_transport_mail_in_canada",period)