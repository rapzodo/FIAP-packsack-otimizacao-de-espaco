import random

def tournament_selection(population, fitness_scores, tournament_size):
    #Realiza a seleção por torneio usando 3 variaveis:
    #1 population: lista de indivíduos (listas binárias).
    #2 fitness_scores: lista com valores de fitness correspondentes aos indivíduos.
    #3 tournament_size: número de competidores por torneio.
      
    tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
    tournament.sort(key=lambda x: x[1], reverse=True)  # Ordena pelo fitness (descendente)
    return tournament[0][0]  # Retorna o melhor indivíduo


def roulette_selection(population, fitness_scores):

    #Realiza a seleção por roleta usando 2 variaveis: (probabilidade proporcional ao fitness).
    #1 population: lista de indivíduos (listas binárias).
    #2 fitness_scores: lista com valores de fitness correspondentes aos indivíduos.
  
    total_fitness = sum(fitness_scores)
    if total_fitness == 0:
        raise ValueError("Total fitness is zero. Cannot perform roulette selection.")
    
    pick = random.uniform(0, total_fitness)
    current = 0
    
    for individual, fitness in zip(population, fitness_scores):
        current += fitness
        if current >= pick:
            return individual
