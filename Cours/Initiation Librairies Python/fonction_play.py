def play(nb_tours)
    """Simule plusieurs tours du jeu Monty Hall.
    
    Args: nb_tours: le nombre de tours testes.
    
    Returns: Tableau avec les gains selon la strategie.
    """
    table = np.zeros(nb_tours, 3)
    