import pytest
import os

from neural_network_model.config import config


@pytest.fixture
def black_grass_dir():
    test_data_dir = os.path.join(config.DATASET_DIR, 'test_data')
    return os.path.join(test_data_dir, 'Black-grass')


@pytest.fixture
def charlock_dir():
    test_data_dir = os.path.join(config.DATASET_DIR, 'test_data')
    return os.path.join(test_data_dir, 'Charlock')
