def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    top_three=[]
    scores.sort(reverse=True)
    if len(scores) <= 3:
        return scores
    else:
        top_three.append(scores[0])
        top_three.append(scores[1])
        top_three.append(scores[2])
    return top_three




     
