from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person

class employment__falls_under_part_three_of_clc(Variable):
    value_type = bool
    entity = Person
    label = u"Do you fall under part III of CLC?"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/acts/L-2/page-1.html"