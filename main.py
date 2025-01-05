def stable_marriage(men_prefs, women_prefs):
    free_men = list(men_prefs.keys())
    proposals = {man: [] for man in men_prefs}
    current_matches = {}
    women_comparison = {}
    for woman, prefs in women_prefs.items():
        women_comparison[woman] = {man: rank for rank, man in enumerate(prefs)}
    while free_men:
        man = free_men[0]
        man_prefs = men_prefs[man]
        for woman in man_prefs:
            if woman not in proposals[man]:
                proposals[man].append(woman)
                if woman not in current_matches:
                    current_matches[woman] = man
                    free_men.remove(man)
                else:
                    current_partner = current_matches[woman]
                    if women_comparison[woman][man] < women_comparison[woman][current_partner]:
                        current_matches[woman] = man
                        free_men.append(current_partner)
                        free_men.remove(man)
                break

    return current_matches


men_preferences = {
    "A": ["X", "Y", "Z"],
    "B": ["Z", "X", "Y"],
    "C": ["Y", "X", "Z"]
}

women_preferences = {
    "X": ["B", "A", "C"],
    "Y": ["A", "C", "B"],
    "Z": ["C", "B", "A"]
}

matches = stable_marriage(men_preferences, women_preferences)

print("Стабильные пары:")
for woman, man in matches.items():
    print(f"{man} и {woman}")




