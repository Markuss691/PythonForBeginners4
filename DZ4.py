class comparison:
    def compare(self,S1,S2):
        count = 0
        for i in range(len(S1)):
            ngrams = [S1[i:i+3]]
            for ngram in ngrams:
                count += S2.count(ngram)
        return count/max(len(S1), len(S2))

if __name__ == '__main__':
    c = comparison()

    StrSr = input('Введите наименование города для сравнения: ')

    towns = [
        'Кадников', 'Казань', 'Калач', 'Калач-на-Дону', 'Калининград', 'Калуга'
        ]
    print('Степень сходства с: ', StrSr)
    
    for town in towns: 
        print(town, c.compare(town,StrSr))

"""import datetime as dt
def compare(S1,S2):
    count = 0
    for i in range(len(S1)):
        ngrams = [S1[i:i+3]]
        for ngram in ngrams:
            count += S2.count(ngram)
    return count/max(len(S1), len(S2))

def distance(s,t):
    n,m = len(t), len(s)
    v0 = [0]*(n+1)
    v1 = [0]*(n+1)
    for i in range(n):
        v0[i]=i
    for i in range(m):
        v1[0]=i+1
        for j in range(n):
            deletionCost = v0[j +1]+1
            insertionCost = v1[j]+1
            if s[i] == t[j]:
                substitutionCost = v0[j]
            else:
                substitutionCost = v0[j] +1
            v1[j+1] = min(deletionCost,insertionCost,substitutionCost)
        v0, v1 = v1, v0
    return v0[n]

pairs = [
    ('hidden','holden'),
    ('организация','организационный'),
    ('го','го____'),
    ('drink','drunk'),
    ('море','гора'),
    ('saturday','sunday')
    ]

if __name__ == '__main__':
    print('Сравнение строк двумя методами')
    for s,t in pairs:
        t0 = dt.datetime.now()
        print('Левенштейн', s, t, distance(s,t),dt.datetime.now() - t0)
        print('Триады',s,t,compare(s,t),dt.datetime.now() - t0)
"""                
           


