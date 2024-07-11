alter = 18
ausweis = True

if alter >= 18:
    print("Du bist alt genug, um in den Club zu gehen!")
elif alter < 18 and ausweis:
    print("Du bist zwar noch nicht 18, aber du hast einen Ausweis. Du darfst rein!")
else:
    print("Du bist nicht alt genug und hast keinen Ausweis. Du darfst nicht rein!")
