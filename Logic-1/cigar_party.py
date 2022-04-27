def cigar_party(cigars, is_weekend):
    if is_weekend == False:
        return 40<=cigars<=60
    else:
        return cigars>=40