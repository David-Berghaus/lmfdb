from lmfdb import db

belyi_galmaps = db.belyi_galmaps

def belyi_friend_lookup(passport_data):
    G = passport_data["G"]
    P = G.perm_group()
    mu = G.index()
    lambda_2 = [int(i) for i in G.S2().cycle_type()]
    lambda_3 = [int(i) for i in G.S3().cycle_type()]
    lambda_T = [int(i) for i in (G.S2()*G.S3()).cycle_type()]
    lambdas = [lambda_T, lambda_3, lambda_2] #To Do: Check if this order is always correct
    for belyi_map in belyi_galmaps.search({'lambdas': lambdas}, projection=['label','base_field','triples']):
        if belyi_map['base_field'] == list(passport_data["K"].polynomial()):
            for triple in belyi_map['triples']:
                P_belyi = PermutationGroup([Permutation(triple[2]), Permutation(triple[1])])
                conj = libgap.RepresentativeAction(gap(f"SymmetricGroup({mu})"), gap(P), gap(P_belyi)) #Check for conjugacy, see: https://ask.sagemath.org/question/44357/determining-if-two-subgroups-of-a-symmetric-group-are-conjugate/?answer=47983#post-id-47983
                if conj != gap("fail"):
                    return belyi_map['label']
    return "\\N"