MIN = -1000
MAX = 1000

def alpha_beta(depth, node, maximizing, values, alpha, beta):
    if depth == 3:
        return values[node]

    if maximizing:
        best = MIN
        for i in range(2):
            value = alpha_beta(depth+1, node*2+i, False, values, alpha, beta)
            best = max(value, best)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best
    else:
        best = MAX
        for i in range(2):
            value = alpha_beta(depth+1, node*2+i, True, values, alpha, beta)
            best = min(value, best)
            alpha = min(alpha, best)
        
            if alpha >= beta:
                break
        
        return best

values = [1,5,6,9,1,2,0,-1]
alpha = MIN
beta = MAX
print(alpha_beta(0,0,True,values,alpha,beta))
