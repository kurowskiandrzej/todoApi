from dependency_injection.view_model_provider import view_models
from dependency_injection.repository_provider import repositories
from dependency_injection.use_case_provider import use_cases

__register = view_models | repositories | use_cases


def resolve(key):
    return __register[key]
