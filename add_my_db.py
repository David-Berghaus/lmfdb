from lmfdb import db

def create_noncongruence_modular_curve_db():
    db.create_table(name='noncong_modular_curve',
        search_columns={'int': ['genus', 'psl2z_index', 'n_c', 'n_e2', 'n_e3'],
                        'int[][]': ['cusp_widths'],
                        'text': ['permS', 'permR', 'permT', 'label', 'monodromy_group', 'K', 'curve', 'base_field_label'],
                        'text[]': ['mf_spaces', 'embeddings', 'friends'],
                        'bool': ['is_congruence'],
                        },
        label_col='label',
        sort=['label'],
        table_description='Noncongruence modular curves',
        #Add proper descriptions later
        col_description={'genus': "Genus of the subgroup",
                            'psl2z_index': "Index of the subgroup in PSL2Z",
                            'n_c': "Number of cusps",
                            'n_e2': "Number of elliptic points of order 2",
                            'n_e3': "Number of elliptic points of order 3",
                            'cusp_widths': "Widths of the cusps",
                            'permS': "Permutation corresponding to the S action",
                            'permR': "Permutation corresponding to the R action",
                            'permT': "Permutation corresponding to the T action",
                            'label': "Label of the curve",
                            'monodromy_group': "Finite group generated by permS and permR",
                            'K': "Field of definition",
                            'curve': "Belyi map / elliptic curve / hyperelliptic curve",
                            'mf_spaces': "Spaces of modular forms",
                            'embeddings': "Embeddings of K into CC",
                            'friends': "Related LMFDB objects",
                            'is_congruence': "True if the subgroup is a congruence subgroup",
                        },
    )

def create_noncongruence_modular_form_space():
    db.create_table(name='noncong_modular_form_space',
        search_columns={'int': ['dim', 'weight'],
                        'text': ['type', 'label'],
                        'text[]': ['basis'],
                        },
        label_col='label',
        sort=['label'],
        table_description='Noncongruence modular form spaces',
        #Add proper descriptions later
        col_description={'dim': "Dimension of the space",
                            'weight': "Weight of the forms in the space",
                            'type': "Hauptmodul / Cusp Form / Holomorphic Modular Form",
                            'label': "Label of the space",
                            'basis': "Basis of the space",
                        },
    )

def create_noncongruence_modular_form():
    db.create_table(name='noncong_modular_form',
        search_columns={'int': ['weight', 'cusp_width', 'valuation'],
                        'text': ['type', 'label', 'K', 'v', 'u_str', 'u'],
                        'text[]': ['coefficients'],
                        },
        label_col='label',
        sort=['label'],
        table_description='Noncongruence modular form',
        #Add proper descriptions later
        col_description={'weight': "Weight of the form",
                            'cusp_width': "Width of the cusp associated to the form",
                            'valuation': "Valuation of the form",
                            'type': "Hauptmodul / Cusp Form / Holomorphic Modular Form",
                            'label': "Label of the form",
                            'K': "Field of definition",
                            'v': "Embedding of v into CC",
                            'u_str': "Expression for u",
                            'u': "Embedding of u into CC",
                            'coefficients': "Coefficients of the form",
                        },
    )

def create_tables():
    create_noncongruence_modular_curve_db()
    create_noncongruence_modular_form_space()
    create_noncongruence_modular_form()

def insert_example_entry():
    """
    Insert example entry for the database entry https://github.com/David-Berghaus/noncong_database/blob/main/7/0/7_0_2_1_1_0_a.json
    """
    create_tables()

    #Insert noncongruence modular curve
    db.noncong_modular_curve.insert_many({'label': '7.0.2.1.1.0.a',
                                            'genus': 0,
                                            'psl2z_index': 7,
                                            'n_c': 2,
                                            'n_e2': 1,
                                            'n_e3': 1,
                                            'cusp_widths': [[1, 1], [6, 1]],
                                            'permS': '(1 6)(2)(3 4)(5 7)',
                                            'permR': '(1 7 6)(2 3 5)(4)',
                                            'permT': '(1)(2 3 4 5 6 7)',
                                            'monodromy_group': 'C7 : C6',
                                            'K': 'v^2 - v + 1',
                                            'curve': '((x^2 + ((331776*v + 195357360)*u)*x + (62079188631552*v + 1006988320853568)*u^2)^3*(x + (-1866240*v + 3015384)*u))/((x + (-145152*v - 3938088)*u)^6) = 1728 + ((x^3 + ((-1679616*v - 418281336)*u)*x^2 + ((706462210805760*v - 9954051182869824)*u^2)*x + (14652604381524017135616*v - 29995890348016962943488)*u^3)^2*(x + (2488320*v + 2567832)*u))/((x + (-145152*v - 3938088)*u)^6)',
                                            'mf_spaces': ['7.0.2.1.1.0.a.0.H', '7.0.2.1.1.0.a.2.M', '7.0.2.1.1.0.a.4.M', '7.0.2.1.1.0.a.4.C'], #Ignore weight 6 space for now
                                            'embeddings': ["('(1 6)(2)(3 4)(5 7)', '(1 7 6)(2 3 5)(4)', '(1)(2 3 4 5 6 7)'): 0.50000000000000000? - 0.866025403784439?*I", "('(1 4)(2)(3 5)(6 7)', '(1 5 4)(2 3 6)(7)', '(1)(2 3 4 5 6 7)'): 0.50000000000000000? + 0.866025403784439?*I"],
                                            'friends': ['Belyi/7T4/6.1/3.3.1/2.2.2.1/a/'],
                                            'base_field_label': '2.0.3.1',
                                            'is_congruence': False,
                                            }
    )

    #Insert noncongruence modular form spaces
    db.noncong_modular_form_space.insert_many({'dim': 1,
                                                'weight': 0, 
                                                'type': 'Hauptmodul', 
                                                'label': '7.0.2.1.1.0.a.0.H', 
                                                'basis': ['7.0.2.1.1.0.a.0.h.a']
                                                },
                                                {'dim': 1, 
                                                'weight': 2, 
                                                'type': 'Holomorphic Modular Form', 
                                                'label': '7.0.2.1.1.0.a.2.M', 
                                                'basis': ['7.0.2.1.1.0.a.2.m.a']
                                                },
                                                {'dim': 3, 
                                                'weight': 4, 
                                                'type': 
                                                'Holomorphic Modular Form', 
                                                'label': '7.0.2.1.1.0.a.4.M', 
                                                'basis': ['7.0.2.1.1.0.a.4.m.a', '7.0.2.1.1.0.a.4.m.b', '7.0.2.1.1.0.a.4.m.c']
                                                },
                                                {'dim': 1, 
                                                'weight': 4, 
                                                'type': 'Cusp Form', 
                                                'label': '7.0.2.1.1.0.a.4.c', 
                                                'basis': ['7.0.2.1.1.0.a.4.C.a']
                                                },
    )

    #Insert noncongruence modular forms
    db.noncong_modular_form.insert_many({'weight': 0, 
                                            'cusp_width': 1, 
                                            'valuation': -1, 
                                            'type': 'Hauptmodul', 
                                            'label': '7.0.2.1.1.0.a.0.H.a', 
                                            'K': 'v^2 - v + 1',
                                            'base_field_label': '2.0.3.1', 
                                            'v': '0.50000000000000000? - 0.866025403784439?*I', 
                                            'u_str': '1/823543', 'u': '1.21426567890201e-6', 
                                            'coefficients': ['1', '0', '\\left(993257717760 v + 2787572739924\\right) u^{2}', '\\left(-2706394677997731840 v + 6101511713277790208\\right) u^{3}', '\\left(3328586427569770370433024 v - 7827560231874195815452926\\right) u^{4}', '\\left(-246690191956662020521813082112 v + 2020405603279225977670392004608\\right) u^{5}', '\\left(-5580185143838191749378579955408699392 v - 6521254171810914172419380962135314088\\right) u^{6}', '\\left(9938190613813312321884804126524437853896704 v + 2804227792950531847927979844886468993376256\\right) u^{7}', '\\left(-9974839286177131485320952878512871361096063123456 v + 13118942247741007156137324828941098437716139050559\\right) u^{8}', '\\left(5920980510425217697466627933402939776440355729874878464 v - 10917596745122026578975532824809483699790840699199291392\\right) u^{9}', '\\left(1218720145755695504853300987617215807685133891794728763916288 v + 13450632275811261322475249223770454667548860483586272476608420\\right) u^{10}']
                                        },
                                        {'weight': 2, 
                                            'cusp_width': 1, 
                                            'valuation': 0, 
                                            'type': 'Holomorphic Modular Form', 
                                            'label': '7.0.2.1.1.0.a.2.M.a', 
                                            'K': 'v^2 - v + 1', 
                                            'base_field_label': '2.0.3.1',
                                            'v': '0.50000000000000000? - 0.866025403784439?*I', 
                                            'u_str': '1/823543', 
                                            'u': '1.21426567890201e-6', 
                                            'coefficients': ['1', '\\left(145152 v + 3938088\\right) u', '\\left(-822203633664 v + 9912322512792\\right) u^{2}', '\\left(1740391304435997696 v + 10016874289782722208\\right) u^{3}', '\\left(-1325606902843077137203200 v + 17635843296056689476437784\\right) u^{4}', '\\left(-986001155724652126040951649792 v + 6401608332802913767486107095280\\right) u^{5}', '\\left(3100912902964312868516294149024038912 v + 15034798163388828143618848172147096160\\right) u^{6}', '\\left(-3000252984943415930673101079191947901454336 v + 5534613957846131694381945490032706213160256\\right) u^{7}', '\\left(1460231491232560275216649073046645665767074299904 v + 14652001319000211071684741091818741347211205766680\\right) u^{8}', '\\left(-484770259404880042604010703500371111731797717407986944 v + 15266107319081243920447029870864664929373988555847624456\\right) u^{9}']
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 0, 
                                            'type': 'Holomorphic Modular Form', 
                                            'label': '7.0.2.1.1.0.a.4.M.a', 
                                            'K': 'v^2 - v + 1', 
                                            'base_field_label': '2.0.3.1',
                                            'v': '0.50000000000000000? - 0.866025403784439?*I', 
                                            'u_str': '1/823543', 
                                            'u': '1.21426567890201e-6', 
                                            'coefficients': ['1', '0', '0', '\\left(-8716378656613662720 v + 2652390428981153280\\right) u^{3}', '\\left(992302248882822449725440 v - 10437549176678568024906000\\right) u^{4}', '\\left(-1749327037768875082050616688640 v + 33206057846322729558248824657920\\right) u^{5}', '\\left(-41435283722508178767277557313217495040 v + 23330145789402750828129049038866350080\\right) u^{6}', '\\left(23043085568220864103491425019456707550904320 v + 44652063385170277783769293247554331678346240\\right) u^{7}', '\\left(-55378144789708242907540890448943706826529864417280 v + 22598337630260777931973449920729775415432359031920\\right) u^{8}', '\\left(-4680421142626202462952371988120706422769660709052088320 v - 80360212876331599751409011412633757924939315215196876800\\right) u^{9}']
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 1, 
                                            'type': 'Holomorphic Modular Form', 
                                            'label': '7.0.2.1.1.0.a.4.M.b', 
                                            'K': 'v^2 - v + 1', 
                                            'base_field_label': '2.0.3.1',
                                            'v': '0.50000000000000000? - 0.866025403784439?*I', 
                                            'u_str': '1/823543', 
                                            'u': '1.21426567890201e-6', 
                                            'coefficients': ['1', '0', '\\left(2503186219008 v + 1981666013148\\right) u^{2}', '\\left(-735133029468733440 v + 8646588590512476160\\right) u^{3}', '\\left(2225957293303600346431488 v + 14714387845533851801579838\\right) u^{4}', '\\left(7400944747362878601281704820736 v + 16250143282316014446906125451264\\right) u^{5}', '\\left(968071723842207847611046230952574976 v + 18407049732437169782327362834291929560\\right) u^{6}', '\\left(5835425985084622306512699428605363677560832 v + 26286894521999987617215478314613476515414016\\right) u^{7}', '\\left(9581753775011366607702987929567782723576885149696 v + 26547577882536129269670895828224258872964694860597\\right) u^{8}']
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 2, 
                                            'type': 'Holomorphic Modular Form', 
                                            'label': '7.0.2.1.1.0.a.4.M.c', 
                                            'K': 'v^2 - v + 1', 
                                            'base_field_label': '2.0.3.1',
                                            'v': '0.50000000000000000? - 0.866025403784439?*I', 
                                            'u_str': '1/823543', 
                                            'u': '1.21426567890201e-6', 
                                            'coefficients': ['1', '\\left(-331776 v + 2292960\\right) u', '\\left(98505621504 v + 4341683520648\\right) u^{2}', '\\left(-299128505000214528 v + 5811733461516158336\\right) u^{3}', '\\left(-970239481776189364764672 v + 10671254120327089934278044\\right) u^{4}', '\\left(-146340174946689663962344759296 v + 11965362359570808323063589703872\\right) u^{5}', '\\left(-749504622237731280587095184074604544 v + 16716264479888861836543989968108784704\\right) u^{6}', '\\left(-1289560062576074108778943976406634184540160 v + 18083225427985344778388525905303434883948800\\right) u^{7}']
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 1, 
                                            'type': 'Cusp Form', 
                                            'label': '7.0.2.1.1.0.a.4.C.a', 
                                            'K': 'v^2 - v + 1', 
                                            'base_field_label': '2.0.3.1',
                                            'v': '0.50000000000000000? - 0.866025403784439?*I', 
                                            'u_str': '1/823543', 
                                            'u': '1.21426567890201e-6', 
                                            'coefficients': ['1', '\\left(-476928 v - 1645128\\right) u', '\\left(2113656643584 v - 1948779949860\\right) u^{2}', '\\left(-3014837912750635008 v + 1550943552608532928\\right) u^{3}', '\\left(88946315776357223989248 v + 5010679639823954956182846\\right) u^{4}', '\\left(4370427376003573551741406657536 v - 1768170041714004803851330005984\\right) u^{5}', '\\left(-4428002569296506142741748008803057664 v - 1347296642395809780631827529421128744\\right) u^{6}', '\\left(-546537820132501701109023760968203773526016 v - 1570959969745212582402304945591725243068928\\right) u^{7}', '\\left(3693875906243105612214715785400782642353505632256 v - 3816669900878826887461587210095433579160596014283\\right) u^{8}']
                                        },
    )
