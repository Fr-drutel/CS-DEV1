def calendrier(année):
    val = False
    if année % 400 == 0:
        val = True
    else:
        val = False
    L = str(année)
    if L[2] != '0' and L[3] != '0':
        if année % 4 == 0:
            val = True
    else:
        val = False
    if val == True:
        return 'Année bissextile'
    if val == False:
        return 'Année pas bissextile'
