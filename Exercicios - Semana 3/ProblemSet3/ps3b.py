# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics

import random
import pylab

'''
Begin helper code
'''

# seed para debbuging para testar programas estocasticos
random.seed(0)

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        # self.maxBirthProb = random.random()
        # self.clearProb = random.random()

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

        # TODO

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb
        # TODO

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb
        # TODO

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        isClear = random.random()
        if isClear>=self.getClearProb():
            return False
        else:
            return True

        # TODO


    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        reproductionProb = self.maxBirthProb * (1-popDensity)
        chanceReproduction = random.random()

        if reproductionProb >= chanceReproduction:
            # SimpleVirus(self.maxBirthProb,self.clearProb)
            return SimpleVirus(self.maxBirthProb,self.clearProb)

        else:
            raise NoChildException()


        # TODO



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        # TODO

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses
        # TODO


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop
        # TODO


    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        """
        return len(self.getViruses())
        # TODO


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """

        listaVirusAtualizado = self.getViruses().copy()
        for v in listaVirusAtualizado:# lista
            eliminado = v.doesClear()
            if eliminado == True:
                self.viruses.remove(v)# getVirus

        listaVirusAtualizado = self.getViruses().copy()
        popDensity = len(self.getViruses())/self.getMaxPop() #getVirus
        # print(popDensity)

        for r in listaVirusAtualizado:
            try:
                reproduzir = r.reproduce(popDensity)
                self.viruses.append(reproduzir)
            except NoChildException:
                continue

        return len(self.getViruses())

        # TODO


# novoVirus = SimpleVirus(0.5,0.5)
# print(novoVirus.getMaxBirthProb())
# print(novoVirus.getClearProb())
# print(novoVirus.doesClear())
# # print(novoVirus.doesClear())
# paciente = Patient([novoVirus],25000)
# print(paciente.getViruses())
# print(paciente.getMaxPop())
# print(paciente.getTotalPop())
# print(paciente.update())

# # teste não reproduz uma unica vez
# print("teste não reproduz uma unica vez")
# # Tudo False
# v1 = SimpleVirus(1.0, 0.0)
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())

# # teste não reprodiz nem cria
# print("teste não reprodiz nem cria")
# # tudo False
# v1 = SimpleVirus(0.0, 0.0)
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())

# # teste onde sempre reproduz ou cria
# print("teste onde sempre reproduz ou cria")
# # tudo True
# v1 = SimpleVirus(1.0, 1.0)
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())

# # teste onde ele sempre esta livre do virus, e ele nunca se reproduz
# v1 = SimpleVirus(0.0, 1.0)
# print("teste onde ele sempre esta livre do virus, e ele nunca se reproduz")
# # tudo True
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())
# print(v1.doesClear())

# print(" ")
# print(" ")
# print(" ")
# # teste paciente que nunca esta livre e sempre reproduz
# print("teste paciente que nunca esta livre e sempre reproduz")
# virus = SimpleVirus(1.0, 0.0)
# patient = Patient([virus], 1000)
# for x in range(100):
#     patient.update()
#     print(patient.getTotalPop())
# print(patient.getTotalPop())

# print(" ")
# print(" ")
# print(" ")
# # teste paciente que nunca esta livre e sempre reproduz
# print("teste paciente que nunca esta livre e sempre reproduz")
# virus = SimpleVirus(1.0, 1.0)
# patient = Patient([virus], 1000)
# for x in range(100):
#     patient.update()
#     print(patient.getTotalPop())
# print(patient.getTotalPop())

#
# PROBLEM 2
#

# from ps3b_precompiled_37 import *

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    listaVirusPorSegundo = []
    # listaContador = []
    # contador = -1

    for tr in range(numTrials):
        virus = SimpleVirus(maxBirthProb,clearProb)
        patient = Patient(numViruses*[virus],maxPop)

        for s in range(300):
            if tr == 0:
                listaVirusPorSegundo.append(patient.update())
            else:
                listaVirusPorSegundo[s] = listaVirusPorSegundo[s] + patient.update()
        # contador = contador + 1
        # listaContador.append(contador)

    MediaVirusPorTentativas = [x / numTrials for x in listaVirusPorSegundo]


    pylab.plot(MediaVirusPorTentativas,label="SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()


    # TODO

# simulationWithoutDrug(100,1000,0.1,0.05,75)
# simulationWithoutDrug(100,1000,0.99,0.05,75)
# simulationWithoutDrug(100,1000,0.1,0.99,75)

#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """


        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        # self.maxBirthProb = maxBirthProb
        # self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

        # TODO


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances
        # TODO

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb
        # TODO

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if drug in self.resistances and True==self.resistances[drug]:
            return True
        else:
            return False

        # TODO


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        for d in activeDrugs:
            drogaTestada = self.isResistantTo(d)
            if drogaTestada == False:
                raise NoChildException

        reproductionProb = self.maxBirthProb * (1-popDensity)
        chanceReproduction = random.random()
        chanceReproduction = 0.001

        if reproductionProb >= chanceReproduction:
            novasResistencias = self.getResistances().copy()

            for key in novasResistencias:
                probabilidadeManterResistencia = self.getMutProb()
                fatorMutacao = random.random()

                if fatorMutacao< probabilidadeManterResistencia:
                    if novasResistencias[key] == True:
                        novasResistencias[key] = False
                    else:
                        novasResistencias[key] = True

            return ResistantVirus(self.maxBirthProb,self.clearProb,novasResistencias,self.getMutProb())

        else:
            raise NoChildException()



        # TODO


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.activeDrugs = []

        # TODO


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)


        # TODO


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.activeDrugs

        # TODO


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        numeroDrogas = len(drugResist)
        popVirusResistente = 0

        for v in self.viruses:
            contador = 0
            for d in drugResist:
                if v.isResistantTo(d)==True:
                    contador = contador + 1
                # else:
                #     break
            if contador == numeroDrogas:
                popVirusResistente = popVirusResistente + 1

        return popVirusResistente


        # TODO


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        listaVirusAtualizado = self.getViruses().copy()
        for v in listaVirusAtualizado:
            eliminado = v.doesClear()
            if eliminado == True:
                self.viruses.remove(v)

        listaVirusAtualizado = self.getViruses().copy()
        popDensity = len(self.getViruses())/self.getMaxPop()

        for r in listaVirusAtualizado:
            try:
                reproduzir = r.reproduce(popDensity,self.activeDrugs)
                self.viruses.append(reproduzir)
            except NoChildException:
                continue

        return len(self.getViruses())

        # TODO


# virus = SimpleVirus(maxBirthProb,clearProb)
# v1 = SimpleVirus(0.8,0.9)
# v1.reproduce(1)

# virus = ResistantVirus(0.1,0.05,{'guttagonol':True, 'srinol':True},0.1)
# print(virus.isResistantTo('guttagonol'))
# virus.reproduce(0.1, ['guttagonol','srinol'])
# virus.getTotalPop()

# virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
# print(virus.getResistances())

# for n in range(10):
#     virus.reproduce(0, [])
#     print(virus.getResistances())

# virus = ResistantVirus(1.0, 0.0, {"drug2": True}, 1.0)
# for n in range(10):
#     virus.reproduce(0, [])
#     print(virus.getResistances())

# virus = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# for n in range(10):
#     virus.reproduce(0, [])
#     print(virus.getResistances())


# virus = ResistantVirus(1.0, 0.0, {"drug2": True}, 1.0)
# for n in range(100):
#     virus.reproduce(0, [])
#     print(virus.getResistances())

# print("teste --------")

# virus = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# for n in range(100):
#     virus.reproduce(0, [])
#     print(virus.getResistances())


# virus = ResistantVirus(1.0, 1.0, {}, 0.0)
# patient = TreatedPatient([virus], 100)
# for n in range(100):
#     print(patient.update())


#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """
    listaVirusPorSegundo = []
    listaVirusResistentes = []
    listaVirusDepoisTratamento = []
    listaVirusResistentesDepoisTratamento = []
    
    
    for tr in range(numTrials):
        virus = ResistantVirus(maxBirthProb,clearProb,resistances,mutProb)
        patient = TreatedPatient(numViruses*[virus],maxPop)
        
        for s in range(150):
            if tr == 0:
                listaVirusPorSegundo.append(patient.update())
                listaVirusResistentes.append(patient.getResistPop(['guttagonol']))
            else:
                listaVirusPorSegundo[s] = listaVirusPorSegundo[s] + patient.update()
                listaVirusResistentes[s] = listaVirusResistentes[s] + patient.getResistPop(['guttagonol'])
        
        patient.addPrescription('guttagonol')
        
        for s in range(150):
            if tr == 0:
                listaVirusDepoisTratamento.append(patient.update())
                listaVirusResistentesDepoisTratamento.append(patient.getResistPop(['guttagonol']))
            else:
                listaVirusDepoisTratamento[s] = listaVirusDepoisTratamento[s] + patient.update()
                listaVirusResistentesDepoisTratamento[s] = listaVirusResistentesDepoisTratamento[s] + patient.getResistPop(['guttagonol'])
    

    listaVirusPorSegundo.extend(listaVirusDepoisTratamento)
    listaVirusResistentes.extend(listaVirusResistentesDepoisTratamento)
    
    MediaVirusPorTentativa = [x/ numTrials for x in listaVirusPorSegundo]
    MediaVirusResistentesPorTentativa = [x / numTrials for x in listaVirusResistentes]
    
    pylab.plot(MediaVirusPorTentativa,label='Resistance Virus - Total Population')
    pylab.plot(MediaVirusResistentesPorTentativa,label='Resistance Virus - Resistante to Guttagonol')
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('time step')
    pylab.ylabel('# viruses')
    pylab.legend(loc='best')
    pylab.show()
    

simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol':False}, 0.005, 100)

    # TODO
