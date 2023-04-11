from lmfdb import db

belyi_galmaps = db.belyi_galmaps

def belyi_friend_lookup(passport_data):
    G = passport_data["G"]
    P = G.perm_group()
    mu = int(G.index())
    c = max(G.cusp_widths())
    [a_s, b_s, c_s] = sorted([int(2),int(3),int(c)])
    base_field = list(map(lambda x: int(x),list(passport_data["K"].polynomial())))
    for belyi_map in belyi_galmaps.search({'a_s': a_s, 'b_s': b_s, 'c_s': c_s, 'base_field': base_field, 'deg': mu}, projection=['label','triples']):
        for triple in belyi_map['triples']:
            P_belyi = PermutationGroup([Permutation(triple[2]), Permutation(triple[1])])
            conj = libgap.RepresentativeAction(gap(f"SymmetricGroup({mu})"), gap(P), gap(P_belyi)) #Check for conjugacy, see: https://ask.sagemath.org/question/44357/determining-if-two-subgroups-of-a-symmetric-group-are-conjugate/?answer=47983#post-id-47983
            if conj != gap("fail"):
                return belyi_map['label']
    return "\\N"