import json


def cushman():
    with open('data/items.json', 'rw') as f:
        questions = json.load(f)
        for q in questions:
            idx = [i for i, c in enumerate(q['title']) if c.isupper()][0]
            title = q['title'][idx:]
            dilemma = q['text'].split('.')[-1]
            text = q['text'].replace(dilemma, '').replace(
                '...', '').replace('\n', '')
            idea = dilemma.split('the right thing to do')[0].split("Is")[1]
            dilemma = dilemma.replace(idea, '<b>'+idea+'</b>')

            new_keys = {
                "type": "long",
                # "answers": ["Yes", "No"],
                "additional": {
                    "dilemma": "Why?",
                    "entered": [],
                    "type": "long"
                },
                "oldTitle": q['title'],
                "entered": [],
                "correct": "",
                "title": title,
                "text": text,
                "dilemma": dilemma
            }
            q.update(new_keys)
        with open('data/new_items.json', 'w') as fp:
            json.dump(questions, fp)

def main():
    files = 'impersonal_moral', 'personal_moral', 'non_moral'
    d = []
    count = 0
    for i, fi in enumerate(files):
        with open(f'data/{fi}.json', 'r') as f:
            questions = json.load(f)
            if i == 0:
                with open(f'data/control_items.json', 'r') as fp:
                    control = json.load(fp)
            
                questions = control + questions;
                
            for q in questions:
                count+=1
                dilemma = q['text'].split('.')[-1]
                text = q['text'].replace(dilemma, '').replace('\n', '')
                # idea = dilemma.split('the right thing to do')[0].split("Is")[1]
                # dilemma = dilemma.replace(idea, '<b>'+idea+'</b>')

                new_keys = {
                    "type": "long",
                    # "answers": ["Yes", "No"],
                    "additional": {
                        "dilemma": "Why?",
                        "entered": [],
                        "type": "long"
                    },
                    "oldTitle": q['title'],
                    "entered": [],
                    "correct": "",
                    "title": q['title'],
                    "text": text,
                    'oldId': q['id'],
                    'id': count,
                    'cond': fi,
                    "dilemma": dilemma
                }
                q.update(new_keys)

            d += questions

    with open('data/new_items_green.json', 'w') as fp:
        json.dump(d, fp)



if __name__ == '__main__':
    main()




