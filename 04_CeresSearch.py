# https://adventofcode.com/2024/day/4
# Day 04: Ceres Search

def ceres_search(data):
    A = data.split()
    part1 = part2 = 0
    for _ in range(4):
        A = [*zip(*A)][::-1]
        m, n = len(A), len(A[0])
        for k in -1, 0, 1:
            for i in range(abs(k), m):
                scan = ''
                for j in range(n):
                    scan += A[i][j]
                    i += k
                    if i < 0 or i == m:
                        break
                part1 += scan.count('XMAS')
        for i in range(m-2):
            for j in range(n-2):
                part2 += A[i][j] + A[i][j+2] + A[i+1][j+1] + A[i+2][j] + A[i+2][j+2] == 'MMASS'
    yield part1, part2


def inputs():

    yield """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

    yield """
MXXMASAMXSAMXSXMAMXXAMXASAXASMSMXAAMAMXXMMXAMXSXMAMSAMSAMMXASXXXXMXSXMSMSXSMSMMSSMMXSAMXSSSSXXXMMSSSMMXMAMXAXAMXMSMSSSMMSASMXSXAAXMSSMXXXSXS
SASAMXSAMAMXAAAMSMSSMSAMXMAMAAAMSSMMSMXXMAXSAMXMMAAAAASASMXSXAMSMSAAXXMASASAMXXAAAXAXXMAXMAMAMSAMXAAMMSXXASMSMAMXAASXXAXSAXAASXSXMXAAAMMMMAA
MASXSXAMMSXMSMMMMAMAASASMAAAMXMMXAMAAAASMAXMAMAMSASMMMMAAAMMMXMAAMMXMSMAMAMAMMMSSMMAMMMSSMAMAMSAMMXMAAAASXSXAMAMMMSMASMMMMMMMSAMXAMSSMXAAMXM
MXMAMMMMAXAMMAAAMAMMMMAMASMXMXXXSAMSSMMMMMMMAMMMAAMXSSMSMAMXAMSMSMSAAAMAXXAMXXAMAMXMXAAMAXXSAMXAMXAXMMXXSASAMSXSASAMMMMAAAXMAMAMAXMAMASXXSAS
SXMXMAXMASAMSSMMSAMMAMAMXXMASAMXMXMXAAXAAMMSAMXMXSMSMSAAXAXMXMASAAMMSMSAMXXAXMMSAMSMSAMSAMXXMSSSMSMSASXMMXMAMAXMMXASMAASXSMXAMAMMXMASAMMXMMM
MMMAXMXMAMAMXMAXSXMXAXXXSMSAMAAMSAMXSASMMSASXSASXMXXAMXMMMSMSSXSMMMXMXMASMSMSAMSXMAAXAXMAXSSMAXAAAASAMMAMAMMMSSSSSXMMSXMMMASMSMSAASAMAXXAMAS
XASMSMSMSSMMAXSXMMMSSMSAXAMMSMMXSASAMMXMAMMSAMASAXMMXMXSAAAAXMASAMSASAMSMAAXAXXXMSMSMSMSXMMAMSSMMMXMAMSASXSXAXXAAMXMMMASMMMMXAAMMMMAXSMMASAS
MMAMAMSAXXXSXSMMSMMAAAMAMSAXAAXASMMMMAAMAMXMAMSMMMASMMASMSMSMMMMAMSASMSAMMMMMMSMAXAXAMXMMXSAMAAMXMASAMXAMXAMXSMMMMSMXSAMMAAAMSMSXSSSMXASXMAS
XMAMMSMMMMMMMSMAAAMMSMMXMXASXSMAXXAAMSMSASAMMMMASXMXXXAXAAAXXSAMXMMAMXSAXXASXAAMSMMMXSAMAASAMMSSSSMSSXMAMMSMSXMASXAAAMAXSSMMAAXMAAAAXXXASMAM
ASXMSAXAAAMAAMMSXSMAMMMAXMASAMMSMMMSMXAMASXSMASAMMSMSMASMMXSAMXXAXMAMAXAMXMSMSXMMAXMASASXXMAMXXXMAMXASMMMAMMXAXXSSMMSSSMMXSASMSMMMSMMSSMAMAS
MAMXSASXXSSSXXAMXXMASASMSMXXAMXAAAAXAMAMAMAXMAMAMMAAXMAXAAXMAMSSMMSASXSSXSAXAXMXXSMMMSXMASMAMXMMSMMMMAXAMXMSSMMMXMXMAAAAXAMXMSMXSAMXXAMXMSAS
AXSAMXMXSMMASMAMXXMASXMXXXMSSMSSSMSMASMMMSMSMASAMSMSMSMSMMMMSMAAAXAMXAXAAMMMMSMSXMASXSXMAMMAXASAAXASXMSXSMMAAAXMASAMMSMMMMSAMASXMXXXMMSSXMAS
MXSAMXMXAAMAMMAMMMMMSXSXMAMAMAMAXAXXAMXXAMXMXASXXAMAXAAAXAXMXMMXMSXSMMMMMMMASAAXAXXMXMXMAXAXSASXMXAXAXMMSAMSSMASMSASMAAXMASXSASMMSMXMXAMXMAM
XAMAMAAXMSMSSSSMSAASMAMXMAMASXMSMMMMMSSSXSASMXXXXSSSSMSMSMMSAMXSAMXXAAAXAASMSMSMSMMSAMMSXSMMAXMAASXSMMSASAMAMMXXXSXMXSSMXMSAMXSAAXMAXMMMSMAM
MMSAXMSMXMAXMXMASXSMMSMMMAXAMAAXMAAAXXAAASASXMMSXMAMXAMMXAAMAMAAAXSXXAXXMXMXMXAAXAASASAMMMXAAAMXMMAAMAMXSSMXSSSMMMMSAMXMAAMMMMSMMSSXSXSASASX
XMAMAAAXAMMMMAMMMMXASAMAXSSSSMMMSSSSSMMMMMMMXMAXAMXMMMMMXMSSSMSSXSMMSSSMSASASXMSMMMMXMAXMMAXSMSAXMSMMXSAMXXXSAMXAAAMASASMSMXMASAMXXXAXMASAXA
MMAMMXMXMSSMSMSMAMXXMAMSMMAAMMMAXAAXMXXAXAXASMMSSMAXASAMMXAAAAXXMSAAAXAASXSASMMMAMXXSSSMAMSMXXSXSMMXXMMMXMSMMXMXSSMMAMXMXAMXAMXAMAMMMMMAMMMM
AMSMSASMAAXXAAAMAMMAMXMAAMMMMSMMSSSMMSMMSMSAXSAAMSSSMSAMASMMMMMMMSAMSMMMMMMMMMMSSMMXMAMMAMMAMMMXMAMAAMASAMXXMASXAAXMSSMSSXXMSMSAMASAMMMAAMAS
SMXASASMMMSSSSMSMSAXAAMMSAMXXMAMAAXAXAAXAMMAMMMMMAMXASXMXXAXSXMAMMXMAAXAMXAAASMAAAMXMAMSSMMAMASMMSMAMSASMSXMSASMSMXXAAAAMXSMMAAXXXMASXSMXSAS
MXMMMAMMMMAAXXAXAXMMMSSMAXMAMXAMMMMSMXMMASXMMMSMMMSMXSXMXASXMASMSSMMXSXSMSMSSSMSSXMAMMXAMXSASMSAAXXSMSASXMMAMXSAMSMMSMMMMXSAMMMMMASAMAMSAMXX
SMSMMMMMAAMXMSXMAAMAXXAXMSXMSSSXSAAXMMSSMMMXSAMMAAAAMMAMSAXAMASAXXAMSAMXMAAMXXXAXXMSSSMASXSASASMMMMAAXASAMXSMMMMMAXAAMAXMAMXMSAXSAMXSAMMMMSX
SAMXAASXSSXMAMAAXXSASXMMXMASMAAASMSMSAAAAAAXMAMSMSSSMSAMXASXMASMSMSMSAASMXMMMSSMMSAMXASAMAMAMMXXMAMMMMSMMMAMAAAASMMSSXSAMXXAXMXMAASAMXSXXAAX
MMMXMSAAAXXAXSMMMXAXSAXMXSSMMMMMMAAAMMSMMMSXMAMXXAAAAXXXMMMMMXSXXAAASMMMXSAAXMAAAAAASMASMMAASXSMSASAXMXAAMAXMMSXSAAAXXXAAAMSXMXMAXMASXSMMMSX
MSSSMXMMMMMSXMAAMMSASMMMAMAAXXXSMSMSMAXXXSAMSASMMSSMSMSXAAAXSXMMMSMXXAXAAXXMSSMMMSMMMXMXSXSASASXSMSAMXMSMSSSMAXASMMSSMSAMSXMASMMMXSXMXMASAAM
XAAAAXXMMXAAMMSMSAMMXAAMASMMXAMXAMXXMASMMSAMSAMMAXAAXAMXSSSSMAXSAXSSSSMMMXAXMASXMAMXXSXMMMMMMMMAMMMMXMMMXAAAAXMAMAAXAAXXMXASXMAAXAMAMMSAMMMA
MMSMMMSMAMSMSAXAMXSSSSMSMSAMSSMMAMXSMXSAAMAMMSMMXSMMMSAXXXMAMAMMMSXMAMXAAXSMMASMSSSMXMAMMXAAXAMXMAAXAMASMMSXMAMSAXXMAMMASMMMSSSMMXXAMAMMSXXS
AAAAMAAMSXMAMAMXAMAMAXAAASAMAXAMASAXAASMMSSMXMXXMXXMSXXXMMSSMXSAMXMMAMMXSMMAMASAAXXMASAMAMMXXXSASMSSXSASAAXAXMMAMSAAAMSMMAAAXMAMSMXMSXSMMAMX
SSSSMXXMMAMSMXMASXMMAMSMXSXMASXMAMXXXMXAAAASAMAAAMMMMXMAAAAAXMSASXAMASMAXASXMASMXSMSMSASXSSSMASASAMMAMXSMMSMMMXAMXXMXXXASXMXSXMMAAAXMASXMASM
AXAXASXXMXMAMAMAXAXMMMXMASXMAMXMASMSMSASMXSMMSMSXXAAXMSASMSSMMSSMMMSAAMASAMMSXXMAMASASAMAAAAMAMMMMMMAMXMAMMMASMSSXMMMASXMASXSXSSMSMSAXMASASA
XMAXSAMXMASMSAMXSSMMXMAMAMXMASASMMAAAXAMMXMXMAAMAMSMSAMAXMAXAXMASAXMMMMAMAMAAAMMSXSMMMAMMMMMMXXAMXAMAMAXAMASMSAAXAXMAXMASXMAMAAXXAXAAMSXMAMX
SXAXMMXMXASXSXXMMMMSASXMASMSASMSXSMMSMMSXAXASMSMMMAASMXAMMSSSMASMSMXAXXMMSMMSXSAMMXXXMAMXSSMXXMAMXSSSSXSASXMMMMMXMMMSMXMMXMAMXMASMSMXAXMMSMM
SAMXSMMSXASAMXMAAAASMSXSXMAMASXMAMXAXAASMASXMMXMXSMMMMMMXXXAXXXMMXXMASMSAMAMAMMASASMSMMXAAASAMSSMAXAMXAMXSAMSAMMASAMASMASXSASXXAMAAAXSXSAMAS
MAMAXAAXMMMXMAAXMMMSXXAMAMSMMMAMAMMMXMMSSMXMAXAXMXMMAXXAMSMMMXSASXMASMAMXSSMAAMXMASAAXSMMSXMXXAXMXMAMMSMAMAMXAMSASASASMXMAMASMMMMMMMMMAMASAM
SAMXSMXXAXAASASAMXXMMMAMAMAASXMSXSASASMMXXMASMSSMMASMMMMSMAAAXSAMSASAMSMXMXSMSXSMMMMMSMAAMAMMMMSMMSAMAAMASAMXXMMXSAMASASMSMXMAXAASMMSMAMMMMM
XXMMMASXSMSMSAXMMXSXAMSXMXSSMAXAXMASAMAMXMSMXAXSAAAXXAMXAMSMSMMAMASAXSXSXSASMMAAASAMMXXMMSASAAXAAASAMSMSASMXAMXSAMXMSMXMAMXAXASXMSAAXXSMXMAS
SXSASAMXAAMAMXMXXAXMSSMAXAMAMSMMSMMMXSXMAXMAMSMSSMSSSMSXMMXXMASXSXAMXSAMXMASAMSMMMAMSAMXASAMMSSSSMSSMAXMASASMMMXAXMMMMMMAMMSMASMASMMXAMXMSMA
AASMMASXMXMAMMMMMSSMMAMMMXSAMXXXAAAAXMASAXMAMAMXXXAAAAMMSXMASXMASAMXMMAMAMAMAXAXAXXMMMSMMSMMXXXAXASMMSSMXMAMAAXXXMMMSAAMASAXMAMMAMAAXSMSAAXM
MXMXSAMMXMSAMMAXMASASAMMAMMXMXMSSSMMXXAMXASASMSASXMSMMMAXASAMAMXMXXMXSAMXMXSMXSXMXXSAXMXAXXXXXMMMMMMAMMMMMAMSMMASAMASXSXXMAXMAXMXMAMXMAMSAMX
MXMASAXXMAXAMXMMSASMMASMAAASMMAAAXASMMAMMXXASXMASAAMAMMMSMMMSMSMMXXXAMASMMMXMAMASAMSMSMMMXXXMXMXAAAMASAAAMXXAASMSAMXSAMXSXMXSSSSSMMMAMXMASAX
XXMASXMMXSSSMXMMMAXAMAXXXMXMASMMMSAAMXMASMSMMASAMMMMAXAMXMMAAAAASASMSSSMAMAXMASAMAMMAAXAXMSMSASXSXSXMSMSXSMSSMMXSXMMMXMAMSXXXAAAXMASAMXAAMSS
MXMAMAMXAAAMAASMMSMAMMSAMXMSMMAXXMMXAAMXAAAMXXMASXSSSSMXAMXXMSMSMASAAMASMMSXSAMXMXMXXSXMSXAASASAMXMMMMAXAAMAMAXAXAAMAAMAMMXMMMMMSSMSSMSMMSAX
MXMSSSSMMSSMSMSAAASAMMAMXAAAXMMMXXSXMXSSMSMMMXMAMAAAAXMMSMMAMMMAMXMMMSAMXAAAMMXMXSMSAMAAAMMMMMMAMMMAMMAMXMMSSMMSSSMMXSSMSMAAMXMAXMAXAXSAMMMS
AMXMAAXAAAAXXAXMSMSXXXSXSMSMSASMSMMAXSAXXAAASMSSMMMMMMSAMAXXMAXXMAXAXMAXMXMMMSSSXAASASXMXMMMSAMAMASMSMXMXXAXXXAXAMAXSAXMAMSXSAMMSMMMMMSAMAAX
AAMMMMMMMSSMMAMXAAMMMMMASXMASAMXAAMMMSAMXMMMSAMXXAMSMAMASXMASAMMSMSMSMMMSMXSAAAXSMAMAMMSAXSASXSASXSXSXAXMMXMMMXSXSAMMMXSXXXASXXMAAAAXASXMMSS
MSAXXMXAAAMXMAXMMMMAMAMAMMMMMAMSSSMAAMXMMMSXMXMMMSMMMAXMMAAMMASXAAXXAAAAAAXAMMXMXMAMAMASAXMAXMAMXAMAMMXAXSASAAASMMXSMXXMMMMMMAMSSSMSMXMASXAX
SAMAAMSSMSSMMSSMSASASAMASAXAMXMXXAAMASMSXAAXMMMSAMASXMASAMSXSAMMMMMXSSMSSSMMXAXSXMASAXXMSMMAMMXMMMMSMAMMASASASXSAMASAMXAAMAMMSMAAAAXMASAMMSM
XAMMXMAAMXAXAXAASMXMSASAMASXXMSXSXMXXXAXMMMSXAAMMSAMAXXAAXXXMAMMSASAXMAMAMAXMMSAAMAXXMAAAXMMSAAXAXMAMXMMAMXMAMMSAMASASMSXXAMMMMMXMMMSXMASXMA
MMMXXMSSMSAMMSMXMASAMAMAMMMXAASAMXMXMMXSASMMXMSSXMASMMSMMSSMSSXASASMMMAMAXAMAXSMSMSMSAMXMXAXMMSXMMXMXASMSMSXAMXSXMMSAMAAASXMSAAMMSAMXSMMMAMS
XASAMMMXMMAMMXXSXMASXXMMMMASMMMMMAAAXAASXMAAMSMMXXMAAXSAMMAMAMMMMMMXASXSMSMXMXMAXAXASAXMMXMXSAXAXSSXMMSAMASMSMXMAMMMAMMMMMAASXXSMMASASXAMAMA
MMMMMAXAMXXMXSXSAXAMMXMSMMAMAMAMSMSAMMMSXSMMMAAMMSSSXMSAMSAMASAXSSSSMMXSAAAASAMXMASMSAMXMASMMASMMMAAAMMAMAMAAMMSAMAXAMAASMMMMASAXMXMASMXSSSS
XAAAXMSMSAMAXMASMMSMSAMAAMAMASAMAAMXMMXMAMMXSMSAAAMAMXSXMSMXMSMSXAAMMMAMXMMMSASXSAMXSAMXSAMAMAMMXSAMSSMSMAMXMXASMMMSSSXXXAXMASAASXMMXMAXXMAM
MSXSXXAXMAMMMMAMAAAAMASMMMMSASMSMSMASXMXAMMMMXXMMXMAXAMXXMSAMXMXMMMMAMXSXSXASAMXMASAMAMAMMXSAMXSAXASXAAASXSMSMMSAXMAMMMSSMMMSMMMMAASXMSMSMSM
MMAXXSASMSMSAMXSMMXMMAMAMAMMAMASAAMMSAMXMSXAMAMXXMSMSMSXMASXSAXMAAXXASAMAXMMMAMXSAMXMSMSMSAMAMAMXXMMMMSMSMSAXMMMXXMASAAXASXSXXMXSXMMAMAXSAMX
AMXMAXASAAXXXXXSASAMSASAMSMMXMAMXMMMSMMASAMMSSXMXMAAAMAAMAMXSAMSSMSSXSAMXMXSASMXMASXMXAAAMXSAMSMSASASXMASAXMASAMMMMXSMMXAMXAMSMXAMAMAMAXMAMX
MMMSSMMMXMMSSXMSAMAMSAMMMMAMXMXSMMAAXAXXMASXAXAMASMSMSXXMASXMXMAAAXXMXAMAMASAMAXSAMXAMSMSMAMASAAXAMMXAMAMXSXASXSAASMMMXMXMMSMAMXMASMMSSMMAMX
XXAAAAXXXMAAXMAMAMMMSXMXAMXMMMAMASMSSMMSMMMMMSSSXSXMXMXMMMSAMXMSMSMASXSMXSAMAMSXMASMXMAAAMASXMMSMMMSMSMAMMSMMMAMXXXAAASXSMXXSMSXXAMAAAMASASX
SMMSSMMXXMMXSAXSAMXAXASXSSMMAMAXMMAMAXAMASXAXAAMMXAMMSASAAXXMAXMAMMAMXMAXMXSXMXASAMXXAMMMMXSAMXAAAAXAXSASXXAASAMXSSMMMSAAMAMAXAXMMSMMMSAASAX
AAMAMASXMMSASMMSXXMXMSMAXMAXMMXSMSSMAMMSAMMMMMSMAXAMXSXSMXSASMSMAMMXXAMXMAAXMASAMASAMXMASMMMMMSXSMSMMMXXMASXMSASAASXAXMXMMASAMSSMAMAMXMASMSS
SXMAMAMAMAMMSAMSXMASXAXXMSSMXSXAAAXMXSXMASAAXXMMXSAMXMAMAXSXMAAMSMAMXMSMSMSSMAMASXMXMASASAAXSAXXXXXAMSAMXAXMASAMAAMSMMMASXXMAMAAMAMSAMXMMMAM
XXMSMMXSMXMAMAMXAMAMSMMXAAAAAXSMMMSAMMXXAXXXMMXAAMAMAMXMSMSAMSMXAMXSAAAASAAXMXSAMXAMXXMASMMSMASAMASMXMAMMMSMXMXMMMAXMASMSMMSMMSSMAMMAMMSAMAM
SAAAASXXMMMSXMMSXMAMAXXXSSMMMMAMXSXAAAAMSSSSSXMMMMAXASXMAASAMMSXXSAMMSMSMMMMXMAXMXSXSXAXMXMAMXMMMXMAXSAMASAMXAAXXXXXMMSAMXMAAXMAXMSMAMASMSAS
SMMSXMAXAAAMASMMSSMSSSMMMAXXMASMXASXMSXMAAAAMSMAASXSMSASMXMAXAAMSMMXMMXMMAAXSSMSSMMAMXMSMASASAMXXSXMASASMSMSMXASXSXXMSMXMASXSMSAMXAMAMXSASAX
XAAAAXASMMMSAMAAXXAAAAAASMMSAAAMAMXXMAMMMMMMMASMMMAAASXMXMSMMMXMAAMXSAMXSMMXMAAMMAMXMAMAMMSXSASXMSAAXSMMMMMAAAMXMXMASXAXSASAMXMXXSMSXSAMMMSM
SMMMMMXSXAAMMXMMMMMMSMXMMAXXMMSAMXMXSAMMAMMXSMSXSMSMMMMMMXAAAAMSMSMAMAMASAMXSMMMMXMMXMSMSXSMSMSAASAMXXMASASXSXXAMXAMAMXMMMMXXMSMMXAXMMASAAMX
MXSAAMASMMMSSXXMASAAAMMSMMSXSAXMXAAAMAMSAXMAMXMASAXASAAAMSSSMSAAAAMASAMXSAMXXASASMMSAAAAAAXAXAXMMMMXMASMSASAAAMSMAMAXXAMASXMMXAASMMMMSAMMSSM
XAMMSMASASXAXMAXASMSXMAAAXAAMASXXMMMSAMXMSMMXXXXMXMAXMMSXMAXAMMMXXMAMAXASAMMSMMXXAASMSMSMMMMMMMXSASAMMMMMMMMMMMXASXMMSXSASAAXSMSXAXAMASMMAXA
MXXSAMXMXMMSSMSMAXMXAMSXSMMXMSMMXSMXSASXAMMAMSMSMSMSMSXXASMSSXSXMSXSSSMAMAMASXMXSMMMXAMXAAAXAXSXSASXSAXXXSSXSMXMAXXAASAMASMSMMXAXSMXSAXXMAMM
MAXSASMSMXAXAAAMSMSMMXMAAXXXMXAMASAXMAXMSMMAAAAAAAAAAAASAMXAAXXAXAAMAMXXMAMMMASAMXAXXXXSMSSSSSMAMXMAMMMMAMMAMMSMSMSXSMAMAMMAAXSSSMAXMASXMXSX
ASXSXMXAMXSXMMMSMAMASAMMMMXMAAMMASMSMSMAAXSMXMSMMMSMSMXMMMMMSMSXMMXMAMAMMSMSSXMXMMMSMSMAAAMXMAMXMMMMXSAAASMAMXSAMXXMXMSMXSSSSMAXAASXMXMMMMAM
MXAMXSSMSMXMXAXAMAMMMAXSAMMAMMSMXSXAAXMSMXXAAXMXMMMXMMXMSAMSAAXMXSASAMASXXAXXMSASXMAMAAMMMXXXXMASXMXAMXXAXMASXMMMXXASAMXXMAXAMMSMMMMMMSXSASX
XMAMAMAXXXAXMASMSMSXSAMMAMSASASXSMXMSMMAMSMSMSAASAMAXMAMMAXSMMMMAAXMXSASAMSMSASASMSMSMXXMMMSMMSAMAXMMMSMASMXSAMSMMASAMSMSMAMXAXSAMXAAAXMAMXM
MSAMXSMMSSMSMXMAAMMXMAMSAMXAMAXSXMAMXASMSSXAXMMMXAXAMSASXSMXASMMSSMMXSAMXMMAAAMAMAAAAMSXSAAAAAMASXMMSAXAAXMASXMAAXSMMXAAAXSSSXXMMMMMSSMXSAMX
MSMSAMXAAAXAMAMSMSSMSAMMASMAMMMSXSMSXMMXAXMXXSASXSMSXSAXAAXMXMAAAMXXAMMMMMMSMXMAMSMSXSAASMSSMMSXMASAAAXMXSMMMMSMSMXAXSMSMMMAMSSMSSMMXAMAMMMM
ASMMXXMMMSMXMMMXAAXASAMSAMXAXAMXAXAAMMSMSSSMASXSAMAMMMXMSMMMXSMMMSXMAMSAXMAMMMSAMXAMXMMMMMMAXAXXMAMXSSSMMAMMAMAAXMXSMMAXXMSAMXSAAAASXXMASAMA
XSMSMASMMXMSAMAMMMSXSAMMMSMSXSMSSMMMSAAXAAAMXMAMAMXMXXSAXASAMAXSXXXAMXMMSMASXAXXXMAMAXXSMSSSMMSMSMSAMAAXXMASASMMMSAXAMAMXXMAMXMMMSMMAXSASASX
MXASXMSASMASAMASAXMXMMMAAAAMAMAXMAXAMXSMMSMMAMXMMMXSAXMASAMSAMSAAMSSXXAAMMMMMSSSSMSSXMAAXAAAMXAAAAXAMSMMXSASASAMAMASMMMSSMSMMASAMAMMSMMASAMM
AMMMAXSAMMAMAXASMMXAMXXMSMMMAMAMXXMXXAMXMAAMASXSAAXMAXMAMAMXSXAMXMAMMSMSSMMMXMAMXAAMAMXMAMSMMMMSMSMMXMXMAMMSXSAMMXAXXAXMAAAMXASAXXMAXAMAMAMA
SAASMMMAMMSSSMMSASMMMAXXMXAMAMAAAXSSSMSXSSSMMSAAMAMMAMMASMMXXSMXAMSXMAAXXAASMMAMMMMSXMASMXAMAXMAAXMSASAMAMAMXMMSSMMSSSMXMMMSMAMAMSMXSAMSSMMS
MSMAAXSMSAAAXXMMMMAAAXMXASXXAXMMSXAAXAXXMMXAXMMAMXAXASXAMAMXXXXSAMXASMSMSSMMASXMXMXMASXSMXMSMSMMSMAMASASASMSASMAAAAAMASXAAAAMSMSMMAAMAMMAMAX
XAMSMMMASMMSMMMASMSMSSMMXMASXSXAXMMMMMMXSAMMXMMXMAMXAMMMSAMXAXMAMXSAMAAXMASXXMXMASASAMXMXMXAAXXSMMXMAMAXAAMSAMMMSMMMMAASXMMXXXAMAMMMMSMSAMXS
AXAAMAMAMSAMXASXSAAAAAASAMXMMAMXSAASMMAAMASXMMAASXSSMMSAMASAXSSMSXMAMSMMMXMXAAAMXSXSAMXMAAXMMMXMAMSMAMXMASMMXMAMMAXXMSASXSXSAMAXXMAAAXASXSXS
MMSMSAMXSMMMSXSMMMMMXSMMAXMAMMSMSXMAAMMSSMMMAMSMSAMAAAMMSMMMMAAAAXSAMMXXSASMMSXSXMASASASXSXSAAAMAMXSASXAAXXAASASXMMXMXAMAMMMXSMMSSMSSMAMXMAS
XAAXXMSXMASAMXMAXMXSAMASAMXAMXMAMAMXMMXAMAAAMAMAMAMMMMSXAAAAMSMMMXMXSMAMSASXMXMAMXAXASASAMASMSSSXSAMXMMMMXMXMSASAAXSAMMMAMXXMAMAAAXMXMXMXMSM
MSSMSASXSAMXSASMMXAMAXAMXMSASMSSSXMAXSMSMSASMSSMXAXXAAXXSSSMXMAMXSXAAMAXMMMAXMXAXMXMAMAMAMAMXAAAAMASXMSMSASMXMASMMAAASASASXSMSMMSSMMAMAMXMAM
AXAAMSMMMXSSMAAMMMMSSMMSXXAASAAXMASXMAAMAXAXXAAXMMXSMXSAXAAXASXMAMMSMSMXAAMXMSMSXSAAAXXXAMXSMMSMMSAMXAAASAMXAMXMMMMXXXAXXAAAAAAXXMAMAMAMMXMS
SMMMMXMASAMXMAMAAAMAXAXMMMMXMMMMSAMSAMXMMMSMMSMMXSAXMAXXMXMSMMXMAMAAXAMSMMMSXSAAASXMXSMSXSAXMXXMASASXSMMMAMSMSMMXAMSSMSMSMMMXMSAXMSMSSMXSAXA
MMSXXXSXSMSMSASMMSMMSMMXASAXMAMMMAXXSXXXXSAMAAXMAMMSMMXSASXMXXXMXSXXSXMAAAXMAMXMMMMSMAAAXMASXMAMMSXMAXXXXXASAMXMMXMXAAXAMXAXSAMMSXXAMAAAMAMM
AAAXMASASAAAAAMAMMXAAXXMMMMXMASXSSMAXXSMMSXXSASMXSASAAAAXMAASMXSASXASMSMMMAMXMMXXAAASMMMSMMSMSMMAMAMAMAMSAAMMMAXMMMSXMMAMSXXAAAAXMXMSMMMXSAX
MMSMSAMAMMMSMSSMMMMSMSMAAAXMAXSXAAMMMASAAMMXXAMXAAXXMMSSMSMMAAAXAXMXMASASMSAMXMMSMSXSXAMAAAXMAXMASAMXSAAAMAMXSMMMAXAAXXXXMXXSSMXMMAMAXAAAASX
XMAMXSMAMSMXXAAASMMAAAASXSSXSASMSMMMSASMMXAXMSSMMSSXSMMAAXAXMMMMMMMMMXMMMAAMASXAAXXXMXSSSMMSSMXSAMASXMXSXXXMAMXAXXSMSMXSAMMMMAMSMSASXSXMASXM
MSMMMMSXMAAXMMMMMASMSMXMXAXAXMSAAAAAMASXMASXMASAMXAXSASMMMSXXAXAAAAMMMSAMXMXSAMSMSXMSAMXMMAMXAAMASMMXXXMASMMSSSMSAMAXAMMAXAAMAMAAMAXXMMXMAXA
XAAAAMAMSMMMSMASXMMAXMXSXMMSMASMSSMSMAMXMAXAMMSXMMXASAMAAMMSSMSSSSXSAAMASMXXXMAXAMAMMXSAMXAXMMMMAMAAAXMXMMMAMAMAAXMAMAMSMMSMSMSXMSXSASMMMASX
SSSMSSXMASAAXXAMAAMAMXAAAXAMMMMAXXXXMXXXMXSAMXSMMASASMMXMMMXMXAMAAXSMSSMMMMMMXAMAMXMAAXASMSMSMAMASMMMMMAAAMXMAMXMXMMMAMAAMAASASMAAASXMASAMAA
XAAAXAAMAMMMMMSMSMMSSMMSSMSXMXMMMSSXAASMMASXMAMAXXAAMXXXSASASMMSAMXMXAAASXAAXMASXMMMMMXAMAXAMXAXAMXMXAXSSMSXSXMMXMMMXXXMMMMMMAMXMMMMASAMAMMX
MSMMMSMMSSSMSXMAAXAAXAMAMAAAMMMSAAMMMMXAAASAMXMMMMMMMXMMSASASAXAAXAMSSSMMSSSSSXAAXXSASMSMAMAMSMSMASAMXMXAMXAXAXSASXMASMSXXAAMAMAXXXXXMASXMXS
AXASAAAXAAAAXAMSMMMSSMMASMSMMAAMMXMAMSSSMMSXMASASAXAMMMAMXMASXMMXMXXAAAMXAMMMMMSMMMSASMAMXSAMAMAMMSMMXSMSMSXSMMSASXMASAAMSSMSXSMSMMSSSXMXSAM
MSAMSSMMMSMMMXMAXASAMMSXMXAASMMXSASMSMAAMAXAMAXMXXMSXMMSSSMXMASASMSMMSMMMXSXXXAMASXMMMMSSMSXSXSASXMASAXXAAAMAAAMXMXSAMMMMAAMMAXAAAXAAXXSXMAS
AAXAXXAAXMAAAXSXSXSASMMAMMMMXAAAMXMMAMXMMSSSMSSSSMXMAMAXAXMASXMAAAAMXMAXMMMAXSMMAMXAAAXMAMXXMXMMMAMAMXSMMSMAXMASXSAMMSAAMXSAMMMMMMMMSMMMXSAM
AMMSAMSSMSSMSXMASMSAMXXMMSXASMMMSAMSSMMSMMAXAAAAAXAXAMMMAMSXSXMXMSMSASMSSMMAMMAMSMSSMSSSMMSASAMSSMMMSMAXXAXXXXASAMXSASMSAXMAAXMASAMXMMAAASAS
XXAXAMXAMXXAMXMASASAMXXSAMMMSMAXSAMAAAAAXMAMMMXMMSMSSMXMAMSSSXXXMAMSASAAAXSMSMAMXAMXMMXAXAMAMXSAAAMSAXAAMSSSSMAMAMAMASAXMSMXMASASASASMXXASAM
XMAXMMMMXMMXMAMXSXMMMAAMAMAXMMSXMAMSMMMSAMXMAXMXXXAAXMAMAXXASAXSSMMMMMMMMMXAAXAMMXMSXMAMXAMAMMMMSMMAAMXSAXAXXAXSXMASXMMMXAAASXMASMMASASXAMMM
XSSMSAAXSASASASAMMSMMXSSSSXSAAMASAMASMXMASASXSASASMMMSSSSSMMMSMAASMAMAXXSMMSMSMSSMAXMAXSAXSAXMXAXAMMMMXAMMAMMSAMXSMMMAXMSMMMMAMAMAMMMAMMSMAM
AAAASXMSAAMASAMXMSASAMXAAXXAMASMMSMAXXAXXSAXAXXMAAXXXAAAMXASAXMSMMSASMXMAMXAAAMAAMMMMMAAMMSMSSMMSSMSSXMMXSAMAAAXMXAMSSMXMASMSMMXSMSXMSMAAMAS
SMMMMMXMMMMXMAMAXSASMSMMMMAXMASXMAMMSXSMMMMMSMXMMMMMSMMMSSMMMSMAAMMMSXASXMSMXMMSXMMAMXMMXAXAAMAAAAAAMMAXAMAMXSXMSMMMAAMXAAAXAAXAAXMAMMMSMSAS
XASXXXAMMSMXXAMXAMXMASXAMXAXSXMASMXMAMXAMAAAMASXSXAMAXXAMMAAAAXMSMAXXMXMAMMSMXAMAMSMSAXXSMMMMSSMSMMMSSSMMSXMXXAAXASMSSMSXSMSXSMAMMSXMAAXXMAS
SXMAXSAXAAAMASXMMMXMAMSMSAMXAXMXMSXMAXSAMXMMSMXAXSMSMSMMSMXMSSSXMMMMMMXSMMAAMMASMMAASXSASAAXMXMAXMMAMXMXMAMXASXMXSMAAXAMAMXMMXMAXXAAMMXSAMXM
MMMXMMAMXSAMAAASXSAMXXMMAMMMMSXSASMXXXMMMAMXMAMSMXXAXXAMAMAAXAXAMMSMXAAMXMSSXSAMXSMMMASASAMXSMMSMXMSMSXMASXMASAMSMMMMMAMMSAMAMXAMASAMAASXMAS
SASASXXMMAAMMSXMASXXSASXMSAAXMAMAMMMSSMSMMXAMSMMAXSMMSSMAXMSMMMMMAAAAMXMAMMAXMASASXAXXMAMMXAXAXXXXSAAASMMMASASXMAAAAXMAXXSAMSMMXSAMSSMMSASAS
XMSAMMMSXSXMAMAMXMAXSAMXAXMMAMAMAMMAMAAAASXMMMAMSMAAAAMMMSMMAXAASXMXXXMXXSMSMSAMMXMMASMXMMMXXXXMAXXMSMXSASXMASXMSSMSSSXSAMXMAAXAMAMXMMXSXMMS
XMMXMAXXAXXMXSAMXMXMMSMMSMMSMSAMXMMAMMMMXMAMASXMXSMMMMSAASASXMMXXAAXSMSMMMMMMMXXMAMXMAAAAXASXMSXSASXMMASXSMMAMAXAAXAAXMMAMXSXSMMSSMAMSAMSSMX
XMASXSMMMMMMMSAMXMXSAMXAAAAAMAMMSMSMXMAXASAMASAMAMXSAMMMXSAMMAMSSSMMSAAAAAAAXSSSSMMAXSAMXMXSAAAAMSAAXMAMXXXMASXMASMMSMXSAMAMMMAXAAMAMMASAMXA
XMXMAMXXAAAAASAMSAXMASMSXXMXMAMXAAAAASMSMSAMXSAMXSASASXSXMASXSMMAMXAXSMSSSMMSAAMASXXXAXSXMASMMMXSMMMMMSSMMASMMXSXMASAAASMSMSASXMSSMAMSXMMMMX
SSSMSMAMXSSMMSMMSAMSMMMMASMSSSSSMSMSMAAAAMMMASXMXMXSAMXAMXSAAAXMAMMMXAMXAAASAMXMAMXXSSMSAXAMAMMXMAASAXXAXXAMAAAXAAXSMSMMAAXMASAAAXXAXMAMASMM
MXASAMXSAMAXMXXAXAMXSAMXAAAAAAAAAMAXASXSXSAMXSASMSAMXMSXASXMMXMXAMXXSSMSSMXMAMXMAMXMAXASXMASAMMASMMSMSSSMMMSMMSAMXMMMMXMMMXSAMMMMXMXXSMMASAA
AMXMMXAMASAMXAMXSAMXSMSMSMMMSMSMMMASAMAXASMSASMSAMXMAAXAMAXXSSMSASMXSAMAXXAXXMAMASAMXMXMMMXMMXSASAMXAMMMAAAAXSAMSMMAASASASAMXSXMXSSSMAXMXSMM
MAAMXMXMAMXMMSSMAXXMMXXAXXXXMAXAXXMMAMXMMMAMXXXMXMASXSSSSSSMAAAASAMXXAMXSSMMSXMSAAAMSMSAMXASXMMASXMMMMASXMMMSAAXMASMMMASAMXXMXMMXXAAAMSXMMXS
MSSSMMSMMSXSAAAAMMMMMAMXMASXSAMMMXXSXMXMSMMSMSMMMSXMMXMAAAMMMMMMMMXSSXMMMMMXMAMMMXMMSAXASMMSAAMAMMMSMSMSSSXXMMMMSAMXSMXMXMXSAAMSMMSMMXSASMAA
MAMAMAMAMAASMMMSAAMASAXASXMMXAMXAXMASMXAAAXAAASXMMMSMSMMMMMASAMXXXMMAMXXAAMMMMMAMXSAMAMXXAXSXMMMAAXAAAAMAMMMXAAXMASAMXMASMMSSMSAAMAXAXSAMMSS
MASMMMSAMXMMAXAMMMMAMMMMSAXAMSMMMSAAASMSMSSMXMMXAAAASAAXMMSASASMMMXMAXSXMMSAAASXMAMASAMXSAMXAXAXSXSMSMMMAMAAXMSMMAXASAMAXXAMAMXMSMXSMMMAMAMM
XMMXAASAMXMSXMXMASMSXSAMXAMSSMAAXMMMMXMAXAXXSXMSSMSSSSSMSAMASXMASASMSMSASASMSMSAMXMAXMAMXSAMMXXXAAMAMAASMSMXSAAMMSXMXAMXMAMSAMSXXAAAAASAMASX
SXAMMMXAMAXMASXMMXAAAXAXMAMXAXMMMMSMSAAMXMAXSAMAAAXAMAXAMMSAMAXSAMXAAASXMAMXXXSASAMSSMSXAMMXXMMAMXMAMSMXAAAXMXMSAAASMSMSMAMMAMAMMMXSMMSXXXSA
AMAMXSSMSXXMAMXXXMMMSSMMMXXSAMXAAXAASASXAXMASAMSMMMSMMMSMMMMSXMXAMASMMMMMSMAMAMXMAXMAAMMMMASXSMAMSMXXXAMSMMMXAXMMMMMAMAAMSXSAMMAAAAXAMXXSASM
MMXMAMAAAASXMXXMXAXAXAXAXAXMAASXSXMXMAMXXSMMSXMAAXAMASXAXMAASASXAMXMMXAAAAMAMAMXXSMSMMMXMAMSAASXMAAXMMSMMAASMMSMSMXMAMSMSAASMMMMSMMSSMAAMMMX
XAAMSSMMMAMAMASXMMMXSMMMMMSSSMSAXAMAMAMXXMAAMASMSMASXMSMMMMMXMASXXXSXSMMMSXXMAXXAXAMXAAXXMSMMMMXSMSSXAAASMMSXAAAAXXSAXMXSMMMMAMXXAAAAMXMXXAX
XSXXMAMXXMSXMASXAXMMMXASAXAXMAMAMXSASXMMXSMMSAMAMXMMAXXXASMMSAMAMXAXXMMSXMASXMSMAMAMMXAXMMAAMMMXSXAMMSSMMMAMMMMSMSAMXXAAXAMXSAMMSMMSSMAMAMAM
MAMXXXMAXMXMAMMMSMMASXXSASMXMSMSMXMAMXMAXSMMMAMAMASXMMMXMAAAAXXAXMAXSXAMAMAMAAXXAXSMMMMAASMMMAMMMMMSAAXAMMSMAMAMXSXMXMMMSSMAMXXXAAAAAMAXASAS
XSXSMSMSMASXSMSMMMMASMAMAXMAMAAASXMAMXMSXMAXSMMMSAMXXMAMMSMMSMSXXASMSMXSMMSSMMMXXXXAXAMXXMAXSAXAAAXMMMXXMAMMAMXSMMAMXAAAXAMXSAMSAMMSSSXMAMAS
AMASXAAAAXXAMAAAMSMMXMAMXMSSSMMMMMSSMSAMASXMAASAMASXSMXSXAAMMAMMMXMAXAMAAAAAAXXASASMMXSXASXMSASXSSSSSSSXMASMMMXSASAMMSMMSMMAMAXSMMXXMAMMSMAM
AMAMSMSMSMMMMSSSMAMAMMSXMXAMXAAAXMAAMMAMAMAASXMAMAMAAAMSMSSMSSSMSMMSMSASMMSSSMSXMASASAMMAMAAMAMMAMXAAAAMMAMAASXSASXSAASAAXMXSSMMAXXAMAMAXAMX
SMAMXXAXAAAAXMAXMMMASXMASMMSXSSMMAXMASXMXSMMXMSSMXXSMMMMAMXAAAXAAXXAAMMXAMAAAAAXSXMAMASXMAMXMMMASMMMMMMMMSMSMMAMAMAXMAMXSMSXMAMXAMSXMXMXSSXX
ASXSXSMSMSMSSMAMXXMAXXMXMAMAAMAXAMMXMSXMAMXAMMAXXAMXMAMMXMMMMMMXMSMMSMASXMMSMMMAMAMXMXMXXAMMSSMAMMAAXAAXMXMXAMXMSMMMSMSAXASXMAMMSMMAXSXAXAMM
AAMMASAAXAAXMMSMSMSMSASXXXMXMMAMMXMAMXXMASAMAMASXXAAXSXMAXAXXXSAASMSMMXMAMXAXXMAXXMASMMMMXSAAAMSSSSSSMXSAAXXAXMAXAMXAAAAMMMAMXSXMASMMMMMSMAA
XXAMAMMSSMSMXAMSMAAAXAXAASMSAMSMXXXMSMMSASASMSASMSSMSMAMMMMSMAXMXMMAAAXSAMMSMXSSMMMXXAAAAAMMSMMAAMAAXMASMMMSSMSMSXMMMSMSMXSAMXMAMXMAMAAAAXXS
MSSMMSXMMMMXMASAMMMSMMMMMAAXMAMMXSXXAAXMXSMMXMAXAMXMAMAMXXAAMXMSASMSXMMXASAAXXXXAXSSSSMSMMXMMAMMXMMMMMMXAXXAMAAXMMSMMAXMAAMMSSMAMSSSMSMSSSMX
XAXAASAMXASAMXSXSAXAASAASMMMMAXSAMXXMSMSXSASAMXMSMSSMSMSAMSXMMAMASAMSXMMXMMSSMMMSMAAXAXAMMAXSXMAMXXMAAMXMSXMMSMSMAMASMSMMMSMAMXASAAAXMAMAAMX
SSSMMSSMMMSMSMMASXSMMMXXXAMXSMMMMSSMAMAMASXMXXXAXAMXXAXMAXMASXSMAMAMAXMASAMXAAAAMMMMMXSXSXMXXAMMSMASXMSAAAMXXAAXMASXMAMAXMAMAMXMMMSMMMSMSMMS
XXAMXMXSXAXXAXMMSASXSSMMSSMMMXAAAAAMXMAMAMAXMMSAMXMMMMXMMMSAMAXMMMMMMXAASAMSSMMXSAXXAMMASAMXXMMAAMXMAASMSMSXSMMMSASXMASAMSASXSXMAMAMXAAXXAXA
MSMSAMXAMASASXMXMAMAAAAMAMAAAMSSMSSMASXMSSMMAASAMASXMSAAAXMAMXMASASAXXMASAMXMSMAXMAMSAMASMMSMAMSXMAMMMMAMASAMMSMMASXMXMMXSASAAMXSSMSMMSSSSMM
ASASXSAMXAMAMASAMAMMMSMMASMMSMXAXMAMASAAAAASMXSAMAXAAASXMXSAMSAMSASASXMASAMXAAMMSXAXMSMXMXAASAMAASXSAAMXMAMAMAAAMAMXMAMSAMSMMAMAMAMXAAAMAAAX
SMAMMMMXAMMAMXSXSSXMAXXSMMXAMXSMMSAMXSXMSSMMMXSAMXSMMMXXSASXSXSAMXMMXMMXSXMMSMSXSMXSXXMASMSXSSSXMASMXXSAMXSMMSSSMXSXSXSMMSXMASMXSAMSMMSMSMMM
"""

for data in inputs():
    print(*ceres_search(data.strip()))
