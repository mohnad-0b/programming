from math import gcd
from Crypto.Util.number import long_to_bytes,isPrime

k1 = 9019465093803586877472891652042526017244423267918585684572141459337752636017501282398583984846819147555479788255766221465302452334708306581657478087163498882790399392556915932241903819600243256898710512837026330099749891149718206725456165654975013707057350042189177818505148923810842478214626652504947902299
k2 = 23938372162005523177999938438562451374665546708075664883194200608993841377868039780046395969369898805670203008718315917149246468698236445400730491330343376568175458641957123986113999188370741703681470314365261825831443108787421922073023609145294588353146041309964285454626205876016177576199911694583578054203
k3 = 7492176105815056287406737107861152687669914817188441973876375606125509278843647128053495385472184164273276753734355681888283710630052589292533918258041321561584337044160204288159261124250897895150472928088930420119607423773142875636276401786832850472958085716356092462792054479554714349979034664376850407259
k4 = 19226181445602743460246708025013176246822001005948560833211736039157554695246287037030410489087800335076044816379819628670911825715971233704410525113162113042540729331798511555022529148709471705473637189586448652726834752638590559219127165638752435997278633564685349397058307290548363125722837867180940021419

c1 = 1490803635449005835981793387807741830923148060654731278738509797435451285285034156065878921946571927216460900511251526914548382779631334897120457669789539503101428807041786196779372071069328112093285546177856847259662170258558289415211977744184992082066716124590295955026240499770848142550445898094801157061
c2 = 6350249974685514311455731678779522359350354799468017596988644954406012738159501505851851861514932395179333372434804220392980343950894714606458923379054304802233466609403548752751709359872922491353578150109676550914201161697356048954377466378161795747517549045847439371181670308693139841054101664947749441303
c3 = 2544223511735543039595079752083782272939464573374775456475586531619250161960313372895971808675158274512437185309522676978160116122909124405173644335952401335143161289490254404665940426997169777822971888908315046502903142588256830588219713706207832651682400227233863085882991692803261801301182265503150372301
c4 = 12100625282820382536088469677465402939756857865013288698256765193122801312845842440176118885229553306158666539700152355154084650895509376550887918252093180450562973419960250796728283309496027020169076272415675948089735523228946553123649235016377673362851198236398841047345542435309022329198769047584615575574

def rsa_decrypt(p,q,c,e=0x10001):
    n = p*q
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    return long_to_bytes(pow(c,d,n))    

q = gcd(k3, k1)
p = (k1//q)
#print(p*q == k1)
print(rsa_decrypt(p,q,c1))

p = (k3//q)
#print(p*q == k3)
print(rsa_decrypt(p,q,c3))

q = gcd(k4, k2)
p = (k2//q)
#print(p*q == k2)
print(rsa_decrypt(p,q,c2))

p = (k4//q)
#print(p*q == k4)
print(rsa_decrypt(p,q,c4))