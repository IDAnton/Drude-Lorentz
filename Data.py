import numpy as np

C = 2.998e10
ELECTRON_MASS_GRAMS = 9.1e-28
ELECTRON_CHARGE = 4.8e-10
ATOMIC_MASS_UNITS = 1.66e-24
MAX_MODES = 10


class Data:
    def __init__(self, w_range=(10, 4500), discretization=1000, free_N=1e18, free_mass=ELECTRON_MASS_GRAMS,
                 free_gamma=1, membrane_epsilon_limit=2, bound_number=0, thickness=100 * 1e-7, N_media=1 + 0j, N_air = 1, free_charge=ELECTRON_CHARGE,
                 free_freq_vibration=1100, angle_degrees=45):
        # global params
        self.discretization = discretization
        self.phi = np.zeros(self.discretization, dtype=np.double)
        self.T = np.zeros(self.discretization, dtype=np.double)
        self.R_23 = np.zeros(self.discretization, dtype=np.double)
        self.R_12 = np.zeros(self.discretization, dtype=np.double)
        self.D = np.zeros(self.discretization, dtype=np.double)
        self.alpha = np.zeros(self.discretization, dtype=np.double)
        self.A = np.zeros(self.discretization, dtype=np.double)
        self.w_range = w_range
        self.w = np.linspace(self.w_range[0], self.w_range[1], self.discretization)
        self.r_12 = np.zeros(self.discretization, dtype=np.complex128)
        self.r_23 = np.zeros(self.discretization, dtype=np.complex128)
        self.epsilon_real = np.zeros(self.discretization, dtype=np.double)
        self.epsilon_im = np.zeros(self.discretization, dtype=np.double)
        self.cos_angle = np.zeros(self.discretization, dtype=np.double)
        self.rTE = np.zeros(self.discretization, dtype=np.complex128)
        self.rTM = np.zeros(self.discretization, dtype=np.complex128)
        self.RTE = np.zeros(self.discretization, dtype=np.double)
        self.RTM = np.zeros(self.discretization, dtype=np.double)
        self.TE_phase = np.zeros(self.discretization, dtype=np.double)
        self.TM_phase = np.zeros(self.discretization, dtype=np.double)
        self.RNP = np.zeros(self.discretization, dtype=np.double)
        self.tau_12 = np.zeros(self.discretization, dtype=np.complex128)
        self.tau_13 = np.zeros(self.discretization, dtype=np.complex128)
        self.tau = np.zeros(self.discretization, dtype=np.complex128)
        N = 1  # ??
        #self.r_12 = (self.N_air - N) / (self.N_air + N)
        #self.r_23 = (N - self.N_media) / (N + self.N_media)
        #self.phi = self.phase()  # phase phi_12(freq)
        #self.epsilon_real = np.real(self.calculate_epsilon())  # imag part of epsilon
        #self.epsilon_imag = np.imag(self.calculate_epsilon())  # real part of epsilon

        #self.R_12 = self.reflection_12_23()[0]  # R_12 reflection coefficient 1-2
        #self.R_23 = self.reflection_12_23()[1]  # R_23 reflection coefficient 2-3
        #self.alpha = self.adsorbtion_coefficient_calc()  # adsorbtion coefficient
        #self.T = self.transmission_of_the_film()  # transmission of the film
        #.A = -np.log(self.T)  # optical density of the film with interference
        #self.D = self.optical_density_of_the_film()  # optical density of the film without interference
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
        self.angle = angle_degrees * np.pi / 180

        # modes params:
        self.bound_number = bound_number
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
        self.N = np.zeros(self.discretization, dtype=np.complex128)
        # experimental data
        self.experiment_x = None
        self.experiment_y = None
        self.experiment2_x = None
        self.experiment2_y = None

    def init_new_charge(self):
        i = self.bound_number
        self.bound_gamma[i] = 1
        self.bound_freq_vibration[i] = 1000
        self.bound_effective_charges[i] = ELECTRON_CHARGE
        self.bound_masses[i] = ATOMIC_MASS_UNITS * 1
        self.bound_N[i] = 1e22
        self.calculate_w_i_plasm()

    def calculate(self):
        self.calculate_w_0_plasm()
        self.calculate_w_i_plasm()
        self.calculate_epsilon()
        self.real_and_imag_of_sqrt_epsilon()
        self.adsorbtion_coefficient_calc()
        self.optical_density_of_film()
        self.reflection_12_23()
        self.transmission_of_the_film()
        self.phase()
        self.A_coef()
        self.angle_cos_calc()
        self.rTE_calc()
        self.rTM_calc()
        self.phases_TE_TM()
        self.RNP_calc()

    def update_w_range(self):
        self.w = np.linspace(self.w_range[0], self.w_range[1], self.discretization)

    def calculate_w_0_plasm(self):  # calculating freq of w0, returns 1 number = w0
        self.w_plasm_0 = self.free_charge / (2 * np.pi * C) * \
                         np.sqrt(4 * np.pi * self.free_N / (self.free_mass * self.membrane_epsilon_limit))

    def calculate_w_i_plasm(self):  # calculating freq for every mode, returns list with all freq (w_i)
        self.w_i_plasm = self.bound_effective_charges / (2 * np.pi * C) * \
            np.sqrt(4 * np.pi * self.bound_N / (3 * self.bound_masses * self.membrane_epsilon_limit))

    def calculate_epsilon(self):  # calculating epsilon(freq), returns epsilon(freq)
        epsilon_free = 1 - np.power(self.w_plasm_0, 2) / (np.power(self.w, 2) + 1j * self.w * self.free_gamma)
        bounded_part = np.zeros(self.discretization, dtype=np.complex128)

        for i in range(self.bound_number):
            bounded_part += self.w_i_plasm[i]**2 / (self.bound_freq_vibration[i] ** 2 - np.power(self.w, 2) - self.w * 1j * self.bound_gamma[i])
        self.epsilon = self.membrane_epsilon_limit * (epsilon_free + bounded_part)
        self.epsilon_real, self.epsilon_im = np.real(self.epsilon), np.imag(self.epsilon)

    def real_and_imag_of_sqrt_epsilon(self):
        """calculating real part and imag part of epsilon in square, returns imag and real parts of N = sqrt(
        epsilon) """
        self.N = np.sqrt(self.epsilon)
        self.N_n, self.N_k = np.real(self.N), np.imag(self.N)

    def adsorbtion_coefficient_calc(self):  # calculating adsorbtion coef, returns alpha coef
        self.alpha = 4 * np.pi * self.N_k * self.w

    def optical_density_of_film(self):  # calculating optical density of the film, returns D coef
        self.D = self.alpha * self.thickness

    def reflection_12_23(self):  # air-film and film-environment
        self.r_12 = (self.N_air - np.sqrt(self.epsilon)) / (self.N_air + np.sqrt(self.epsilon))
        self.r_23 = (np.sqrt(self.epsilon) - self.N_media) / (np.sqrt(self.epsilon) + self.N_media)
        self.R_12 = self.r_12 * np.conjugate(self.r_12)
        self.R_23 = self.r_23 * np.conjugate(self.r_23)

    #def transmission_of_the_film(self):  # returns transmission
        #delta = 2 * self.thickness * self.N_n
        #self.T = ((1 - self.R_12) * (1 - self.R_23) * np.exp(-self.alpha*self.thickness)) / (1 + self.R_12 * self.R_23 + 2 * np.sqrt(self.R_12 * self.R_23) * np.exp(-2 * self.alpha * self.thickness) * np.cos(delta * self.w))

    def phase(self):  # returns phase_12
        self.phi = np.arccos(np.real(self.r_12 / np.absolute(self.r_12)))

    def angle_cos_calc(self):
        self.cos_angle = np.sqrt(1 - (self.N_air * self.N_air) * np.power(np.sin(self.angle), 2) / (self.N * self.N))

    def rTE_calc(self):
        self.rTE = (self.N_air * np.cos(self.angle) - self.N * self.cos_angle) / (self.N_air * np.cos(self.angle) + self.N * self.cos_angle)
        self.RTE = self.rTE * np.conjugate(self.rTE)

    def rTM_calc(self):
        self.rTM = (self.N_air * self.cos_angle - self.N * np.cos(self.angle)) / (self.N_air * self.cos_angle + self.N * np.cos(self.angle))
        self.RTM = self.rTM * np.conjugate(self.rTM)

    def phases_TE_TM(self):
        self.TE_phase = np.arccos(np.real(self.rTE / np.sqrt(self.RTE)))
        self.TM_phase = np.arccos(np.real(self.rTM / np.sqrt(self.RTM)))

    def RNP_calc(self):
        self.RNP = (self.RTE + self.RTM) / 2

    def transmission_of_the_film(self):  # returns transmission:
        self.tau_12 = 2 * self.N_air / (self.N_air + self.N)
        self.tau_13 = 2 * self.N_air / (self.N_media + self.N)
        self.tau = (self.tau_12 * self.tau_13 * np.exp(-1 * self.alpha * self.thickness)) / (1 + self.r_12 * self.r_23 * np.exp(-2 * self.alpha * self.thickness) * np.cos(2 * np.pi * 2 * self.thickness * self.N_n * self.w))
        self.T = self.tau * np.conjugate(self.tau)

    def A_coef(self):  # optical density of the film with interference
        self.A = -np.log(self.T)