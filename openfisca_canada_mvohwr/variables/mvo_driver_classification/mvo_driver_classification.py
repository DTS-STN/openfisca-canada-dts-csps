from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class mvo__is_cmvo(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"
    
    def formula(persons, period, parameters):
        return persons("mvo__is_motor_vehicle_operator",period) &\
            not_(persons("mvo__is_bus_operator",period)) &\
            (persons("mvo__is_classified_as_cmvo",period) + persons("mvo__operates_close_to_home_terminal",period))

class mvo__is_hmvo(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("mvo__is_motor_vehicle_operator",period) &\
            not_(persons("mvo__is_bus_operator",period)) &\
            not_(persons("mvo__is_cmvo",period))

class mvo__is_bus_operator(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("mvo__is_motor_vehicle_operator",period) &\
            persons("mvo__operates_a_bus",period)

class mvo__is_other(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return not_(persons("mvo__is_bus_operator",period)) &\
            not_(persons("mvo__is_cmvo",period)) &\
            not_(persons("mvo__is_hmvo",period)) 


class mvo__is_motor_vehicle_operator(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return (persons("mvo__vehicle_is_operated_by_employee",period)) &\
            not_(persons("mvo__vehicle_is_designed_for_rails",period)) &\
            not_(persons("mvo__vehicle_is_powered_by_muscles",period))

class mvo__is_classified_as_cmvo(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("mvo__has_collective_cmvo_agreement",period) +\
            persons("mvo__is_cmvo_under_prevailing_industry_practice",period)

class mvo__operates_close_to_home_terminal(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

    def formula(persons, period, parameters):
        return persons("mvo__distance_from_home_terminal",period) <=\
            parameters(period).mvo_driver_classification.mvo_max_distance_from_home_terminal 

class mvo__vehicle_is_operated_by_employee(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

class mvo__vehicle_is_designed_for_rails(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

class mvo__vehicle_is_powered_by_muscles(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

class mvo__operates_a_bus(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

class mvo__has_collective_cmvo_agreement(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

class mvo__is_cmvo_under_prevailing_industry_practice(Variable):
    value_type = bool
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"

class mvo__distance_from_home_terminal(Variable):
    value_type = float
    entity = Person
    label = u"TODO"
    definition_period = DAY
    reference = u"TODO"