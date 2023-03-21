from lmfdb import db

def create_noncongruence_modular_curve_db():
    db.create_table(name='noncong_modular_curve',
        search_columns={'int': ['genus', 'psl2z_index', 'n_c', 'n_e2', 'n_e3'],
                        'int[]': ['cusp_widths'],
                        'text': ['permS', 'permR', 'permT', 'label', 'monodromy_group', 'K', 'L', 'v_L', 'belyi_map', 'elliptic_curve', 'hyperelliptic_curve'],
                        'text[]': ['mf_spaces', 'friends', 'passport_reps'],
                        'double precision[]': ['passport_embeddings'],
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
                            'monodromy_group': "Finite group generated by permS and permR (represented by its /Groups/Abstract label)",
                            'K': "Base field of the curve (represented by its /NumberField label)",
                            'L': "Base field of the coefficients",
                            'v_L': "v (the generator of K) expressed in terms of w (the generator of L)",
                            'belyi_map': "Belyi map",
                            'elliptic_curve': "Elliptic curve",
                            'hyperelliptic_curve': "Hyperelliptic curve",
                            'mf_spaces': "Spaces of modular forms",
                            'friends': "Related LMFDB objects",
                            'passport_reps': "Passport representatives",
                            'passport_embeddings': "Embeddings of the passport representatives into CC",
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
                        'text': ['type', 'label', 'K', 'u_str'],
                        'double precision[]': ['u', 'v'],
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
                            'u_str': "Expression for u",
                            'u': "Embedding of u into CC",
                            'v': "Embedding of v into CC",
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
                                            'monodromy_group': '42.1', #Groups/Abstract/42.1
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'L': 'x^2 - x + 1',
                                            'v_L': 'w',
                                            'belyi_map': '((x^2 + ((331776*v + 195357360)*u)*x + (62079188631552*v + 1006988320853568)*u^2)^3*(x + (-1866240*v + 3015384)*u))/((x + (-145152*v - 3938088)*u)^6) = 1728 + ((x^3 + ((-1679616*v - 418281336)*u)*x^2 + ((706462210805760*v - 9954051182869824)*u^2)*x + (14652604381524017135616*v - 29995890348016962943488)*u^3)^2*(x + (2488320*v + 2567832)*u))/((x + (-145152*v - 3938088)*u)^6)',
                                            'elliptic_curve': '\n',
                                            'hyperelliptic_curve': '\n',
                                            'mf_spaces': ['7.0.2.1.1.0.a.0.H', '7.0.2.1.1.0.a.2.M', '7.0.2.1.1.0.a.4.M', '7.0.2.1.1.0.a.4.C'], #Ignore weight 6 space for now
                                            'friends': ['Belyi/7T4/6.1/3.3.1/2.2.2.1/a/'],
                                            'passport_reps': [['(1 6)(2)(3 4)(5 7)', '(1 7 6)(2 3 5)(4)', '(1)(2 3 4 5 6 7)'],['(1 4)(2)(3 5)(6 7)', '(1 5 4)(2 3 6)(7)', '(1)(2 3 4 5 6 7)']],
                                            'passport_embeddings': [[0.50000000000000000, -0.866025403784439], [0.50000000000000000, 0.866025403784439]], #Stored as [real, imag]
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
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'u_str': '1/823543', 
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficients': ['1',
                                                            '0',
                                                            '(993257717760*v + 2787572739924)*u^2',
                                                            '(-2706394677997731840*v + 6101511713277790208)*u^3',
                                                            '(3328586427569770370433024*v - 7827560231874195815452926)*u^4',
                                                            '(-246690191956662020521813082112*v + 2020405603279225977670392004608)*u^5',
                                                            '(-5580185143838191749378579955408699392*v - 6521254171810914172419380962135314088)*u^6',
                                                            '(9938190613813312321884804126524437853896704*v + 2804227792950531847927979844886468993376256)*u^7',
                                                            '(-9974839286177131485320952878512871361096063123456*v + 13118942247741007156137324828941098437716139050559)*u^8',
                                                            '(5920980510425217697466627933402939776440355729874878464*v - 10917596745122026578975532824809483699790840699199291392)*u^9',
                                                            '(1218720145755695504853300987617215807685133891794728763916288*v + 13450632275811261322475249223770454667548860483586272476608420)*u^10'
                                                            ], #Only store first ten coefficients in this prototype
                                        },
                                        {'weight': 2, 
                                            'cusp_width': 1, 
                                            'valuation': 0, 
                                            'type': 'Holomorphic Modular Form', 
                                            'label': '7.0.2.1.1.0.a.2.M.a', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'u_str': '1/823543', 
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficients': ['1',
                                                            '(145152*v + 3938088)*u',
                                                            '(-822203633664*v + 9912322512792)*u^2',
                                                            '(1740391304435997696*v + 10016874289782722208)*u^3',
                                                            '(-1325606902843077137203200*v + 17635843296056689476437784)*u^4',
                                                            '(-986001155724652126040951649792*v + 6401608332802913767486107095280)*u^5',
                                                            '(3100912902964312868516294149024038912*v + 15034798163388828143618848172147096160)*u^6',
                                                            '(-3000252984943415930673101079191947901454336*v + 5534613957846131694381945490032706213160256)*u^7',
                                                            '(1460231491232560275216649073046645665767074299904*v + 14652001319000211071684741091818741347211205766680)*u^8',
                                                            '(-484770259404880042604010703500371111731797717407986944*v + 15266107319081243920447029870864664929373988555847624456)*u^9'
                                                            ], #Only store first ten coefficients in this prototype
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 0, 
                                            'type': 'Holomorphic Modular Form', 
                                            'label': '7.0.2.1.1.0.a.4.M.a', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'u_str': '1/823543', 
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficients': ['1',
                                                            '0',
                                                            '0',
                                                            '(-8716378656613662720*v + 2652390428981153280)*u^3',
                                                            '(992302248882822449725440*v - 10437549176678568024906000)*u^4',
                                                            '(-1749327037768875082050616688640*v + 33206057846322729558248824657920)*u^5',
                                                            '(-41435283722508178767277557313217495040*v + 23330145789402750828129049038866350080)*u^6',
                                                            '(23043085568220864103491425019456707550904320*v + 44652063385170277783769293247554331678346240)*u^7',
                                                            '(-55378144789708242907540890448943706826529864417280*v + 22598337630260777931973449920729775415432359031920)*u^8',
                                                            '(-4680421142626202462952371988120706422769660709052088320*v - 80360212876331599751409011412633757924939315215196876800)*u^9'
                                                            ], #Only store first ten coefficients in this prototype
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 1, 
                                            'type': 'Holomorphic Modular Form', 
                                            'label': '7.0.2.1.1.0.a.4.M.b', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'u_str': '1/823543', 
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficients': ['1',
                                                            '0',
                                                            '(2503186219008*v + 1981666013148)*u^2',
                                                            '(-735133029468733440*v + 8646588590512476160)*u^3',
                                                            '(2225957293303600346431488*v + 14714387845533851801579838)*u^4',
                                                            '(7400944747362878601281704820736*v + 16250143282316014446906125451264)*u^5',
                                                            '(968071723842207847611046230952574976*v + 18407049732437169782327362834291929560)*u^6',
                                                            '(5835425985084622306512699428605363677560832*v + 26286894521999987617215478314613476515414016)*u^7',
                                                            '(9581753775011366607702987929567782723576885149696*v + 26547577882536129269670895828224258872964694860597)*u^8'
                                                            ], #Only store first ten coefficients in this prototype
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 2, 
                                            'type': 'Holomorphic Modular Form', 
                                            'label': '7.0.2.1.1.0.a.4.M.c', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1 
                                            'u_str': '1/823543', 
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficients': ['1',
                                                            '(-331776*v + 2292960)*u',
                                                            '(98505621504*v + 4341683520648)*u^2',
                                                            '(-299128505000214528*v + 5811733461516158336)*u^3',
                                                            '(-970239481776189364764672*v + 10671254120327089934278044)*u^4',
                                                            '(-146340174946689663962344759296*v + 11965362359570808323063589703872)*u^5',
                                                            '(-749504622237731280587095184074604544*v + 16716264479888861836543989968108784704)*u^6',
                                                            '(-1289560062576074108778943976406634184540160*v + 18083225427985344778388525905303434883948800)*u^7'
                                                            ], #Only store first ten coefficients in this prototype
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 1, 
                                            'type': 'Cusp Form', 
                                            'label': '7.0.2.1.1.0.a.4.C.a', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1 
                                            'u_str': '1/823543', 
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficients': ['1',
                                                            '(-476928*v - 1645128)*u',
                                                            '(2113656643584*v - 1948779949860)*u^2',
                                                            '(-3014837912750635008*v + 1550943552608532928)*u^3',
                                                            '(88946315776357223989248*v + 5010679639823954956182846)*u^4',
                                                            '(4370427376003573551741406657536*v - 1768170041714004803851330005984)*u^5',
                                                            '(-4428002569296506142741748008803057664*v - 1347296642395809780631827529421128744)*u^6',
                                                            '(-546537820132501701109023760968203773526016*v - 1570959969745212582402304945591725243068928)*u^7',
                                                            '(3693875906243105612214715785400782642353505632256*v - 3816669900878826887461587210095433579160596014283)*u^8'
                                                            ], #Only store first ten coefficients in this prototype
                                        },
    )
