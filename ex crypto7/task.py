from libnum import s2n
from gmpy2 import next_prime
from random import randint
from secret import flag

def chaos_maker(p, g, seed):
    res = 0
    x = seed
    for _ in range(randint(0, 114514)):
        x = pow(g, x, p)
    for i in range(256):
        x = pow(g, x, p)
        if x < (p-1) // 2:
            res -= (1 << i) - 1
        elif x > (p-1) // 2:
            res += (1 << i) + 1
        else:
            res ^= (1 << i + 1)
    return res if res > 0 else -res

def keygen(p, g):
    u, v = chaos_maker(p, g, randint(0, 1<<64)), chaos_maker(p, g, randint(0, 1<<64))
    return next_prime(u**2 + v**2) * next_prime(2*u*v)

p = 74318463376311964657848870236469351222861371046000989980725143814597652972079
g = 10135979321704650132001133858909900216529170765388975908180263641843583056994
N = keygen(p, g)
print(N)#de范围
# N = 46560744052031492000075598084262814175984839629218579003339825251165084535288738001196294968344403225296587992393409186512832442084313772062189640462381680977493272839744503195012137744652370256066011590369737294828406013950810998314546935103160880000499234316605414326064476117367727072344004644766745175963
e = 65537
c = pow(s2n(flag), e, N)
print(c)
# c = 23334367507777982721463578689282517343702422017568936413397591619899938216343800551132594869485665306596562901129144338015710969994575939792628945297846703002122172051500112438041566171992504143239954624689779597268840813422509867439815100802585538453946245512563984478922752113443379737653491922857109660034
#6823543364853153184661707949524243679410252419273226135154824438042922822213333396609719599860912483890019975825854178560359753940763837029724016787737750
#10135979321704650132001133858909900216529170765388975908180263641843583056994
#16541727033902313631938712144098272550467140666520080577065369143987589948307
#82708635169511568159693560720491362752335703332600402885326845719937949743067
#20217666374769494439036203731675666450570949703524542927524340064873721048499
#16541727033902313631938712144098272550467140666520080577065369143987589948307

#16541727033902313631938712144098272550467140666520080577065369143987589948307
#82708635169511568159693560720491362752335703332600402885326845719937949743067

#49625181101706940895816136432294817651401421999560241731196107431962769845943
#82708635169511568159693560720491362752335703332600402885326845719937949743067

#49625181101706940895816136432294817651401421999560241731196107431962769845943
#49625181101706940895816136432294817651401421999560241731196107431962769845943

#49625181101706940895816136432294817651401421999560241731196107431962769845943
#82708635169511568159693560720491362752335703332600402885326845719937949743067

#23893605715636675246133695319253060350674758740529005277983310985759852147667
#16541727033902313631938712144098272550467140666520080577065369143987589948307

#16541727033902313631938712144098272550467140666520080577065369143987589948307
#16541727033902313631938712144098272550467140666520080577065369143987589948307

#25357444092905821748743775482823293874460389976846331429079325120801505412339
#82708635169511568159693560720491362752335703332600402885326845719937949743067

#为什么是固定的数
#547257466528269269370368367273708005203239421248669117458104548723337307333049226525212498600941254174244133694648943904438959466731639375598045864332591
#547257466528269269370368367273708005203239421248669117458104548723337307333049226525212498600941254174244133694648943904438959466731639375598045864332591

#7114347064867500501814788774558204067642112476232698526955359133403384995583059202987145926653537374312759273503592865768794107508152767168664474246732747
#2736287332641346346851841836368540026016197106243345587290522743616686536715929984257939181972966484880737775567876038524412324221786487935168204923275383
#19466897753611084381908344423371363212856060579966668426110712661811951565629156851996571661954188955844549448173311656113820949444411656267294236042523169253008738655803444706465694792446784346841516712796553675681371380203363334377729221851621057447956766537034599783793174541898375069622938622201485067101

#4573991417773312288441226970917287895340655409695666574310330610934559963949129684079331049626576496124257369769715794924814746169798538495337872450024567
#4560478887735577244753069727280900043360328510405575978817537906027810894631850932121713231355058885485638318275500444548050368860891827558317786353922471
#20859591293438911248103749880693910881772005401452096430004673111818124739338051841250266199617815217279173495435309388842017527844561115229266889069483744282343650262760344326751477886048049245535043968895179034954030878278422584334060520401840242568858361957765976355619809590968264220622690444180763345057

#49开头
#49开头
#9303376930980577579296262243653036088455070161227374996787777328296734225016689979259884908248350573877346415561653147953651079473644168261988559268125799
#8208861997924039040555525509105620078048591318730036761871568230850059610316846403060299191237313092754897672169402293185072196162967536457057784044654771
#76370137341089638729025043507072271065819929967561545363972795827108425374618211335664982868497241777198900976197765218817268228307165604962553204211098374087727505143571221231319632868680049350516170413509162661928758728060291477333202456888931663232982571322887992842076907447032002728070642907501153537029

#13681436663206731734259209181842700130080985531216727936452613718083432683833069179449079354706133494451274413312536787633149255549573894961730902629133577
#13681436663206731734259209181842700130080985531216727936452613718083432683833069179449079354706133494451274413312536787633149255549573894961730902629133577
#187181709169337349826041773301647723200539044038141042558756852517422611211706504608922586370671340550820124465800758668634116991541678362469524733584476612244734086361867232759326341994451816885559164506146351977146854929941052118625200940953283439110257478136938542428760347052154587925685369201965708814929

#7114347064867500501814788774558204067642112476232698526955359133403384995583059202987145926653537374312759273503592865768794107508152767168664474246732747
#2736287332641346346851841836368540026016197106243345587290522743616686536715929984257939181972966484880737775567876038524412324221786487935168204923275383
#19466897753611084381908344423371363212856060579966668426110712661811951565629156851996571661954188955844549448173311656113820949444411656267294236042523169253008738655803444706465694792446784346841516712796553675681371380203363334377729221851621057447956766537034599783793174541898375069622938622201485067101

#13681436663206731734259209181842700130080985531216727936452613718083432683833069179449079354706133494451274413312536787633149255549573894961730902629133577
#13681436663206731734259209181842700130080985531216727936452613718083432683833069179449079354706133494451274413312536787633149255549573894961730902629133577
#187181709169337349826041773301647723200539044038141042558756852517422611211706504608922586370671340550820124465800758668634116991541678362469524733584476612244734086361867232759326341994451816885559164506146351977146854929941052118625200940953283439110257478136938542428760347052154587925685369201965708814929

#8060224167508953559985795829105353706264995426539040211450848476875819847783411399182952191088483169979850012499608700022085398954278777225222262273498079
#5776606591131731176687221654555806721589749446513729573168881347635227133113794767302741712092017955351737968930616386238529534813063208506333298381433797
#46560744052031492000075598084262814175984839629218579003339825251165084535288738001196294968344403225296587992393409186512832442084313772062189640462381680977493272839744503195012137744652370256066011590369737294828406013950810998314546935103160880000499234316605414326064476117367727072344004644766745175963#居然跑出来了！

#思路 打印两个大素数 及其乘积 复现随机数生成