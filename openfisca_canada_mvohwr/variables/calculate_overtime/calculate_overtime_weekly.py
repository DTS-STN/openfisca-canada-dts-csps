from openfisca_core.model_api import *
from openfisca_canada_mvohwr.entities import Person


class calculate_overtime_weekly__overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Calculate weekly overtime based off work category"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        work_category_majority_type = persons("work_category_majority_type", period)
        WorkCategory = work_category_majority_type.possible_values
        return select(
            [
                work_category_majority_type == WorkCategory.OTHER,
                work_category_majority_type == WorkCategory.CMVO,
                work_category_majority_type == WorkCategory.HMVO
            ],
            [
                max_(0, persons("calculate_overtime_weekly__clc_overtime_worked_hours", period)),
                max_(0, persons("calculate_overtime_weekly__cmvo_overtime_worked_hours", period)),
                max_(0, persons("calculate_overtime_weekly__hmvo_overtime_worked_hours", period)),
            ],
            max_(0, persons("calculate_overtime_weekly__clc_overtime_worked_hours", period))
        )


class calculate_overtime_weekly__clc_overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"calculate CLC overtime weekly hours"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        ot_hours = persons("summed_hours__clc_cmvo_worked_hours", period) - persons("standard_hours__weekly_clc", period)
        return ot_hours

class calculate_overtime_weekly__cmvo_overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"calculate CMVO overtime weekly hours"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        ot_hours = persons("summed_hours__clc_cmvo_worked_hours", period) - persons("standard_hours__weekly_cmvo", period)
        return ot_hours


class calculate_overtime_weekly__hmvo_overtime_worked_hours(Variable):
    value_type = float
    entity = Person
    label = u"Calculate the weekly HMVO overtime worked hours"
    definition_period = DAY
    reference = u"https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._990/page-1.html"

    def formula(persons, period, parameters):
        ot_hours = persons("summed_hours__clc_hmvo_cmvo_worked_hours", period) - persons("standard_hours__weekly_hmvo", period)
        return ot_hours
