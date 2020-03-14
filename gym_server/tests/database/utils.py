from gym_server.experiments.models import ExperimentStatus
from gym_server.database.models import ExperimentModel


def populate_experiments_table(db, count=100):
    experiments = [ExperimentModel(
        id=f'Experiment',
        name=f'Experiment {index}',
        description='Just another experiment',
        status=ExperimentStatus.not_started,
        config_name=f'experiment_{index}_config.json',
        owner_id='id',
    ) for index in range(count)]
    db.session.bulk_save_objects()
    db.session.commit()