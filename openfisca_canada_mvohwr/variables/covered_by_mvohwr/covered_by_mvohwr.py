from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class is_covered_by_mvohwr(Variable):
    value_type = bool
    entity = Person
    label = u"Are you covered by mvohwr?"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
      return (persons("does_transport_goods_or_passangers_by_motor_vehicle",period) +\
        persons("does_transport_mail_in_canada",period)) *\
        persons("falls_under_part_three_of_clc",period) *\
        persons("is_there_an_employment_relationship",period)

class does_transport_goods_or_passangers_by_motor_vehicle(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

class does_transport_mail_in_canada(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

class falls_under_part_three_of_clc(Variable):
    value_type = bool
    entity = Person
    label = u"Do you fall under part III of CLC?"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-1.html"

class is_there_an_employment_relationship(Variable):
    value_type = bool
    entity = Person
    label = u"Is there an employment relationship?"
    definition_period = DAY
    reference = u"TODO"