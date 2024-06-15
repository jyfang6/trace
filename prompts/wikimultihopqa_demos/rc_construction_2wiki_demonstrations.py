

generate_reasoning_chains_2wikimultihopqa_examplars = [
    [
        {
            "question": "Where was the husband of Mollena Williams-Haas born?", 
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Mollena Williams-Haas; nationality; American>",
                "C. <Mollena Williams-Haas; occupation; BDSM educator>", 
                "D. <Mollena Williams-Haas; spouse; Georg Friedrich Haas>",
                "E. <Mollena Williams-Haas; occupation; writer>", 
            ],
            "answer": "D", 
        },
        {
            "question": "Where was the husband of Mollena Williams-Haas born?", 
            "triples": [
                "<Mollena Williams-Haas; spouse; Georg Friedrich Haas>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Georg Friedrich Haas; place of birth; Graz, Austria>",
                "C. <Georg Friedrich Haas; nationality; Austrian>", 
                "D. <Georg Friedrich Haas; date of birth; 16 August 1953>",
                "E. <Georg Friedrich Haas; occupation; composer>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Where was the husband of Mollena Williams-Haas born?", 
            "triples": [
                "<Mollena Williams-Haas; spouse; Georg Friedrich Haas>",
                "<Georg Friedrich Haas; place of birth; Graz, Austria>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Georg Friedrich Haas; nationality; Austrian>",
                "C. <Georg Friedrich Haas; date of birth; 16 August 1953>", 
                "D. <Georg Friedrich Haas; occupation; composer>",
                "E. <Mollena Williams-Haas; nationality; American>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Where did the director of film The Man Who Owed A Death die?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Man Who Owed a Death; director; Mario Soffici>", 
                "C. <The Man Who Owed a Death; year of release; 1955>",
                "D. <The Man Who Owed a Death; starring actors; Amelia Bence and Carlos Cores>",
                "E. <The Man Who Knew Too Little; director; Jon Amiel>"
            ],
            "answer": "B", 
        },
        {
            "question": "Where did the director of film The Man Who Owed A Death die?", 
            "triples": [
                "<The Man Who Owed a Death; director; Mario Soffici>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Mario Soffici; notable films; Prisioneros de la tierra, El Curandero, El hombre que debía una muerte, Rosaura a las 10>", 
                "C. <Mario Soffici; place of death; Buenos Aires>",
                "D. <Mario Soffici; occupation; film director, actor, screenwriter>",
                "E. <Mario Soffici; notable film; El Alma de Bandoneón>"
            ],
            "answer": "C", 
        },
        {
            "question": "Where did the director of film The Man Who Owed A Death die?", 
            "triples": [
                "<The Man Who Owed a Death; director; Mario Soffici>",
                "<Mario Soffici; place of death; Buenos Aires>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Mario Soffici; notable films; Prisioneros de la tierra, El Curandero, El hombre que debía una muerte, Rosaura a las 10>", 
                "C. <Mario Soffici; nationality; Argentine>",
                "D. <Mario Soffici; year of moving to Argentina; 1920s>",
                "E. <Mario Soffici; occupation; film director, actor, screenwriter>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Which film has the director who was born earlier, Ciguli Miguli or Last Hurrah For Chivalry?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Ciguli Miguli; director; Branko Marjanovi\u0107>", 
                "C. <Ciguli Miguli; year of release; 1952>",
                "D. <Last Hurrah for Chivalry; precursor to; heroic bloodshed films>",
                "E. <Ciguli Miguli; country of origin; Yugoslavia>"
            ],
            "answer": "B", 
        },
        {
            "question": "Which film has the director who was born earlier, Ciguli Miguli or Last Hurrah For Chivalry?", 
            "triples": [
                "<Ciguli Miguli; director; Branko Marjanovi\u0107>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Ciguli Miguli; year of release; 1952>", 
                "C. <Ciguli Miguli; country of origin; Yugoslavia>",
                "D. <Last Hurrah for Chivalry; country of origin; Hong Kong>",
                "E. <Last Hurrah for Chivalry; occupation of John Woo; writer, producer, director>"
            ],
            "answer": "E", 
        },
        {
            "question": "Which film has the director who was born earlier, Ciguli Miguli or Last Hurrah For Chivalry?", 
            "triples": [
                "<Ciguli Miguli; director; Branko Marjanovi\u0107>",
                "<Last Hurrah for Chivalry; occupation of John Woo; writer, producer, director>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <John Woo; occupation; film director, producer, and screenwriter>", 
                "C. <John Woo; notable films; A Better Tomorrow, The Killer, Hard Boiled, Red Cliff>",
                "D. <John Woo; date of birth; 1 May 1946>",
                "E. <John Woo; founder and chairman; Lion Rock Productions>"
            ],
            "answer": "D", 
        },
        {
            "question": "Which film has the director who was born earlier, Ciguli Miguli or Last Hurrah For Chivalry?", 
            "triples": [
                "<Ciguli Miguli; director; Branko Marjanovi\u0107>",
                "<Last Hurrah for Chivalry; occupation of John Woo; writer, producer, director>",
                "<John Woo; date of birth; 1 May 1946>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <John Woo; occupation; film director, producer, and screenwriter>", 
                "C. <John Woo; notable films; A Better Tomorrow, The Killer, Hard Boiled, Red Cliff>",
                "D. <Ciguli Miguli; year of release; 1952>",
                "E. <Branko Marjanovi\u0107; date of birth; 12 May 1909>"
            ],
            "answer": "E", 
        },
    ],
    [
        {
            "question": "Did Yanic Gentry and Sverre Farstad share the same nationality?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Yanic Gentry; full name; Yanic Arno Gentry Torfer>", 
                "C. <Sverre Farstad; nationality; Norwegian>",
                "D. <Yanic Gentry; nationality; Mexican>",
                "E. <Yanic Gentry; date of birth; 20 February 1991>"
            ],
            "answer": "C", 
        },
        {
            "question": "Did Yanic Gentry and Sverre Farstad share the same nationality?", 
            "triples": [
                "<Sverre Farstad; nationality; Norwegian>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Yanic Gentry; full name; Yanic Arno Gentry Torfer>", 
                "C. <Sverre Farstad; occupation; speed skater>",
                "D. <Sverre Farstad; notable achievements; Olympic gold medal and European Championship>",
                "E. <Yanic Gentry; nationality; Mexican>"
            ],
            "answer": "E", 
        },
        {
            "question": "Did Yanic Gentry and Sverre Farstad share the same nationality?", 
            "triples": [
                "<Sverre Farstad; nationality; Norwegian>", 
                "<Yanic Gentry; nationality; Mexican>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Yanic Gentry; full name; Yanic Arno Gentry Torfer>", 
                "C. <Sverre Farstad; occupation; speed skater>",
                "D. <Sverre Farstad; notable achievements; Olympic gold medal and European Championship>",
                "E. <Sverre Farstad; date of birth; 8 February 1920>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Are both villages, Kusejabad and Shaneh Tarash, located in the same country?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Shaneh Tarash; location; Shahidabad Rural District, Bandpey-ye Gharbi District, Babol County, Mazandaran Province, Iran>", 
                "C. <Shaneh Tarash Mahalleh; type; village>",
                "D. <Kusejabad; location; Khararud Rural District, in the Central District of Khodabandeh County, Zanjan Province, Iran>",
                "E. <Shaneh Tarash; type; village>"
            ],
            "answer": "B", 
        },
        {
            "question": "Are both villages, Kusejabad and Shaneh Tarash, located in the same country?", 
            "triples": [
                "<Shaneh Tarash; location; Shahidabad Rural District, Bandpey-ye Gharbi District, Babol County, Mazandaran Province, Iran>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Shaneh Tarash Mahalleh; location; Do Hezar Rural District, Khorramabad District, Tonekabon County, Mazandaran Province, Iran>", 
                "C. <Kusejabad; location; Khararud Rural District, in the Central District of Khodabandeh County, Zanjan Province, Iran>",
                "D. <Shaneh Tarash Mahalleh; type; village>",
                "E. <Shaneh Tarash Mahalleh; population at the 2006 census; 74>"
            ],
            "answer": "C", 
        },
        {
            "question": "Are both villages, Kusejabad and Shaneh Tarash, located in the same country?", 
            "triples": [
                "<Shaneh Tarash; location; Shahidabad Rural District, Bandpey-ye Gharbi District, Babol County, Mazandaran Province, Iran>",
                "<Kusejabad; location; Khararud Rural District, in the Central District of Khodabandeh County, Zanjan Province, Iran>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Shaneh Tarash Mahalleh; type; village>", 
                "C. <Shaneh Tarash; type; village>",
                "D. <Shaneh Tarash Mahalleh; population at the 2006 census; 74>",
                "E. <Kusejabad; population in 2006; 427>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Where was the director of film 4.3.2.1. born?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Noel Clarke; occupation; director>", 
                "C. <Lizzie Borden (director); occupation; filmmaker>",
                "D. <4.3.2.1.; director; Noel Clarke and Mark Davis>",
                "E. <Lizzie Borden (director); nationality; American>"
            ],
            "answer": "D", 
        },
        {
            "question": "Where was the director of film 4.3.2.1. born?", 
            "triples": [
                "<4.3.2.1.; director; Noel Clarke and Mark Davis>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Noel Clarke; place of origin; London>", 
                "C. <Noel Clarke; year of birth; 1975>",
                "D. <Noel Clarke; occupation; director>",
                "E. <Noel Clarke; nationality; English>"
            ],
            "answer": "B", 
        },
        {
            "question": "Where was the director of film 4.3.2.1. born?", 
            "triples": [
                "<4.3.2.1.; director; Noel Clarke and Mark Davis>",
                "<Noel Clarke; place of origin; London>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Noel Clarke; occupation; director>", 
                "C. <Noel Clarke; year of birth; 1975>",
                "D. <Noel Clarke; role in \"Adulthood\"; director>",
                "E. <Noel Clarke; nationality; English>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Where did the performer of song I Know Why (And So Do You) die?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <I Know Why (And So Do You); song by; Glenn Miller and His Orchestra>", 
                "C. <I Don't Know Why; artist; American singer-songwriter Stevie Wonder>",
                "D. <I Know Why (And So Do You); release year; 1941>",
                "E. <I Don't Know Why; release year; 1968>"
            ],
            "answer": "B", 
        },
        {
            "question": "Where did the performer of song I Know Why (And So Do You) die?", 
            "triples": [
                "<I Know Why (And So Do You); song by; Glenn Miller and His Orchestra>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Glenn Miller; death date; December 15, 1944>", 
                "C. <Glenn Miller; disappearance; while traveling to entertain U.S. troops in France during World War II>",
                "D. <Glenn Miller; nationality; American>",
                "E. <Glenn Miller; disappearance location; over the English Channel>"
            ],
            "answer": "E", 
        },
        {
            "question": "Where did the performer of song I Know Why (And So Do You) die?", 
            "triples": [
                "<I Know Why (And So Do You); song by; Glenn Miller and His Orchestra>",
                "<Glenn Miller; disappearance location; over the English Channel>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Glenn Miller; disappearance; while traveling to entertain U.S. troops in France during World War II>", 
                "C. <Glenn Miller; death date; December 15, 1944>",
                "D. <Glenn Miller; nationality; American>",
                "E. <Glenn Miller; band; one of the best-known big bands>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Which country the director of film Why? (Film) is from?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Why?; director; Karel Smyczek>", 
                "C. <Why?; film festival; 1988 Cannes Film Festival>",
                "D. <Why?; type; drama film>",
                "E. <Karel Smyczek; notable film; Why?>"
            ],
            "answer": "B", 
        },
        {
            "question": "Which country the director of film Why? (Film) is from?", 
            "triples": [
                "<Why?; director; Karel Smyczek>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Karel Smyczek; notable film; Why?>", 
                "C. <Karel Smyczek; occupation; film director, actor and screenwriter>",
                "D. <Karel Smyczek; film festival; Cannes Film Festival>",
                "E. <Karel Smyczek; nationality; Czech>"
            ],
            "answer": "E", 
        },
        {
            "question": "Which country the director of film Why? (Film) is from?", 
            "triples": [
                "<Why?; director; Karel Smyczek>",
                "<Karel Smyczek; nationality; Czech>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Karel Smyczek; notable film; Why?>", 
                "C. <Karel Smyczek; occupation; film director, actor and screenwriter>",
                "D. <Karel Smyczek; film festival; Cannes Film Festival>",
                "E. <Karel Smyczek; section at the film festival; Un Certain Regard>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who is Eleonora, Princess Of Ligne's maternal grandfather?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Eleonora, Princess of Ligne; mother; Princess Maria Elisabeth of Bavaria>", 
                "C. <Eleonora, Princess of Ligne; head of the House of Ligne; since 2005>",
                "D. <Antoine, 13th Prince of Ligne; mother; Philippine de Noailles>",
                "E. <Eleonora, Princess of Ligne; spouse; Michel, 14th Prince of Ligne>"
            ],
            "answer": "B", 
        },
        {
            "question": "Who is Eleonora, Princess Of Ligne's maternal grandfather?", 
            "triples": [
                "<Eleonora, Princess of Ligne; mother; Princess Maria Elisabeth of Bavaria>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Princess Maria Elisabeth of Bavaria; grandparent; Ludwig III of Bavaria>", 
                "C. <Eleonora, Princess of Ligne; father; Prince Pedro Henrique of Orl\u00e9ans-Braganza>",
                "D. <Princess Maria Elisabeth of Bavaria; parent; Prince Franz of Bavaria>",
                "E. <Eleonora, Princess of Ligne; brother; Prince Luiz>"
            ],
            "answer": "D", 
        },
        {
            "question": "Who is Eleonora, Princess Of Ligne's maternal grandfather?", 
            "triples": [
                "<Eleonora, Princess of Ligne; mother; Princess Maria Elisabeth of Bavaria>",
                "<Princess Maria Elisabeth of Bavaria; parent; Prince Franz of Bavaria>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Princess Maria Elisabeth of Bavaria; grandparent; Ludwig III of Bavaria>", 
                "C. <Princess Maria Elisabeth of Bavaria; sibling order; eldest daughter>",
                "D. <Eleonora, Princess of Ligne; brother; Prince Luiz>",
                "E. <Antoine, 13th Prince of Ligne; mother; Philippine de Noailles>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Where was the performer of song Where Do You Come From born?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Where Do You Come From; song; first recorded by Elvis Presley>", 
                "C. <Where Do You Come From; included on; the soundtrack album \"Girls! Girls! Girls!\">",
                "D. <Do You (Bro'Sis song); album; Never Forget( Where You Come From)>",
                "E. <Elvis Presley; place of birth; Tupelo, Mississippi>"
            ],
            "answer": "B", 
        },
        {
            "question": "Where was the performer of song Where Do You Come From born?", 
            "triples": [
                "<Where Do You Come From; song; first recorded by Elvis Presley>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Elvis Presley; place of birth; Tupelo, Mississippi>", 
                "C. <Elvis Presley; nationality; American>",
                "D. <Elvis Presley; date of birth; January 8, 1935>",
                "E. <Elvis Presley; first single; \"Heartbreak Hotel\">"
            ],
            "answer": "B", 
        },
        {
            "question": "Where was the performer of song Where Do You Come From born?", 
            "triples": [
                "<Where Do You Come From; song; first recorded by Elvis Presley>",
                "<Elvis Presley; place of birth; Tupelo, Mississippi>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Elvis Presley; place of relocation; Memphis, Tennessee>", 
                "C. <Elvis Presley; nationality; American>",
                "D. <Elvis Presley; date of birth; January 8, 1935>",
                "E. <Elvis Presley; first single; \"Heartbreak Hotel\">"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "What is the date of death of Odo Of Wetterau's father?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Odo of Wetterau; date of death; 2 December 949>", 
                "C. <Odo of Wetterau; year of birth; c. 895>",
                "D. <Odo I, Count of Troyes; date of death; 10 June 871>",
                "E. <Herbert of Wetterau; father; Odo of Wetterau>"
            ],
            "answer": "E", 
        },
        {
            "question": "What is the date of death of Odo Of Wetterau's father?", 
            "triples": [
                "<Herbert of Wetterau; father; Odo of Wetterau>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Odo of Wetterau; date of death; 2 December 949>", 
                "C. <Herbert of Wetterau; year of death; 992>",
                "D. <Herbert of Wetterau; year of birth; c. 930>",
                "E. <Herbert of Wetterau; noble status; important nobleman in central Germany and leader of the Conradines>"
            ],
            "answer": "C", 
        },
        {
            "question": "What is the date of death of Odo Of Wetterau's father?", 
            "triples": [
                "<Herbert of Wetterau; father; Odo of Wetterau>",
                "<Herbert of Wetterau; year of death; 992>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Odo of Wetterau; date of death; 2 December 949>", 
                "C. <Herbert of Wetterau; year of birth; c. 930>",
                "D. <Odo of Wetterau; year of birth; c. 895>",
                "E. <Herbert of Wetterau; event; followed Emperor Otto II to Italy in 976>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Are the directors of films Dark Side Romance and Stand Clear of the Closing Doors both from the same country?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Dark Side Romance; director; Prachya Pinkaew>", 
                "C. <Stand Clear of the Closing Doors; director; Sam Fleischner>",
                "D. <Stand Clear of the Closing Doors; type; drama film>",
                "E. <Stand Clear of the Closing Doors; film festival; 2013 Deauville American Film Festival>"
            ],
            "answer": "B", 
        },
        {
            "question": "Are the directors of films Dark Side Romance and Stand Clear of the Closing Doors both from the same country?", 
            "triples": [
                "<Dark Side Romance; director; Prachya Pinkaew>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Prachya Pinkaew; nationality; Thai>", 
                "C. <Prachya Pinkaew; occupation; film director, film producer, screenwriter>",
                "D. <Prachya Pinkaew; Tom-Yum-Goong; starring Tony Jaa>",
                "E. <Stand Clear of the Closing Doors; director; Sam Fleischner>"
            ],
            "answer": "E", 
        },
        {
            "question": "Are the directors of films Dark Side Romance and Stand Clear of the Closing Doors both from the same country?", 
            "triples": [
                "<Dark Side Romance; director; Prachya Pinkaew>",
                "<Stand Clear of the Closing Doors; director; Sam Fleischner>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Prachya Pinkaew; occupation; film director, film producer, screenwriter>", 
                "C. <Prachya Pinkaew; nationality; Thai>",
                "D. <Prachya Pinkaew; film; Tom-Yum-Goong>",
                "E. <Prachya Pinkaew; starring Tony Jaa; martial arts film>"
            ],
            "answer": "C", 
        },
        {
            "question": "Are the directors of films Dark Side Romance and Stand Clear of the Closing Doors both from the same country?", 
            "triples": [
                "<Dark Side Romance; director; Prachya Pinkaew>",
                "<Stand Clear of the Closing Doors; director; Sam Fleischner>",
                "<Prachya Pinkaew; nationality; Thai>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Prachya Pinkaew; occupation; film director, film producer, screenwriter>", 
                "C. <Prachya Pinkaew; date of birth; September 2, 1962>",
                "D. <Sam Fleischner; occupation; filmmaker>",
                "E. <Sam Fleischner; nationality; American>"
            ],
            "answer": "E", 
        },
    ],
    [
        {
            "question": "Are both villages, Bizdan and Bodella, located in the same country?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Bizdan; population at the 2006 census; 206>", 
                "C. <Bodella; location; mid Cornwall, England, United Kingdom>",
                "D. <Bizdan; number of families at the 2006 census; 47>",
                "E. <Bodella; surrounding area; china clay quarries>"
            ],
            "answer": "C", 
        },
        {
            "question": "Are both villages, Bizdan and Bodella, located in the same country?", 
            "triples": [
                "<Bodella; location; mid Cornwall, England, United Kingdom>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Bodella; surrounding area; china clay quarries>", 
                "C. <Bodella; proximity to; St Dennis>",
                "D. <Bizdan; type; village>",
                "E. <Bizdan; location; Nasrovan Rural District, in the Central District of Darab County, Fars Province, Iran>"
            ],
            "answer": "E", 
        },
        {
            "question": "Are both villages, Bizdan and Bodella, located in the same country?", 
            "triples": [
                "<Bodella; location; mid Cornwall, England, United Kingdom>",
                "<Bizdan; location; Nasrovan Rural District, in the Central District of Darab County, Fars Province, Iran>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Bodella; surrounding area; china clay quarries>", 
                "C. <Bodella; proximity to; St Dennis>",
                "D. <Bodella; proximity distance to St Dennis; half-a-mile>",
                "E. <Bizdan; type; village>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who is the spouse of the director of film Where Does It Hurt?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Where Does It Hurt?; director; Rod Amateau>", 
                "C. <Where Does It Hurt?; type; American comedy film>",
                "D. <Where Does It Hurt?; starring; Peter Sellers, Jo Ann Pflug, Rick Lenz, Pat Morita, Harold Gould>",
                "E. <Where Does It Hurt?; writer; Rod Amateau>"
            ],
            "answer": "B", 
        },
        {
            "question": "Who is the spouse of the director of film Where Does It Hurt?", 
            "triples": [
                "<Where Does It Hurt?; director; Rod Amateau>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Where Does It Hurt?; writer; Rod Amateau>", 
                "C. <Rod Amateau; spouse's daughter; Coleen Gray (from 1955)>",
                "D. <Rod Amateau; spouse; Coleen Gray (1945-1949)>",
                "E. <Rod Amateau; spouse; Sandra Burns (1959-1962)>"
            ],
            "answer": "D", 
        },
        {
            "question": "Who is the spouse of the director of film Where Does It Hurt?", 
            "triples": [
                "<Where Does It Hurt?; director; Rod Amateau>",
                "<Rod Amateau; spouse; Coleen Gray (1945-1949)>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Rod Amateau; spouse's daughter; Coleen Gray (from 1955)>", 
                "C. <Rod Amateau; sued for child support; Coleen Gray (in 1955)>",
                "D. <Where Does It Hurt?; writer; Rod Amateau>",
                "E. <Where Does It Hurt?; type; American comedy film>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Do the movies We Make Movies and Orchids To You, originate from the same country?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <We Make Movies; country of origin; American>", 
                "C. <Orchids to You; type; American drama film>",
                "D. <Orchids to You; director; William A. Seiter>",
                "E. <We Make Movies; release year; 2016>"
            ],
            "answer": "B", 
        },
        {
            "question": "Do the movies We Make Movies and Orchids To You, originate from the same country?", 
            "triples": [
                "<We Make Movies; country of origin; American>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Orchids to You; type; American drama film>", 
                "C. <Orchids to You; director; William A. Seiter>",
                "D. <We Make Movies; release year; 2016>",
                "E. <We Make Movies; type; mockumentary comedy independent film>"
            ],
            "answer": "B", 
        },
        {
            "question": "Do the movies We Make Movies and Orchids To You, originate from the same country?", 
            "triples": [
                "<We Make Movies; country of origin; American>",
                "<Orchids to You; type; American drama film>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Orchids to You; director; William A. Seiter>", 
                "C. <Orchids to You; plot; a flower shop owner and a married attorney who begin a romance after meeting in court>",
                "D. <We Make Movies; type; mockumentary comedy independent film>",
                "E. <Orchids to You; release year; 1935>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who was born earlier, Siobhan Chamberlain or Aloyzas Stasiulevi\u010dius?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Siobhan Chamberlain; date of birth; 15 August 1983>", 
                "C. <Siobhan Chamberlain; full name; Siobhan Rebecca Chamberlain>",
                "D. <Aloyzas Stasiulevi\u010dius; date of birth; June 2, 1931>",
                "E. <Siobhan Chamberlain; position; goalkeeper>"
            ],
            "answer": "B", 
        },
        {
            "question": "Who was born earlier, Siobhan Chamberlain or Aloyzas Stasiulevi\u010dius?", 
            "triples": [
                "<Siobhan Chamberlain; date of birth; 15 August 1983>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Aloyzas Stasiulevi\u010dius; date of birth; June 2, 1931>", 
                "C. <Aloyzas Stasiulevi\u010dius; place of birth; Ariogala>",
                "D. <Siobhan Chamberlain; full name; Siobhan Rebecca Chamberlain>",
                "E. <Siobhan Chamberlain; position; goalkeeper>"
            ],
            "answer": "B", 
        },
        {
            "question": "Who was born earlier, Siobhan Chamberlain or Aloyzas Stasiulevi\u010dius?", 
            "triples": [
                "<Siobhan Chamberlain; date of birth; 15 August 1983>",
                "<Aloyzas Stasiulevi\u010dius; date of birth; June 2, 1931>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Aloyzas Stasiulevi\u010dius; place of birth; Ariogala>", 
                "C. <Aloyzas Stasiulevi\u010dius; nationality; Lithuanian>",
                "D. <Siobhan Chamberlain; international tournaments; FIFA Women's World Cups, UEFA Women's Championships>",
                "E. <Siobhan Chamberlain; position; goalkeeper>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "When is the director of film What? (Film) 's birthday?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <What? (film); director; Roman Polanski>", 
                "C. <What? (film); writer; Roman Polanski>",
                "D. <What? (film); release year; 1972>",
                "E. <What? (film); starring; Marcello Mastroianni>"
            ],
            "answer": "B", 
        },
        {
            "question": "When is the director of film What? (Film) 's birthday?", 
            "triples": [
                "<What? (film); director; Roman Polanski>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Roman Polanski; year of birth; 1933>", 
                "C. <Roman Polanski; occupation; film director, producer, writer, and actor>",
                "D. <Roman Polanski; original name; Raymond Thierry Liebling>",
                "E. <Roman Polanski; first feature-length film; Knife in the Water (1962)>"
            ],
            "answer": "B", 
        },
        {
            "question": "When is the director of film What? (Film) 's birthday?", 
            "triples": [
                "<What? (film); director; Roman Polanski>",
                "<Roman Polanski; year of birth; 1933>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <What? (film); writer; Roman Polanski>", 
                "C. <Roman Polanski; occupation; film director, producer, writer, and actor>",
                "D. <Roman Polanski; first feature-length film; Knife in the Water (1962)>",
                "E. <Roman Polanski; original name; Raymond Thierry Liebling>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "What is the place of birth of the composer of film Sagaptham?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Sagaptham; soundtrack composer; Karthik Raja>", 
                "C. <Karthik Raja; genre of music; film music>",
                "D. <Karthik Raja; occupation; composer>",
                "E. <Karthik Raja; nationality; Indian>"
            ],
            "answer": "B", 
        },
        {
            "question": "What is the place of birth of the composer of film Sagaptham?", 
            "triples": [
                "<Sagaptham; soundtrack composer; Karthik Raja>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Karthik Raja; genre of music; film music>", 
                "C. <Karthik Raja; place of residence; Chennai, India>",
                "D. <Karthik Raja; occupation; composer>",
                "E. <Karthik Raja; nationality; Indian>"
            ],
            "answer": "C", 
        },
        {
            "question": "What is the place of birth of the composer of film Sagaptham?", 
            "triples": [
                "<Sagaptham; soundtrack composer; Karthik Raja>",
                "<Karthik Raja; place of residence; Chennai, India>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Karthik Raja; genre of music; film music>", 
                "C. <Karthik Raja; occupation; composer>",
                "D. <Sagaptham; cinematography; S. K. Bhupathi>",
                "E. <Sagaptham; story and dialogues writers; Naveen Krishna and Velumani>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Are both Shenendehowa High School and Opeongo High School located in the same country?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Opeongo High School; location; Renfrew County, Ontario, Canada>", 
                "C. <Shenendehowa High School; type; public high school>",
                "D. <Shenendehowa High School; location; Clifton Park, New York, United States>",
                "E. <Shenendehowa High School; part of; Shenendehowa Central School District>"
            ],
            "answer": "B", 
        },
        {
            "question": "Are both Shenendehowa High School and Opeongo High School located in the same country?", 
            "triples": [
                "<Opeongo High School; location; Renfrew County, Ontario, Canada>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Shenendehowa High School; type; public high school>", 
                "C. <Shenendehowa High School; location; Clifton Park, New York, United States>",
                "D. <Shenendehowa High School; part of; Shenendehowa Central School District>",
                "E. <Opeongo High School; student population; between 400 and 500 students>"
            ],
            "answer": "C", 
        },
        {
            "question": "Are both Shenendehowa High School and Opeongo High School located in the same country?", 
            "triples": [
                "<Opeongo High School; location; Renfrew County, Ontario, Canada>",
                "<Shenendehowa High School; location; Clifton Park, New York, United States>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Shenendehowa High School; type; public high school>", 
                "C. <Shenendehowa High School; part of; Shenendehowa Central School District>",
                "D. <Shenendehowa High School; building location; on the district's main campus off of NY 146>",
                "E. <Opeongo High School; student population; between 400 and 500 students>"
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Which film came out earlier, Sachein or Bettie Page Reveals All?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Sachein; release year; 2005>", 
                "C. <Sachein; starring; Bipasha Basu>",
                "D. <Bettie Page Reveals All; director; Mark Mori>",
                "E. <The Notorious Bettie Page; release year; 2005>"
            ],
            "answer": "B", 
        },
        {
            "question": "Which film came out earlier, Sachein or Bettie Page Reveals All?", 
            "triples": [
                "<Sachein; release year; 2005>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Sachein; starring; Bipasha Basu>", 
                "C. <Sachein; starring; Vijay and Genelia D'Souza>",
                "D. <Bettie Page Reveals All; commentator; Rebecca Romijn>",
                "E. <Bettie Page Reveals All; director; Mark Mori>"
            ],
            "answer": "D", 
        },
        {
            "question": "Which film came out earlier, Sachein or Bettie Page Reveals All?", 
            "triples": [
                "<Sachein; release year; 2005>",
                "<Bettie Page Reveals All; commentator; Rebecca Romijn>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Sachein; starring; Bipasha Basu>", 
                "C. <Bettie Page Reveals All; director; Mark Mori>",
                "D. <Bettie Page Reveals All; commentator; Hugh Hefner>",
                "E. <Bettie Page Reveals All; commentator; Naomi Campbell>"
            ],
            "answer": "C", 
        },
        {
            "question": "Which film came out earlier, Sachein or Bettie Page Reveals All?", 
            "triples": [
                "<Sachein; release year; 2005>",
                "<Bettie Page Reveals All; commentator; Rebecca Romijn>",
                "<Bettie Page Reveals All; director; Mark Mori>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Bettie Page Reveals All; commentator; Rebecca Romijn>", 
                "C. <Bettie Page Reveals All; commentator; Mamie Van Doren>",
                "D. <Bettie Page Reveals All; commentator; Bunny Yeager>",
                "E. <Bettie Page Reveals All; subject; life history and cultural influence of Bettie Page>"
            ],
            "answer": "B", 
        },
    ],
]


reasoning_chains_2wikimultihopqa_examplars = [
    {
        "question": "Where was the husband of Mollena Williams-Haas born?",
        "chains": "<Mollena Williams-Haas; spouse; Georg Friedrich Haas>, <Georg Friedrich Haas; place of birth; Graz, Austria>", 
    },
    {
        "question": "Where did the director of film The Man Who Owed A Death die?", 
        "chains": "<The Man Who Owed a Death; director; Mario Soffici>, <Mario Soffici; place of death; Buenos Aires>", 
    },
    {
        "question": "Which film has the director who was born earlier, Ciguli Miguli or Last Hurrah For Chivalry?", 
        "chains": "<Ciguli Miguli; director; Branko Marjanovi\u0107>, <Last Hurrah for Chivalry; occupation of John Woo; writer, producer, director>, <John Woo; date of birth; 1 May 1946>, <Branko Marjanovi\u0107; date of birth; 12 May 1909>", 
    },
    {
        "question": "Did Yanic Gentry and Sverre Farstad share the same nationality?", 
        "chains": "<Sverre Farstad; nationality; Norwegian>, <Yanic Gentry; nationality; Mexican>", 
    },
    {
        "question": "Are both villages, Kusejabad and Shaneh Tarash, located in the same country?", 
        "chains": "<Shaneh Tarash; location; Shahidabad Rural District, Bandpey-ye Gharbi District, Babol County, Mazandaran Province, Iran>, <Kusejabad; location; Khararud Rural District, in the Central District of Khodabandeh County, Zanjan Province, Iran>", 
    },
    {
        "question": "Where was the director of film 4.3.2.1. born?", 
        "chains": "<4.3.2.1.; director; Noel Clarke and Mark Davis>, <Noel Clarke; place of origin; London>", 
    },
    {
        "question": "Where did the performer of song I Know Why (And So Do You) die?", 
        "chains": "<I Know Why (And So Do You); song by; Glenn Miller and His Orchestra>, <Glenn Miller; disappearance location; over the English Channel>", 
    },
    {
        "question": "Which country the director of film Why? (Film) is from?", 
        "chains": "<Why?; director; Karel Smyczek>, <Karel Smyczek; nationality; Czech>", 
    },
    {
        "question": "Who is Eleonora, Princess Of Ligne's maternal grandfather?", 
        "chains": "<Eleonora, Princess of Ligne; mother; Princess Maria Elisabeth of Bavaria>, <Princess Maria Elisabeth of Bavaria; parent; Prince Franz of Bavaria>", 
    },
    {
        "question": "Where was the performer of song Where Do You Come From born?", 
        "chains": "<Where Do You Come From; song; first recorded by Elvis Presley>, <Elvis Presley; place of birth; Tupelo, Mississippi>", 
    },
    {
        "question": "What is the date of death of Odo Of Wetterau's father?", 
        "chains": "<Herbert of Wetterau; father; Odo of Wetterau>, <Herbert of Wetterau; year of death; 992>", 
    },
    {
        "question": "Are the directors of films Dark Side Romance and Stand Clear of the Closing Doors both from the same country?", 
        "chains": "<Dark Side Romance; director; Prachya Pinkaew>, <Stand Clear of the Closing Doors; director; Sam Fleischner>, <Prachya Pinkaew; nationality; Thai>, <Sam Fleischner; nationality; American>", 
    },
    {
        "question": "Are both villages, Bizdan and Bodella, located in the same country?", 
        "chains": "<Bodella; location; mid Cornwall, England, United Kingdom>, <Bizdan; location; Nasrovan Rural District, in the Central District of Darab County, Fars Province, Iran>", 
    },
    {
        "question": "Who is the spouse of the director of film Where Does It Hurt?", 
        "chains": "<Where Does It Hurt?; director; Rod Amateau>, <Rod Amateau; spouse; Coleen Gray (1945-1949)>", 
    },
    {
        "question": "Do the movies We Make Movies and Orchids To You, originate from the same country?", 
        "chains": "<We Make Movies; country of origin; American>, <Orchids to You; type; American drama film>", 
    },
    {
        "question": "Who was born earlier, Siobhan Chamberlain or Aloyzas Stasiulevi\u010dius?", 
        "chains": "<Siobhan Chamberlain; date of birth; 15 August 1983>, <Aloyzas Stasiulevi\u010dius; date of birth; June 2, 1931>", 
    },
    {
        "question": "When is the director of film What? (Film) 's birthday?", 
        "chains": "<What? (film); director; Roman Polanski>, <Roman Polanski; year of birth; 1933>", 
    },
    {
        "question": "What is the place of birth of the composer of film Sagaptham?", 
        "chains": "<Sagaptham; soundtrack composer; Karthik Raja>, <Karthik Raja; place of residence; Chennai, India>", 
    },
    {
        "question": "Are both Shenendehowa High School and Opeongo High School located in the same country?", 
        "chains": "<Opeongo High School; location; Renfrew County, Ontario, Canada>, <Shenendehowa High School; location; Clifton Park, New York, United States>", 
    },
    {
        "question": "Which film came out earlier, Sachein or Bettie Page Reveals All?", 
        "chains": "<Sachein; release year; 2005>; <Bettie Page Reveals All; commentator; Rebecca Romijn>, <Bettie Page Reveals All; director; Mark Mori>, <Bettie Page Reveals All; commentator; Rebecca Romijn>", 
    }
]
