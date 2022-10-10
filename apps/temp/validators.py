# First party
from abstracts.validators import APIValidator


class TempModelValidator:
    """TempModelValidator."""

    def validate_number(self, number: int) -> None:
        if number == 13:
            raise APIValidator(
                f'Число имеет неправильное значение: {number}',
                'error',
                '400'
            )
