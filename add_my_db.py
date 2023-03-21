from lmfdb import db

def create_noncongruence_modular_curve_db():
    db.create_table(name='noncong_modular_curve',
        search_columns={'int': ['genus', 'psl2z_index', 'n_c', 'n_e2', 'n_e3'],
                        'int[]': ['cusp_widths'],
                        'text': ['permS', 'permR', 'permT', 'label', 'monodromy_group', 'K', 'v_L', 'belyi_map', 'elliptic_curve', 'hyperelliptic_curve'],
                        'text[]': ['friends', 'passport_reps'],
                        'numeric[]': ['L'],
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
                            'friends': "Related LMFDB objects",
                            'passport_reps': "Passport representatives",
                            'passport_embeddings': "Embeddings of the passport representatives into CC",
                            'is_congruence': "True if the subgroup is a congruence subgroup",
                        },
    )

def create_noncongruence_modular_form_space():
    db.create_table(name='noncong_modular_form_space',
        search_columns={'int': ['dim', 'weight'],
                        'text': ['label', 'mf_curve'],
                        },
        label_col='label',
        sort=['label'],
        table_description='Noncongruence modular form spaces',
        #Add proper descriptions later
        col_description={'dim': "Dimension of the space",
                            'weight': "Weight of the forms in the space",
                            'label': "Label of the space",
                            'mf_curve': "Parent modular curve",
                        },
    )

def create_noncongruence_modular_form():
    db.create_table(name='noncong_modular_form',
        search_columns={'int': ['weight', 'cusp_width', 'valuation'],
                        'text': ['label', 'K', 'u_str', 'mf_space'],
                        'double precision[]': ['u', 'v'],
                        'numeric[]': ['coefficient_numerators', 'coefficient_denominators'],
                        },
        label_col='label',
        sort=['label'],
        table_description='Noncongruence modular form',
        #Add proper descriptions later
        col_description={'weight': "Weight of the form",
                            'cusp_width': "Width of the cusp associated to the form",
                            'valuation': "Valuation of the form",
                            'label': "Label of the form",
                            'K': "Field of definition",
                            'u_str': "Expression for u",
                            'mf_space': "Parent modular form space",
                            'u': "Embedding of u into CC",
                            'v': "Embedding of v into CC",
                            'coefficient_numerators': "Numerators of the coefficients of the form",
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
                                            'L': [1,-1,1],
                                            'v_L': 'w',
                                            'belyi_map': '((x^2 + ((331776*v + 195357360)*u)*x + (62079188631552*v + 1006988320853568)*u^2)^3*(x + (-1866240*v + 3015384)*u))/((x + (-145152*v - 3938088)*u)^6) = 1728 + ((x^3 + ((-1679616*v - 418281336)*u)*x^2 + ((706462210805760*v - 9954051182869824)*u^2)*x + (14652604381524017135616*v - 29995890348016962943488)*u^3)^2*(x + (2488320*v + 2567832)*u))/((x + (-145152*v - 3938088)*u)^6)',
                                            'elliptic_curve': None,
                                            'hyperelliptic_curve': None,
                                            'friends': ['Belyi/7T4/6.1/3.3.1/2.2.2.1/a/'],
                                            'passport_reps': [['(1 6)(2)(3 4)(5 7)', '(1 7 6)(2 3 5)(4)', '(1)(2 3 4 5 6 7)'],['(1 4)(2)(3 5)(6 7)', '(1 5 4)(2 3 6)(7)', '(1)(2 3 4 5 6 7)']],
                                            'passport_embeddings': [[0.50000000000000000, -0.866025403784439], [0.50000000000000000, 0.866025403784439]], #Stored as [real, imag]
                                            'is_congruence': False,
                                            }
    )

    #Insert noncongruence modular form spaces
    db.noncong_modular_form_space.insert_many({'dim': 1,
                                                'weight': 0, 
                                                'label': '7.0.2.1.1.0.a.0.H', 
                                                'mf_curve': '7.0.2.1.1.0.a',
                                                },
                                                {'dim': 1, 
                                                'weight': 2, 
                                                'label': '7.0.2.1.1.0.a.2.M', 
                                                'mf_curve': '7.0.2.1.1.0.a',
                                                },
                                                {'dim': 3, 
                                                'weight': 4,  
                                                'label': '7.0.2.1.1.0.a.4.M', 
                                                'mf_curve': '7.0.2.1.1.0.a',
                                                },
                                                {'dim': 1, 
                                                'weight': 4, 
                                                'label': '7.0.2.1.1.0.a.4.C', 
                                                'mf_curve': '7.0.2.1.1.0.a',
                                                },
    )

    #Insert noncongruence modular forms
    db.noncong_modular_form.insert_many({'weight': 0, 
                                            'cusp_width': 1, 
                                            'valuation': -1, 
                                            'label': '7.0.2.1.1.0.a.0.H.a', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'u_str': '1/823543', 
                                            'mf_space': '7.0.2.1.1.0.a.0.H',
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficient_numerators': [[1, 0],
                                                                    [0, 0],
                                                                    [2787572739924, 993257717760],
                                                                    [6101511713277790208, -2706394677997731840],
                                                                    [-7827560231874195815452926, 3328586427569770370433024],
                                                                    [2020405603279225977670392004608, -246690191956662020521813082112],
                                                                    [-6521254171810914172419380962135314088,
                                                                    -5580185143838191749378579955408699392],
                                                                    [2804227792950531847927979844886468993376256,
                                                                    9938190613813312321884804126524437853896704],
                                                                    [13118942247741007156137324828941098437716139050559,
                                                                    -9974839286177131485320952878512871361096063123456],
                                                                    [-10917596745122026578975532824809483699790840699199291392,
                                                                    5920980510425217697466627933402939776440355729874878464],
                                                                    [13450632275811261322475249223770454667548860483586272476608420,
                                                                    1218720145755695504853300987617215807685133891794728763916288]
                                                                    ], #Only store first ten coefficients in this prototype
                                            'coefficient_denominators': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                        },
                                        {'weight': 2, 
                                            'cusp_width': 1, 
                                            'valuation': 0, 
                                            'label': '7.0.2.1.1.0.a.2.M.a', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'u_str': '1/823543', 
                                            'mf_space': '7.0.2.1.1.0.a.2.M',
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficient_numerators': [[1, 0],
                                                                    [3938088, 145152],
                                                                    [9912322512792, -822203633664],
                                                                    [10016874289782722208, 1740391304435997696],
                                                                    [17635843296056689476437784, -1325606902843077137203200],
                                                                    [6401608332802913767486107095280, -986001155724652126040951649792],
                                                                    [15034798163388828143618848172147096160,
                                                                    3100912902964312868516294149024038912],
                                                                    [5534613957846131694381945490032706213160256,
                                                                    -3000252984943415930673101079191947901454336],
                                                                    [14652001319000211071684741091818741347211205766680,
                                                                    1460231491232560275216649073046645665767074299904],
                                                                    [15266107319081243920447029870864664929373988555847624456,
                                                                    -484770259404880042604010703500371111731797717407986944]
                                                                    ], #Only store first ten coefficients in this prototype
                                            'coefficient_denominators': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 0,  
                                            'label': '7.0.2.1.1.0.a.4.M.a', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'u_str': '1/823543', 
                                            'mf_space': '7.0.2.1.1.0.a.4.M',
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficient_numerators': [[1, 0],
                                                                    [0, 0],
                                                                    [0, 0],
                                                                    [2652390428981153280, -8716378656613662720],
                                                                    [-10437549176678568024906000, 992302248882822449725440],
                                                                    [33206057846322729558248824657920, -1749327037768875082050616688640],
                                                                    [23330145789402750828129049038866350080,
                                                                    -41435283722508178767277557313217495040],
                                                                    [44652063385170277783769293247554331678346240,
                                                                    23043085568220864103491425019456707550904320],
                                                                    [22598337630260777931973449920729775415432359031920,
                                                                    -55378144789708242907540890448943706826529864417280],
                                                                    [-80360212876331599751409011412633757924939315215196876800,
                                                                    -4680421142626202462952371988120706422769660709052088320]
                                                                    ], #Only store first ten coefficients in this prototype
                                            'coefficient_denominators': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 1,  
                                            'label': '7.0.2.1.1.0.a.4.M.b', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1
                                            'u_str': '1/823543', 
                                            'mf_space': '7.0.2.1.1.0.a.4.M',
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficient_numerators': [[1, 0],
                                                                    [0, 0],
                                                                    [1981666013148, 2503186219008],
                                                                    [8646588590512476160, -735133029468733440],
                                                                    [14714387845533851801579838, 2225957293303600346431488],
                                                                    [16250143282316014446906125451264, 7400944747362878601281704820736],
                                                                    [18407049732437169782327362834291929560,
                                                                    968071723842207847611046230952574976],
                                                                    [26286894521999987617215478314613476515414016,
                                                                    5835425985084622306512699428605363677560832],
                                                                    [26547577882536129269670895828224258872964694860597,
                                                                    9581753775011366607702987929567782723576885149696]
                                                                    ], #Only store first ten coefficients in this prototype
                                            'coefficient_denominators': [1, 1, 1, 1, 1, 1, 1, 1, 1],
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 2, 
                                            'label': '7.0.2.1.1.0.a.4.M.c', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1 
                                            'u_str': '1/823543', 
                                            'mf_space': '7.0.2.1.1.0.a.4.M',
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficient_numerators': [[1, 0],
                                                                    [2292960, -331776],
                                                                    [4341683520648, 98505621504],
                                                                    [5811733461516158336, -299128505000214528],
                                                                    [10671254120327089934278044, -970239481776189364764672],
                                                                    [11965362359570808323063589703872, -146340174946689663962344759296],
                                                                    [16716264479888861836543989968108784704,
                                                                    -749504622237731280587095184074604544],
                                                                    [18083225427985344778388525905303434883948800,
                                                                    -1289560062576074108778943976406634184540160]
                                                                    ], #Only store first ten coefficients in this prototype
                                            'coefficient_denominators': [1, 1, 1, 1, 1, 1, 1, 1],
                                        },
                                        {'weight': 4, 
                                            'cusp_width': 1, 
                                            'valuation': 1, 
                                            'label': '7.0.2.1.1.0.a.4.C.a', 
                                            'K': '2.0.3.1', #NumberField/2.0.3.1 
                                            'u_str': '1/823543', 
                                            'mf_space': '7.0.2.1.1.0.a.4.C',
                                            'u': [1.21426567890201e-6, 0.0], #Stored as [real, imag]
                                            'v': [0.50000000000000000, -0.866025403784439], #Stored as [real, imag]
                                            'coefficient_numerators': [[1, 0],
                                                                    [-1645128, -476928],
                                                                    [-1948779949860, 2113656643584],
                                                                    [1550943552608532928, -3014837912750635008],
                                                                    [5010679639823954956182846, 88946315776357223989248],
                                                                    [-1768170041714004803851330005984, 4370427376003573551741406657536],
                                                                    [-1347296642395809780631827529421128744,
                                                                    -4428002569296506142741748008803057664],
                                                                    [-1570959969745212582402304945591725243068928,
                                                                    -546537820132501701109023760968203773526016],
                                                                    [-3816669900878826887461587210095433579160596014283,
                                                                    3693875906243105612214715785400782642353505632256]
                                                                    ], #Only store first ten coefficients in this prototype
                                            'coefficient_denominators': [1, 1, 1, 1, 1, 1, 1, 1, 1],	
                                        },
    )
