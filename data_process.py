import json
import os
import numpy as np

np.random.seed(42)

linda = json.load(open(os.path.join('data','linda.json')))
bill = json.load(open(os.path.join('data','bill.json')))

def get_list_items():
    return ["order","training 1","hobby 1","work 1","hobby 2"]

def build_tree(data,name):
    d = {}
    def update_d(d,l_k,qi,q):
        if len(l_k) == 0:
            q['info']['type'] = name
            d['question'] = q
            return
        i = l_k.pop(0)
        if i == 'order':
            key = qi[i]
        else:
            key = qi[i][0]+'-'+qi[i][1]
        try:
            d[key]
        except KeyError:
            d[key] = {}
        update_d(d[key],list(l_k),qi,q)
    for k in data:
        q = data[k]
        qi = q["info"]
        update_d(d,get_list_items(),qi,q)
    return d

COUNT = 0
def rebuild(d,l_k):
    global COUNT
    l_d = [d]
    for k in l_k:
        l_d.append(l_d[-1][k])
    l_d.reverse()
    for di in l_d:
        l_r = [k for k in di.keys() if di[k] == {}]
        for r in l_r:
            COUNT += 1
            del di[r]

def query(tree,style,order,hist,avoid):
    #print('----- query',style,order,len(hist))
    #print([str(k)[:10] for k in tree])
    if len(hist) == 5:
        out = tree['question']
        del tree['question']
        return out,hist
    elif len(hist) == 0:
        key = order
    else:
        if len(hist) == 1:
            filtered_keys = [k for k in tree.keys() if k[0] == style and not(k in avoid)]
        else:
            filtered_keys = [k for k in tree.keys() if not(k in avoid)]
        key = filtered_keys[0]#np.random.choice(filtered_keys)
    hist.append(key)
    return query(tree[key],style,order,hist,avoid)

def add_premium(add):
    linda_question_info = np.random.choice([linda,bill])[np.random.choice(list(linda.keys()))]['info']
    name = linda_question_info['name'][1]
    training = linda_question_info['training 1'][1]
    hobby = linda_question_info['hobby 1'][1]
    hobby2_qinfo = np.random.choice([linda,bill])[np.random.choice(list(linda.keys()))]['info']
    hobby2 = hobby2_qinfo['hobby 1'][1]
    while hobby2 == hobby:
        hobby2_qinfo = np.random.choice([linda,bill])[np.random.choice(list(linda.keys()))]['info']
        hobby2 = hobby2_qinfo['hobby 1'][1]
    if np.random.random() > 0.5:
        question = "What was %s's hobby during college ?" % name
        answers = ['%s %s.' % (name,hobby),'%s %s and %s.' % (name,hobby,hobby2)]
        correct_answer = answers[0]
    else:
        question = "What were %s's training and hobbies back in college ?" % name
        answers = ['%s %s.' % (name,hobby2),'%s %s and %s.' % (name,training,hobby)]
        correct_answer = answers[1]

    order = int(np.random.random()>0.5)
    answers = [answers[1-order],answers[order]]
    
    premium_q= '%s %s. During college, %s %s. %s' % (name,training,name,hobby,question)
    info = {'nature':'premium',
            'order':order,
            'name':linda_question_info['name'],
            'training 1':linda_question_info['training 1'],
            'hobby 1':linda_question_info['hobby 1'],
            'hobby 2':hobby2_qinfo['hobby 2'],
            'question type':question,
            'correct answer':correct_answer}
    premium = {'question':premium_q,'answers':answers,'info':info}
    print('Premium:',premium)
    add.append(premium)

def add_catch(add):
    answers = ['A','B']
    percents = [i*10 for i in range(11)]
    answer = np.random.choice(answers)
    percent = np.random.choice(percents)
    catch_q = 'Let there be 100 people. {} of them are carpenters. {} of them are flower shop owners. Considering this particular group of people...'.format(percent,100-percent)
    catch_a = ['How many would you say are carpenters.'.format(percent),'How many would you say are flower shop owners.'.format(100-percent)]
    if answer == 'B':
        catch_a.reverse()
    catch = {"question":catch_q,"answers":catch_a,"info":{'nature':'catch',"answer":answer,"percent":str(percent)}}
    print('Catch:',catch)
    add.append(catch)

def make_database(linda_tree,bill_tree):
    db = []
    while linda_tree != {}:
        #print('- i',i)
        avoid = []
        add = []
        for lbl,tree in [('linda',linda_tree),('bill',bill_tree)]:
            for style in ['S','A']:
                for order in [0,1]:
                    #print('--- start query',style,order)
                    out,hist = query(tree,style,order,[],avoid)
                    avoid += hist[1:]
                    rebuild(tree,hist)
                    out['info']['style'] = style
                    out['info']['nature'] = 'question'
                    add.append(out)
                    #print(out)
                    #print(tree[hist[0]][hist[1]][hist[2]][hist[3]].keys())
                    #assert False
        np.random.shuffle(add)
        db.append(add)
    assert linda_tree ==  {}
    assert bill_tree == {}
    return db


linda_tree =  build_tree(linda,'linda')
bill_tree = build_tree(bill,'bill')

db = make_database(linda_tree,bill_tree)
print(len(db))

#Verif
#All vignettes appear exactly once in each set
for i in range(len(db)):
    d = {}
    l_i = get_list_items()[1:]
    for j in range(len(db[i])):
        for it in l_i:
            try:
                d[db[i][j]["info"][it][1]] += 1
            except KeyError:
                d[db[i][j]["info"][it][1]] = 1
    assert len(d.keys()) == 32
    for k in d:
        assert d[k] == 1

#No duplication of question
for i in range(len(db)):
    d = {}
    for j in range(len(db[i])):
        q = db[i][j]["question"]
        a = db[i][j]["answers"]
        try:
            d[q+a[0]+a[1]] += 1
        except KeyError:
            d[q+a[0]+a[1]] = 1
    for k in d:
        assert d[k] == 1
    
#Blocks each have the right composition L/B S/A O/R
for i in range(len(db)):
    d = []
    for j in range(len(db[i])):
        type_ = db[i][j]["info"]["type"]
        style = ""
        for k in get_list_items()[1:]:
            style += db[i][j]["info"][k][0]
        order = db[i][j]["info"]["order"]
        d.append((type_,style,order))
    pattern = 'SA'
    for t in ['linda','bill']:
        for s in range(2):
            if t == 'linda':
                ss = pattern[s]*2+pattern[1-s]+pattern[s]
            else:
                ss = pattern[s]*3+pattern[1-s]
            for o in range(2):
                assert (t,ss,o) in d

#Add catch & premium
for i in range(len(db)):
    add_catch(db[i])
    #add_premium(db[i])
    np.random.shuffle(db[i])

np.random.shuffle(db)

for i in range(len(db)):
    for j in range(len(db[i])):
        db[i][j]['info']['index_um'] = i

json.dump(db,open(os.path.join('data','db.json'),'w'))

"""
#Example condition
def extract_condition(l,c_name):
    ext = []
    for e in l:
        if e['info']['nature'] == c_name or e['info']['nature'] == 'question' and e['info']['type'] == c_name:
            ext.append(e)
    return e
def fold_condition(l):
    assert len(l)%2 == 0
    l2 = []
    indexs = list(range(len(l)))
    while len(indexs)>0:
        j = np.random.randint(1,len(indexs))
        l2.append([l[indexs[0]],l[indexs[j]]])
    return l2

db_ex = []
for i in range(len(db)):
    add_catch(db[i])
    add_premium(db[i])
    db_ex.append([])
    for c_name in ['linda','bill','premium','catch']:
        lq = extract_condition(db[i],c_name)
        fq = fold_condition(lq)
        db_ex[i] += fq

for i in range(len(db)):
    for j in range(len(db[i])):
        for k in range(len(db[i][j])):
            db[i][j][k]['info']['index_um'] = i

json.dump(db_ex,open(os.path.join('data','db_ex.json'),'w'))
"""