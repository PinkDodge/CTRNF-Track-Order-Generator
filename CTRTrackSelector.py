import random;

ctrTracks = ["Crash Cove","Roo's Tubes","Mystery Caves","Sewer Speedway",
             "Coco Park","Tiger Temple","Papu's Pyramid","Dingo Canyon",
             "Blizzard Bluff","Dragon Mines","Polar Pass","Tiny Arena",
             "N. Gin Labs","Cortex Castle","Hot Air Skyway","Oxide Station",
             "Slide Coliseum","Turbo Track"];
cnkTracks = ["Inferno Island","Jungle Boogie","Tiny Temple",
             "Meteor Gorge","Barin Ruins","Deep Sea Driving",
             "Out of Time","Clockwork Wumpa","Thunder Struck",
             "Assembly Lane","Android Alley","Electron Avenue",
             "Hyper Spaceway"];
bonusTracks = ["Retro Stadium","Twilight Tour"];

while True:
    trackTotal = [];
    userIn = input("1 = Use all\n2 = CTR only\n3 = CNK only\n4 = CTR and CNK\n5 = CTR + bonus\n6 = CNK + bonus\n7 = Bonus only\n\nEnter a number: ");
    if(userIn=="1"):
        trackTotal += ctrTracks;
        trackTotal += cnkTracks;
        trackTotal += bonusTracks;
    elif(userIn=="2"):
        trackTotal += ctrTracks;
    elif(userIn=="3"):
        trackTotal += cnkTracks;
    elif(userIn=="4"):
        trackTotal += ctrTracks;
        trackTotal += cnkTracks;
    elif(userIn=="5"):
        trackTotal += ctrTracks + bonusTracks;
    elif(userIn=="6"):
        trackTotal += cnkTracks + bonusTracks;
    else:
        trackTotal += bonusTracks;

    print("---TRACK ORDER---");
    count=0;
    while(len(trackTotal)>0):
        count+=1;
        randomID = random.randrange(len(trackTotal));
        print("#"+str(count)+" - "+trackTotal[randomID]);
        del trackTotal[randomID];
    print("-----------------------------");
