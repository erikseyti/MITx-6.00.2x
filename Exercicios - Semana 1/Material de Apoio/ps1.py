###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # indica se uma das vacas já foi selecionada para fazer o transporte
    dicionario_viagem = {}
    # indica a ordem de viagem entre as vacas, e a quantidade de viagens, pelo numero de listas dentro dela
    viagens = []
    # indica o nome das vacas que serão transportada em uma viagem.
    listaViagem = []
    
    while len(dicionario_viagem) < len(cows):
        copias_cow = sorted(cows.items(), key=lambda c: -c[1])
        
        pesoViagem = limit
        listaViagem = []
        
        for vaca in copias_cow:
            if vaca[0] not in dicionario_viagem and vaca[1] <= pesoViagem:
                listaViagem.append(vaca[0])
                pesoViagem = pesoViagem - vaca[1]
                dicionario_viagem[vaca[0]] = vaca[1] 
        
        viagens.append(listaViagem)
        
    return viagens


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    copia_cows = cows.copy()
    listaCows = []
    listaViagensExcluidas = []
    listaViagens = []
    listaViagensDisponiveis = []
    
    for key in cows.keys():
        listaCows.append(key)

            
    for partition in get_partitions(listaCows):
        listaViagens.append(partition)
        
        for viagem in partition:
            pesoMaximo = 0
            for vaca in viagem:
                pesoMaximo = pesoMaximo + copia_cows.get(vaca)
                
                if pesoMaximo > limit:
                    listaViagensExcluidas.append(partition)
                    break

    for viagem in listaViagens:
        if viagem not in listaViagensExcluidas:
            listaViagensDisponiveis.append(viagem)
            
    viagensOrdenadas = sorted(listaViagensDisponiveis, key=len)
    
    return viagensOrdenadas[0]
    
    

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
# print(cows)

# print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))

# print(brute_force_cow_transport({'Boo': 20, 'Lotus': 40, 'Miss Bella': 25, 'Milkshake': 40, 'MooMoo': 50, 'Horns': 25}, 100))


