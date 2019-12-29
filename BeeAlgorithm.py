import numpy as np
import random

class Bee_Algorithm():
    def __init__(self, nPioneerBees, nFollowerBees,
                 cap_filename, req_filename, dist_filename):
        self.capacities = self.read_values_from_file(cap_filename)
        self.demands = self.read_values_from_file(req_filename)
        self.distances = self.read_values_from_file(dist_filename)
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

    def read_values_from_file(self, filename):
        with open(filename) as f:
            array = []
            for line in f:
                array.append(float(line))
            return array

    def print_matrix(self, index):
        print(self.PioneerBees[index].get_matrix())


class PioneerBee():
    def __init__(self, pStores, pCustomers, pCapacities, pDemands, pDistances):
        self.num_of_stores = pStores
        self.num_of_customers = pCustomers
        self.capacities2 = pCapacities
        self.demands = pDemands
        self.distances = pDistances

        self.pioneer_bees = np.zeros((self.num_of_customers, self.num_of_stores))

        self.random_matrix()

    def get_matrix(self):
        return self.pioneer_bees

    def random_matrix(self):
        print("random_matrix {}".format(self.capacities2[0]))

        with open("C:/Users/user/Desktop/CerenProje/Müşteri-Talep.txt") as f:
            array = []
            for line in f:
                array.append(float(line))
            return array

        for customer in range(self.num_of_customers):
            while (self.pioneer_bees[customer].sum() == 0):
                seed = np.random.randint(self.num_of_stores)
                if (self.capacities2[seed] >= self.demands[customer]):
                    self.pioneer_bees[customer, seed] = 1
                    self.capacities2[seed] -= self.demands[customer]
        print("CIKMIYOKİ {}".format(self.capacities2[0]))

a = Bee_Algorithm(10, 0,
                  "C:/Users/user/Desktop/CerenProje/Depo-Kapasite.txt",
                  "C:/Users/user/Desktop/CerenProje/Müşteri-Talep.txt",
                  "C:/Users/user/Desktop/CerenProje/Uzaklık-km.txt")