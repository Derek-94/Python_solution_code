pref = list(map(float, input().split()));
pref_en = list(enumerate(pref));
pref_en.sort(key = lambda x: x[1], reverse=True);

hor, ver = input().split();

movies_info = [];
generes = [];

for i in range(int(hor)):
    tmp_input = list(input());
    movies_info.append(tmp_input);
for i in range(int(hor)):
    tmp_input = list(input());
    generes.append(tmp_input);

genres_total = [];
for i in range(int(hor)):
    for j in range(int(ver)):
        genres_total.append([generes[i][j], pref[ord(generes[i][j]) - 65]])
print(genres_total)