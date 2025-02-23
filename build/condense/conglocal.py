def condense_local_interactables(original_list):
    condensed_dict = {}

    for item in original_list:
        for key, value_list in item.items():
            # Extract the identifier (e.g., "T14" from "local_interactables_T14")
            identifier = key.split('_')[-1]

            if value_list:  # Check if the list is not empty
                condensed_dict.setdefault(identifier, [])

                for interactable in value_list:
                    # Convert 'bounding_box' list to tuple
                    if 'bounding_box' in interactable:
                        interactable['bounding_box'] = tuple(interactable['bounding_box'])

                    condensed_dict[identifier].append(interactable)

    return condensed_dict

# Your original list of dictionaries
original_local_interactables = [
    {
        "local_interactables_T14": [
            {
                "bounding_box": [
                    5,
                    128,
                    483,
                    214
                ],
                "eid": "EID123",
                "associated_tid": "T15",
                "name": "file1"
            },
            {
                "bounding_box": [
                    6,
                    226,
                    476,
                    297
                ],
                "eid": "EID124",
                "associated_tid": "T15",
                "name": "file2"
            },
            {
                "bounding_box": [
                    6,
                    314,
                    478,
                    394
                ],
                "eid": "EID125",
                "associated_tid": "T15",
                "name": "file3"
            },
            {
                "bounding_box": [
                    3,
                    411,
                    476,
                    502
                ],
                "eid": "EID126",
                "associated_tid": "T15",
                "name": "file4"
            },
            {
                "bounding_box": [
                    8,
                    522,
                    478,
                    596
                ],
                "eid": "EID127",
                "associated_tid": "T15",
                "name": "fle5"
            },
            {
                "bounding_box": [
                    94,
                    20,
                    212,
                    33
                ],
                "eid": "EID128",
                "associated_tid": "T13",
                "name": "files"
            },
            {
                "bounding_box": [
                    1131,
                    659,
                    1198,
                    691
                ],
                "eid": "EID129",
                "associated_tid": "T14",
                "name": "next"
            },
            {
                "bounding_box": [
                    13,
                    656,
                    79,
                    676
                ],
                "eid": "EID130",
                "associated_tid": "T13",
                "name": "back"
            }
        ]
    },
    {
        "local_interactables_T50": [
            {
                "bounding_box": [
                    390,
                    692,
                    462,
                    708
                ],
                "eid": "EID274",
                "associated_tid": "T49",
                "name": "cancel"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T12": [
            {
                "bounding_box": [
                    583,
                    314,
                    835,
                    363
                ],
                "eid": "EID90",
                "associated_tid": "T22",
                "name": "gen"
            },
            {
                "bounding_box": [
                    236,
                    411,
                    481,
                    452
                ],
                "eid": "EID91",
                "associated_tid": "T21",
                "name": "rss"
            },
            {
                "bounding_box": [
                    226,
                    252,
                    487,
                    306
                ],
                "eid": "EID92",
                "associated_tid": "T15",
                "name": "repo"
            },
            {
                "bounding_box": [
                    228,
                    536,
                    1218,
                    747
                ],
                "eid": "EID93",
                "associated_tid": "T8",
                "name": "unclick"
            },
            {
                "bounding_box": [
                    202,
                    8,
                    1101,
                    168
                ],
                "eid": "EID94",
                "associated_tid": "T8",
                "name": "unclick2"
            }
        ]
    },
    {
        "local_interactables_T37": [
            {
                "bounding_box": [
                    954,
                    138,
                    1059,
                    167
                ],
                "eid": "EID251",
                "associated_tid": "T37",
                "name": "add"
            },
            {
                "bounding_box": [
                    953,
                    139,
                    1061,
                    169
                ],
                "eid": "EID252",
                "associated_tid": "T38",
                "name": "add"
            },
            {
                "bounding_box": [
                    253,
                    210,
                    471,
                    251
                ],
                "eid": "EID253",
                "associated_tid": "T38",
                "name": "patient1"
            },
            {
                "bounding_box": [
                    513,
                    209,
                    736,
                    253
                ],
                "eid": "EID254",
                "associated_tid": "T38",
                "name": "patient2"
            },
            {
                "bounding_box": [
                    777,
                    210,
                    999,
                    245
                ],
                "eid": "EID255",
                "associated_tid": "T38",
                "name": "patient3"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T7": [
            {
                "bounding_box": [
                    3,
                    212,
                    616,
                    366
                ],
                "eid": "EID43",
                "associated_tid": "T8",
                "name": "routing"
            }
        ]
    },
    {
        "local_interactables_T56": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T19": [
            {
                "bounding_box": [
                    12,
                    105,
                    253,
                    177
                ],
                "eid": "EID170",
                "associated_tid": "T19",
                "name": "chat1"
            },
            {
                "bounding_box": [
                    16,
                    213,
                    249,
                    290
                ],
                "eid": "EID171",
                "associated_tid": "T19",
                "name": "chat2"
            },
            {
                "bounding_box": [
                    15,
                    327,
                    254,
                    409
                ],
                "eid": "EID172",
                "associated_tid": "T19",
                "name": "chat3"
            },
            {
                "bounding_box": [
                    15,
                    445,
                    251,
                    513
                ],
                "eid": "EID173",
                "associated_tid": "T19",
                "name": "chat4"
            },
            {
                "bounding_box": [
                    100,
                    23,
                    184,
                    33
                ],
                "eid": "EID174",
                "associated_tid": "T18",
                "name": "contacts"
            },
            {
                "bounding_box": [
                    334,
                    22,
                    441,
                    34
                ],
                "eid": "EID175",
                "associated_tid": "T21",
                "name": "operations"
            },
            {
                "bounding_box": [
                    484,
                    20,
                    515,
                    33
                ],
                "eid": "EID176",
                "associated_tid": "T21",
                "name": "rss"
            },
            {
                "bounding_box": [
                    1060,
                    651,
                    1111,
                    696
                ],
                "eid": "EID177",
                "associated_tid": "T19",
                "name": "send"
            }
        ]
    },
    {
        "local_interactables_T46": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T31": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T48": [
            {
                "bounding_box": [
                    252,
                    143,
                    376,
                    212
                ],
                "eid": "EID263",
                "associated_tid": "T49",
                "name": "masters"
            },
            {
                "bounding_box": [
                    414,
                    142,
                    535,
                    210
                ],
                "eid": "EID264",
                "associated_tid": "T54",
                "name": "billing"
            },
            {
                "bounding_box": [
                    584,
                    143,
                    706,
                    211
                ],
                "eid": "EID265",
                "associated_tid": "T55",
                "name": "inward"
            },
            {
                "bounding_box": [
                    748,
                    146,
                    875,
                    208
                ],
                "eid": "EID266",
                "associated_tid": "T56",
                "name": "purchase"
            },
            {
                "bounding_box": [
                    914,
                    148,
                    1039,
                    211
                ],
                "eid": "EID267",
                "associated_tid": "T57",
                "name": "sales"
            },
            {
                "bounding_box": [
                    1083,
                    142,
                    1206,
                    208
                ],
                "eid": "EID268",
                "associated_tid": "T58",
                "name": "roi"
            },
            {
                "bounding_box": [
                    248,
                    257,
                    376,
                    319
                ],
                "eid": "EID269",
                "associated_tid": "T59",
                "name": "reports"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T54": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T34": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T36": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T32": [
            {
                "bounding_box": [
                    237,
                    123,
                    357,
                    148
                ],
                "eid": "EID243",
                "associated_tid": "T33",
                "name": "create"
            },
            {
                "bounding_box": [
                    396,
                    122,
                    510,
                    150
                ],
                "eid": "EID244",
                "associated_tid": "T35",
                "name": "invite"
            },
            {
                "bounding_box": [
                    261,
                    179,
                    402,
                    197
                ],
                "eid": "EID245",
                "associated_tid": "T34",
                "name": "invitedpatients"
            },
            {
                "bounding_box": [
                    827,
                    261,
                    891,
                    271
                ],
                "eid": "EID246",
                "associated_tid": "T36",
                "name": "edit"
            },
            {
                "bounding_box": [
                    830,
                    350,
                    893,
                    364
                ],
                "eid": "EID247",
                "associated_tid": "T36",
                "name": "edit"
            },
            {
                "bounding_box": [
                    827,
                    443,
                    893,
                    454
                ],
                "eid": "EID248",
                "associated_tid": "T36",
                "name": "edit"
            },
            {
                "bounding_box": [
                    828,
                    541,
                    890,
                    553
                ],
                "eid": "EID249",
                "associated_tid": "T36",
                "name": "edit4"
            },
            {
                "bounding_box": [
                    828,
                    638,
                    887,
                    650
                ],
                "eid": "EID250",
                "associated_tid": "T36",
                "name": "edit5"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T42": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T26": [
            {
                "bounding_box": [
                    660,
                    526,
                    997,
                    570
                ],
                "eid": "EID207",
                "associated_tid": "T28",
                "name": "send"
            }
        ]
    },
    {
        "local_interactables_T59": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T29": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            },
            {
                "bounding_box": [
                    910,
                    25,
                    937,
                    52
                ],
                "eid": "EID241",
                "associated_tid": "T30",
                "name": "notif"
            },
            {
                "bounding_box": [
                    1273,
                    34,
                    1282,
                    53
                ],
                "eid": "EID242",
                "associated_tid": "T31",
                "name": "menu"
            }
        ]
    },
    {
        "local_interactables_T35": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T10": [
            {
                "bounding_box": [
                    340,
                    143,
                    540,
                    551
                ],
                "eid": "EID66",
                "associated_tid": "T9",
                "name": "unclick"
            },
            {
                "bounding_box": [
                    565,
                    583,
                    979,
                    722
                ],
                "eid": "EID67",
                "associated_tid": "T9",
                "name": "unclick1"
            },
            {
                "bounding_box": [
                    1017,
                    215,
                    1239,
                    251
                ],
                "eid": "EID69",
                "associated_tid": "T8",
                "name": "not2"
            },
            {
                "bounding_box": [
                    1020,
                    281,
                    1242,
                    319
                ],
                "eid": "EID70",
                "associated_tid": "T8",
                "name": "not3"
            }
        ]
    },
    {
        "local_interactables_T28": [
            {
                "bounding_box": [
                    616,
                    514,
                    928,
                    552
                ],
                "eid": "EID211",
                "associated_tid": "T29",
                "name": "verify"
            }
        ]
    },
    {
        "local_interactables_T11": [
            {
                "bounding_box": [
                    459,
                    178,
                    603,
                    318
                ],
                "eid": "EID83",
                "associated_tid": "T24",
                "name": "emr"
            },
            {
                "bounding_box": [
                    663,
                    177,
                    811,
                    321
                ],
                "eid": "EID84",
                "associated_tid": "T16",
                "name": "messenger"
            },
            {
                "bounding_box": [
                    460,
                    382,
                    609,
                    517
                ],
                "eid": "EID85",
                "associated_tid": "T13",
                "name": "files"
            },
            {
                "bounding_box": [
                    680,
                    397,
                    789,
                    503
                ],
                "eid": "EID86",
                "associated_tid": "T12",
                "name": "others"
            },
            {
                "bounding_box": [
                    828,
                    183,
                    1276,
                    738
                ],
                "eid": "EID88",
                "associated_tid": "T8",
                "name": "unclick2"
            },
            {
                "bounding_box": [
                    319,
                    566,
                    864,
                    704
                ],
                "eid": "EID89",
                "associated_tid": "T8",
                "name": "unclick3"
            }
        ]
    },
    {
        "local_interactables_T6": [
            {
                "bounding_box": [
                    4,
                    211,
                    613,
                    364
                ],
                "eid": "EID42",
                "associated_tid": "T7",
                "name": "booting"
            }
        ]
    },
    {
        "local_interactables_T27": [
            {
                "bounding_box": [
                    594,
                    643,
                    901,
                    673
                ],
                "eid": "EID209",
                "associated_tid": "T29",
                "name": "verify"
            }
        ]
    },
    {
        "local_interactables_T64": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T5": [
            {
                "bounding_box": [
                    4,
                    213,
                    612,
                    363
                ],
                "eid": "EID41",
                "associated_tid": "T6",
                "name": "secure"
            }
        ]
    },
    {
        "local_interactables_T20": []
    },
    {
        "local_interactables_T33": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T58": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T53": [
            {
                "bounding_box": [
                    383,
                    688,
                    458,
                    708
                ],
                "eid": "EID277",
                "associated_tid": "T49",
                "name": "cance;"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T16": [
            {
                "bounding_box": [
                    98,
                    21,
                    185,
                    35
                ],
                "eid": "EID136",
                "associated_tid": "T18",
                "name": "contacts"
            },
            {
                "bounding_box": [
                    337,
                    21,
                    440,
                    32
                ],
                "eid": "EID138",
                "associated_tid": "T20",
                "name": "operations"
            },
            {
                "bounding_box": [
                    27,
                    103,
                    249,
                    176
                ],
                "eid": "EID201",
                "associated_tid": "T17",
                "name": "contact1"
            },
            {
                "bounding_box": [
                    29,
                    219,
                    239,
                    284
                ],
                "eid": "EID202",
                "associated_tid": "T17",
                "name": "contact2"
            },
            {
                "bounding_box": [
                    21,
                    330,
                    247,
                    396
                ],
                "eid": "EID203",
                "associated_tid": "T17",
                "name": "contact3"
            },
            {
                "bounding_box": [
                    25,
                    438,
                    238,
                    514
                ],
                "eid": "EID204",
                "associated_tid": "T17",
                "name": "contact4"
            }
        ]
    },
    {
        "local_interactables_T63": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T21": []
    },
    {
        "local_interactables_T51": [
            {
                "bounding_box": [
                    389,
                    504,
                    448,
                    521
                ],
                "eid": "EID275",
                "associated_tid": "T49",
                "name": "clear"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T8": []
    },
    {
        "local_interactables_T18": [
            {
                "bounding_box": [
                    94,
                    18,
                    186,
                    36
                ],
                "eid": "EID150",
                "associated_tid": "T18",
                "name": "contacts"
            },
            {
                "bounding_box": [
                    233,
                    23,
                    303,
                    31
                ],
                "eid": "EID151",
                "associated_tid": "T19",
                "name": "groups"
            },
            {
                "bounding_box": [
                    336,
                    22,
                    444,
                    32
                ],
                "eid": "EID152",
                "associated_tid": "T20",
                "name": "operations"
            },
            {
                "bounding_box": [
                    487,
                    17,
                    523,
                    34
                ],
                "eid": "EID153",
                "associated_tid": "T21",
                "name": "rss"
            },
            {
                "bounding_box": [
                    120,
                    317,
                    447,
                    407
                ],
                "eid": "EID157",
                "associated_tid": "T18",
                "name": "contact4"
            }
        ]
    },
    {
        "local_interactables_T15": []
    },
    {
        "local_interactables_T22": [
            {
                "bounding_box": [
                    119,
                    21,
                    168,
                    34
                ],
                "eid": "EID186",
                "associated_tid": "T22",
                "name": "chat"
            },
            {
                "bounding_box": [
                    217,
                    19,
                    286,
                    32
                ],
                "eid": "EID187",
                "associated_tid": "T23",
                "name": "history"
            },
            {
                "bounding_box": [
                    1060,
                    652,
                    1112,
                    695
                ],
                "eid": "EID190",
                "associated_tid": "T22",
                "name": "send"
            }
        ]
    },
    {
        "local_interactables_T4": [
            {
                "bounding_box": [
                    565,
                    611,
                    734,
                    642
                ],
                "eid": "EID40",
                "associated_tid": "T5",
                "name": "proceed"
            }
        ]
    },
    {
        "local_interactables_T39": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T30": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T1": [
            {
                "bounding_box": [
                    514,
                    546,
                    737,
                    597
                ],
                "eid": "EID37",
                "associated_tid": "T2",
                "name": "luberaplus"
            },
            {
                "bounding_box": [
                    519,
                    542,
                    736,
                    600
                ],
                "eid": "EID212",
                "associated_tid": "T2",
                "name": "luberaplus"
            }
        ]
    },
    {
        "local_interactables_T2": [
            {
                "bounding_box": [
                    508,
                    434,
                    733,
                    492
                ],
                "eid": "EID38",
                "associated_tid": "T3",
                "name": "login"
            }
        ]
    },
    {
        "local_interactables_T60": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T49": [
            {
                "bounding_box": [
                    251,
                    145,
                    375,
                    209
                ],
                "eid": "EID270",
                "associated_tid": "T50",
                "name": "company"
            },
            {
                "bounding_box": [
                    416,
                    149,
                    535,
                    212
                ],
                "eid": "EID271",
                "associated_tid": "T51",
                "name": "product"
            },
            {
                "bounding_box": [
                    585,
                    148,
                    708,
                    205
                ],
                "eid": "EID272",
                "associated_tid": "T52",
                "name": "unit"
            },
            {
                "bounding_box": [
                    748,
                    150,
                    872,
                    205
                ],
                "eid": "EID273",
                "associated_tid": "T53",
                "name": "product"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T62": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T13": [
            {
                "bounding_box": [
                    675,
                    140,
                    910,
                    185
                ],
                "eid": "EID95",
                "associated_tid": "T14",
                "name": "records"
            },
            {
                "bounding_box": [
                    674,
                    220,
                    905,
                    264
                ],
                "eid": "EID96",
                "associated_tid": "T14",
                "name": "staff"
            },
            {
                "bounding_box": [
                    674,
                    300,
                    907,
                    341
                ],
                "eid": "EID97",
                "associated_tid": "T14",
                "name": "admin"
            },
            {
                "bounding_box": [
                    672,
                    381,
                    906,
                    423
                ],
                "eid": "EID98",
                "associated_tid": "T14",
                "name": "medical"
            },
            {
                "bounding_box": [
                    674,
                    461,
                    910,
                    501
                ],
                "eid": "EID99",
                "associated_tid": "T14",
                "name": "dept"
            },
            {
                "bounding_box": [
                    677,
                    536,
                    906,
                    576
                ],
                "eid": "EID100",
                "associated_tid": "T14",
                "name": "system"
            },
            {
                "bounding_box": [
                    92,
                    18,
                    214,
                    31
                ],
                "eid": "EID101",
                "associated_tid": "T13",
                "name": "files"
            }
        ]
    },
    {
        "local_interactables_T9": [
            {
                "bounding_box": [
                    379,
                    137,
                    964,
                    679
                ],
                "eid": "EID50",
                "associated_tid": "T8",
                "name": "unclick"
            },
            {
                "bounding_box": [
                    1017,
                    147,
                    1241,
                    184
                ],
                "eid": "EID51",
                "associated_tid": "T10",
                "name": "not1"
            },
            {
                "bounding_box": [
                    1021,
                    220,
                    1241,
                    249
                ],
                "eid": "EID52",
                "associated_tid": "T10",
                "name": "not2"
            },
            {
                "bounding_box": [
                    1019,
                    281,
                    1237,
                    321
                ],
                "eid": "EID53",
                "associated_tid": "T10",
                "name": "not3"
            },
            {
                "bounding_box": [
                    1026,
                    351,
                    1238,
                    394
                ],
                "eid": "EID54",
                "associated_tid": "T10",
                "name": "not4"
            }
        ]
    },
    {
        "local_interactables_T61": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T55": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T41": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T45": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T47": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T3": [
            {
                "bounding_box": [
                    537,
                    595,
                    704,
                    626
                ],
                "eid": "EID39",
                "associated_tid": "T4",
                "name": "login"
            }
        ]
    },
    {
        "local_interactables_T17": [
            {
                "bounding_box": [
                    350,
                    159,
                    1243,
                    531
                ],
                "eid": "EID144",
                "associated_tid": "T17",
                "name": "body"
            },
            {
                "bounding_box": [
                    100,
                    20,
                    182,
                    30
                ],
                "eid": "EID147",
                "associated_tid": "T18",
                "name": "contacts"
            },
            {
                "bounding_box": [
                    235,
                    23,
                    300,
                    32
                ],
                "eid": "EID148",
                "associated_tid": "T19",
                "name": "groups"
            },
            {
                "bounding_box": [
                    336,
                    20,
                    445,
                    34
                ],
                "eid": "EID149",
                "associated_tid": "T20",
                "name": "operations"
            },
            {
                "bounding_box": [
                    27,
                    103,
                    249,
                    176
                ],
                "eid": "EID178",
                "associated_tid": "T17",
                "name": "contact1"
            },
            {
                "bounding_box": [
                    29,
                    219,
                    239,
                    284
                ],
                "eid": "EID179",
                "associated_tid": "T17",
                "name": "contact2"
            },
            {
                "bounding_box": [
                    21,
                    330,
                    247,
                    396
                ],
                "eid": "EID180",
                "associated_tid": "T17",
                "name": "contact3"
            },
            {
                "bounding_box": [
                    25,
                    438,
                    238,
                    514
                ],
                "eid": "EID181",
                "associated_tid": "T17",
                "name": "contact4"
            },
            {
                "bounding_box": [
                    1055,
                    652,
                    1106,
                    707
                ],
                "eid": "EID182",
                "associated_tid": "T17",
                "name": "send"
            }
        ]
    },
    {
        "local_interactables_T38": [
            {
                "bounding_box": [
                    201,
                    83,
                    843,
                    724
                ],
                "eid": "EID256",
                "associated_tid": "T37",
                "name": "unclick"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T25": [
            {
                "bounding_box": [
                    672,
                    543,
                    1001,
                    590
                ],
                "eid": "EID201",
                "associated_tid": "T29",
                "name": "login"
            },
            {
                "bounding_box": [
                    851,
                    503,
                    1015,
                    515
                ],
                "eid": "EID204",
                "associated_tid": "T26",
                "name": "forgot"
            },
            {
                "bounding_box": [
                    926,
                    621,
                    991,
                    633
                ],
                "eid": "EID205",
                "associated_tid": "T27",
                "name": "create"
            }
        ]
    },
    {
        "local_interactables_T40": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T52": [
            {
                "bounding_box": [
                    389,
                    504,
                    464,
                    521
                ],
                "eid": "EID276",
                "associated_tid": "T49",
                "name": "clear"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T43": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T23": [
            {
                "bounding_box": [
                    121,
                    23,
                    166,
                    32
                ],
                "eid": "EID191",
                "associated_tid": "T22",
                "name": "chat"
            },
            {
                "bounding_box": [
                    221,
                    21,
                    288,
                    30
                ],
                "eid": "EID192",
                "associated_tid": "T23",
                "name": "history"
            },
            {
                "bounding_box": [
                    4,
                    229,
                    289,
                    312
                ],
                "eid": "EID198",
                "associated_tid": "T22",
                "name": "conv1"
            },
            {
                "bounding_box": [
                    5,
                    329,
                    287,
                    398
                ],
                "eid": "EID199",
                "associated_tid": "T22",
                "name": "conv2"
            }
        ]
    },
    {
        "local_interactables_T57": [
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    },
    {
        "local_interactables_T24": [
            {
                "bounding_box": [
                    768,
                    437,
                    971,
                    479
                ],
                "eid": "EID200",
                "associated_tid": "T25",
                "name": "login"
            }
        ]
    },
    {
        "local_interactables_T44": [
            {
                "bounding_box": [
                    419,
                    154,
                    534,
                    211
                ],
                "eid": "EID261",
                "associated_tid": "T45",
                "name": "w"
            },
            {
                "bounding_box": [
                    583,
                    151,
                    710,
                    213
                ],
                "eid": "EID262",
                "associated_tid": "T46",
                "name": "digitalhpy"
            },
            {
                "bounding_box": [
                    2,
                    76,
                    199,
                    101
                ],
                "eid": "EID230",
                "associated_tid": "T29",
                "name": "dashboard"
            },
            {
                "bounding_box": [
                    4,
                    107,
                    197,
                    133
                ],
                "eid": "EID231",
                "associated_tid": "T32",
                "name": "calender"
            },
            {
                "bounding_box": [
                    3,
                    141,
                    197,
                    167
                ],
                "eid": "EID232",
                "associated_tid": "T37",
                "name": "patients"
            },
            {
                "bounding_box": [
                    5,
                    174,
                    196,
                    196
                ],
                "eid": "EID233",
                "associated_tid": "T42",
                "name": "reports"
            },
            {
                "bounding_box": [
                    4,
                    204,
                    194,
                    230
                ],
                "eid": "EID234",
                "associated_tid": "T43",
                "name": "profile"
            },
            {
                "bounding_box": [
                    7,
                    236,
                    195,
                    260
                ],
                "eid": "EID235",
                "associated_tid": "T45",
                "name": "workspace"
            },
            {
                "bounding_box": [
                    4,
                    302,
                    197,
                    329
                ],
                "eid": "EID236",
                "associated_tid": "T48",
                "name": "inventory"
            },
            {
                "bounding_box": [
                    3,
                    334,
                    198,
                    364
                ],
                "eid": "EID237",
                "associated_tid": "T60",
                "name": "lab"
            },
            {
                "bounding_box": [
                    6,
                    368,
                    194,
                    393
                ],
                "eid": "EID238",
                "associated_tid": "T63",
                "name": "feedbacks"
            },
            {
                "bounding_box": [
                    2,
                    400,
                    199,
                    428
                ],
                "eid": "EID239",
                "associated_tid": "T64",
                "name": "diag"
            }
        ]
    }
]

# Perform the conversion
condensed_local_interactables = condense_local_interactables(original_local_interactables)

# Print or use the condensed dictionary as needed
print(condensed_local_interactables)
