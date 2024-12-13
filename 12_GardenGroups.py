# https://adventofcode.com/2024/day/12
# Day 12: Garden Groups

from itertools import *

def garden_groups(data):
    A = {i + 1j * j: v for i, r in enumerate(data.split()) for j, v in enumerate(r)}
    vis = set()
    def dfs(z, t):
        if z in vis or A.get(z, -1) != t:
            return 0, []
        vis.add(z)
        area = 1
        fences = []
        for i in range(4):
            y = z + 1j ** i
            a, f = dfs(y, t)
            area += a
            fences += f + [(z, i)] * (A.get(y, -1) != t)
        return area, fences
    part1 = part2 = 0
    for z in A:
        a, f = dfs(z, A[z])
        part1 += a * len(f)
        ds = {}
        def find(p):
            ds.setdefault(p, p)
            if ds[p] != p:
                ds[p] = find(ds[p])
            return ds[p]
        for p, q in combinations(f, 2):
            if p[1] == q[1] and abs(p[0] - q[0]) == 1:
                ds[find(p)] = find(q)
        part2 += a * len({*map(find, f)})
    yield part1, part2


def inputs():

    yield """
AAAA
BBCD
BBCC
EEEC
"""

    yield """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

    yield """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

    yield """
TTTTTTTTTTTTTTDDDDDDDDDDDDAAAKKKKKKKKKKKKKKKKKKKKKKKRRRRRRRRRRRRRXXXXXXXXXXZFFFFFFFFFFOFVVVVVVQQQQQUQQQQQQQQQQQQQQQQQCCGGNNNNHHHHHHHHHHHHHHH
TTTTTTTTTTTTTTDDDDDDDDDDDDAAAAAAKKKKKFKKKKKKKKKKKKKKRRRRRRRRRRRXXXXXXXXXXXXZFFFFFFFFFFFFFFFVMMQQQQQQQQQQQQQQQQQQQQQQQGGGGNNNNHHHHHHHHHHHHHHH
TTTTTTTTTTTTDDDDDDDDDDDUAAAAAAAAAKKFFFKKKKKKKKKKKKKKRRRRRRRRRRXXXXXXXXMXMMFFFFFFFFFFFFFFFMMMMMNQQQQQQQQQQQQQQQQQQQQQZZGGNNNNHHHHHHHHHHHHHHHH
TTTTTTTBTTTTDDDDDDDDDDUUUAAAAAAAKKKKFFKKKKKKKKKVLLLLLRRRRRRRRRXXXXXXXMMMMMFMMMMFFFFFFFFFXMMHMMNQQQQQQQIQQQQQQQQQQQQQQQGGNNNNVVVHHHHHHHHHHHHH
TTTTBTBBTTTTDDDDDDDDDDUUUAAAAAAAKKKFFKKKKKKKKKNLLLLLLRRRRRRRRRXXXXXXXMMMMMMMMMFFFFFFFFHXXXMHHNNQQQQQQQIIIQQQQQQQQQQQQQGGVVVVVOHHHHHRRRHRHHHD
TBBBBBBBTTTTDDDDDDDDUDUUUAAAFAAAKKKFFKFFFKKKKKKWWLLLLRRRRRROOOOOXBMMMMMMMMMMEFFMFFFFHHHHXMMHHHHQQQQQQQQIIQQQQQQQQQQQGGGGGVVVVVVZHHXRRRRRHDHD
BBBBBBBBBTTTDDDDDDDUUUUUUGUFFFFKKKKKKFFFKKKKKKKWLLLLLLRRRROOOEOOOMMMMMMMMMMMMMUMMFFFFFHHHHHHHHHQQQQQIIIIIIQQIQQIIQQQUGGGGVVZVZZZZZRRRRRRDDHH
BBBBBBBBTTTTDDDDDDXUUUUUUUUFFFFKKKKKKFIFKKKKKKKKLLLLLLRRLLOOOOOOOOMMMMMMMMMMMMMMFFFFFFHHHHHHHHHHHZZIIIIIIIQIIQQIIQQQGGGGGGGZZZZZZZRRRRMMHHHH
BBBBBBBBTTTTDDXXXXXUUUUXUUFFFKKKKKKKKFEEKKKKKKKKKFLLLLLLLOOOOOOOOOMMMMMMMMMMMMMMFFFFFFFHHHHHHHHHHIIIIIIIIIIIIIIIINQQGGGGGGGZGZZZZZRRRRRRHHHH
BBBBBBBBBBDDDDXXXXUUUUUUSFFFFKKKKKKEEEEEEKKKKKKKKFKKKLLLLLTOOOOOOOOOMMMMMMMMSWSFFFFFFFFHIIIIHHHHHMMIWIIIIIIIIIIGGGGGGGGGGGGGGGZZZZRRRRRRNHHH
BBBBBBBBBBBDXDXXXXXXOOOOOOOOOOKKKKEEEEEKKKKKKKKKKKKKKLLLLLOOOOOOOOOOOOMMMMMMSSSSSFFFFFHIIIIIHHHHHIIIIIIIIIIIIIWGGGGGGGGGGGZGGZZZZZZRRNNNNHHN
BBBBBBBBBBBDXXXXXXXGOOOOOOOOOOXKKKKEEEEEKKBKKKNKKKKKKKKLLLLOOOOOOOOOOOMMLLMMSSSSSSFFFFHIIIIIHHHHHIIIIIIIIIIIIIIIGGGGGGGGGGZZZZZZZZZRRRRRNHHN
BBBBBBBBBBBBXXXXXXXXOOOOOOOOOOKKKKKKXEEEEEENKNNNKKLLKKKKLLLLLOOOOLOOLLLLLLLSSSSSSSFFFHHIIIIIHBHHHIIIIIIIIIIIIIIGGGGGGGGGGGZZZZZZZZZRZRRNNNNN
BBBBBBBBBBBBBXXXXXXXOOOOOOOOOOXKXKKKKEEEEEENNNNNNLLLLKKKLLLLLOOOLLLLLLLLLLLSSSSSSSFFFFFIIIHBBBHHHIIIIIIIIIIIICCGGGGGGGGGGGZZZZZZZZZZZRRNNNNN
BBBBBBBBBBBBCXXXXOOOOOOOOOOOOOXKXKKKKESSSSSSNNNLLLLLLKOOLLLLLOLLLLLLLLLLLAAASSSSSSSFFFFIIIBBBBBBIIIBIIIIIIIICCCGMGGGGGGGGZZZZZZZZZZZNNRNNNNN
BBBBBBJBBBBXXXXXXOOOOOOOOOOOOOXXXKKKXESSSSSSSSSSSLLLLLLOOLOLLLLLLLLLLLAAAAAASSSSSSSFFFFIIIVBBBBBBIBBBIIIIIIIICGGGGGGGGGGGZZZZZZZZZZZNNNNNNNN
BBBBBBBBBBXXXXXXXOOOOOOOOOOOOOXXXXNKXXSSSSSSSSSSSLLLLLOOOOOLLLLLLLLLLAAAAAAASSSSSSSSZFFFBBBBBBBBBBBBBBIIIIIIICCXXXGGGGGGGGGIZZZZZZZNNNNNNNNN
FBBAABABBBFXXXXOOOOOOOOOOOOOOOXXXXNKXSSSSSSSSSSSSLLLLLLOOOOLLLLLLLLLEWAAAAAASSSSSSDDZFFFBBBBBBBBBBBBBBBIIIIICCCCCXGGGGGGGIIIZIIIZNZNNNNNNNNN
FBBAAAAAAAXXXXXOOOOOOOOGGGVVVXXXXXXXXSSSSSSSSSSSSLLLLLLOOOOOOLOOOLLLEEEEAAASSSESSSDDZFFFBBBBBBBBBBBBBBBIBBIIIIIIIIXGXXGGIIIIIIIIINNNNNNNNNNI
FBFAAAAAAAAAXXXOOOOOOOOGGGVVVXXXXXXXXSSSSSSSSSSSSLLLLLLOOOOOOOOOOLLEEEEAAAATSSSSDDDZZFZZSSSBBBBBBBBBBBBBBBIIIIIIIIXXXXIIIIIIIIIIINNNNNNNNNNI
FFFFGAAAAAAAXLXOOOOOOOOGGGVVVXXXXXXXXSSSSSSSSSSSSLLLLLOOOOOOOOOOLLLEEEEAAAAASDDDDDZZZZZSSTTBBBBBOOBBBBBBBBIIIIIIIIXXIIIIIIIIIIIIIINNNNNNNNII
FFGGGAAAAAAAXAAOOOOOOOOGGGGVVXXXXXXXXSSSSSSSNNNNLLLLLOOOOOOOOOOOLLLLEEELXDADDDDDDDZZZZZSZZTBBBBBOOOBBBBBBBIIIIIIIIXXXIIIIIIIIIIINNNNNNNNNNII
FFFGGGGAAAAAAAAOOOOOOOOGVVGVVVVXXXXXXSSSSSSSNNLLLLBLLOOOOOOOOOOOLLLEEXXXXDDDDDDDDDZZZZZZZTTTTBBOOOBBBBBBBIIIIIIIIIXXIIIIIIIIIIINNNNNVNNVNNNI
FFGGGPGALAAAOOOOOOOOOOOGVVVVVVVVXXXXXSSSSSSSNDDLLLLLLOOOOOOOOOOOOLLEEXXXXXDDDDDDDZZZZZZZZTTTBBOOOOOOBBBIIIIIIIIIIIIIIIIIIIIIIINNNNVVVVNVFNII
GGGGGPGGLLAAOOOOOOOOOOOVVVVVVVXXXXXXXXXXDDDDDDDDLDDOOOOOOOOOOOOOTXXXXXXXXXXDDDDDZZZZZZZZZTTTTBBIOOOOBBBIIIIIIIIIIIXXXIIIIIIIINNNVVVVVVVVFJII
GGGGGGGGGGGIOOOOOOOOOOOEVVVVVVXXXXXXXXXXDDDDDDDWWWWOOOOOMOOOOOOOXXXVXXXXXXXXDDDDZZZZZZZZZZTTTTLIIIIOOOOIIIIIIIIIIIXXXXIIIIIIINNNNVVVVVVVJJJI
GGGGGGGGGGGIOOOOOOOOOOEEEEVVVVVXXXXXXXXXDDDDDDDWWWWWWWWWWOOHHOOXXXXXXXXXXXXDDDDDZZZZZZZZZZZZZZLIIIIIIIOIIIIIIIIIIIXXXXIIIIIIINNNNVVVVVVVJJJJ
GGGGGGGGSGSMOOOOOOOOOOEEEVVVVVVVXXBXXDXDDDDDDDDWWWWWWWWWWHHHHOKGGGXXXXXXXXXDDDDDZZZZZZZZZNNNNIIIIIIIIOOIIIIIIIIIIXXXXIIIIIIINNNNNNNVVVVVVJJJ
GGGGGGGWWWWWWWOOOOOOOOLLLLVVVSVVXXBBDDDDDDDDDDDWWWWWWWWWWHHHHGGGGGXXXXXXXXDDDDDVCZZZZZZZNNNNNIIIIIIIIIIIIIIIIIIIIXXXXIIIIIIIINNNNNTVVVVJVJJJ
GGGGGGGWWWWWWWOOOOOOOOLLLLLLSSSXXXBDDDDDDDDDDDDWWWWWWWWWWHHHHGGGGGGXXXXXXXXDDDVVCCCZZZZIIIINNIIIIIIIIIIIIIHHHHXHHXXXXIIIIIINNNNNNNNLLLLJJJJJ
GGGGGGGWWWWWWWOOOOOOOOLLLLLLSSSSSDDDDDDDDDDDDDDWWWWWWWWWWHHHHGNNGGGGGXXXXXXVVVYVVCVZZZIIIIINIIIIIIIIIIIIIIHHHHHHHXXXXIIJIIINNNNNNNNNLLLJJJJJ
GGGGGGGWWWWWWWOOOOOOOOLLLLLLSSSSDDDDDDDDDPPDDDDWWWWWWWWWWHHHGGGGGGGGGXXXXXXVXVVVVVVVFZZIIIIIIIIIIIIIIIIIIIHHHHHHHXXXGGIIYNNNNNNNNNNQLLLJJJJJ
GGGGGGGWWWWWWWOOOOOOOOLLLLLLSSSSSSSDSSSDDDPDDDDWWWWTHHTHHHHHHGYGGGGGGSXXXXXXXVVVVVVVFIIIIIIIIIIIIIIIIIIIIIHHHHHHHXXXGGYYYNNNNNYNNNNLLLLLLJJJ
GGGGGGTWWWWWWWSOOOOOOOLLLLLVVSSVSSSDSSDDDDDDDDDWWWWTTHTTHHHHHGYGHGGGGGXXXXXXVVVVVVFFFIFFFIIIIIIIIIIIIIBHHHHHHHHHHHHGGGGYYNYYYYYNLLLLLLLLLJJJ
GBBBBBBWWWWWWWSOOOOOOOLLLLVVVVVVVSSSSSSSDDDMDDDDDDDTTTTTHHHHHGYGHHHHGHHHSXXXXVVXXVFFFFFFFIIIIIIIIIIMIBBBBHHHHHHHHHHGGGYYYYYYYYYYLLLLLLLLLJJJ
WBBBBBBWWWWWWWSSSSLLLLLLLLLVVVVVVVSSSSSDDDDMMMDDDDDTTTTTTTTTHGGGGHHHHHHSSSSXXVVVXXXFFFFFFFIIIIIIIIIIIBZZBBHHHHHHHHHGGGYYYYYYYYYXLLLLLLLLLLJJ
GBBBBBBWWWWWWWSSSLLLLLLLLLLVVVVVVVSSSSSDDDDDMMMMMMTTTTTTTZZHHZZHHHHHHHSSSGSXXXXXXXFFFFFFIIIIIIIIZIZZZZZZBHHHHHHHHHGGGGGGYYYYYYYXXLLLLLLLLJJJ
GBBBBBBBBJJJJJSSSSSLLLLLLLLVVVVVVVVVSSSDSSSMMMMMTTTTTTTTTTZZZZZZHHHHSSSSSSSSSSSSXFFFFFFFFIIIIIIZZZZZZZZZBHHTTTHHHGGGGGGGYYYYXXXXXXXLLLLLJJJJ
LBBBBBBBBJJJJSSSSSSSHLLLLLLOOVVVVVVVVVSSSSSMMMMMMMTTTTTTTTZZZZZZZZZSSSSSSSSSSSSSFFFFFFFFFIIIZIZZZZZZZZZZZZTTTHHHHGGGGGGGGYYXXXXXXXXXLLJLJJJJ
VBBBBBBBBJJJSSSSSSSSWLBLLLOOOVVVVVVVOZZSZSMMWMMMMTTTTTTTTTZZZZZZZZZCSSSSSSSSSSJJJJJFFFFFFFFZZZZZZZYYYYYYYYYYTTHGGGGGGGGGYYXXXXXXXXXXXLJJJJJJ
VBBBBBBBBJJSSSSSSSSSWWLLLLOOOOVVVVVOOZZZZMVMMMMMMTTTTTTTTZZZZZZZZZZZSSSSSSSSSSSSSJFFFFFFFFLLNZZZZZYYYYYYYYYYTTGGGGGGGGGGYYYXXXXXXXXXXLJJJJJJ
VBBBBBBBBJSSSSSSSSSSWLLLLLLOOOOOOOOOOZZZZMMMMMMMMMTTTTTTTYZZZZZZZZZZZZSSSSSSSSSSSFFFFFFFFFLLZZZZZZYYYYYYYYYYTTGGGGGGGGGGYYYXXXXXXXXXXJJJJJJJ
VJJJJBBBBJLSSSSSSSSWWWLLWLOOOOOOOOLOZZZZZZMMMMMMMVTTTTTTTZZZZZZZZZZZSSSSSSSSSSSSSSFFFFFLLLLLZZZZZZYYYYYYYYYYTTTFFGGGFGGQQQYXCCXXXXXXXXJJJJJJ
VVVJJBBBBLLLSSSSSSSWWWWWWWWOOOWWOLLLZZZZZZNNMMMMQTTTTTTTMMMMZZZZZZEZZSSSSSSSSSSSSLFLLFFLLLLLLZZZZKYYYYYYYYYYTFFFFGFFFGQQYYYPKCKXXXXVJJJJJJJJ
VVVJJBBBBLLLLSSSSSSWWWWWWWWWOWWWLLLLLLZZZZZNNMMQQTTTTTTMMMMMZZZZZZESSSSSSSSSSSLSSLLLFFFLLLLLLLLLZLYYYYYYYYYYFFFFFFFFFQQQYYYPKKKKKBBJJLJJJJJJ
BBBBJPPJLLLLLSQQLWSWWWWWWWWWOWWWLLLLLLZZZNNNNMMMTTTTTTMMMMMZZYZYYYESSSKKKSSSSLLLLLLLFLLLLLLLLLLLLLYYYYYYYYYYTFFFFFFFFQQQPPPPPKKKKBBLILJJLJJJ
LLLLLPPJFLLLLLLLLWWWWWWWWWWWWWWWLLLLLLLLLMNMMMMTTTTTTMMMMMMMHYYYYYYYSSKKKSSSSSSSLLLLLLLLLLLLLLLLLLYYYYYYYYYYTFFFFFTTTQQTPPPXPKTKKBBLLLLLLLLJ
LLLLLLLFFFLLLLLLLWWWWWWWWWWWAAAAZZZLLLLLMMMMMMMMMMTTTTMMMMMMMMMYYYYYYYKKKSSSSSSSLLLLLLLTTTLLYYYYYYYYYYYYYYYYFFFFFFFTQQQTPPXXTKTKPLLLLLLLLLLL
LLLLLLLFFLLLLLLLLLWWWWWWWWWWAAAAZZZZZLLLMMMMMMMMMMMMMMMMMMMMMMYYYYYYYYYKTTTTTSSTTTTLLTLLTLLLYYYYYYYYYYYTTAAAAAFFFFZTTQTTXXXXTTTTTLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLBOOOWWWWWWAAAAZZZZZLZLLMMMMMMMMMMMMMMMMMMMMMYYYYYYYYYKKTTTTTTTTTLLTTTTTTRRYYYYYYYYYYYTTAAAAAZZZZZTTQTTTXXTTTTTTTLLLLLLLLLL
LLLLLLLLLLLLLLLLLLOOOOWWWWWWWWAZZZZZZZZZLLJPPMMMMMMMMMFFFFFMMYYYYYYYYYTTTTTTTTTTTLLTTTTTTTTRYYYYYYYYYYYOOOAAAAAZZZZZTTTTTTTTTTTTTTLLLLLLLLLL
LLLLLLLLLLLLLLLLOLOOOOOWWWWWWAAZZZZZZZZZLJJPPPMLMMMMMMFCFFFMMYYYYYYYYTTTTTTTTTTTTTLLTTTTTTRRYYYYYYYYYYYOOAAAAAZZZZZZTTTTTTTTTTTTULLLLLLLLLLL
LLLLLLLLLLLLLLLOOOOOOOOWWWWLLLAAAZZZZZZZLLJJPPMLMLLMFFFFFFFFMYYYYYYYYYYTTTTTTTTTTTTTTTTTTRRRYYYYYYYYYYYAAAAAAAZZZZZZZTTTTTTTTTTTTLLLLLLLLLLL
LLLLLLLLLLLWLLLLOOOOOOOOWWBLLLALAAZZZZLLLLJJPPLLLLLMFFFFFFFFFFYYYYYYYYYTTTTTTTTQTTTTTTTTRRRAYYYYYYYYYYAXXXAAAAAAAAZZTTTTTTTTTTTTFFFWLLLLLLLL
LLLLLLLLLLLLLLLLZOOOOOBBBBBLLLLLZZZZLLLLLIJJPLLLLLLMFFFFFFFFFFYYYYYYYYYYYYTTTTTTWTTTTTTRRRRRYYYYYYYYYYAACCCQQAAAAFCZTTTTTTTTTTTTTFWWLLLLLLLL
LLLLLLLLLLLLLLLLLSOSSSBBBBBLLLLLLZLLLLILIILLPLLLLLLLFFFFFFFFFFFYYYYYYYYYTTTTTTTWWTTTTTTRRRRRAAAAAAAAAAAACCCCCAAAAFCTTTTTLLLLLLLLWFWWLLLLLLLL
LLLLLLLLLLVLLLYLSSSSSSSSBBLLLLLLLLLLLLIIIIILLLLLLLCCCCCCCCFFFFFFYYYYYYYYTTTTWTTWWWTTTWTTTRRRRRAAAAAAAAACCCCCCCAAACCCCRTTLLLLLLLLWWWWWLLLLLLL
LLLLLLLLLLLWLSSSSSSSSSSBBBLLLLLLLLLLLIIIIICCCCCCCCCCCCCCCCFFFFFFFYYYYYYYTTTTTTWWWWWTWWTRRRRRYAAAAAAAAAACCCCCCCCCCCCCCTTTLLLLLLLLWWWWWWLLLLLL
LLLLLLLLLLLWWWSSSSSSSSBBBBLLLLLLLLLLLIICCCCCCCCCCCCCCCCCCCFFFFFFYYYYYYXYTGTTTTWWWWWWWRTRRRRRRAAAAAAAAAACCCCCCCCCCCCCCCCTLLLLLLLLWWWWWWWLLLLL
LLLLLLALLLLLWWSSSSSSSSBBBLLLLLLLLLLLLIICCCCCCCCCCCCCCCCCCCPPPFFPYYYYYYXXXGTTTTXWWWWWWRRRRRRRRAAAAAAACCCCCCCCCCCCCCCCMMMMLLLLLLLLWWWWWWLLLLLL
ALLLLLAAAWWWWSSSSZSSSSSBBLLLLLLLLLLLCCCCCCCCCCCCCCCCCCCCCCFPPPPPPYYYYXXXXXXXXXXXXWWWRRRRRRRRRAAAAAACCCCCCCCCCCCCCCCCCCMMLLLLLLLLWWMMMMVLLLLL
AAAAAAAAWWWWWWWSZZSSSOOBBLLLLLLLLLLLCCCCCCCCCCCCCCCCCCCCCCPPPPPPPYYYYVXXXXXXXXXXWWRRRRRRRRRAAAAAAAAYYCCCCCCCCCCCCCCCCMMMLLLLLLMMWWMMMMVVVVLL
AAAAAAAAWWWWWWWWWOSSSZOOBLLLLLLLLLLICCCCCCCCCCCCCCCCCCCCCCPPPPPPPYYYYYXXXXXXXXXXWWRRRRRRRRRRAAAAAAAYYYYCCCCCCCCCCCCCCMWWLLLLLLMMWMMMMMMVVVVV
AAAAAAAAIWDDWWWWOOSSSOOLLLLLLLLLLLLLCCCCCCCCCCCCCCCCCCCCCCPPPPPPPPPPPXXXXXXXXXXXWWRRRRRRRRAAAAAAAAAAYYYCCCCCCCCCCCCCCHWWLLLLLLMMMMMMMMMVVVVN
AAAVAAAKBBDDWWWOOOOOOOOOLLLLLLLLLLLUCCCCCCCCCCCCCCCCCCCCCCPPPPPPPPPPXXXXXXXXXXXXWWRRRRRRRRAAAAAAAAAAYYYYYCCCCYYYYOHHHHWMLLLLLLMMMMMMMMMVVVVV
AAAVAAAKBBIIIOOOOOOOOVVOOVVVZZZLLLUUUUUUUUUUUIIICCCCCCCCCCPPPPPPFPPFFFHXXXXXXXXPAAARRRRAARRAAAAAAAAAYYYYYYYYYYYYYYHHHHWWLLLLLLMMMMMMMVVVVVVV
AAAVVAAKBBIRIOOOOOOOOOVVVVVVVZLLLLUBUUUUUUUUUIIICCCCCCCCCCPPPPPPFFPFFFXXXXXXXXNAAAABRRAAAAAAAAAAAAAAAYYYYYYYYYYYYYHYYWWMLLLLLLNMMVMVVVVVVVVV
AAAVVVBBBBRRIOOOOOOOOOVVVVVVVZSSLLLUUUUUUUUUUIIACCCCCCCCCCPPPPPPFFFFFFXXXXUXXNNAAABBRRKKAAAAAAAAAAAAAYSYYYYYYYYYYYYYYWWWLLLLLLNNMVVVVVVVVVVV
AAAAAVBBBBRRIOOORROOOOOVVVVVVSSLLLUUUUUUUUUUCCCAAAPPPPPPPPPPPPPPPPFFFXXXXXXNNNNAAAAAAKKKKKKAAAAAAAAAAYSSYYYYYYYYYYYYYYWWLLLLLLNVVVVVVVVVVVVV
AAAAABBPRRRRROGRROOOOOOVVVVJJSSSLLLUUUUUUUUUUCCAAAAPPPPPPPPPPFFFFFFFFXXXXXXXXNNAAAAAAKKKKKKAAAAAAAAAAYSZSYYYYYYYYYYYYYNNNNNNNNVVOOVVVVVVVVVV
AAAAAPPPRRRRRBRRRROOOOOVVSFSSHSSSSLLUUUUUUUUUUMMMMMPPPPPLIIPPPFFFFFFFXXXXXXXXNNAAAAAKKKKLLAAAAAAAAAAAASSSZYYYYYYYYYYYYNNNNNNNNVVNOVVVVVVVVVV
AAGGAPPRRRRRRRRRRROOOOOBVSFSSSSSSSLUUUUUUUUUUMMMMMMPPPPMIIIIIINNFFIFXXXXXXXXXNNAAAAAALLLLLGAAAAAAAAAAASSSZSSYYYYYYYYYNNNNNNNNNNNNVVVVVVVVVVV
AAGGRPRRRRRRRRRRRGOOOOOOOSSSSSSSSSLLUUUUUUUUMMMMMMMPPPMMIIIIIIIIFFIIXXXXXXXXAOAAAAAAALLLLLLLAAAAAAASSSSSSSSSYDYYYYYYYYNNNNNNNNNOOOVVVVVVVVVV
GGGGRRRRRRRRRRRRRRBBBBOOOSSSSSSSSSSLULUUUUUUUMMMMMMPPPMMMIIIIIIIIIIHOOOOOOOOOOXAAAAAAALLLLLCASADSASSSSSSIISSYDDDDDYYYYNNNNNNNNNOOOOOVVVVVVVV
GGTTRRURRRRRRRRRRVVBBBAKSSSSSSSSSSLLLLUUUUUMMMMMMMMMPPMMIIIIIIIIIIIIOOOOOOOOOAAAAAAAAAALLLLAASSSSAASSSSSSSSSYDDDDNNMMYYNNNNNNNNNNOOOVVVVVVVV
OOFTTTRRRRRRRRRRRVVBBBASSSSSSSSSSSSLSLUUUUUMMMMMMMMMMPMIIIIIIIOOOOOOOOOOOOOOOAAAAAAAAALLLLLTASSSSASSSSSSSSSUDDDDDNNNNNNNNNNNNNNNNOOOVOVVVVVV
OOOTTTRRRRRRRRRRRVVVBBAAASSSSSSSSSSSSLLLUUUMMMMMMMMMMMMIIIIIIIOOOOOOOJJJJJOOOOAAAAALLLLLLLLTSSSSSSSSSSSSSSSUDDDDDDDDNNNNNNNNNNNNNNOOOOOOOVNN
OOOOTRRRRRRRRRRRRVVVBBAAASSSSSSSSSSSSLLLUUMMMMMMMMMMMMMMMIIIIIOOOOOOOJJJJJOOOOOAAAAIIILLLLTTTTSDSSSSSSSSSSSDDDDDDDDDINDNNNNNONOOOOOOOOOOOVNN
OOOORRRRRRRRRRRRRRVVAAAAASSSSSSSSSSSLLLLMMMMFMMOOMMMMMMMMIIOOOOOOOOOOJJJJJOOOZOAAAAIIILLLLLLTSSSSSSSSSSSSSSDDDDDDDDDDLNNQNNOOOOOOOOOOOOOOOOO
OOORRRRRRRRRVVVRRVVVAAAAAAHSSSSSSSSSLLLLLMMMMMMOOOMMMMMMIIIOOOOOOOOOJJJJJJJZZZAAAAIIQLLLLLLLLLSSSSSSSSSSSSSDDDDDDDDLLLNNQQNOOOOOOOOOOOOOOOOO
OORRRRRVRRRRVVVVVVVAAAAAAAASSSSSSSSSLLLLLLMMMMOOOOOOMMCCIIIOOOOOOOOOOOJJJJJJZAAAAAIQQLLLLLLLLOSSNNSSNNNSSSSDDDDDDDDLLLLNQQNLOOOOOOOOOOOOOOOH
OORRMMVVRRRRVVVVVVVAAAAAAAASSSSSSSSSLLLLLLLLMLOOOOOOOMCCOIIOOOOOOOOOOOJJJJJZZAAAAAAAQLLLLLLLLOSSONSSNNNSSSSGGDDDDDLLGGGQQQOOOOOOOOOOOOOOOOHH
RRRMMMMVVVVVVVVVVAAAAAAAAAASSSSKKHHHHKLLLLLLLLOOOOOOOMCCCCIOOOOOOOOOOOJJJJJJAAAAAAAAQQLLLLLLLOOOONNNNRRNONSSGDDDDDLLGGQQQQCOOOOOOOOOOOOOHHHH
MMMMMMMMVVVVVVVVVVAAAAAAAAAAASSKKHHJJKLLLLLLLLOOOOOOOOCCCCKOOOOOOOOOOOJZZZJJJAAAAAAQQLLLLLLLLLOONNNNNNNNNNGGGDDDDGGGGGQQQCCCCOOOYOOOOOFHHHHH
SSMMMMMMVVVVVVVVVAAAAAAAAAAASSSKKKHHKKLLLLLLOLOOOOOOOCCCCCCOOOOOOOOOOOZZZZZZFZZZZZZQQLLLLLLLLLOOONNNNNNNNGGGGGGDGGGGGGQQCCCCCOOOOOOOOFFHHHHH
SMMMMMMMMMMVVVVVAAAAAAAAAAFAAKKKKKHKKKKKLLLOOOOOOOOOAACCCCCOOOOOOOOOJJJZZZZZZZZZZZZZQLLLLLLLLOOOONNNNNNNNGGGGGGDDGGGGGGCCCCCCCZZZOOOOFFFFHHH
SSSMMMMMMMVVVVVVAAAAAAAAAAFIYIKKKKKKKKKKKKKOOOOOOOOOOACCCCCJJJJJJJJJJJZZZZZZZZZZZZZZLLLLLLLLLOOOONNNNNGGGGGGGGGGGGGGGGGGCCCCCZZHHOOFEFFFFFFF
VSVVMMMMMMMVVVVVAAIAAIAIIIIIIIIKKKKKKKKKKKSSOOOOOOOOOACCCCJJMJJJJJJJJZZZZZZZZZZZZZZZSSSSSSSULOOOONNNNNGGGGGGGGGGGGGGGGGGCCCCCZHHHHFFFFFFFFVV
VVVVMMMMMMMVVVVVAVIIIIIIIIIIIIKKKKKKKKKKKKSSOOKKKKOQUACCCJJJJJJJJJJJZZKZZZZZZZZZZZZSSSSSSSSOOOOOGGNNGGGGGGGGGGGGGGGGGGGCCCCHHZHHHHHFFFFFFFFV
VVMMMMMMVVVVVVVVVVIIIIIIIIIIIKKKKKKKKKKKKKDDDDDKKUOUUUULLJJJJJJJJRRRRZZZZZZZZZZZZZZSSSSSSSSOOOOOGGNNGGGGGGGGGGGGGGGGGGCCCCCHHZHHHHHYHFFFFFFF
VVVVVVVMVVVVVVVVIIIIIIIIIIIIIKKKKKKKNNKKKDDDDDDKKUOUUUULLLJJJJJJJRRRRRRZZZZZZZZZZZZSSSSSSSSOOOOOOGGGBGGGGGGGGGGGGGGZZGCCCCHHHHHHHHHHHJFFFFFF
VVVVVVVVVVVVVVVVIIIIIIIIIIIIIIRKKKKKPNNNNNDDDDDDDUUUUUUULLJJJJJJJRRRRRRBRZRZZZUZZZZSSSSSSSSOOOOOOGGGGGGGGGGGGGGGGGGGGGCCCHHHHHHHHHHHHFFFFMFO
VVVVVVVVVVVVVVVIIIIIIIIIIIIISSSTTKDDDNDDDDDDDDDDDDUUUUUUSLLJJJJJJZZRRRRRRRRRRRUZZZZSSSSSSSSOOOOOOGGGGGGGGGGGGGGGGGGGIGCCCCCCHHHHHHHHHIIFFVVV
VVVVVVVVVVVPVVIIIIVIIIIIIIISSSSSSSSGDDDDDDDDDDDDDDUUZZZZZZZZJJOJJJRRRRRRRRRRRRUZYZZSSSSSSSSOOOOGGGGGGGGGGGGGFGGGGGGKOCCCCCCCMHHHHHHHHHHNNVVV
VVVVVVVVVVUUVVUUIIIIIIIIIIISSSSSSSGGDDDDDDDDDDDDDDDUZZZZZZZZJJOOJJJRRRRRRRRRIRUUYYOSSSSSOOOOOOOOGGGGGGGGGGGGGGGGGGGOOOOOCCMCMMHHHHHHHHHHVVVM
VVVVVVVVVUUUUUUUIIIIIITISSIISSSSSSSSDDDDDDDDDDDDDDDIZZZZZZZZJJOOOJRRRRRRRRRRUUUUYYYSSSSOOOOOOOOGGGGGGGGGGGGGHHHHTGTTOOOOOOMMMMMMHHHHHHHMMVVM
PVVVVVVVUUUUUUUUIIIIISSSSSSSSSSSSSSSDDDDDDDDDDDDDZZZZZZZZZZZOJOORRRRRRRRRRRUUUUUUUUSSSSOOOOOOOOPPGGGGGGGGGGHHHHHTTTOOOOOOOMMMMMMMHMMHHHMMMMM
PVXVVVVVVUUUUUUUUIIISSSSSSSSSSSSSSGFFDDDDDDDDDYYDZZZZZZZZSSOOOOOOORRRRRRRJUUUUUUUUOSSSSOOOOOOPPPPGGGGGGGGGGHHHHHTTOOOOOOOOOMMMMMMMMHHHHHHMMM
PPVVVVVVEUUUUUUFUUFJJFSSSSSSSSSSSSFFFIDDDDDYYDDYYZZZZZZZZSSSXOOOOOORROZRRJJUUUUUUUUSSSSOOOOOOOPPGGGGGGGGGGGGHHHHTTTOOOOOOOOMMMMMMMMHHHHHMMMM
PPPPVVVVEEEUUUFFFFFFFFSSSSSSSSSSSSFFFFDDDDDRYYYYIZZZZZZZZXXYXXOOOOORROORRQJUUUUUUUUUOOOOOOOPPPPPGGGGGGGGHGHHHHHHTTTOOOOOOOMMMMMMMMMAMUUHHHMM
PPPPPEVEEEEEEYFFFFFFFFFSSSSSSSSSSSSFFFDDDDDDYYYYYZZZZZZZZXXXXXXOOOOOOOOQQQJUUUUUUUQOOOOTOOOPPPSSSSGGGGGHHGHHHHHHTTTOOOOXXOOMMMMMMMMAMUUUHMMM
PPEEEEVEDEEEYYFFFFFFFFFSSSSSSSSSSSFFFDDDDDDYYYZZZZZZZZZZZXXXXXXOOOOOOQOQQQJUUUUUUUQQOOOOXOOPPPPSSSGGGGGHHHHHHHHHHHTTOOOXXXXMMMMMMMMMMUUUHMMM
PPEEEEEEEEYYYYFFFFFFFFFSSSBSSSSSSFFFFFDFDDDYYYZZZZZZZZZZZXXXXXXOOOOOQQQQQQJUUUUUQQQQQQQQOODPPPPSSBBGGGGHHBHBHHHHHTTTTTTXXXMMMMMMMMMMMUUUGGGG
PPEHEEEEEEEYYYFFFFFFFFBBBBBSSSSSSSFFFFFFDYYYYYZZZZZFXXXXXXXXXXXOOOOOUOQQQQUUUUUUQQDDDQQQQQDDDPPSGBBKBOBBBBBBHHHHHTLTTTTXXXXMMMMMMMFFUUGGGGGG
PPPEEVEXEEYYYYFFFBBFFBBBBBBBSSSSSFFFFFFFYYYYYYZZZZZFFXAXXXXXXXXXOOOOOOQQQQQURUUUVQDDDDDDJQDPPPPSGGBBBBBBBBRRHHHLLLLLLTTTXXXXXXMMTFFFUGGGGGSS
PPPEEVEXXXXYYYYFFBTTBBBBBFFBSFSFFFFPPFYYYYYYYYZZZZZFFAAXXXXXXXXXOOOOQQQQQQQQRQQVVVDDDDDDDDDDDPPPBBBBBBBBBBBBHHHHLLLLLTXXXXXXXXXXFFFFFGGGGGGS
PPPEPXXXXXYYYYYFFFTTBBBBBFFFFFSFFFFPPPGSSSYYYYZZZZZFAAAAXXXXXXWOOOOOQQQQQQQQQQQQVVDDDDDDDDDDDPPPPBBBBBBBBBBNNLLLLLLLLLLXXXXXXGFFFFFFGGGGGGGG
PPPPPXXXXXYYYYYYTTTTTTCFFFFFFFFFFFPPPZZZZZZZZZZZZZZZZAAAATAXXWWWWWAQQQQQQQQQQQXVVVDDDDDDDDDDDPPPPBBBBBBBBBBLLLLLLLLLLLLXLLXXXGGFFFFFGGGGGGGG
PPPPPXXXXXXYXXTTTTTTTTFFFFFFFFFFFZZZZZZZZZZZZZZZZZZZZJAAAAAAWWWAWWASQAQQQQQQXXXVVDDDDDDDDDDDDPMBBBLBBBBBBBBLLLLLLLLLLLLLLXXGGGGGGFGGGGGGGGGG
PPPXXXXXXXXXXXTTTTTTTTFFJFFFFFFFFZZZZZZZZZZZZZZJJZZZZJAAAAAAWWAAAAAAAAQQQQQXXXXVXDDDDDDDDDDDDPMBBLLLLBBBBBLLLLLLLLLLLLLLLLLLGGGGGGGGGGGGGGGG
PPPXXXXXXXXXXXXTTTTTTTTFFFFFFFFFFZZZZZZZZZZZZZZZZZZZZJAAAAAWWAAAAAAAQQQQQQXXXXXXXYDDDDDDDDDDDMMMMMMMLBBBBBBBLLLLLLLLXXXXXXNNNNNGGGGGGZGGGGGG
PPPXXXXXXXXXXXXXTTTTTTTFFFFFFFFFFZZZZZZZZZZZZZZZZZZZZJAAAAAZZZAAAAAAJJJQQQQXXXXXYYDDDDDDDDDDDMMMMMMMLLBMBBLLLLLLLXXXXXXXXXNNNNNGGGGGGZGZZNGG
PPPXXXXXXXXXXXXXXTTTTTTTVVDFFFFFFZZZZZZZZZZZZZZZZZZZZJAAAAZZZELALLAJJJJJQQXXXXXXYXDDDDDDDDDDMMMMMMMMMMYMYYLLLLLLXXXXXXXXXXNNNNPPPPGZZZZZGGGV
PPPXXXXXXXXXXXXXTTTTTTTDDVDFFFFFFZZZZZZZZZZZZZZJJJJJJJAAZZZZZLLLLLJJJJJYXXXXXXXXXXTDDDDDDDMMMMMMMMMMYYYMYYYZLLLLXXXXXXXXXXNNNNNPPPPZZZZZZZZZ
PPPPXXXXXRRXXXEXTTTTTDDDDDDXDDMMFFFFGZZZZZZZZZZJJJJJJJJJJJJJZZZZLCJJJLLYYXXXXXXXXXXDDDDDDDMMMMMMMMMMMYYYYYLLLLLLXXXXXKXXXXNNNNNNPPPZZZZZZZZZ
PPPPXXXXXRXXXXXXTTTTTTDDDDDDDDDMIFZFGZZZZZZZZZZAAGAAZJJJJJJJZZZZLLJJLLLYYYYXXXXXXXQDDDDDDDMMMMMMMMMMMYYYYYYYLLLRXXXXXNXXXXNNNNNNPPPZZZZZZZZZ
PPPPPXXXXRXVXXTTWTTTDDDDDDDDDDDMIPFFULLLLLLGGGGGGGGAZJJJJJJJZZZZZLLJLLLLYYYXXXXXYYYYYDDDDDMMMMMIIMMMYYYYYYYYZLLRRXXXXNXXXXNNNNNNNNPZZZZZZZZZ
PPPPPPDXDRXVVDATTTTTDDDDDDDDDDBIIIUUULLHLGGGGGGGGGGZZJJJJJJJZZCLLLLLLLLLYYYYXXYYYYYYYGGGMMMMMMMMIIMYYYYYYYYYZRRRRRZMNNXXXXNNNNNNNNNLZZZZZZZZ
PPPPPPDDDRDDDDTTTTTTDDDDDDDDDDDIIUUUILLLLLLLGGGGGGGGZJJJJJJJZCCLLLLLLLLLUUUXXXYYYYYYGGGGMMMMMMMMIIMMYYYYYYYZZRRRRZZMMNXXXXNNNNNNNNNNZZZZZZZZ
PPPPDDDDDDDDDDNNTTTTDDKDDDDDDDIIIUUIILLLLGGLGGGGGGGGZJJJJJJJCCCCLLLLLLLLUUYYYYYYYYYYYGGGGGMGMMMMMMMMYYYYYYYYZRRRZZMMMMXXXXNNNNNNBBNZZZZZZZZZ
PPPPPDDDDHDDDDDDZZZKKKKDKKDDIIIIIIIIILLLGGGGGGGGGGGGGJJJJJJJCCCLLLLLUULUUUYYYYYYYYYYYGGGGZGGGGMMMMMYYYYYYYZZZZZZZZZMMMXXXXNNNNNNBBNZZZZZZZZZ
PPPPPDDDDDDDDQDDDZZKKKKDKKKDDIIIIIIIIIILGGGGXGGGGGGGGJJJJJJJCCCCLLLLLUUUUUUYYYYYYYYYYGGGGGGGNGMMMMMYIYBBBZZZZZZZZZZMMMMMMNNNNNNNBBZZZZZZZZZZ
PPPDDDDDDDDDDQDQZZZZKKKKKKKIIIIIIIIIIUULGXXXXGGGGGGGGJJJJJJJCCCCCLLLLUUUUUUUYYYYYYYYYGGGGGGGGGMMMMMMMYBQQQQZZZZZZZZMMMMNNNNNNNNNBBZZZZZZZZZZ
PPPPDDDDDDDDZQQQZZZZZKKKKKKIIIIIIIIIIYYYYYXXYGGGGGGXXXXXXXXXXCCCCCLLLUUUUUTUYYYYYYYYYGGGGGGGGGMMMMMMBBBQQQQZZZZZZMMMMMMMNXXNNNBBBBBBZZZFZZZZ
PPPPDDDDDDDDZQQQZZZZZZZKKKKIIIIIIIIIIYYYXXXYYYYGXXXXXXXXXXXXCCPCCCCCUUUUUUTUYYYYYYYYYYGGGGGGGLMMMMMMBBBQQQQBZZZZZZZMMMSSSSXNNNNBBBBBZQZZZZZZ
PTTTDDDDDDDDZZZZZZZZZZZZKKKKIIIIIIIIIYYYYYYYYYYXXXXXXXXXXXXPPCPPCCCCCUUUUUUUYYYYYYYYYYGGGGGGGMMMMMMMMBBQQQQBZZZZZZZMSSSSSSSLLBBBBBYYQQQQQZZZ
PTTTADDDDDZZZZZZZZZZZZZKKKKIIOOIIIIIIYYYYYYYYYYYZXXXXXXXXXPPPPPCCCCCCCUUUUUYYYYYYYYYYYGGGGGGGMMMMUMUMKKQQQQZZZZZZHHSSSSSLLLLLBBBBYYQQQQQQQZZ
TTTTAADTDDDZZZZZZZZZZZZKKKKIIIIIIIIIIIYYYYYYYYZZZZZXXXXXXPPPPPPPPCCCCCUUUUUUYYYYYYYYYMMGGGGGGMMMUUUUUUKQQQQZZBZZZZSSSSSSSLLLLLBYYYYYYQQQQQQQ
TTTTTATTTTDDZZZZZZZZZKKKKKKIIIIIIIIIIIIYYYYYYYYYZZXXXXXXXPPPPPPPPPCUUUUUAUUYYYYYYYEEEGGGGGGTMMMMVVUUUBBQQQQNNZZZZNSSSSSLLLLLLLBLLYYYYYQQQQQQ
TTTTTTTTTTZZZZZZZTZZKKKKKIIIIIIIIIIIIGIGYYYYYYYYZZXXXXXXXXPPPPPPPPCCCUUUAUUYYYYYYEEEEEEESGGTTTMUUUUUUBBQQQQNNNZNNNSSSSSSSLLLLLLLLYYYYYQQQQQQ
TTTTTTTTTTVVZZZZZZZZZZZKKAAAIAAIIIIGGGGGYYYYYYYYZYYYXXXXXXPPPPPPPPCCCUUUAAAYYYYYYEEEEEEEEGEEEEMMUUUUUUUXXBKKKINNNNSSSSSSSLLLLLLLLLYYYYYLQQQQ
TTTTTTTTTTTTPZZZZZZZZKKKAAAAAAAIIGGGGGGGGYYYYYYYYYYYXXXXXXPPPPPPPPPCCUUAAAAYYYYEEEEEEEEEEEEEEEMMUUUUUUUXXBIIIIIIIISSSSSSSLLLLLLLYLYYYYYLLLLQ
TTTTTTTTTTTTTLLZZZNAAAALLAAAAAGIGGGGGGGGGYYYYYYYNYXXXXXXXPPPPPPPPPPPPPIIAAAAAYYEEEEEEEELEEEQEMMQUUUUUUUUIIIIIIIIIIISSSSSSLLLLLLLYYYYYYYLLLQQ
TTTTTTTTTTTTLLZZLLAAAAQQLCAAAAGGGGGGGGGOGYYYYYYYXXXXXXXXXPPPPPPPPPKKIIIAAAAAAAEEEEEEEEEEEEQQQQMQQUUUUUUIIIIIIIIIIIISSSSSSSLLLLLYYYYYYYYLLLLQ
TTTTTTTTTTTTLLLLLLLLAAQLLLALAAAGGGGGGGGGGYYYYYYYXXXXXXXXXPPPPPPPPPPPIIIAAAAAAAAEEEEEEEEVVVQQQQQQQQUUUVVIIIIIIIIIIIISSSSSSSLLYYYYYYYYYYYLLLQQ
TTTTTTTTTTTTLLLLLLLVAAVVLLLLGGGGGGGGGEGGGYYYYYRYYXRRXXXXXPPPPPPPPPPPPIIIIAAAAAAAEEEEEEEVVQQQQQQQQQQUVVVVVIIIIIIIPIISSSSSSSLYYYYYYYYYYYYYYYQQ
TTTTTTTTTTTTLLLLLLLVVVVVLLLLLGGGGGGGGEYYYYYYYYRYRRRRXXXXXPPPPPPPPIIIIIIAAAAAAAAAEEEEEEEQQQQQQQQQQQQUVVVVVIIIIIIIIIGSSSSSSSSYVVYYYYYYYYYYYQQQ
TTTTTTTTTTTTTLLLLLLLVVLLLLLLGGGGFGGGGGGYYYYYYYRYRRRRXXRRPPPPPPPIIIIIIIIIIIAAAAAAAAAEEEEQQQQQQQQQQQUUVFFFIIIIIIIIYYGGSSSSSSSSVYYYYYYYYYYQQQQQ
TTTTTTTTTMTLLLLLLLLLLVLLLLLLGSSGGGGSSSYYYYYYYRRRRRRRRRRRRRPPPPPIIIIIIIIIIIIAAAAAAAAEHEEQQQQQQQQQQQQQVVFFIIIIIIIYYYGGGVVSVSVVVYYYYYYYQQQQQQQQ
TTTTTTTTLLLLLLLLLLLLLLLLLLLLGSSSGTGSSYYYYYYYYYRRRRRRRRRRRRRPRRIIIIIIIIIIIAAAAAAAAAAEHEEQQQQQQQQQQQQQQFFFFIIIIIIIIYYGGGVVVVVVVYYYWYYYQQQQQQQQ
"""

for data in inputs():
    print(*garden_groups(data.strip()))