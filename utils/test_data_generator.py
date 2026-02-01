from faker import Faker
from .config_loader import config


class TestDataGenerator:
    """Generate test data using Faker"""

    def __init__(self):
        seed = config.get('test_data.seed')
        locale = config.get('test_data.locale')
        self.fake = Faker(locale)
        if seed is not None:
            Faker.seed(seed)

    def random_sentence(self, num_words: int) -> str:
        return self.fake.sentence(nb_words=num_words)

    def random_integer(self, min_value: int, max_value: int) -> int:
        return self.fake.random_int(min=min_value, max=max_value)


test_data = TestDataGenerator()
