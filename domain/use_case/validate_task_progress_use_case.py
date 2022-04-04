class ValidateTaskProgressUseCase:
    """Difference between start and end must be at least 1.
    Current cannot be outside start...end range.
    """
    def __call__(
            self,
            start: int,
            end: int,
            current: int
    ) -> bool:
        if start == end:
            return False
        elif start <= current <= end:
            return True
        elif start >= current >= end:
            return True
        else:
            return False
