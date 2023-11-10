
def gale_shapley(preferences):
 
    men, women = preferences

    men_matches = {}
    women_matches = {}

    men_prefs = {man: iter(prefs) for man, prefs in men.items()}

    unengaged_men = set(men)
    while unengaged_men:
        man = unengaged_men.pop()
        woman = next(men_prefs[man])

        if woman not in women_matches:
            men_matches[man] = woman
            women_matches[woman] = man
        else:
            current_partner = women_matches[woman]
            if women[woman].index(man) < women[woman].index(current_partner):
                men_matches[man] = woman
                women_matches[woman] = man
                unengaged_men.add(current_partner)

    return men_matches


course_pref={"c1":{"1":20,"2":50},"c2":{"1":60,"2":10}}
student_pref={"1":{"c1":1,"c2":2},"2":{"c1":2,"c2":1}}
course_vacancies={"c1":2,"c2":1}

l=[]
r=[]
for key, value in course_vacancies.items():
    for i in range(value):
        l.append(key+"_"+str(i))
# print(l)
for key,value in student_pref.items():
    # print(key)
    r.append(key)
m=len(l)
n=len(r)
edges_l_r = [[0 for _ in range(n)] for _ in range(m)]
edges_r_l = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    course=l[i].split("_")[0]
    for j in range(n):
        edges_l_r[i][j]=course_pref[course][r[j]]
        edges_r_l[i][j]=student_pref[r[j]][course]

l_pref={}
r_pref={}
for i in range(m):
    original_list = edges_l_r[i]
    sorted_indexes = sorted(range(len(original_list)), key=lambda k: original_list[k], reverse=True)
    new_list = [r[j] for j in sorted_indexes]
    l_pref[l[i]]=new_list

for i in range(n):
    original_list = edges_r_l[i]
    sorted_indexes = sorted(range(len(original_list)), key=lambda k: original_list[k], reverse=True)
    new_list = [l[j] for j in sorted_indexes]
    r_pref[r[i]]=new_list


print(l_pref)
print(r_pref)


preferences=(l_pref,r_pref)
matches=gale_shapley(preferences)
for man, woman in matches.items():
    print(f"{man} is matched with {woman}")





 
