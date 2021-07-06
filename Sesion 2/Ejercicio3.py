def attack(base_atacada):
    print("La Base {} es destruida".format(base_atacada))
    return cnj_bases.difference(base_atacada)

def game_over(bases_restantes):
    if len(bases_restantes) == 0 :
        return True
    else :
        return False

cnj_bases = {1,2,3,4,5,6,7,8,9,10}

lst_bases = (3,5,1,2,10,8,4,6,7,9)

print("Bases Terrestres = {}".format(cnj_bases))

for i in lst_bases :
    cnj_bases = attack({i})
    if game_over(cnj_bases) :
        print("GAME OVER : Bases Terrestes Eliminadas.")
    else :
        print("Aun quedan las bases : {}".format(cnj_bases))





