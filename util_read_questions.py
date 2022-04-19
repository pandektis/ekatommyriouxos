def read_qans(fname):
    """
    Συνάρτηση που διαβάζει το αρχείο με τις ερωταπαντήσεις
    και τις επιστρέφει σε μια λίστα από λεξικά.
    Κάθε λεξικό έχει τα εξής κλειδιά:
    'id' : αριθμός ερώτησης
    'question' : κείμενο ερώτησης
    'answers' : λίστα με πλειάδες δύο μελών. Κάθε πλειάδα έχει την απάντηση ως πρώτο μέλος και True/False για το αν είναι η σωστή
    'dif' : αριθμός 1-3 για τη δυσκολία κάθε ερώτησης
    """
    list_of_qans = []
    qan = {}

    with open(fname, mode='r',encoding="utf8") as f:
        for line in f:
            if line == '\n':
                if len(qan["answers"]) > 4:
                    print("ERROR: ", num, qan["question"])
                    exit()
                list_of_qans.append(qan.copy())
                qan = {}
                continue

            if line[0].isnumeric():
                num, _, q = (s.strip() for s in line.partition("."))
                qan.update({"id" : int(num), "question" : q})
            else:
                letter, _, ans = (s.strip() for s in line.partition("."))
                if len(letter.strip()) > 1:
                    qan["question"] = qan["question"] + " " + letter
                else:
                    a, status, difficulty = ans.partition("(*)")
                    #print(a, status, difficulty)
                    status = bool(status)
                    if difficulty:
                        qan.update({"dif" : int(difficulty)})
                    qan.update({"answers" :qan.setdefault("answers", []) + [(a, status)]})

    return list_of_qans        

def print_qan(q):
    '''
    Βοηθητική συνάρτηση για την εμφάνιση της μορφής μιας ερωταπάντησης
    '''
    import random
    #random.shuffle(qan["answers"])
    print(f'{q["id"]} -- επίπεδο {q["dif"]}')
    print(q["question"])
    for a in q["answers"]:
        print(a[0], " --> είναι: ", a[1])
    print()



    
if __name__ == '__main__':
    q_list = read_qans("q_ans.txt")
    print(q_list[2])
    for q in q_list:
        print_qan(q)