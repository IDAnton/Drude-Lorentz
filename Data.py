import numpy as np

C = 2.998e10
MAX_MODES = 10


class Data:
    def __init__(self, w_range=(10, 4500), discretization=1000, free_N=10e10, free_mass=9.1e-28,
                 free_gamma=30, membrane_epsilon_limit=2, modes_number=1, thickness=100, N_media=1, free_charge=4.8,
                 free_freq_vibration=1100):
        # global params
        self.w_range = w_range
        self.discretization = discretization
        self.w = np.linspace(self.w_range, self.discretization)

        # free charge params
        self.free_N = free_N
        self.free_mass = free_mass
        self.free_gamma = free_gamma
        self.free_charge = free_charge
        self.free_freq_vibration = free_freq_vibration
        # membrane params
        self.membrane_epsilon_limit = membrane_epsilon_limit
        self.thickness = thickness
        self.N_media = N_media
        self.N_media_from_w = None

        # modes params:
        self.modes_number = modes_number
        self.bound_N = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_masses = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_effective_charges = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_freq_vibration = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_gamma = np.zeros(MAX_MODES, dtype=np.double)
        # calculated params
        self.w_plasm_modes = np.zeros(MAX_MODES, dtype=np.complex128)
        self.epsilon = np.zeros(self.discretization, dtype=np.complex128)

    def calculate_w_0_plasm(self):  # calculating freq of w0, returns 1 number = w0
        return (self.free_charge / 2 * np.pi * C) * (
            np.sqrt(4 * np.pi * self.free_N / self.free_mass * self.membrane_epsilon_limit))

    def calculate_w_i_plasm(self):  # calculating freq for every mode, returns list with all freq (w_i)
        return (self.bound_effective_charges / 2 * np.pi * C) * (
            np.sqrt(4 * np.pi * self.bound_N / 3 * self.bound_masses * self.membrane_epsilon_limit))

    def calculate_epsilon(self):  # calculating epsilon(freq), returns epsilon(freq)
        return self.membrane_epsilon_limit * (1 - np.power(self.calculate_w_0_plasm(), 2) / (
                    np.power(self.free_freq_vibration, 2) + j * self.free_freq_vibration * self.free_gamma) + np.sum(
            np.power(self.calculate_w_i_plasm(), 2) / (np.power(self.bound_freq_vibration,
                                                                2) - self.free_freq_vibration - self.free_freq_vibration * j * self.bound_gamma)))

    def real_and_imag_of_sqrt_epsilon(
            self):  # calculating real part and imag part of epsilon in square, returns imag and real parts of N = sqrt(epsilon)
        N = np.sqrt(self.calculate_epsilon())
        return np.imag(N), np.real(N)

    def adsorbtion_coefficient_calc(self):  # calculating adsorbtion coef, returns alpha coef
        alpha = 4 * np.pi * self.real_and_imag_of_sqrt_epsilon()[0] * self.bound_freq_vibration
        return alpha

    def optical_density_of_film(self):  # calculating optical density of the film, returns D coef
        D = self.adsorbtion_coefficient_calc() * self.thickness
        return D
