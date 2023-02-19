import numpy as np

C = 2.998e10
MAX_MODES = 10


class Data:
    def __init__(self, w_range=(10, 4500), discretization=1000, free_N=10e10, free_mass=9.1e-28,
                 free_w_fade=30, membrane_epsilon_limit=2, modes_number=1, thickness=100, N_media=1):
        # global params
        self.w_range = w_range
        self.discretization = discretization
        self.w = np.linspace(self.w_range, self.discretization)

        # free charge params
        self.free_N = free_N
        self.free_mass = free_mass
        self.free_w_fade = free_w_fade

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
        self.bound_w_fade = np.zeros(MAX_MODES, dtype=np.double)
        self.bound_gamma = np.zeros(MAX_MODES, dtype=np.double)

        # calculated params
        self.w_plasm_modes = np.zeros(MAX_MODES, dtype=np.complex128)
        self.epsilon = np.zeros(self.discretization, dtype=np.complex128)

    def calculate_w_plasm(self):
        pass
