import networkx as nx

def gale_shapley(preferences):
    # Create a bipartite graph
    G = nx.Graph()

    # Split preferences into two groups (men and women)
    men, women = preferences

    # Add nodes for men and women
    G.add_nodes_from(men, bipartite=0)
    G.add_nodes_from(women, bipartite=1)

    # Generate edges based on men's preferences
    for man, woman_list in men.items():
        for woman in woman_list:
            G.add_edge(man, woman)

    # Initialize empty matches for men and women
    men_matches = {}
    women_matches = {}

    # Create dictionaries to store men's preferences as queues
    men_prefs = {man: iter(prefs) for man, prefs in men.items()}

    # While there are unengaged men
    unengaged_men = set(men)
    while unengaged_men:
        man = unengaged_men.pop()
        woman = next(men_prefs[man])

        # If woman is unengaged, they become a pair
        if woman not in women_matches:
            men_matches[man] = woman
            women_matches[woman] = man
        else:
            # If woman prefers this man over her current partner
            current_partner = women_matches[woman]
            if women[woman].index(man) < women[woman].index(current_partner):
                men_matches[man] = woman
                women_matches[woman] = man
                unengaged_men.add(current_partner)

    return men_matches

# Example preferences
men_preferences = {
    'M1': ['W2', 'W1', 'W3'],
    'M2': ['W1', 'W2', 'W3'],
    'M3': ['W2', 'W1', 'W3'],
}

women_preferences = {
    'W1': ['M2', 'M1', 'M3'],
    'W2': ['M1', 'M2', 'M3'],
    'W3': ['M2', 'M1', 'M3'],
}

preferences = (men_preferences, women_preferences)

matches = gale_shapley(preferences)

# Print the resulting stable matches
for man, woman in matches.items():
    print(f"{man} is matched with {woman}")
