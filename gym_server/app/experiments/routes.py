"""Routes for handling experiment data, /experiments

Experiments support CRUD operations.

As an overview:
- To create an experiment, POST /experiments
- To modify an experiment, PATCH /experiments/:experiment_id or
    PUT /experiments/:experiment_id/:sub_resource where :sub_resource is a
    property like status or config
- To retrieve experiment data, GET /experiments/:experiment_id
    - GET requests sent to /experiments will return all public experiments, and
        all experiments owned by the requesting user (specified using auth token)
- To remove experiment data, DELETE /experiments/:experiment_id
"""

import json
from pathlib import Path
from uuid import uuid4

from flask import Response, request, make_response

from ..experiments import bp

CONFIG_STORAGE_PATH = str(Path.home() / 'gym_server' / 'config' / 'experiments')


def store_config(config_json: str) -> str:
    """Store an experiment configuration as a JSON file.

    Write an experiment configuration to file.

    Returns:
        The URI of the config.
    """
    # TODO: Support remote storage of files into Cloud bucket
    uuid = uuid4()
    path = f'{CONFIG_STORAGE_PATH}/config_{uuid}.json'
    with open(path) as f:
        json.dump(config_json, f)
    return path


@bp.route('/experiments', methods=['POST'])
def create_experiment() -> Response:
    """Upload an experiment config to create a new experiment.

    This endpoint supports POST requests only.
    """
    body_json = request.json
    return make_response((
        'OK', 200
    ))


@bp.route('/experiments', methods=['GET'])
def get_experiments() -> Response:
    """Fetches all experiments accessible to the current user.

    This endpoint supports GET requests only.

    If the request is authenticated, it will get all experiments that belong
    to its auth token and public experiments. Otherwise, only public
    experiments are returned.
    """
    return make_response((
        'OK', 200
    ))


@bp.route('/experiments/<string:experiment_id>', methods=['GET'])
def get_experiment(experiment_id: str) -> Response:
    """Fetch experiment data.

    This endpoint supports GET requests only.

    Args:
        experiment_id (str): The ID of the experiment
    """
    return make_response((
        'OK', 200
    ))


@bp.route('/experiments/<string:experiment_id>', methods=['PATCH'])
def modify_experiment(experiment_id: str) -> Response:
    """Update experiment attributes.

    This endpoint supports PATCH operations only.

    Args:
        experiment_id (str): The ID of the experiment
    """
    return make_response((
        'OK', 200
    ))


@bp.route('/experiments/<string:experiment_id>/<string:resource>', methods=['PUT'])
def modify_experiment(experiment_id: str, resource: str) -> Response:
    """Modify experiment subresources.

    This endpoint supports PUT operations only.

    Modifying `status` is the way to start and stop experiments. Modifying
    `config` is the way to modify an experiment's configuration, which requires
    the experiment to have the "stopped" status.

    Args:
        experiment_id (str): The ID of the experiment
        resource (str): The subresource to modify, one of (status, config).
    """
    return make_response((
        'OK', 200
    ))


@bp.route('/experiments/<string:experiment_id>', methods=['DELETE'])
def delete_experiment(experiment_id: str) -> Response:
    """Delete an experiment.

    This endpoint supports DELETE operations only.

    If the requested experiment resource is running, it will be stopped.

    Args:
        experiment_id (str): The ID of the experiment

    Returns:
        Response: a 200 OK response if the deletion was done.
    """
    # TODO(auth): Handle experiment permissions
    # TODO: Check if experiment exists
    # TODO: Stop experiment if running
    ExperimentModel.query.filter_by(id=experiment_id).delete()
    # TODO: Handle experiment not existing
    db.session.commit()
    return make_response((
        'OK',
        200,
    ))
