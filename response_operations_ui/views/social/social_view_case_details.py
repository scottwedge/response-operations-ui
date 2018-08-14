import logging

from flask import render_template
from flask_login import login_required
from structlog import wrap_logger

from response_operations_ui.common.mappers import map_social_case_status
from response_operations_ui.controllers import case_controller, sample_controllers


logger = wrap_logger(logging.getLogger(__name__))


@login_required
def view_social_case_details(case_id):
    social_case = case_controller.get_case_by_id(case_id)
    sample_attributes = sample_controllers.get_sample_attributes(social_case['sampleUnitId'])

    mapped_status = map_social_case_status(social_case['caseGroup']['caseGroupStatus'])

    return render_template('social-view-case-details.html', attributes=sample_attributes['attributes'],
                           status=mapped_status)