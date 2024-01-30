d = {'state': 'preparation', 'teamSize': 15, 'attacksPerMember': 2, 'preparationStartTime': '20240130T053602.000Z', 'startTime': '20240131T043602.000Z', 'endTime': '20240201T043602.000Z', 'clan': 
    
{'tag': '#20C2GRC0Q', 
     'name': 'KEBUMEN 86', 
     'clanLevel': 22,
     'attacks': 0, 
     'stars': 0, 
     'destructionPercentage': 0.0, 
     'members': [
    {'tag': '#28PLGJ2LY', 'name': 'HK', 'townhallLevel': 16, 'mapPosition': 2, 'opponentAttacks': 0}, 
    {'tag': '#9RYYR0PYU', 'name': 'Bazal', 'townhallLevel': 14, 'mapPosition': 7, 'opponentAttacks': 0}, 
    {'tag': '#9JVVPQVP0', 'name': 'FaiK', 'townhallLevel': 16, 'mapPosition': 3, 'opponentAttacks': 0}, 
    {'tag': '#2CLLYVVP8', 'name': 'NOMAAN_12', 'townhallLevel': 12, 'mapPosition': 13, 'opponentAttacks': 0}, 
    {'tag': '#2CUJ8980L', 'name': 'Hannan', 'townhallLevel': 13, 'mapPosition': 9, 'opponentAttacks': 0}, 
    {'tag': '#8CLGP0Y0L', 'name': 'Dark Soul', 'townhallLevel': 11, 'mapPosition': 15, 'opponentAttacks': 0}, 
    {'tag': '#820UJ29GG', 'name': 'ahmad.2015', 'townhallLevel': 15, 'mapPosition': 4, 'opponentAttacks': 0}, 
    {'tag': '#22Q0PY8R0', 'name': 'Ken Kaneki', 'townhallLevel': 14, 'mapPosition': 6, 'opponentAttacks': 0}, 
    {'tag': '#P8CQV8UQ', 'name': 'HaYaAn', 'townhallLevel': 13, 'mapPosition': 10, 'opponentAttacks': 0}, 
    {'tag': '#88U8R08Y2', 'name': 'HK', 'townhallLevel': 16, 'mapPosition': 1, 'opponentAttacks': 0}, 
    {'tag': '#RVR8PPRY', 'name': 'AJD', 'townhallLevel': 12, 'mapPosition': 14, 'opponentAttacks': 0}, 
    {'tag': '#8LQ9CCVQ2', 'name': 'Kaneki', 'townhallLevel': 13, 'mapPosition': 11, 'opponentAttacks': 0}, 
    {'tag': '#8CR2PQRRY', 'name': 'xHKx', 'townhallLevel': 15, 'mapPosition': 5, 'opponentAttacks': 0}, 
    {'tag': '#8L0JGGRQV', 'name': 'Darksoul', 'townhallLevel': 13, 'mapPosition': 8, 'opponentAttacks': 0}, 
    {'tag': '#8QJL2PCV2', 'name': 'nomaan', 'townhallLevel': 13, 'mapPosition': 12, 'opponentAttacks': 0}]},
     
     
'opponent': {'tag': '#2QCPUGQJ8', 'name': 'KINGS OF RECON', 'badgeUrls': {'small': '', 'large': '', 'medium': ''}, 'clanLevel': 13, 'attacks': 0, 'stars': 0, 'destructionPercentage': 0.0, 'members': [
{'tag': '#20YPP20Y9', 'name': 'EPICSH00T3R', 'townhallLevel': 16, 'mapPosition': 2, 'opponentAttacks': 0}, {'tag': '#99R02U9YR', 'name': '《Mistery St☆r》', 'townhallLevel': 15, 'mapPosition': 5, 'opponentAttacks': 0}, {'tag': '#228J9QQQ', 'name': 'lumcao', 'townhallLevel': 13, 'mapPosition': 8, 'opponentAttacks': 0}, {'tag': '#RR0LRPQC', 'name': 'MKclasher', 'townhallLevel': 12, 'mapPosition': 15, 'opponentAttacks': 0}, {'tag': '#QCRRU0QLR', 'name': 'In And Out ;)', 'townhallLevel': 12, 'mapPosition': 14, 'opponentAttacks': 0}, {'tag': '#JP2LJQYR', 'name': 'JAMES', 'townhallLevel': 13, 'mapPosition': 10, 'opponentAttacks': 0}, {'tag': '#9YVRYJ99', 'name': 'SHOOTER78', 'townhallLevel': 16, 'mapPosition': 1, 'opponentAttacks': 0}, {'tag': '#90PPQ9J2', 'name': 'EPICVI3JITO', 'townhallLevel': 13, 'mapPosition': 9, 'opponentAttacks': 0}, {'tag': '#JC2RJ9R8', 'name': 'Andres', 'townhallLevel': 12, 'mapPosition': 13, 'opponentAttacks': 0}, {'tag': '#2VG0CCYPV', 'name': 'pancho', 'townhallLevel': 16, 'mapPosition': 4, 'opponentAttacks': 0}, {'tag': '#8PQGY2RRG', 'name': 'krishna', 'townhallLevel': 13, 'mapPosition': 11, 'opponentAttacks': 0}, {'tag': '#QCG98YYJ0', 'name': 'MamaClasher', 'townhallLevel': 13, 'mapPosition': 7, 'opponentAttacks': 0}, {'tag': '#22JV9CJ8Q', 'name': 'Dom', 'townhallLevel': 16, 'mapPosition': 3, 'opponentAttacks': 0}, {'tag': '#QC2G2Q0GY', 'name': 'thedude86', 'townhallLevel': 13, 'mapPosition': 6, 'opponentAttacks': 0}, {'tag': '#2V090CLVP', 'name': 'ALPHA LION', 'townhallLevel': 12, 'mapPosition': 12, 'opponentAttacks': 0}]}}

for i in range(len(d['clan']['members'])):
    for key, value in  d['clan']['members'][i].items():
        print(f'{key}, {value}')
        i += 1

# for i in range(len(d['clan']['members'])):