class ValidateTaskProgressUseCase:
    def __call__(
            self,
            start_value: int,
            end_value: int,
            current_progress: int
    ) -> bool:
        if start_value == end_value:
            return False
        elif start_value <= current_progress <= end_value:
            return True
        elif start_value >= current_progress >= end_value:
            return True
        else:
            return False
