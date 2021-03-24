from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class daily_work_schedule__total_hours_bus_operator(Variable):
    value_type = float
    entity = Person
    label = u"Total daily hours worked as a bus operator?"
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

class daily_work_schedule__total_hours_city_operator(Variable):
    value_type = float
    entity = Person
    label = u"Total daily hours worked as a city motor vehicle operator?"
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

class daily_work_schedule__total_hours_highway_operator(Variable):
    value_type = float
    entity = Person
    label = u"Total daily hours worked as a highway motor vehicle operator?"
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

class daily_work_schedule__total_hours_other(Variable):
    value_type = float
    entity = Person
    label = u"Total daily hours worked as anything other than a motorized vehicle operator?"
    definition_period = DAY
    default_value=0
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"

class daily_work_schedule__is_holiday(Variable):
    value_type = bool
    entity = Person
    label = u"was this considered a general holiday?"
    definition_period = DAY
    default_value=False
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-36.html#h-342197"
    