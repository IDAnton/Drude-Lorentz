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
        self.w = np.linspace(self.w_range[0], self.w_range[1], self.discretization)

        self.w = np.linspace(self.w_range, self.discretization)
        self.r_12 = (self.N_air - N) / (self.N_air + N)
        self.r_23 = (N - self.N_media) / (N + self.N_media)
        self.phi = self.phase()  # phase phi_12(freq)
        self.epsilon_real = np.real(self.calculate_epsilon())  # imag part of epsilon
        self.epsilon_imag = np.imag(self.calculate_epsilon())  # real part of epsilon
        self.n = self.real_and_imag_of_sqrt_epsilon()[2]  # real part of N (n(freq))
        self.k = self.real_and_imag_of_sqrt_epsilon()[1]  # imag part of N (k(freq))
        self.N = self.real_and_imag_of_sqrt_epsilon()[0]  # N refraction coefficient
        self.R_12 = self.reflection_12_23()[0]  # R_12 reflection coefficient 1-2
        self.R_23 = self.reflection_12_23()[1]  # R_23 reflection coefficient 2-3
        self.alpha = self.adsorbtion_coefficient_calc()  # adsorbtion coefficient
        self.T = self.transmission_of_the_film()  # transmission of the film
        self.A = -np.log(self.T)  # optical density of the film with interference
        self.D = self.optical_density_of_the_film()  # optical density of the film without interference
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
        self.N_air = N_air
        self.N_media_from_w = None

        # modes params:
        self.modes_number = modes_number
        self.bound_N = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_masses = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_effective_charges = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_freq_vibration = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_gamma = np.zeros(MAX_MODES, dtype=np.double)
        # calculated params
        self.w_plasm_0 = None
        self.w_i_plasm = np.zeros(MAX_MODES, dtype=np.complex128)
        self.epsilon = np.zeros(self.discretization, dtype=np.complex128)
        self.N_n = np.zeros(self.discretization, dtype=np.double)  # real part of Refractive index
        self.N_k = np.zeros(self.discretization, dtype=np.double)  # complex part of Refractive index

        self.calculate()

    def calculate(self):
        self.calculate_w_0_plasm()
        self.calculate_w_i_plasm()
        self.calculate_epsilon()
        self.real_and_imag_of_sqrt_epsilon()

    def update_w_range(self):
        self.w = np.linspace(self.w_range[0], self.w_range[1], self.discretization)

    def calculate_w_0_plasm(self):  # calculating freq of w0, returns 1 number = w0
        return (self.free_charge / 2 * np.pi * C) * (
            np.sqrt(4 * np.pi * self.free_N / self.free_mass * self.membrane_epsilon_limit))

    def calculate_w_i_plasm(self):  # calculating freq for every mode, returns list with all freq (w_i)
        return (self.bound_effective_charges / 2 * np.pi * C) * (
            np.sqrt(4 * np.pi * self.bound_N / 3 * self.bound_masses * self.membrane_epsilon_limit))

    def calculate_epsilon(self):  # calculating epsilon(freq), returns epsilon(freq)
        epsilon_free = self.membrane_epsilon_limit * (1 - np.power(self.w_plasm_0, 2) / (
                np.power(self.w, 2) + 1j * self.w * self.free_gamma))
        bounded_part = np.zeros(self.discretization, dtype=np.complex128)

        for gamma_i, w_i in zip(self.bound_gamma, self.bound_freq_vibration):
            bounded_part += 1 / (np.power(w_i, 2) - self.w - self.w * 1j * gamma_i)
        bounded_part *= np.sum(self.w_i_plasm)
        self.epsilon = epsilon_free + bounded_part

    def real_and_imag_of_sqrt_epsilon(self):
        """calculating real part and imag part of epsilon in square, returns imag and real parts of N = sqrt(
        epsilon) """
        N = np.sqrt(self.epsilon)
        self.N_n, self.N_n = np.real(N), np.imag(N)

    def adsorbtion_coefficient_calc(self):  # calculating adsorbtion coef, returns alpha coef
        alpha = 4 * np.pi * self.real_and_imag_of_sqrt_epsilon()[1] * self.bound_freq_vibration
        return alpha

    def optical_density_of_film(self):  # calculating optical density of the film, returns D coef
        D = self.adsorbtion_coefficient_calc() * self.thickness
        return D

    def reflection_12_23(self):  # air-film and film-environment
        R_12 = self.r_12 * np.conjugate(self.r_12)
        R_23 = self.r_23 * np.conjugate(self.r_23)
        return R_12, R_23

    def transmission_of_the_film(self):  # returns transmission
        delta = 2 * self.thickness * self.n
        T = ((1 - self.R_12) * (1 - self.R_23) * np.exp(-self.alpha*self.thickness)) / (1 + self.R_12 * self.R_23 + 2 * np.sqrt(self.R_12 * self.R_23) * np.exp(-2 * self.alpha * self.thickness) * np.cos(delta * self.bound_freq_vibration))
        return T

    def phase(self):  # returns phase_12
        return np.arccos(np.real(self.r_12 / np.absolute(self.r_12)))
