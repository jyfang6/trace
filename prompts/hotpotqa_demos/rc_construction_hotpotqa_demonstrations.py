

generate_reasoning_chains_hotpotqa_examplars = [
    [
        {
            "question": "Who distributed a movie whose cast includes an actor who acted in \"Him\"?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Fionn Whitehead; notable work; \"Him\" (2016 ITV miniseries)>",
                "C. <Dunkirk (2017 film); cast; Fionn Whitehead, Tom Glynn-Carney, Jack Lowden, Harry Styles, Aneurin Barnard, James D'Arcy, Barry Keoghan, Kenneth Branagh, Cillian Murphy, Mark Rylance, Tom Hardy>",
                "D. <Fionn Whitehead; occupation; actor>",
                "E. <Fionn Whitehead; notable work; \"Dunkirk\" (2017)>",
            ],
            "answer": "B"
        },
        {
            "question": "Who distributed a movie whose cast includes an actor who acted in \"Him\"?",
            "triples": [
                "<Fionn Whitehead; notable work; \"Him\" (2016 ITV miniseries)>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Dunkirk (2017 film); cast; Fionn Whitehead, Tom Glynn-Carney, Jack Lowden, Harry Styles, Aneurin Barnard, James D'Arcy, Barry Keoghan, Kenneth Branagh, Cillian Murphy, Mark Rylance, Tom Hardy>",
                "C. <Fionn Whitehead; notable work; \"Dunkirk\" (2017)>",
                "D. <Fionn Whitehead; first major role; protagonist in \"Dunkirk\" (2017)>",
                "E. <Dunkirk (2017 film); distributor; Warner Bros. Pictures>",
            ],
            "answer": "B"
        },
        {
            "question": "Who distributed a movie whose cast includes an actor who acted in \"Him\"?",
            "triples": [
                "<Fionn Whitehead; notable work; \"Him\" (2016 ITV miniseries)>",
                "<Dunkirk (2017 film); cast; Fionn Whitehead, Tom Glynn-Carney, Jack Lowden, Harry Styles, Aneurin Barnard, James D'Arcy, Barry Keoghan, Kenneth Branagh, Cillian Murphy, Mark Rylance, Tom Hardy>",
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Fionn Whitehead; notable work; \"Dunkirk\" (2017)>",
                "C. <Fionn Whitehead; first major role; protagonist in \"Dunkirk\" (2017)>",
                "D. <Dunkirk (2017 film); director; Christopher Nolan>",
                "E. <Dunkirk (2017 film); distributor; Warner Bros. Pictures>",
            ],
            "answer": "E"
        },
        {
            "question": "Who distributed a movie whose cast includes an actor who acted in \"Him\"?",
            "triples": [
                "<Fionn Whitehead; notable work; \"Him\" (2016 ITV miniseries)>",
                "<Dunkirk (2017 film); cast; Fionn Whitehead, Tom Glynn-Carney, Jack Lowden, Harry Styles, Aneurin Barnard, James D'Arcy, Barry Keoghan, Kenneth Branagh, Cillian Murphy, Mark Rylance, Tom Hardy>",
                "<Dunkirk (2017 film); distributor; Warner Bros. Pictures>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Fionn Whitehead; notable work; \"Dunkirk\" (2017)>",
                "C. <Fionn Whitehead; first major role; protagonist in \"Dunkirk\" (2017)>",
                "D. <Fionn Whitehead; occupation; actor>",
                "E. <Dunkirk (2017 film); director; Christopher Nolan>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Which magazine published papers more often; The Wittenburg Door or Sports Collectors Digest?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Sports Collectors Digest; purpose; provides an avenue through which sellers, traders and avid buyers of sports memorabilia may interact>",
                "C. <The Wittenburg Door; type; Christian satire and humor magazine>",
                "D. <Mike Yaconelli; role in The Wittenburg Door; satirical magazine>",
                "E. <Sports Collectors Digest; type; American advertising weekly paper>",
            ],
            "answer": "E"
        },
        {
            "question": "Which magazine published papers more often; The Wittenburg Door or Sports Collectors Digest?",
            "triples": [
                "<Sports Collectors Digest; type; American advertising weekly paper>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <The Wittenburg Door; type; Christian satire and humor magazine>",
                "C. <Mike Yaconelli; role in The Wittenburg Door; satirical magazine>",
                "D. <The Wittenburg Door; publication frequency; bimonthly>",
                "E. <The Wittenburg Door; start year of publication; 1971>",
            ],
            "answer": "D"
        },
        {
            "question": "Which magazine published papers more often; The Wittenburg Door or Sports Collectors Digest?",
            "triples": [
                "<Sports Collectors Digest; type; American advertising weekly paper>",
                "<The Wittenburg Door; publication frequency; bimonthly>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Sports Collectors Digest; purpose; provides an avenue through which sellers, traders and avid buyers of sports memorabilia may interact>",
                "C. <The Wittenburg Door; type; Christian satire and humor magazine>",
                "D. <Mike Yaconelli; role in The Wittenburg Door; satirical magazine>",
                "E. <The Wittenburg Door; reference to; the door of the All Saints' Church in Wittenberg>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Where is the headquarters of the company that produces the soft drink that the ICP traditionally sprays the audience with ?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Faygo; parent company; National Beverage Corporation>",
                "C. <FTFO; album art; alludes to ICP tradition of spraying audience with Faygo>",
                "D. <Faygo; type; soft drink company>",
                "E. <Jones Soda; type of soft drink; carbonated soft drink>",
            ],
            "answer": "C"
        },
        {
            "question": "Where is the headquarters of the company that produces the soft drink that the ICP traditionally sprays the audience with ?",
            "triples": [
                "<FTFO; album art; alludes to ICP tradition of spraying audience with Faygo>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <FTFO; record label; Psychopathic Records>",
                "C. <Faygo; parent company; National Beverage Corporation>",
                "D. <Faygo; location; Detroit, Michigan>",
                "E. <Faygo; type; soft drink company>",
            ],
            "answer": "E"
        },
        {
            "question": "Where is the headquarters of the company that produces the soft drink that the ICP traditionally sprays the audience with ?",
            "triples": [
                "<FTFO; album art; alludes to ICP tradition of spraying audience with Faygo>",
                "<Faygo; type; soft drink company>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <FTFO; record label; Psychopathic Records>",
                "C. <Faygo; parent company; National Beverage Corporation>",
                "D. <Faygo; location; Detroit, Michigan>",
                "E. <FTFO; artist; Shaggy 2 Dope>",
            ],
            "answer": "D"
        },
        {
            "question": "Where is the headquarters of the company that produces the soft drink that the ICP traditionally sprays the audience with ?",
            "triples": [
                "<FTFO; album art; alludes to ICP tradition of spraying audience with Faygo>",
                "<Faygo; type; soft drink company>",
                "<Faygo; location; Detroit, Michigan>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <FTFO; record label; Psychopathic Records>",
                "C. <Faygo; parent company; National Beverage Corporation>",
                "D. <Faygo; distribution regions; Midwest, Mid-Atlantic, and Central Southern regions of the United States, southern Canada>",
                "E. <Faygo; original name; Feigenson Brothers Bottling Works>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "What  are three alternate names of the University where W.G. Godfrey received his BA and MA degrees?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <W. G. Godfrey; education; BA and MA from the University of Waterloo, Ph.D. from Queen's University>",
                "C. <W. G. Godfrey; academic position; department chair at Mount Allison University>",
                "D. <W. G. Godfrey; academic title; Professor Emeritus at Mount Allison University, granted in 2007>",
                "E. <W. G. Godfrey; occupation; historian>",
            ],
            "answer": "B"
        },
        {
            "question": "What  are three alternate names of the University where W.G. Godfrey received his BA and MA degrees?",
            "triples": [
                "<W. G. Godfrey; education; BA and MA from the University of Waterloo, Ph.D. from Queen's University>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <University of Waterloo; type; public research university>",
                "C. <University of Waterloo; location; Waterloo, Ontario>",
                "D. <University of Waterloo; academic programs; administered by six faculties and ten faculty-based schools>",
                "E. <W. G. Godfrey; academic position; department chair at Mount Allison University>",
            ],
            "answer": "B"
        },
        {
            "question": "What  are three alternate names of the University where W.G. Godfrey received his BA and MA degrees?",
            "triples": [
                "<W. G. Godfrey; education; BA and MA from the University of Waterloo, Ph.D. from Queen's University>",
                "<University of Waterloo; type; public research university>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <University of Waterloo; academic programs; administered by six faculties and ten faculty-based schools>",
                "C. <University of Waterloo; location; Waterloo, Ontario>",
                "D. <W. G. Godfrey; academic position; department chair at Mount Allison University>",
                "E. <University of Waterloo; membership; U15, a group of research-intensive universities in Canada>",
            ],
            "answer": "B"
        },
        {
            "question": "What  are three alternate names of the University where W.G. Godfrey received his BA and MA degrees?",
            "triples": [
                "<W. G. Godfrey; education; BA and MA from the University of Waterloo, Ph.D. from Queen's University>",
                "<University of Waterloo; type; public research university>",
                "<University of Waterloo; academic programs; administered by six faculties and ten faculty-based schools>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <W. G. Godfrey; academic position; department chair at Mount Allison University>",
                "C. <University of Waterloo; co-op program; largest post-secondary co-op program of its kind in the world>",
                "D. <University of Waterloo; affiliated university colleges; four>",
                "E. <University of Waterloo; notable feature; cooperative education (co-op) programs>",
            ],
            "answer": "C"
        },
    ],
    [
        {
            "question": "Who has perofrmed in more bands, Paul Draper or Kevin Max?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Paul Draper (musician); role in Mansun; frontman>",
                "C. <Paul Draper (musician); former band; Mansun>",
                "D. <Paul Draper (musician); date of birth; 26 September 1970>",
                "E. <Paul Draper (musician); occupation; singer-songwriter, musician, record producer>",
            ],
            "answer": "C"
        },
        {
            "question": "Who has perofrmed in more bands, Paul Draper or Kevin Max?",
            "triples": [
                "<Paul Draper (musician); former band; Mansun>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Paul Draper (musician); role in Mansun; frontman>",
                "C. <Kevin Max; lead singer of the band; Audio Adrenaline>",
                "D. <Kevin Max; group he was a member of; DC Talk>",
                "E. <Slipping Away (Mansun song); writer of the song; Paul Draper>",
            ],
            "answer": "C"
        },
        {
            "question": "Who has perofrmed in more bands, Paul Draper or Kevin Max?",
            "triples": [
                "<Paul Draper (musician); former band; Mansun>",
                "<Kevin Max; lead singer of the band; Audio Adrenaline>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Paul Draper (musician); role in Mansun; frontman>",
                "C. <Slipping Away (Mansun song); writer of the song; Paul Draper>",
                "D. <Paul Draper (musician); occupation; singer-songwriter, musician, record producer>",
                "E. <Kevin Max; group he was a member of; DC Talk>",
            ],
            "answer": "E"
        },
        {
            "question": "Who has perofrmed in more bands, Paul Draper or Kevin Max?",
            "triples": [
                "<Paul Draper (musician); former band; Mansun>",
                "<Kevin Max; lead singer of the band; Audio Adrenaline>",
                "<Kevin Max; group he was a member of; DC Talk>",
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Paul Draper (musician); role in Mansun; frontman>",
                "C. <Slipping Away (Mansun song); writer of the song; Paul Draper>",
                "D. <Six (Mansun song); writer of the song; Paul Draper>",
                "E. <Kevin Max; duration as lead singer of Audio Adrenaline; 2012-2014>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Which state did this male American academic and politician serve as a senator under whom Natalie Ravitz was a prominent staffer?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Natalie Ravitz; previous role; staffer for United States Senators Barbara Boxer and Paul Wellstone>",
                "C. <Natalie Ravitz; previous occupation; Rupert Murdoch\u2019s Chief of Staff at 21st Century Fox and News Corp>",
                "D. <Natalie Ravitz; previous occupation; Communications Director for the New York City Department of Education>",
                "E. <Elizabeth Warren; position; senior United States Senator from Massachusetts>",
            ],
            "answer": "B"
        },
        {
            "question": "Which state did this male American academic and politician serve as a senator under whom Natalie Ravitz was a prominent staffer?",
            "triples": [
                "<Natalie Ravitz; previous role; staffer for United States Senators Barbara Boxer and Paul Wellstone>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Paul Wellstone; represented; Minnesota in the United States Senate>",
                "C. <Paul Wellstone; occupation; academic and politician>",
                "D. <Paul Wellstone; nationality; American>",
                "E. <Paul Wellstone; party affiliation; Democratic Farmer-Labor Party>",
            ],
            "answer": "C"
        },
        {
            "question": "Which state did this male American academic and politician serve as a senator under whom Natalie Ravitz was a prominent staffer?",
            "triples": [
                "<Natalie Ravitz; previous role; staffer for United States Senators Barbara Boxer and Paul Wellstone>",
                "<Paul Wellstone; occupation; academic and politician>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Paul Wellstone; represented; Minnesota in the United States Senate>",
                "C. <Paul Wellstone; nationality; American>",
                "D. <Paul Wellstone; party affiliation; Democratic Farmer-Labor Party>",
                "E. <Paul Wellstone; role in the Democratic Party; leader of the progressive wing>",
            ],
            "answer": "B"
        },
        {
            "question": "Which state did this male American academic and politician serve as a senator under whom Natalie Ravitz was a prominent staffer?",
            "triples": [
                "<Natalie Ravitz; previous role; staffer for United States Senators Barbara Boxer and Paul Wellstone>",
                "<Paul Wellstone; occupation; academic and politician>",
                "<Paul Wellstone; represented; Minnesota in the United States Senate>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Paul Wellstone; party affiliation; Democratic Farmer-Labor Party>",
                "C. <Paul Wellstone; nationality; American>",
                "D. <Paul Wellstone; role in the Democratic Party; leader of the progressive wing>",
                "E. <Paul Wellstone; date of birth; July 21, 1944>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "A board of coaches representing what British producer of newsreels and documentaries, active from 1910 through 1970, named William Inwood Smith a first-team All-American in 1935?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Inwood Smith, selected as a first-team All-American by; Grantland Rice for \"Collier's Weekly\" and a board of coaches for Path\u00e9 News>",
                "C. <Inwood Smith; All-American football player for; Ohio State University Buckeyes>",
                "D. <Inwood Smith; sports; football, competitive swimmer, basketball player, track and field athlete>",
                "E. <Inwood Smith; full name; William Inwood Smith>",
            ],
            "answer": "B"
        },
        {
            "question": "A board of coaches representing what British producer of newsreels and documentaries, active from 1910 through 1970, named William Inwood Smith a first-team All-American in 1935?",
            "triples": [
                "<Inwood Smith, selected as a first-team All-American by; Grantland Rice for \"Collier's Weekly\" and a board of coaches for Path\u00e9 News>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Path\u00e9 News; type; producer of newsreels and documentaries>",
                "C. <Inwood Smith; All-American football player for; Ohio State University Buckeyes>",
                "D. <Inwood Smith; sports; football, competitive swimmer, basketball player, track and field athlete>",
                "E. <Path\u00e9 News; founder; Charles Path\u00e9>",
            ],
            "answer": "B"
        },
        {
            "question": "A board of coaches representing what British producer of newsreels and documentaries, active from 1910 through 1970, named William Inwood Smith a first-team All-American in 1935?",
            "triples": [
                "<Inwood Smith, selected as a first-team All-American by; Grantland Rice for \"Collier's Weekly\" and a board of coaches for Path\u00e9 News>",
                "<Path\u00e9 News; type; producer of newsreels and documentaries>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Inwood Smith; All-American football player for; Ohio State University Buckeyes>",
                "C. <Inwood Smith; sports; football, competitive swimmer, basketball player, track and field athlete>",
                "D. <Path\u00e9 News; founder; Charles Path\u00e9>",
                "E. <Path\u00e9 News; duration of operation; 1910-1970>",
            ],
            "answer": "E"
        },
        {
            "question": "A board of coaches representing what British producer of newsreels and documentaries, active from 1910 through 1970, named William Inwood Smith a first-team All-American in 1935?",
            "triples": [
                "<Inwood Smith, selected as a first-team All-American by; Grantland Rice for \"Collier's Weekly\" and a board of coaches for Path\u00e9 News>",
                "<Path\u00e9 News; type; producer of newsreels and documentaries>",
                "<Path\u00e9 News; duration of operation; 1910-1970>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Inwood Smith; All-American football player for; Ohio State University Buckeyes>",
                "C. <Inwood Smith; sports; football, competitive swimmer, basketball player, track and field athlete>",
                "D. <Path\u00e9 News; founder; Charles Path\u00e9>",
                "E. <Path\u00e9 News; legacy; British Path\u00e9>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "What was the occupation of both Marguerite Radclyffe Hall and Charles Bukowski?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Charles Bukowski; occupation; poet, novelist, short story writer>",
                "C. <Radclyffe Hall; full name; Marguerite Radclyffe Hall>",
                "D. <Radclyffe Hall; occupation; poet and author>",
                "E. <Charles Bukowski; occupation; poet>",
            ],
            "answer": "B"
        },
        {
            "question": "What was the occupation of both Marguerite Radclyffe Hall and Charles Bukowski?",
            "triples": [
                "<Charles Bukowski; occupation; poet, novelist, short story writer>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Radclyffe Hall; full name; Marguerite Radclyffe Hall>",
                "C. <Radclyffe Hall; occupation; poet and author>",
                "D. <Charles Bukowski; occupation; poet>",
                "E. <Radclyffe Hall; nationality; English>",
            ],
            "answer": "C"
        },
        {
            "question": "What was the occupation of both Marguerite Radclyffe Hall and Charles Bukowski?",
            "triples": [
                "<Charles Bukowski; occupation; poet, novelist, short story writer>",
                "<Radclyffe Hall; occupation; poet and author>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Radclyffe Hall; full name; Marguerite Radclyffe Hall>",
                "C. <Radclyffe Hall; notable work; The Well of Loneliness>",
                "D. <Charles Bukowski; occupation; poet>",
                "E. <Radclyffe Hall; nationality; English>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Which genus of plant life is more palm like, Pandanus or Eriogonum?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Pandanus; physical characteristics; palm-like, dioecious trees and shrubs>",
                "C. <Eriogonum; scientific name; genus of flowering plants in the family Polygonaceae>",
                "D. <Pandanus; classification; order Pandanales, family Pandanaceae>",
                "E. <Pandanus; common names; pandan, screw palm, screw pine>",
            ],
            "answer": "B"
        },
        {
            "question": "Which genus of plant life is more palm like, Pandanus or Eriogonum?",
            "triples": [
                "<Pandanus; physical characteristics; palm-like, dioecious trees and shrubs>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Eriogonum; scientific name; genus of flowering plants in the family Polygonaceae>",
                "C. <Pandanus; classification; order Pandanales, family Pandanaceae>",
                "D. <Pandanus; common names; pandan, screw palm, screw pine>",
                "E. <Pandanus; type; genus of monocots>",
            ],
            "answer": "B"
        },
        {
            "question": "Which genus of plant life is more palm like, Pandanus or Eriogonum?",
            "triples": [
                "<Pandanus; physical characteristics; palm-like, dioecious trees and shrubs>",
                "<Eriogonum; scientific name; genus of flowering plants in the family Polygonaceae>",
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Pandanus; classification; order Pandanales, family Pandanaceae>",
                "C. <Pandanus; common names; pandan, screw palm, screw pine>",
                "D. <Pandanus; type; genus of monocots>",
                "E. <Eriogonum inflatum; family; Polygonaceae>",
            ],
            "answer": "C"
        },
        {
            "question": "Which genus of plant life is more palm like, Pandanus or Eriogonum?",
            "triples": [
                "<Pandanus; physical characteristics; palm-like, dioecious trees and shrubs>",
                "<Eriogonum; scientific name; genus of flowering plants in the family Polygonaceae>",
                "<Pandanus; common names; pandan, screw palm, screw pine>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Pandanus; classification; order Pandanales, family Pandanaceae>",
                "C. <Pandanus; type; genus of monocots>",
                "D. <Eriogonum inflatum; family; Polygonaceae>",
                "E. <Eriogonum; includes; California buckwheat (\"Eriogonum fasciculatum\")>",
            ],
            "answer": "D"
        },
    ],
    [
        {
            "question": "Who is credited with composing the music for the song named in a famous Guatemalan lottery dedicated to help the deafblind?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Santa Lucia; year of composition; 1835>",
                "C. <Loter\u00eda Santa Luc\u00eda; purpose; to help the deafblind across the country>",
                "D. <Santa Lucia; type; traditional Neapolitan song>",
                "E. <Santa Lucia; composer; A. Longo (1835)>",
            ],
            "answer": "C"
        },
        {
            "question": "Who is credited with composing the music for the song named in a famous Guatemalan lottery dedicated to help the deafblind?",
            "triples": [
                "<Loter\u00eda Santa Luc\u00eda; purpose; to help the deafblind across the country>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Santa Lucia; year of composition; 1835>",
                "C. <Loter\u00eda Santa Luc\u00eda; location; Guatemala>",
                "D. <Santa Lucia; type; traditional Neapolitan song>",
                "E. <Santa Lucia; composer; A. Longo (1835)>",
            ],
            "answer": "E"
        },
        {
            "question": "Who is credited with composing the music for the song named in a famous Guatemalan lottery dedicated to help the deafblind?",
            "triples": [
                "<Loter\u00eda Santa Luc\u00eda; purpose; to help the deafblind across the country>",
                "<Santa Lucia; composer; A. Longo (1835)>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples",
                "B. <Santa Lucia; year of composition; 1835>",
                "C. <Loter\u00eda Santa Luc\u00eda; location; Guatemala>",
                "D. <Santa Lucia; type; traditional Neapolitan song>",
                "E. <Loter\u00eda Santa Luc\u00eda; type; lottery>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "What lake borders the city where the 308th Bombardment Wing was last stationed?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <375th Bombardment Squadron; last assignment; 308th Bombardment Wing>",
                "C. <308th Bombardment Wing (U.S. Army Air Forces); location; Nagoya, Japan>",
                "D. <736th Bombardment Squadron; last station; Columbus Air Force Base, Mississippi>",
                "E. <720th Bombardment Squadron; last station; Minot Air Force Base, North Dakota>",
            ],
            "answer": "B"
        },
        {
            "question": "What lake borders the city where the 308th Bombardment Wing was last stationed?",
            "triples": [
                "<375th Bombardment Squadron; last assignment; 308th Bombardment Wing>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <425th Bombardment Squadron; last assignment; 308th Bombardment Wing>",
                "C. <308th Bombardment Wing (U.S. Army Air Forces); last assignment; Far East Air Forces>",
                "D. <375th Bombardment Squadron; location; Plattsburgh Air Force Base, New York>",
                "E. <308th Bombardment Wing (U.S. Army Air Forces); location; Nagoya, Japan>",
            ],
            "answer": "D"
        },
        {
            "question": "What lake borders the city where the 308th Bombardment Wing was last stationed?",
            "triples": [
                "<375th Bombardment Squadron; last assignment; 308th Bombardment Wing>",
                "<375th Bombardment Squadron; location; Plattsburgh Air Force Base, New York>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Plattsburgh Air Force Base; location; city of Plattsburgh, New York>",
                "C. <375th Bombardment Squadron; location; Plattsburgh Air Force Base, New York>",
                "D. <425th Bombardment Squadron; location of last assignment; Plattsburgh Air Force Base, New York>",
                "E. <Plattsburgh Air Force Base; location; western shore of Lake Champlain opposite Burlington, Vermont>",
            ],
            "answer": "E"
        },
        {
            "question": "What lake borders the city where the 308th Bombardment Wing was last stationed?",
            "triples": [
                "<375th Bombardment Squadron; last assignment; 308th Bombardment Wing>",
                "<375th Bombardment Squadron; location; Plattsburgh Air Force Base, New York>",
                "<Plattsburgh Air Force Base; location; western shore of Lake Champlain opposite Burlington, Vermont>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Plattsburgh Air Force Base; location; city of Plattsburgh, New York>",
                "C. <425th Bombardment Squadron; location of last assignment; Plattsburgh Air Force Base, New York>",
                "D. <Plattsburgh Air Force Base; location; extreme northeast corner of New York>",
                "E. <Plattsburgh Air Force Base; location; 20 miles (32 km) south of the Canada–United States border>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Justin Shenkarow voices Harold Berman, a character from a television series that aired on what station?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Title: Justin Shenkarow; notable roles; Matthew Brock in \"Picket Fences\", Simon Holmes in \"Eerie, Indiana\", Harold Berman on \"Hey Arnold!\">",
                "C. <Title: Justin Shenkarow; occupation; actor, voice actor, producer, writer, director>",
                "D. <Hey Arnold!; network; Nickelodeon>",
                "E. <Hey Arnold!; type; American animated television series>",
            ],
            "answer": "B"
        },
        {
            "question": "Justin Shenkarow voices Harold Berman, a character from a television series that aired on what station?",
            "triples": [
                "<Title: Justin Shenkarow; notable roles; Matthew Brock in \"Picket Fences\", Simon Holmes in \"Eerie, Indiana\", Harold Berman on \"Hey Arnold!\">"  
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Hey Arnold!; type; American animated television series>",
                "C. <Hey Arnold!; air dates; October 7, 1996 to June 8, 2004>",
                "D. <Hey Arnold!; network; Nickelodeon>",
                "E. <Hey Arnold!; main character; Arnold>",
            ],
            "answer": "D"
        },
        {
            "question": "Justin Shenkarow voices Harold Berman, a character from a television series that aired on what station?",
            "triples": [
                "<Title: Justin Shenkarow; notable roles; Matthew Brock in \"Picket Fences\", Simon Holmes in \"Eerie, Indiana\", Harold Berman on \"Hey Arnold!\">",
                "<Hey Arnold!; network; Nickelodeon>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Hey Arnold!; air dates; October 7, 1996 to June 8, 2004>",
                "C. <Hey Arnold!; type; American animated television series>",
                "D. <Hey Arnold!; creator; Craig Bartlett>",
                "E. <Hey Arnold!; main character; Arnold>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "What is the 5th studio album released by the singer of \"A Girl's Gotta Do (What a Girl's Gotta Do)\"?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <A Girl's Gotta Do (What a Girl's Gotta Do); artist; American country music artist Mindy McCready>",
                "C. <A Girl's Gotta Do (What a Girl's Gotta Do); release date; February 1997>",
                "D. <Ten Thousand Angels; fourth single; \"A Girl's Gotta Do (What a Girl's Gotta Do)\">",
                "E. <A Girl's Gotta Do (What a Girl's Gotta Do); songwriters; Robert Byrne and Rick Bowles>",
            ],
            "answer": "B"
        },
        {
            "question": "What is the 5th studio album released by the singer of \"A Girl's Gotta Do (What a Girl's Gotta Do)\"?",
            "triples": [
                "<A Girl's Gotta Do (What a Girl's Gotta Do); artist; American country music artist Mindy McCready>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Mindy McCready; number of studio albums; five>",
                "C. <Mindy McCready; fourth album; self-titled>",
                "D. <Mindy McCready; debut album release year; 1996>",
                "E. <Mindy McCready; fifth album; I'm Still Here>",
            ],
            "answer": "E"
        },
        {
            "question": "What is the 5th studio album released by the singer of \"A Girl's Gotta Do (What a Girl's Gotta Do)\"?",
            "triples": [
                "<A Girl's Gotta Do (What a Girl's Gotta Do); artist; American country music artist Mindy McCready>",
                "<Mindy McCready; fifth album; I'm Still Here>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Mindy McCready; third album; I'm Not So Tough>",
                "C. <Mindy McCready; debut album release year; 1996>",
                "D. <Mindy McCready; fourth album; self-titled>",
                "E. <Mindy McCready; number of studio albums; five>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Which profession does Boris Barnet have in common with Baltasar Korm\u00e1kur?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Baltasar Korm\u00e1kur; recognition; best known for directing the films \"101 Reykjav\u00edk\", \"Hafi\u00f0\", \"A Little Trip to Heaven\", \"Contraband\", \"2 Guns\", and \"Everest\">",
                "C. <Baltasar Korm\u00e1kur; occupation; actor, theater and film director, film producer>",
                "D. <Boris Barnet; occupation; film director, actor, and screenwriter>",
                "E. <Baltasar Breki Samper; relation to director; son of Icelandic director Baltasar Korm\u00e1kur>",
            ],
            "answer": "C"
        },
        {
            "question": "Which profession does Boris Barnet have in common with Baltasar Korm\u00e1kur?",
            "triples": [
                "<Baltasar Korm\u00e1kur; occupation; actor, theater and film director, film producer>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Baltasar Korm\u00e1kur; recognition; best known for directing the films \"101 Reykjav\u00edk\", \"Hafi\u00f0\", \"A Little Trip to Heaven\", \"Contraband\", \"2 Guns\", and \"Everest\">",
                "C. <Boris Barnet; occupation; film director, actor, and screenwriter>",
                "D. <Boris Barnet; number of films directed; 27>",
                "E. <Boris Barnet; time period of film direction; 1927-1963>",
            ],
            "answer": "C"
        },
        {
            "question": "Which profession does Boris Barnet have in common with Baltasar Korm\u00e1kur?",
            "triples": [
                "<Baltasar Korm\u00e1kur; occupation; actor, theater and film director, film producer>",
                "<Boris Barnet; occupation; film director, actor, and screenwriter>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Baltasar Korm\u00e1kur; recognition; best known for directing the films \"101 Reykjav\u00edk\", \"Hafi\u00f0\", \"A Little Trip to Heaven\", \"Contraband\", \"2 Guns\", and \"Everest\">",
                "C. <Baltasar Breki Samper; relation to director; son of Icelandic director Baltasar Korm\u00e1kur>",
                "D. <Baltasar Korm\u00e1kur; family; father is the Spanish painter Baltasar Samper, son is actor Baltasar Breki Samper>",
                "E. <Boris Barnet; number of films directed; 27>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Who directed the movie containing the phrase inspiring the name of The Dismemberment Plan?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Dismemberment Plan; origin of the name; a stray phrase uttered by Ned Ryerson in the comedy \"Groundhog Day\">",
                "C. <The Dismemberment Plan; also known as; D-Plan, The Plan>",
                "D. <The Dismemberment Plan Is Terrified; band; The Dismemberment Plan>",
                "E. <A People's History of the Dismemberment Plan; artist; The Dismemberment Plan>",
            ],
            "answer": "B"
        },
        {
            "question": "Who directed the movie containing the phrase inspiring the name of The Dismemberment Plan?",
            "triples": [
                "<The Dismemberment Plan; origin of the name; a stray phrase uttered by Ned Ryerson in the comedy \"Groundhog Day\">"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Groundhog Day (film); starring; Bill Murray, Andie MacDowell, Chris Elliott>",
                "C. <Groundhog Day (film); story; based on a story by Danny Rubin>",
                "D. <Groundhog Day (film); genre; fantasy-comedy film>",
                "E. <Groundhog Day (film); director; Harold Ramis>",
            ],
            "answer": "E"
        },
        {
            "question": "Who directed the movie containing the phrase inspiring the name of The Dismemberment Plan?",
            "triples": [
                "<The Dismemberment Plan; origin of the name; a stray phrase uttered by Ned Ryerson in the comedy \"Groundhog Day\">",
                "<Groundhog Day (film); director; Harold Ramis>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <The Dismemberment Plan; also known as; D-Plan, The Plan>",
                "C. <Groundhog Day (film); story; based on a story by Danny Rubin>",
                "D. <Groundhog Day (film); starring; Bill Murray, Andie MacDowell, Chris Elliott>",
                "E. <Groundhog Day (film); genre; fantasy-comedy film>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Where was the rock band the star of \"Her Name is Nicole\" played alongside from?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Nicole Scherzinger; group she was a member of; the Pussycat Dolls>",
                "C. <Nicole Scherzinger; career path; pursued a musical career alongside the American rock band Days of the New and later auditioned for \"Popstars\" and became a member of the short-lived girl group Eden's Crush>",
                "D. <Nicole Scherzinger; role in the group; lead singer>",
                "E. <Days of the New; notable supporting musician; Nicole Scherzinger>",
            ],
            "answer": "C"
        },
        {
            "question": "Where was the rock band the star of \"Her Name is Nicole\" played alongside from?",
            "triples": [
                "<Nicole Scherzinger; career path; pursued a musical career alongside the American rock band Days of the New and later auditioned for \"Popstars\" and became a member of the short-lived girl group Eden's Crush>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Days of the New; notable supporting musician; Nicole Scherzinger>",
                "C. <Nicole Scherzinger; group she was a member of; the Pussycat Dolls>",
                "D. <Nicole Scherzinger; place of birth; Honolulu, Hawaii>",
                "E. <Days of the New; origin; Charlestown, Indiana>",
            ],
            "answer": "E"
        },
        {
            "question": "Where was the rock band the star of \"Her Name is Nicole\" played alongside from?",
            "triples": [
                "<Nicole Scherzinger; career path; pursued a musical career alongside the American rock band Days of the New and later auditioned for \"Popstars\" and became a member of the short-lived girl group Eden's Crush>",
                "<Days of the New; origin; Charlestown, Indiana>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Days of the New; notable supporting musician; Nicole Scherzinger>",
                "C. <Days of the New; formation year; 1995>",
                "D. <Nicole Scherzinger; place of upbringing; Louisville, Kentucky>",
                "E. <Nicole Scherzinger; group she was a member of; the Pussycat Dolls>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "Who does the goalkeeper play for which Ahmad Khormali's tracksuit bottoms resemble?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Ahmad Khormali; occupation; football goalkeeper>",
                "C. <Amir Abedzadeh; position; goalkeeper>",
                "D. <Ahmad Khormali; fashion style; wears pyjama-like tracksuit bottoms>",
                "E. <Ahmad Khormali; inspiration; Hungarian goalkeeper G\u00e1bor Kir\u00e1ly>",
            ],
            "answer": "D"
        },
        {
            "question": "Who does the goalkeeper play for which Ahmad Khormali's tracksuit bottoms resemble?",
            "triples": [
                "<Ahmad Khormali; fashion style; wears pyjama-like tracksuit bottoms>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Ahmad Khormali; occupation; football goalkeeper>",
                "C. <Amir Abedzadeh; position; goalkeeper>",
                "D. <Ahmad Khormali; inspiration; Hungarian goalkeeper G\u00e1bor Kir\u00e1ly>",
                "E. <Ahmad Ali Jaber; occupation; football goalkeeper>",
            ],
            "answer": "D"
        },
        {
            "question": "Who does the goalkeeper play for which Ahmad Khormali's tracksuit bottoms resemble?",
            "triples": [
                "<Ahmad Khormali; fashion style; wears pyjama-like tracksuit bottoms>",
                "<Ahmad Khormali; inspiration; Hungarian goalkeeper G\u00e1bor Kir\u00e1ly>",
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <G\u00e1bor Kir\u00e1ly; position; goalkeeper>",
                "C. <Ahmad Khormali; occupation; football goalkeeper>",
                "D. <Amir Abedzadeh; position; goalkeeper>",
                "E. <G\u00e1bor Kir\u00e1ly; occupation; professional footballer>",
            ],
            "answer": "B"
        },
        {
            "question": "Who does the goalkeeper play for which Ahmad Khormali's tracksuit bottoms resemble?",
            "triples": [
                "<Ahmad Khormali; fashion style; wears pyjama-like tracksuit bottoms>",
                "<Ahmad Khormali; inspiration; Hungarian goalkeeper G\u00e1bor Kir\u00e1ly>",
                "<G\u00e1bor Kir\u00e1ly; position; goalkeeper>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Ahmad Khormali; occupation; football goalkeeper>",
                "C. <Amir Abedzadeh; position; goalkeeper>",
                "D. <G\u00e1bor Kir\u00e1ly; occupation; professional footballer>",
                "E. <G\u00e1bor Kir\u00e1ly; current team; Szombathelyi Halad\u00e1s>",
            ],
            "answer": "E"
        },
    ],
    [
        {
            "question": "When was the actress who is performing a routine bugging operation in \"One Last Dance\" born?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <One Last Dance (2003 film); starring; Patrick Swayze, Lisa Niemi, George de la Pe\u00f1a>",
                "C. <One Last Dance (Spooks); type; episode of the first series of the British television series \"Spooks\">",
                "D. <One Last Dance (R5 song); artist; American pop rock band R5>",
                "E. <Keeley Hawes; occupation; actress>",
            ],
            "answer": "E"
        },
        {
            "question": "When was the actress who is performing a routine bugging operation in \"One Last Dance\" born?",
            "triples": [
                "<Keeley Hawes; occupation; actress>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <One Last Dance (Spooks); type; episode of the first series of the British television series \"Spooks\">",
                "C. <One Last Dance (Spooks); television network that aired the episode; BBC One>",
                "D. <Keeley Hawes; birthdate; 10 February 1976>",
                "E. <One Last Dance (Spooks); air date; 27 June 2002>",
            ],
            "answer": "D"
        },
        {
            "question": "When was the actress who is performing a routine bugging operation in \"One Last Dance\" born?",
            "triples": [
                "<Keeley Hawes; occupation; actress>",
                "<Keeley Hawes; birthdate; 10 February 1976>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <One Last Dance (Spooks); air date; 27 June 2002>",
                "C. <One Last Dance (Spooks); television network that aired the episode; BBC One>",
                "D. <One Last Dance (Spooks); viewership; over 7 million viewers in the UK>",
                "E. <One Last Dance (Spooks); plot; based on the Iranian Embassy Siege in 1980>",
            ],
            "answer": "A"
        },
    ],
    [
        {
            "question": "In which National Football League (NFL) team did a cast member of \"Do You Believe?\" play for?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Do You Believe? (film); starring; Ted McGinley, Mira Sorvino, Andrea Logan White, Lee Majors, Alexa PenaVega, Sean Astin, Madison Pettis, Cybill Shepherd, and Brian Bosworth>",
                "C. <Do You Believe? (film); genre; Christian ensemble drama film>",
                "D. <Marcus Jones (athlete); league he played in; National Football League (NFL)>",
                "E. <Brian Bosworth; league he played in; National Football League (NFL)>",
            ],
            "answer": "B"
        },
        {
            "question": "In which National Football League (NFL) team did a cast member of \"Do You Believe?\" play for?",
            "triples": [
                "<Do You Believe? (film); starring; Ted McGinley, Mira Sorvino, Andrea Logan White, Lee Majors, Alexa PenaVega, Sean Astin, Madison Pettis, Cybill Shepherd, and Brian Bosworth>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Brian Bosworth; occupation; former professional football player>",
                "C. <Brian Bosworth; league he played in; National Football League (NFL)>",
                "D. <Brian Bosworth; team he played for; Seattle Seahawks>",
                "E. <Do You Believe? (film); genre; Christian ensemble drama film>",
            ],
            "answer": "D"
        },
        {
            "question": "In which National Football League (NFL) team did a cast member of \"Do You Believe?\" play for?",
            "triples": [
                "<Do You Believe? (film); starring; Ted McGinley, Mira Sorvino, Andrea Logan White, Lee Majors, Alexa PenaVega, Sean Astin, Madison Pettis, Cybill Shepherd, and Brian Bosworth>",
                "<Brian Bosworth; team he played for; Seattle Seahawks>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <Brian Bosworth; occupation; former professional football player>",
                "C. <Brian Bosworth; league he played in; National Football League (NFL)>",
                "D. <Brian Bosworth; position; linebacker>",
                "E. <Brian Bosworth; nationality; American>",
            ],
            "answer": "A"
        }
    ],
    [
        {
            "question": "Consider the racer for whom the bend at the 26th Milestone, Isle of Man is dedicated. When were they born?",
            "triples": [],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <26th Milestone, Isle of Man; named after; Joey Dunlop>",
                "C. <26th Milestone, Isle of Man; event; Joey Dunlop died after a racing motorcycle crash in Estonia in July 2000>",
                "D. <Joey Dunlop; achievement; won a record 26 races in total at the Isle of Man TT meeting>",
                "E. <11th Milestone, Isle of Man; event; Isle of Man TT races>",
            ],
            "answer": "B"
        },
        {
            "question": "Consider the racer for whom the bend at the 26th Milestone, Isle of Man is dedicated. When were they born?",
            "triples": [
                "<26th Milestone, Isle of Man; named after; Joey Dunlop>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <26th Milestone, Isle of Man; event; Joey Dunlop died after a racing motorcycle crash in Estonia in July 2000>",
                "C. <Joey Dunlop; achievement; won a record 26 races in total at the Isle of Man TT meeting>",
                "D. <Joey Dunlop; date of birth; 25 February 1952>",
                "E. <Joey Dunlop; full name; William Joseph Dunlop>",
            ],
            "answer": "D"
        },
        {
            "question": "Consider the racer for whom the bend at the 26th Milestone, Isle of Man is dedicated. When were they born?",
            "triples": [
                "<26th Milestone, Isle of Man; named after; Joey Dunlop>",
                "<Joey Dunlop; date of birth; 25 February 1952>"
            ],
            "candidate_triples": [
                "A. no need for additional knowledge triples", 
                "B. <26th Milestone, Isle of Man; event; Joey Dunlop died after a racing motorcycle crash in Estonia in July 2000>",
                "C. <Joey Dunlop; achievement; won a record 26 races in total at the Isle of Man TT meeting>",
                "D. <Joey Dunlop; date of death; 2 July 2000>",
                "E. <26th Milestone, Isle of Man; alternative name; \"Joey\u2019s\">",
            ],
            "answer": "A"
        },
    ]
]


reasoning_chains_hotpotqa_examplars = [
    {
        "question": "Who distributed a movie whose cast includes an actor who acted in \"Him\"?",
        "chains": "<Fionn Whitehead; notable work; \"Him\" (2016 ITV miniseries)>, <Dunkirk (2017 film); cast; Fionn Whitehead, Tom Glynn-Carney, Jack Lowden, Harry Styles, Aneurin Barnard, James D'Arcy, Barry Keoghan, Kenneth Branagh, Cillian Murphy, Mark Rylance, Tom Hardy>, <Dunkirk (2017 film); distributor; Warner Bros. Pictures>",
    },
    {
        "question": "Which magazine published papers more often; The Wittenburg Door or Sports Collectors Digest?",
        "chains": "<Sports Collectors Digest; type; American advertising weekly paper>, <The Wittenburg Door; publication frequency; bimonthly>",
    },
    {
        "question": "Where is the headquarters of the company that produces the soft drink that the ICP traditionally sprays the audience with ?",
        "chains": "<FTFO; album art; alludes to ICP tradition of spraying audience with Faygo>, <Faygo; type; soft drink company>, <Faygo; location; Detroit, Michigan>", 
    },
    {
        "question": "What  are three alternate names of the University where W.G. Godfrey received his BA and MA degrees?",
        "chains": "<W. G. Godfrey; education; BA and MA from the University of Waterloo, Ph.D. from Queen's University>, <University of Waterloo; type; public research university>, <University of Waterloo; academic programs; administered by six faculties and ten faculty-based schools>, <University of Waterloo; co-op program; largest post-secondary co-op program of its kind in the world>"
    },
    {
        "question": "Who has perofrmed in more bands, Paul Draper or Kevin Max?",
        "chains": "<Paul Draper (musician); former band; Mansun>, <Kevin Max; lead singer of the band; Audio Adrenaline>, <Kevin Max; group he was a member of; DC Talk>",
    },
    {
        "question": "Which state did this male American academic and politician serve as a senator under whom Natalie Ravitz was a prominent staffer?",
        "chains": "<Natalie Ravitz; previous role; staffer for United States Senators Barbara Boxer and Paul Wellstone>, <Paul Wellstone; occupation; academic and politician>, <Paul Wellstone; represented; Minnesota in the United States Senate>", 
    },
    {
        "question": "A board of coaches representing what British producer of newsreels and documentaries, active from 1910 through 1970, named William Inwood Smith a first-team All-American in 1935?",
        "chains": "<Inwood Smith, selected as a first-team All-American by; Grantland Rice for \"Collier's Weekly\" and a board of coaches for Path\u00e9 News>, <Path\u00e9 News; type; producer of newsreels and documentaries>, <Path\u00e9 News; duration of operation; 1910-1970>"
    },
    {
        "question": "What was the occupation of both Marguerite Radclyffe Hall and Charles Bukowski?",
        "chains": "<Charles Bukowski; occupation; poet, novelist, short story writer>, <Radclyffe Hall; occupation; poet and author>"
    },
    {
        "question": "Which genus of plant life is more palm like, Pandanus or Eriogonum?",
        "chains": "<Pandanus; physical characteristics; palm-like, dioecious trees and shrubs>, <Eriogonum; scientific name; genus of flowering plants in the family Polygonaceae>, <Pandanus; common names; pandan, screw palm, screw pine>, <Eriogonum inflatum; family; Polygonaceae>",
    },
    {
        "question": "Who is credited with composing the music for the song named in a famous Guatemalan lottery dedicated to help the deafblind?",
        "chains": "<Loter\u00eda Santa Luc\u00eda; purpose; to help the deafblind across the country>, <Santa Lucia; composer; A. Longo (1835)>",
    },
    {
        "question": "What lake borders the city where the 308th Bombardment Wing was last stationed?",
        "chains": "<375th Bombardment Squadron; last assignment; 308th Bombardment Wing>, <375th Bombardment Squadron; location; Plattsburgh Air Force Base, New York>, <Plattsburgh Air Force Base; location; western shore of Lake Champlain opposite Burlington, Vermont>",
    },
    {
        "question": "Justin Shenkarow voices Harold Berman, a character from a television series that aired on what station?",
        "chains": "<Title: Justin Shenkarow; notable roles; Matthew Brock in \"Picket Fences\", Simon Holmes in \"Eerie, Indiana\", Harold Berman on \"Hey Arnold!\">, <Hey Arnold!; network; Nickelodeon>", 
    },
    {
        "question": "What is the 5th studio album released by the singer of \"A Girl's Gotta Do (What a Girl's Gotta Do)\"?",
        "chains": "<A Girl's Gotta Do (What a Girl's Gotta Do); artist; American country music artist Mindy McCready>, <Mindy McCready; fifth album; I'm Still Here>", 
    },
    {
        "question": "Which profession does Boris Barnet have in common with Baltasar Korm\u00e1kur?",
        "chains": "<Baltasar Korm\u00e1kur; occupation; actor, theater and film director, film producer>, <Boris Barnet; occupation; film director, actor, and screenwriter>", 
    },
    {
        "question": "Who directed the movie containing the phrase inspiring the name of The Dismemberment Plan?",
        "chains": "<The Dismemberment Plan; origin of the name; a stray phrase uttered by Ned Ryerson in the comedy \"Groundhog Day\">, <Groundhog Day (film); director; Harold Ramis>", 
    },
    {
        "question": "Where was the rock band the star of \"Her Name is Nicole\" played alongside from?",
        "chains": "<Nicole Scherzinger; career path; pursued a musical career alongside the American rock band Days of the New and later auditioned for \"Popstars\" and became a member of the short-lived girl group Eden's Crush>, <Days of the New; origin; Charlestown, Indiana>",
    },
    {
        "question": "Who does the goalkeeper play for which Ahmad Khormali's tracksuit bottoms resemble?",
        "chains": "<Ahmad Khormali; fashion style; wears pyjama-like tracksuit bottoms>, <Ahmad Khormali; inspiration; Hungarian goalkeeper G\u00e1bor Kir\u00e1ly>, <G\u00e1bor Kir\u00e1ly; position; goalkeeper>, <G\u00e1bor Kir\u00e1ly; current team; Szombathelyi Halad\u00e1s>", 
    },
    {
        "question": "When was the actress who is performing a routine bugging operation in \"One Last Dance\" born?",
        "chains": "<Keeley Hawes; occupation; actress>, <Keeley Hawes; birthdate; 10 February 1976>", 
    },
    {
        "question": "In which National Football League (NFL) team did a cast member of \"Do You Believe?\" play for?",
        "chains": "<Do You Believe? (film); starring; Ted McGinley, Mira Sorvino, Andrea Logan White, Lee Majors, Alexa PenaVega, Sean Astin, Madison Pettis, Cybill Shepherd, and Brian Bosworth>, <Brian Bosworth; team he played for; Seattle Seahawks>", 
    },
    {
        "question": "Consider the racer for whom the bend at the 26th Milestone, Isle of Man is dedicated. When were they born?",
        "chains": "<26th Milestone, Isle of Man; named after; Joey Dunlop>, <Joey Dunlop; date of birth; 25 February 1952>"
    }
]