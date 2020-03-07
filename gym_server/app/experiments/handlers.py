from flask import jsonify

from gym_server.experiments.errors import UnknownExperimentError
from gym_server.logging import logger
from ..experiments import bp


@bp.app_errorhandler(UnknownExperimentError)
def handle_invalid_experiment_id(error: UnknownExperimentError):
    logger.debug('Experiment with unknown ID', error)
    # response = jsonify(error)
    # response.status_code = error.status_code
    # TODO: Create custom base class for client errors
    response = jsonify({
        'errorCode': 10,
        'message': 'Experiment with the given ID does not exist.'
    })
    return response
