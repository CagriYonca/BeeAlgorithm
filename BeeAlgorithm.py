import numpy as np

def read_values_from_file(filename):
    f = open(filename, "r")
    array = []
    for line in f:
        array.append(float(line))
    f.close()

    return array

class Bee_Algorithm():
    def __init__(self, nPioneerBees, nFollowerBees,
                 cap_filename, req_filename, dist_filename):
        self.capacities = read_values_from_file(cap_filename)
        self.demands = read_values_from_file(req_filename)
        self.distances = read_values_from_file(dist_filename)
        self.num_of_stores = len(self.capacities)
        self.num_of_customers = len(self.demands)

        self.pioneer_bee_number = nPioneerBees

        self.PioneerBees = self.init_pioneers()
        self.nFollowerBee = nFollowerBees

    def init_pioneers(self):
        array = []

        for i in range(self.pioneer_bee_number):
            array.append(PioneerBee(self.num_of_stores, self.num_of_customers,
                                    self.capacities, self.demands,
                                    self.distances))
        return array

    def print_matrix(self, index):
        print(self.PioneerBees[index].get_matrix()[0])

class PioneerBee():
    def __init__(self, pStores, pCustomers, pCapacities, pDemands, pDistances):
        self.num_of_stores = pStores
        self.num_of_customers = pCustomers
        self.capacities2 = pCapacities  # NULL
        self.demands = pDemands
        self.distances = pDistances
        self.cost_val = 0

        self.pioneer_bees = np.zeros((self.num_of_customers, self.num_of_stores))

        self.random_matrix()

    def get_matrix(self):
        return self.pioneer_bees

    def random_matrix(self):
        self.capacities = read_values_from_file("Depo-Kapasite.txt")

        for customer in range(self.num_of_customers):
            while (self.pioneer_bees[customer].sum() == 0):
                seed = np.random.randint(self.num_of_stores)
                if (self.capacities[seed] >= self.demands[customer]):
                    self.pioneer_bees[customer, seed] = 1
                    self.capacities[seed] -= self.demands[customer]

    def evaluate_cost_function(self):
        for i in range(self.num_of_customers):
            self.cost_val += self.distances[i * self.num_of_stores + np.where(self.pioneer_bees[i] == 1)[0][0]] * self.demands[i]

a = Bee_Algorithm(10, 0,"Depo-Kapasite.txt","Müşteri-Talep.txt","Uzaklık-km.txt")
pri = a.PioneerBees[0]
pri.evaluate_cost_function()