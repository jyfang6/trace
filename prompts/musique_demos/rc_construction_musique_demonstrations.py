

generate_reasoning_chains_musique_examplars = [
    [
        {
            "question": "Who was the premier of the country that invaded the country that produced The Guard Post?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Guard Post; type; 2008 Korean horror film>", 
                "C. <The Guard Post; director; Kong Su-chang>", 
                "D. <The Guard Post; writer; Kong Su-chang>",
                "E. <North Korea; head of government; Premier Pak Pong-ju>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who was the premier of the country that invaded the country that produced The Guard Post?", 
            "triples": [
                "<The Guard Post; type; 2008 Korean horror film>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Korean War; cause; North Korea invaded South Korea following a series of clashes along the border>", 
                "C. <The Guard Post; director; Kong Su-chang>", 
                "D. <The Korean War; China's involvement; China came to the aid of North Korea>",
                "E. <The Guard Post; writer; Kong Su-chang>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who was the premier of the country that invaded the country that produced The Guard Post?", 
            "triples": [
                "<The Guard Post; type; 2008 Korean horror film>",
                "<The Korean War; cause; North Korea invaded South Korea following a series of clashes along the border>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Guard Post; director; Kong Su-chang>", 
                "C. <The Korean War; start date; 25 June 1950>", 
                "D. <North Korea; head of government; Premier Pak Pong-ju>",
                "E. <The Korean War; South Korea's support; United States>", 
            ],
            "answer": "D", 
        },
        {
            "question": "Who was the premier of the country that invaded the country that produced The Guard Post?", 
            "triples": [
                "<The Guard Post; type; 2008 Korean horror film>",
                "<The Korean War; cause; North Korea invaded South Korea following a series of clashes along the border>",
                "<North Korea; head of government; Premier Pak Pong-ju>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Guard Post; director; Kong Su-chang>", 
                "C. <The Korean War; China's involvement; China came to the aid of North Korea>", 
                "D. <The Guard Post; writer; Kong Su-chang>",
                "E. <The Korean War; start date; 25 June 1950>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who created the borders of countries on the continent where Legend of the Lost was filmed?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Legend of the Lost; location work; Rome and Libya>", 
                "C. <Legend of the Lost; location of the lost city; near Tripoli, in northwest Libya>", 
                "D. <Africa; outcome of European occupation; creation of many colonial territories>",
                "E. <Libya; bordering countries; Mediterranean Sea, Egypt, Sudan, Chad, Niger, Algeria, Tunisia>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who created the borders of countries on the continent where Legend of the Lost was filmed?", 
            "triples": [
                "<Legend of the Lost; location work; Rome and Libya>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Legend of the Lost; location of the lost city; near Tripoli, in northwest Libya>", 
                "C. <Libya; bordering countries; Mediterranean Sea, Egypt, Sudan, Chad, Niger, Algeria, Tunisia>", 
                "D. <Libya; location; Maghreb region in North Africa>",
                "E. <Legend of the Lost; lost city referred to; Leptis Magna ruins>", 
            ],
            "answer": "D", 
        },
        {
            "question": "Who created the borders of countries on the continent where Legend of the Lost was filmed?", 
            "triples": [
                "<Legend of the Lost; location work; Rome and Libya>",
                "<Libya; location; Maghreb region in North Africa>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Legend of the Lost; lost city referred to; Leptis Magna ruins>", 
                "C. <Libya; regions; Tripolitania, Fezzan, Cyrenaica>", 
                "D. <Legend of the Lost; headquarters; Ghadames>",
                "E. <Africa; outcome of European occupation; creation of many colonial territories>", 
            ],
            "answer": "E", 
        },
        {
            "question": "Who created the borders of countries on the continent where Legend of the Lost was filmed?", 
            "triples": [
                "<Legend of the Lost; location work; Rome and Libya>",
                "<Libya; location; Maghreb region in North Africa>",
                "<Africa; outcome of European occupation; creation of many colonial territories>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Legend of the Lost; location of the lost city; near Tripoli, in northwest Libya>", 
                "C. <Legend of the Lost; lost city referred to; Leptis Magna ruins>", 
                "D. <Libya; regions; Tripolitania, Fezzan, Cyrenaica>",
                "E. <Africa; period of European occupation; late 19th century>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "How many theater companies are in residence in the city where Askville's owner is headquartered?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Seattle; ranking; probably second only to New York for number of equity theaters>", 
                "C. <Seattle; number of equity theaters; 28>", 
                "D. <Askville; founder; Amazon.com>",
                "E. <Houston; has; The Alley Theatre>", 
            ],
            "answer": "D", 
        },
        {
            "question": "How many theater companies are in residence in the city where Askville's owner is headquartered?", 
            "triples": [
                "<Askville; founder; Amazon.com>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Seattle; ranking; probably second only to New York for number of equity theaters>", 
                "C. <AmazonFresh; location; Seattle, Washington>", 
                "D. <Seattle; number of theatrical production companies; around 100>",
                "E. <Seattle; number of live theatre venues; over two dozen>", 
            ],
            "answer": "C", 
        },
        {
            "question": "How many theater companies are in residence in the city where Askville's owner is headquartered?", 
            "triples": [
                "<Askville; founder; Amazon.com>",
                "<AmazonFresh; location; Seattle, Washington>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Seattle; number of theatrical production companies; around 100>", 
                "C. <Seattle; number of live theatre venues; over two dozen>", 
                "D. <Seattle; ranking; probably second only to New York for number of equity theaters>",
                "E. <Seattle; number of equity theaters; 28>", 
            ],
            "answer": "B", 
        },
        {
            "question": "How many theater companies are in residence in the city where Askville's owner is headquartered?", 
            "triples": [
                "<Askville; founder; Amazon.com>",
                "<AmazonFresh; location; Seattle, Washington>",
                "<Seattle; number of theatrical production companies; around 100>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Seattle; number of equity theaters; 28>", 
                "C. <Seattle; type of theatre; fringe theatre>", 
                "D. <Seattle; venue; 5th Avenue Theatre>",
                "E. <AmazonFresh; subsidiary of; Amazon.com>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Which county shares a border with the county in which Wayne is located?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Wayne, Washington County, Wisconsin; location; in Washington County, Wisconsin, United States>", 
                "C. <Wayne, Washington County, Wisconsin; contains; Kohlsville>", 
                "D. <Wayne, Washington County, Wisconsin; population as of the 2000 census; 1,727>",
                "E. <Tatra County; location; Lesser Poland Voivodeship, southern Poland, on the Slovak border>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Which county shares a border with the county in which Wayne is located?", 
            "triples": [
                "<Wayne, Washington County, Wisconsin; location; in Washington County, Wisconsin, United States>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Wayne, Washington County, Wisconsin; contains; Kohlsville>", 
                "C. <Wayne, Washington County, Wisconsin; contains; Wayne>", 
                "D. <Wayne, Washington County, Wisconsin; population as of the 2000 census; 1,727>",
                "E. <Colgate, Wisconsin; location; in Washington County, Wisconsin, United States, straddling the county line with Waukesha County>", 
            ],
            "answer": "E", 
        },
        {
            "question": "Which county shares a border with the county in which Wayne is located?", 
            "triples": [
                "<Wayne, Washington County, Wisconsin; location; in Washington County, Wisconsin, United States>",
                "<Colgate, Wisconsin; location; in Washington County, Wisconsin, United States, straddling the county line with Waukesha County>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Wayne, Washington County, Wisconsin; contains; Kohlsville>", 
                "C. <Wayne, Washington County, Wisconsin; population as of the 2000 census; 1,727>", 
                "D. <Colgate, Wisconsin; location; partially in the town of Lisbon>",
                "E. <Colgate, Wisconsin; location; partially in the village of Richfield>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who is the spouse of the person who made The Circe Invidiosa?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Circe Invidiosa; artist; John William Waterhouse>", 
                "C. <Circe Invidiosa; creation year; 1892>", 
                "D. <Circe Invidiosa; mythological character; Circe>",
                "E. <Circe Invidiosa; inspiration; Ovid's \"Metamorphoses\">", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who is the spouse of the person who made The Circe Invidiosa?", 
            "triples": [
                "<Circe Invidiosa; artist; John William Waterhouse>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Esther Kenworthy Waterhouse; marriage; John William Waterhouse>", 
                "C. <Circe Invidiosa; creation year; 1892>", 
                "D. <Circe Offering the Cup to Ulysses; creator; John William Waterhouse>",
                "E. <Circe Invidiosa; mythological character; Circe>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who is the spouse of the person who made The Circe Invidiosa?", 
            "triples": [
                "<Circe Invidiosa; artist; John William Waterhouse>",
                "<Esther Kenworthy Waterhouse; marriage; John William Waterhouse>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Circe Invidiosa; creation year; 1892>", 
                "C. <Circe Offering the Cup to Ulysses; creator; John William Waterhouse>", 
                "D. <Esther Kenworthy Waterhouse; name change; Esther Kenworthy Waterhouse>",
                "E. <Circe Invidiosa; mythological character; Circe>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "When did the home country of Privilege's performer gain independence from England?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Privilege (Ivor Cutler album); release year; 1983>", 
                "C. <Privilege (Ivor Cutler album); record label; Rough Trade Records>", 
                "D. <Privilege (Ivor Cutler album); type; album>",
                "E. <Privilege (Ivor Cutler album); artist; Ivor Cutler>", 
            ],
            "answer": "E", 
        },
        {
            "question": "When did the home country of Privilege's performer gain independence from England?", 
            "triples": [
                "<Privilege (Ivor Cutler album); artist; Ivor Cutler>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Privilege (Ivor Cutler album); release year; 1983>", 
                "C. <Privilege (Ivor Cutler album); record label; Rough Trade Records>", 
                "D. <IVOR CUTLER; co-producers; Vanishing Point and National Theatre of Scotland>",
                "E. <History of Scotland; event; The Declaration of Arbroath was written in 1320>", 
            ],
            "answer": "D", 
        },
        {
            "question": "When did the home country of Privilege's performer gain independence from England?", 
            "triples": [
                "<Privilege (Ivor Cutler album); artist; Ivor Cutler>",
                "<IVOR CUTLER; co-producers; Vanishing Point and National Theatre of Scotland>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Privilege (Ivor Cutler album); release year; 1983>", 
                "C. <History of Scotland; event; Edward I died in 1307>", 
                "D. <History of Scotland; event; The Declaration of Arbroath was written in 1320>",
                "E. <History of Scotland; event; The Declaration of Arbroath helped convince Pope John XXII to overturn the earlier excommunication and nullify the various acts of submission by Scottish kings to English ones>", 
            ],
            "answer": "E", 
        },
        {
            "question": "When did the home country of Privilege's performer gain independence from England?", 
            "triples": [
                "<Privilege (Ivor Cutler album); artist; Ivor Cutler>",
                "<IVOR CUTLER; co-producers; Vanishing Point and National Theatre of Scotland>",
                "<History of Scotland; event; The Declaration of Arbroath helped convince Pope John XXII to overturn the earlier excommunication and nullify the various acts of submission by Scottish kings to English ones>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <History of Scotland; event; The Declaration of Arbroath helped Scotland's sovereignty be recognised by the major European dynasties>", 
                "C. <Privilege (Ivor Cutler album); artist; Ivor Cutler>", 
                "D. <History of Scotland; event; The Declaration of Arbroath was written in 1320>",
                "E. <Privilege (Ivor Cutler album); release year; 1983>", 
            ],
            "answer": "B", 
        },
    ],
    [
        {
            "question": "What is the population of the city where the cast member of The Adventures of Rex and Rinty lived when he died?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Rin Tin Tin; location; Long Island, New York>", 
                "C. <Rin Tin Tin; location; Los Angeles>", 
                "D. <The Adventures of Rex and Rinty; starring; Rex and Rin Tin Tin, Jr.>",
                "E. <Rin Tin Tin; event; Nanette died in Hempstead>", 
            ],
            "answer": "D", 
        },
        {
            "question": "What is the population of the city where the cast member of The Adventures of Rex and Rinty lived when he died?", 
            "triples": [
                "<The Adventures of Rex and Rinty; starring; Rex and Rin Tin Tin, Jr.>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Rin Tin Tin; location; Long Island, New York>", 
                "C. <Rin Tin Tin; location; Los Angeles>", 
                "D. <Rin Tin Tin; event; Nanette died in Hempstead>",
                "E. <Rin Tin Tin; location; Hempstead>", 
            ],
            "answer": "C", 
        },
        {
            "question": "What is the population of the city where the cast member of The Adventures of Rex and Rinty lived when he died?", 
            "triples": [
                "<The Adventures of Rex and Rinty; starring; Rex and Rin Tin Tin, Jr.>",
                "<Rin Tin Tin; location; Los Angeles>",
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Rin Tin Tin; location; Long Island, New York>", 
                "C. <Southern California; population of Los Angeles; 3,792,621>", 
                "D. <Rin Tin Tin; event; Nanette died in Hempstead>",
                "E. <Rin Tin Tin; location; Hempstead>", 
            ],
            "answer": "C", 
        },
        {
            "question": "What is the population of the city where the cast member of The Adventures of Rex and Rinty lived when he died?", 
            "triples": [
                "<The Adventures of Rex and Rinty; starring; Rex and Rin Tin Tin, Jr.>",
                "<Rin Tin Tin; location; Los Angeles>",
                "<Southern California; population of Los Angeles; 3,792,621>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Rin Tin Tin; location; Long Island, New York>", 
                "C. <Southern California; most populous city; Los Angeles>", 
                "D. <Southern California; ranking of Los Angeles; second most populous in the United States>",
                "E. <Southern California; population of San Diego; 1,307,402>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "What is the capital of the county that contains the city where Adam Blackstone was born?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Adam Blackstone; birthplace; Trenton, NJ>", 
                "C. <Adam Blackstone; birthdate; December 4, 1982>", 
                "D. <Adam Blackstone; profession; multi-instrumentalist, songwriter, producer, and bassist>",
                "E. <Adam Blackstone; role in performances; directed and played>", 
            ],
            "answer": "B", 
        },
        {
            "question": "What is the capital of the county that contains the city where Adam Blackstone was born?", 
            "triples": [
                "<Adam Blackstone; birthplace; Trenton, NJ>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Adam Blackstone; birthdate; December 4, 1982>", 
                "C. <15th Legislative District (New Jersey); municipalities in Mercer County; Ewing Township, Hopewell Borough, Hopewell Township, Lawrence Township, Pennington Borough, Trenton City, West Windsor Township>", 
                "D. <Adam Blackstone; role in performances; directed and played>",
                "E. <Nigeria; division; thirty-six states and one Federal Capital Territory>", 
            ],
            "answer": "C", 
        },
        {
            "question": "What is the capital of the county that contains the city where Adam Blackstone was born?", 
            "triples": [
                "<Adam Blackstone; birthplace; Trenton, NJ>",
                "<15th Legislative District (New Jersey); municipalities in Mercer County; Ewing Township, Hopewell Borough, Hopewell Township, Lawrence Township, Pennington Borough, Trenton City, West Windsor Township>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Adam Blackstone; profession; multi-instrumentalist, songwriter, producer, and bassist>", 
                "C. <15th Legislative District (New Jersey); number of districts in the New Jersey Legislature; 40>", 
                "D. <Adam Blackstone; role in performances; directed and played>",
                "E. <WAEY; service area; Princeton and Mercer County, West Virginia>", 
            ],
            "answer": "E", 
        },
        {
            "question": "What is the capital of the county that contains the city where Adam Blackstone was born?", 
            "triples": [
                "<Adam Blackstone; birthplace; Trenton, NJ>",
                "<15th Legislative District (New Jersey); municipalities in Mercer County; Ewing Township, Hopewell Borough, Hopewell Township, Lawrence Township, Pennington Borough, Trenton City, West Windsor Township>",
                "<WAEY; service area; Princeton and Mercer County, West Virginia>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Adam Blackstone; birthdate; December 4, 1982>", 
                "C. <WAEY; location; Princeton, West Virginia>", 
                "D. <WAEY; owner and operator; Princeton Broadcasting, Inc.>",
                "E. <Tatra County; location; Lesser Poland Voivodeship, southern Poland, on the Slovak border>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "What city holds the university where Hal Patterson was educated?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Hal Patterson; college basketball player; University of Kansas>", 
                "C. <Hal Patterson; full name; Harold \"Prince Hal\" Edward Patterson>", 
                "D. <Hal Patterson; date of birth; October 4, 1932>",
                "E. <Patterson Tract, California; location; Tulare County, California>", 
            ],
            "answer": "B", 
        },
        {
            "question": "What city holds the university where Hal Patterson was educated?", 
            "triples": [
                "<Hal Patterson; college basketball player; University of Kansas>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Center for the Study of Science Fiction; location; Lawrence, KS>", 
                "C. <Hal Patterson; full name; Harold \"Prince Hal\" Edward Patterson>", 
                "D. <Hal Patterson; member of; Canadian Football Hall of Fame>",
                "E. <Center for the Study of Science Fiction; association; University of Kansas>", 
            ],
            "answer": "E", 
        },
        {
            "question": "What city holds the university where Hal Patterson was educated?", 
            "triples": [
                "<Hal Patterson; college basketball player; University of Kansas>",
                "<Center for the Study of Science Fiction; association; University of Kansas>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Center for the Study of Science Fiction; location; Lawrence, KS>", 
                "C. <Center for the Study of Science Fiction; founder; James Gunn>", 
                "D. <Hal Patterson; professional football league; Canadian Football League>",
                "E. <Hal Patterson; date of birth; October 4, 1932>", 
            ],
            "answer": "B", 
        },
        {
            "question": "What city holds the university where Hal Patterson was educated?", 
            "triples": [
                "<Hal Patterson; college basketball player; University of Kansas>",
                "<Center for the Study of Science Fiction; association; University of Kansas>",
                "<Center for the Study of Science Fiction; location; Lawrence, KS>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Center for the Study of Science Fiction; founder; James Gunn>", 
                "C. <Center for the Study of Science Fiction; creation date; 1968>", 
                "D. <Hal Patterson; professional football league; Canadian Football League>",
                "E. <Hal Patterson; member of; Canadian Football Hall of Fame>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who was president when the state where Glick-Sower House is located became a state?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Glick\u2013Sower House; year built; 1859>", 
                "C. <Glick\u2013Sower House; built for; Dr. George Glick>", 
                "D. <Glick\u2013Sower House; listed year; 1993>",
                "E. <Glick\u2013Sower House; location; Marshalltown, Iowa>", 
            ],
            "answer": "E", 
        },
        {
            "question": "Who was president when the state where Glick-Sower House is located became a state?", 
            "triples": [
                "<Glick\u2013Sower House; location; Marshalltown, Iowa>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Iowa; signed into law by; President James K. Polk>", 
                "C. <Iowa; date of statehood; December 28, 1846>", 
                "D. <Glick\u2013Sower House; year built; 1859>",
                "E. <Iowa; order of statehood; 29th>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who was president when the state where Glick-Sower House is located became a state?", 
            "triples": [
                "<Glick\u2013Sower House; location; Marshalltown, Iowa>",
                "<Iowa; signed into law by; President James K. Polk>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Iowa; date of statehood; December 28, 1846>", 
                "C. <Iowa; order of statehood; 29th>", 
                "D. <Glick\u2013Sower House; year built; 1859>",
                "E. <Glick\u2013Sower House; built for; Dr. George Glick>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who was in charge of the birthplace of The Birds and the Bees' performer?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Birds and the Bees (Jewel Akens song); international hit; 1965>", 
                "C. <The Birds and the Bees (Jewel Akens song); release year; 1964>", 
                "D. <The Birds and the Bees (Jewel Akens song); release type; single>",
                "E. <The Bee Gees; songwriting; wrote all of their own hits>", 
            ],
            "answer": "C", 
        },
        {
            "question": "Who was in charge of the birthplace of The Birds and the Bees' performer?", 
            "triples": [
                "<The Birds and the Bees (Jewel Akens song); release year; 1964>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Birds and the Bees (Jewel Akens song); release year; 1964>", 
                "C. <The Birds and the Bees (Jewel Akens song); release type; single>", 
                "D. <Jewel Akens; birthplace; Houston, Texas>",
                "E. <Jewel Akens; birthdate; September 12, 1933>", 
            ],
            "answer": "D", 
        },
        {
            "question": "Who was in charge of the birthplace of The Birds and the Bees' performer?", 
            "triples": [
                "<The Birds and the Bees (Jewel Akens song); release year; 1964>",
                "<Jewel Akens; birthplace; Houston, Texas>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Birds and the Bees (Jewel Akens song); release year; 1964>", 
                "C. <Jewel Akens; birthdate; September 12, 1933>", 
                "D. <Jewel Akens; death place; Inglewood, California>",
                "E. <Houston; notable event; electing Annise Parker as mayor in 2009>", 
            ],
            "answer": "E", 
        },
        {
            "question": "Who was in charge of the birthplace of The Birds and the Bees' performer?", 
            "triples": [
                "<The Birds and the Bees (Jewel Akens song); release year; 1964>",
                "<Jewel Akens; birthplace; Houston, Texas>",
                "<Houston; notable event; electing Annise Parker as mayor in 2009>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Birds and the Bees (Jewel Akens song); release year; 1964>", 
                "C. <Jewel Akens; birthdate; September 12, 1933>", 
                "D. <Jewel Akens; death place; Inglewood, California>",
                "E. <Houston; political reputation; often a contested area in statewide elections>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "When was Harry Hillel Wellington's employer created?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Harry H. Wellington; date of birth; August 13, 1926>", 
                "C. <Harry H. Wellington; position at Yale Law School; Dean>", 
                "D. <Harry H. Wellington; tenure at New York Law School; 1992-2000>",
                "E. <Harry H. Wellington; tenure at Yale Law School; 1975-1985>", 
            ],
            "answer": "C", 
        },
        {
            "question": "When was Harry Hillel Wellington's employer created?", 
            "triples": [
                "<Harry H. Wellington; position at Yale Law School; Dean>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Harry H. Wellington; tenure at Yale Law School; 1975-1985>", 
                "C. <Yale University; established; Yale Law School (1843)>", 
                "D. <Harry H. Wellington; tenure at New York Law School; 1992-2000>",
                "E. <Yale University; established; Yale Divinity School (1822)>", 
            ],
            "answer": "C", 
        },
        {
            "question": "When was Harry Hillel Wellington's employer created?", 
            "triples": [
                "<Harry H. Wellington; position at Yale Law School; Dean>",
                "<Yale University; established; Yale Law School (1843)>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Harry H. Wellington; tenure at Yale Law School; 1975-1985>", 
                "C. <Yale University; established; the Sheffield Scientific School (1847)>", 
                "D. <Yale University; established; Yale Graduate School of Arts and Sciences (1847)>",
                "E. <Yale University; established; Yale Divinity School (1822)>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who is the deputy prime minister of the place where After Sunset was filmed?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <After the Sunset; filming location; Bahamas>", 
                "C. <Prime Minister of India; deputy; Deputy Prime Minister of India>", 
                "D. <Prime Minister of the Bahamas; head of government; the head of government of the Bahamas>",
                "E. <Nazem Akkari; position; temporary Deputy Prime Minister>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who is the deputy prime minister of the place where After Sunset was filmed?", 
            "triples": [
                "<After the Sunset; filming location; Bahamas>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Prime Minister of the Bahamas; head of government; the head of government of the Bahamas>", 
                "C. <Prime Minister of the Bahamas; head of state; Elizabeth II, the Queen of the Bahamas>", 
                "D. <Prime Minister of the Bahamas; current holder; Hubert Minnis>",
                "E. <Prime Minister of the Bahamas; party leader; leader of the governing Free National Movement party (FNM)>", 
            ],
            "answer": "D", 
        },
        {
            "question": "Who is the deputy prime minister of the place where After Sunset was filmed?", 
            "triples": [
                "<After the Sunset; filming location; Bahamas>", 
                "<Prime Minister of the Bahamas; current holder; Hubert Minnis>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Prime Minister of the Bahamas; head of government; the head of government of the Bahamas>", 
                "C. <Prime Minister of the Bahamas; party leader; leader of the governing Free National Movement party (FNM)>", 
                "D. <Prime Minister of the Bahamas; head of state; Elizabeth II, the Queen of the Bahamas>",
                "E. <Prime Minister of the Bahamas; election; Bahamas general election of May 10, 2017>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "How long did the original broadcaster of the series which has the episode Adverse Events, reign in the 18-49 demographics in the Nielsen ratings?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Adverse Events; third episode of; the fifth season of \"House\">", 
                "C. <American Idol; Fox's 18-49 demographic victory; 8 straight years from 2004 to 2012>", 
                "D. <This Is Us; average viewership; 14.70>",
                "E. <List of Once Upon a Time episodes; 18 - 49 rating; 3.6 / 9>", 
            ],
            "answer": "B", 
        },
        {
            "question": "How long did the original broadcaster of the series which has the episode Adverse Events, reign in the 18-49 demographics in the Nielsen ratings?", 
            "triples": [
                "<Adverse Events; third episode of; the fifth season of \"House\">"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <House; premiere date; November 16, 2004>", 
                "C. <Adverse Events; guest star; Breckin Meyer>", 
                "D. <House; network; Fox>",
                "E. <90210 (season 1); premiere viewers; 4.65 million>", 
            ],
            "answer": "D", 
        },
        {
            "question": "How long did the original broadcaster of the series which has the episode Adverse Events, reign in the 18-49 demographics in the Nielsen ratings?", 
            "triples": [
                "<Adverse Events; third episode of; the fifth season of \"House\">", 
                "<House; network; Fox>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <American Idol; Fox's 18-49 demographic victory; 8 straight years from 2004 to 2012>", 
                "C. <House; premiere date; November 16, 2004>", 
                "D. <Adverse Events; air date; September 30, 2008>",
                "E. <American Idol; ranking; lost the leading position in both the total viewers number and the 18/49 demo, coming in second to NBC Sunday Night Football>", 
            ],
            "answer": "B", 
        },
        {
            "question": "How long did the original broadcaster of the series which has the episode Adverse Events, reign in the 18-49 demographics in the Nielsen ratings?", 
            "triples": [
                "<Adverse Events; third episode of; the fifth season of \"House\">", 
                "<House; network; Fox>",
                "<American Idol; Fox's 18-49 demographic victory; 8 straight years from 2004 to 2012>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <American Idol; impact on Fox; pushed Fox to become the number one U.S. TV network amongst adults 18\u201349>", 
                "C. <American Idol; viewership drop; 23% in total viewers and 30% in the 18/49 demo>", 
                "D. <American Idol; ranking; first time in eight years>",
                "E. <American Idol; season ten; the overall viewer number has increased this season>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who is the child of the director of The Man Who Haunted Himself?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Man Who Haunted Himself; director; Basil Dearden>", 
                "C. <The Man Who Haunted Himself; writer; Basil Dearden>", 
                "D. <The Man Who Haunted Himself; year of release; 1970>",
                "E. <The Haunting (1963 film); director; Robert Wise>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who is the child of the director of The Man Who Haunted Himself?", 
            "triples": [
                "<The Man Who Haunted Himself; director; Basil Dearden>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Man Who Haunted Himself; writer; Basil Dearden>", 
                "C. <James Dearden; parents; Melissa Stribling and Basil Dearden>", 
                "D. <The Man Who Haunted Himself; year of release; 1970>",
                "E. <The Man Who Haunted Himself; genre; psychological thriller>", 
            ],
            "answer": "C", 
        },
        {
            "question": "Who is the child of the director of The Man Who Haunted Himself?", 
            "triples": [
                "<The Man Who Haunted Himself; director; Basil Dearden>",
                "<James Dearden; parents; Melissa Stribling and Basil Dearden>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Man Who Haunted Himself; writer; Basil Dearden>", 
                "C. <James Dearden; profession; film director and screenwriter>", 
                "D. <James Dearden; year of birth; 1949>",
                "E. <James Dearden; nationality; English>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "when was the last time the team Corrie Artman played for won a superbowl?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Corrie Artman; teams played for; New York Giants, Boston Braves, Pittsburgh Pirates>", 
                "C. <Corrie Artman; sport; American football>", 
                "D. <New York Giants; Super Bowl wins; XXI (1986), XXV (1990), XLII (2007), XLVI (2011)>",
                "E. <Corrie Artman; position; offensive lineman>", 
            ],
            "answer": "B", 
        },
        {
            "question": "when was the last time the team Corrie Artman played for won a superbowl?", 
            "triples": [
                "<Corrie Artman; teams played for; New York Giants, Boston Braves, Pittsburgh Pirates>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <New York Giants; Super Bowl wins; XXI (1986), XXV (1990), XLII (2007), XLVI (2011)>", 
                "C. <New York Giants; teams with more championship appearances; Green Bay Packers (13), Chicago Bears (9)>", 
                "D. <New York Giants; NFL championship titles since the advent of the Super Bowl; 4>",
                "E. <New York Giants; NFL championship titles in the pre-Super Bowl era; 4>", 
            ],
            "answer": "B", 
        },
        {
            "question": "when was the last time the team Corrie Artman played for won a superbowl?", 
            "triples": [
                "<Corrie Artman; teams played for; New York Giants, Boston Braves, Pittsburgh Pirates>",
                "<New York Giants; Super Bowl wins; XXI (1986), XXV (1990), XLII (2007), XLVI (2011)>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <New York Giants; NFL championship titles in the pre-Super Bowl era; 4>", 
                "C. <New York Giants; Hall of Fame players; 28>", 
                "D. <New York Giants; championship appearances; 19>",
                "E. <New York Giants; NFL championship titles; 8>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "How many people from the ethnicity comprising the most immigrants at the start of the 20th century live in the country where Cilada.com is based?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Brazil; diversity; most multicultural and ethnically diverse nation due to over a century of mass immigration from around the world>", 
                "C. <Cilada.com; country of release; Brazil>", 
                "D. <New York City; largest immigrant group in 1900; Germans>",
                "E. <New York City; third largest immigrant group in 1900; Jews>", 
            ],
            "answer": "C", 
        },
        {
            "question": "How many people from the ethnicity comprising the most immigrants at the start of the 20th century live in the country where Cilada.com is based?", 
            "triples": [
                "<Cilada.com; country of release; Brazil>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Germans; number of people claiming German ancestry in Brazil; 5 million>", 
                "C. <Brazil; population; over 208 million people>", 
                "D. <Germans; second largest centre of German-descended people; Brazil>",
                "E. <New York City; largest immigrant group in 1900; Germans>", 
            ],
            "answer": "E", 
        },
        {
            "question": "How many people from the ethnicity comprising the most immigrants at the start of the 20th century live in the country where Cilada.com is based?", 
            "triples": [
                "<Cilada.com; country of release; Brazil>",
                "<New York City; largest immigrant group in 1900; Germans>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <New York City; Dominican American, Puerto Rican American, and South American populations; largest in the United States>", 
                "C. <New York City; second largest immigrant group in 1900; Irish>", 
                "D. <Germans; number of people claiming German ancestry in Brazil; 5 million>",
                "E. <Germans; second largest centre of German-descended people; Brazil>", 
            ],
            "answer": "D", 
        },
        {
            "question": "How many people from the ethnicity comprising the most immigrants at the start of the 20th century live in the country where Cilada.com is based?", 
            "triples": [
                "<Cilada.com; country of release; Brazil>",
                "<New York City; largest immigrant group in 1900; Germans>",
                "<Germans; number of people claiming German ancestry in Brazil; 5 million>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <New York City; third largest immigrant group in 1900; Jews>", 
                "C. <Germans; second largest centre of German-descended people; Brazil>", 
                "D. <New York City; proportion of German immigrants in the city's population; 25%>",
                "E. <Germans; largest centre of German-descended people outside Germany; United States>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who was in charge of the city where the performer of Boss Life was born?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Boss Life (album); artist; American rapper Slim Thug>", 
                "C. <Boss Life (album); release date; November 19, 2013>", 
                "D. <Judge Da Boss; birthplace; Phoenix, Arizona>",
                "E. <Boss Life (album); type; album>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who was in charge of the city where the performer of Boss Life was born?", 
            "triples": [
                "<Boss Life (album); artist; American rapper Slim Thug>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Tha Thug Show; artist; Houston recording artist Slim Thug>", 
                "C. <Boss Life (album); release date; November 19, 2013>", 
                "D. <Houston; political reputation; most politically diverse city in Texas>",
                "E. <Judge Da Boss; record label; Louder Than Life/Sony Records>", 
            ],
            "answer": "B", 
        },
        {
            "question": "Who was in charge of the city where the performer of Boss Life was born?", 
            "triples": [
                "<Boss Life (album); artist; American rapper Slim Thug>",
                "<Tha Thug Show; artist; Houston recording artist Slim Thug>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Boss Life (album); release date; November 19, 2013>", 
                "C. <Tha Thug Show; label; Boss Hogg Outlawz>", 
                "D. <Houston; political reputation; most politically diverse city in Texas>",
                "E. <Houston; notable event; electing Annise Parker as mayor in 2009>", 
            ],
            "answer": "E", 
        },
        {
            "question": "Who was in charge of the city where the performer of Boss Life was born?", 
            "triples": [
                "<Boss Life (album); artist; American rapper Slim Thug>",
                "<Tha Thug Show; artist; Houston recording artist Slim Thug>",
                "<Houston; notable event; electing Annise Parker as mayor in 2009>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Houston; milestone; first U.S. city with a population over 1 million to elect a gay mayor>", 
                "C. <Boss Life (album); release date; November 19, 2013>", 
                "D. <Houston; political reputation; most politically diverse city in Texas>",
                "E. <Tha Thug Show; label; Boss Hogg Outlawz>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "What's the record label owned by the performer of Things That U Do?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Things That U Do; featured artist; Mariah Carey>", 
                "C. <Things That U Do; producer; Swizz Beatz>", 
                "D. <Things That U Do; origin; rapper Jay-Z's 1999 album \"Vol. 3... Life and Times of S. Carter\">",
                "E. <Things That U Do; description; overblown production>", 
            ],
            "answer": "D", 
        },
        {
            "question": "What's the record label owned by the performer of Things That U Do?", 
            "triples": [
                "<Things That U Do; origin; rapper Jay-Z's 1999 album \"Vol. 3... Life and Times of S. Carter\">"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Christi\u00f3n; record label; Jay-Z's Roc-A-Fella Records>", 
                "C. <Things That U Do; producer; Swizz Beatz>", 
                "D. <Things That U Do; featured artist; Mariah Carey>",
                "E. <Things That U Do; description; commercially aimed song>", 
            ],
            "answer": "B", 
        },
        {
            "question": "What's the record label owned by the performer of Things That U Do?", 
            "triples": [
                "<Things That U Do; origin; rapper Jay-Z's 1999 album \"Vol. 3... Life and Times of S. Carter\">",
                "<Christi\u00f3n; record label; Jay-Z's Roc-A-Fella Records>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Things That U Do; producer; Swizz Beatz>", 
                "C. <Things That U Do; featured artist; Mariah Carey>", 
                "D. <Things That U Do; type; single>",
                "E. <Things That U Do; description; commercially aimed song>", 
            ],
            "answer": "A", 
        },
    ],
    [
        {
            "question": "Who is the mother of the person under whom the entity from which Satyricon originated reached its greatest extent?", 
            "triples": [], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Roman Empire; person who reached the greatest extent of the empire; Trajan>", 
                "C. <Roman Empire; line of emperors; Five Good Emperors>", 
                "D. <W. C. Firebaugh; subject of \"Satyricon\"; low life under the Roman Empire>",
                "E. <Roman Empire; person who succeeded Vespasian; Titus>", 
            ],
            "answer": "D", 
        },
        {
            "question": "Who is the mother of the person under whom the entity from which Satyricon originated reached its greatest extent?", 
            "triples": [
                "<W. C. Firebaugh; subject of \"Satyricon\"; low life under the Roman Empire>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <W. C. Firebaugh; original author of \"Satyricon\"; Petronius>", 
                "C. <Roman Empire; person who reached the greatest extent of the empire; Trajan>", 
                "D. <Roman Empire; event that increased the size of the empire; Octavian's victory>",
                "E. <Roman Empire; line of emperors; Five Good Emperors>", 
            ],
            "answer": "C", 
        },
        {
            "question": "Who is the mother of the person under whom the entity from which Satyricon originated reached its greatest extent?", 
            "triples": [
                "<W. C. Firebaugh; subject of \"Satyricon\"; low life under the Roman Empire>", 
                "<Roman Empire; person who reached the greatest extent of the empire; Trajan>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <W. C. Firebaugh; original author of \"Satyricon\"; Petronius>", 
                "C. <Trajan; origin; hailed on his mother's side from the Gens Marcia, of an Italic family of Sabine origin>", 
                "D. <Roman Empire; event that increased the size of the empire; Octavian's victory>",
                "E. <Roman Empire; line of emperors; Five Good Emperors>", 
            ],
            "answer": "C", 
        },
        {
            "question": "Who is the mother of the person under whom the entity from which Satyricon originated reached its greatest extent?", 
            "triples": [
                "<W. C. Firebaugh; subject of \"Satyricon\"; low life under the Roman Empire>", 
                "<Roman Empire; person who reached the greatest extent of the empire; Trajan>",
                "<Trajan; origin; hailed on his mother's side from the Gens Marcia, of an Italic family of Sabine origin>"
            ], 
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Trajan; birthplace; Roman province of Hispania Baetica (in what is now Andalusia in modern Spain)>", 
                "C. <W. C. Firebaugh; original author of \"Satyricon\"; Petronius>", 
                "D. <Roman Empire; person who succeeded Titus; Domitian>",
                "E. <Roman Empire; person who succeeded Vespasian; Titus>", 
            ],
            "answer": "A", 
        },
    ],
]

reasoning_chains_musique_examplars = [
    {
        "question": "Who was the premier of the country that invaded the country that produced The Guard Post?", 
        "chains": "<The Guard Post; type; 2008 Korean horror film>, <The Korean War; cause; North Korea invaded South Korea following a series of clashes along the border>, <North Korea; head of government; Premier Pak Pong-ju>", 
    },
    {
        "question": "Who created the borders of countries on the continent where Legend of the Lost was filmed?", 
        "chains": "<Legend of the Lost; location work; Rome and Libya>, <Libya; location; Maghreb region in North Africa>, <Africa; outcome of European occupation; creation of many colonial territories>", 
    },
    {
        "question": "How many theater companies are in residence in the city where Askville's owner is headquartered?", 
        "chains": "<Askville; founder; Amazon.com>, <AmazonFresh; location; Seattle, Washington>, <Seattle; number of theatrical production companies; around 100>", 
    },
    {
        "question": "Which county shares a border with the county in which Wayne is located?", 
        "chains": "<Wayne, Washington County, Wisconsin; location; in Washington County, Wisconsin, United States>, <Colgate, Wisconsin; location; in Washington County, Wisconsin, United States, straddling the county line with Waukesha County>", 
    },
    {
        "question": "Who is the spouse of the person who made The Circe Invidiosa?", 
        "chains": "<Circe Invidiosa; artist; John William Waterhouse>, <Esther Kenworthy Waterhouse; marriage; John William Waterhouse>", 
    },
    {
        "question": "When did the home country of Privilege's performer gain independence from England?", 
        "chains": "<Privilege (Ivor Cutler album); artist; Ivor Cutler>, <IVOR CUTLER; co-producers; Vanishing Point and National Theatre of Scotland>, <History of Scotland; event; The Declaration of Arbroath helped convince Pope John XXII to overturn the earlier excommunication and nullify the various acts of submission by Scottish kings to English ones>, <History of Scotland; event; The Declaration of Arbroath helped Scotland's sovereignty be recognised by the major European dynasties>", 
    },
    {
        "question": "What is the population of the city where the cast member of The Adventures of Rex and Rinty lived when he died?", 
        "chains": "<The Adventures of Rex and Rinty; starring; Rex and Rin Tin Tin, Jr.>, <Rin Tin Tin; location; Los Angeles>, <Southern California; population of Los Angeles; 3,792,621>", 
    },
    {
        "question": "What is the capital of the county that contains the city where Adam Blackstone was born?", 
        "chains": "<Adam Blackstone; birthplace; Trenton, NJ>, <15th Legislative District (New Jersey); municipalities in Mercer County; Ewing Township, Hopewell Borough, Hopewell Township, Lawrence Township, Pennington Borough, Trenton City, West Windsor Township>, <WAEY; service area; Princeton and Mercer County, West Virginia>", 
    },
    {
        "question": "What city holds the university where Hal Patterson was educated?", 
        "chains": "<Hal Patterson; college basketball player; University of Kansas>, <Center for the Study of Science Fiction; association; University of Kansas>, <Center for the Study of Science Fiction; location; Lawrence, KS>", 
    },
    {
        "question": "Who was president when the state where Glick-Sower House is located became a state?", 
        "chains": "<Glick\u2013Sower House; location; Marshalltown, Iowa>, <Iowa; signed into law by; President James K. Polk>", 
    },
    {
        "question": "Who was in charge of the birthplace of The Birds and the Bees' performer?", 
        "chains": "<The Birds and the Bees (Jewel Akens song); release year; 1964>, <Jewel Akens; birthplace; Houston, Texas>, <Houston; notable event; electing Annise Parker as mayor in 2009>", 
    },
    {
        "question": "When was Harry Hillel Wellington's employer created?", 
        "chains": "<Harry H. Wellington; position at Yale Law School; Dean>, <Yale University; established; Yale Law School (1843)>", 
    },
    {
        "question": "Who is the deputy prime minister of the place where After Sunset was filmed?", 
        "chains": "<After the Sunset; filming location; Bahamas>, <Prime Minister of the Bahamas; current holder; Hubert Minnis>", 
    },
    {
        "question": "How long did the original broadcaster of the series which has the episode Adverse Events, reign in the 18-49 demographics in the Nielsen ratings?", 
        "chains": "<Adverse Events; third episode of; the fifth season of \"House\">; <House; network; Fox>; <American Idol; Fox's 18-49 demographic victory; 8 straight years from 2004 to 2012>", 
    },
    {
        "question": "Who is the child of the director of The Man Who Haunted Himself?", 
        "chains": "<The Man Who Haunted Himself; director; Basil Dearden>, <James Dearden; parents; Melissa Stribling and Basil Dearden>", 
    },
    {
        "question": "when was the last time the team Corrie Artman played for won a superbowl?", 
        "chains": "<Corrie Artman; teams played for; New York Giants, Boston Braves, Pittsburgh Pirates>, <New York Giants; Super Bowl wins; XXI (1986), XXV (1990), XLII (2007), XLVI (2011)>", 
    },
    {
        "question": "How many people from the ethnicity comprising the most immigrants at the start of the 20th century live in the country where Cilada.com is based?", 
        "chains": "<Cilada.com; country of release; Brazil>, <New York City; largest immigrant group in 1900; Germans>, <Germans; number of people claiming German ancestry in Brazil; 5 million>", 
    },
    {
        "question": "Who was in charge of the city where the performer of Boss Life was born?", 
        "chains": "<Boss Life (album); artist; American rapper Slim Thug>, <Tha Thug Show; artist; Houston recording artist Slim Thug>, <Houston; notable event; electing Annise Parker as mayor in 2009>", 
    },
    {
        "question": "What's the record label owned by the performer of Things That U Do?", 
        "chains": "<Things That U Do; origin; rapper Jay-Z's 1999 album \"Vol. 3... Life and Times of S. Carter\">, <Christi\u00f3n; record label; Jay-Z's Roc-A-Fella Records>", 
    },
    {
        "question": "Who is the mother of the person under whom the entity from which Satyricon originated reached its greatest extent?", 
        "chains": "<W. C. Firebaugh; subject of \"Satyricon\"; low life under the Roman Empire>, <Roman Empire; person who reached the greatest extent of the empire; Trajan>, <Trajan; origin; hailed on his mother's side from the Gens Marcia, of an Italic family of Sabine origin>", 
    },
]
