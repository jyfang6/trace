
generate_knowledge_triples_template = "Given a title and a text, extract all the knowledge triples in the form of <title; relation; tail entity>, "\
        "where title is the provided title, tail entity is a phrase in the text and relation denotes a description of the relation "\
        "between the title and the tail entity.\n\n" \
        "{examplars}\n\n" \
        "Title: {title}\n" \
        "Text: {text}\n" \
        "Knowledge Triples: "

generate_knowledge_triples_chat_template = "Given a title and a text, extract all the knowledge triples in the form of <title; relation; tail entity>, "\
        "where title is the provided title, tail entity is a phrase in the text and relation denotes a description of the relation "\
        "between the title and the tail entity. \n\nThe followings are some examples: \n\n{examplars}"