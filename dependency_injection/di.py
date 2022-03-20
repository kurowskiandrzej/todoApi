from dependency_injection.view_model_provider import view_models
from dependency_injection.repository_provider import repositories
from dependency_injection.use_case_provider import use_cases

register = view_models | repositories | use_cases


def resolve(key):
    return register[key]
