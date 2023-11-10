import networkx as nx
def matching(course_pref,course_vacancies):
    # course_pref={"c1":{"1":20,"2":50},"c2":{"1":60,"2":10}}
    #course_vacancies={"c1":2,"c2":1}
    left_nodes=[]
    right_nodes=[]
    edges=[]
    G = nx.Graph()
    for course_id,student_list in course_pref.items():
        for roll,token_score in student_list.items():
            l=course_vacancies[course_id]
            right_nodes.append(roll)
            for i in range(l):
                edges.append((course_id+"_"+str(i),roll,{"weight":token_score}))
                left_nodes.append(course_id+"_"+str(i))

    G.add_nodes_from(left_nodes, bipartite=0)
    G.add_nodes_from(right_nodes, bipartite=1)

    G.add_edges_from(edges)
    matching = nx.max_weight_matching(G, weight='weight')
    max_weight = sum(G[match[0]][match[1]]['weight'] for match in matching)
    return matching, max_weight


# for match in matching:
#     if(match[0][0]=="c"):
#         print(match[0].split("_")[0],"->",match[1])
#     else:
#         print(match[1].split("_")[0],"->",match[0])

