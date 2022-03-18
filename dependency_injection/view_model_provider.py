from presentation.view_model.LoginViewModel import LoginViewModel
from domain.use_case.use_case_wrapper.LoginViewModelUseCases import LoginViewModelUseCases
from domain.use_case.use_case_wrapper.RegisterViewModelUseCases import RegisterViewModelUseCases
from dependency_injection.use_case_provider import use_cases


view_models = {
    LoginViewModel: LoginViewModel(use_cases[LoginViewModelUseCases]),
    RegisterViewModel: RegisterViewModel(use_cases[RegisterViewModelUseCases])
}


def inject(key):
    return view_models[key]
