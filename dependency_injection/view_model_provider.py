from presentation.view_model.login_view_model import LoginViewModel
from presentation.view_model.register_view_model import RegisterViewModel
from domain.use_case.use_case_wrapper.login_view_model_use_cases import LoginViewModelUseCases
from domain.use_case.use_case_wrapper.register_view_model_use_cases import RegisterViewModelUseCases
from dependency_injection.use_case_provider import use_cases


view_models = {
    LoginViewModel: LoginViewModel(use_cases[LoginViewModelUseCases]),
    'LoginViewModelFake': LoginViewModel(use_cases['LoginViewModelUseCasesFake']),
    RegisterViewModel: RegisterViewModel(use_cases[RegisterViewModelUseCases])
}


def inject(key):
    return view_models[key]
