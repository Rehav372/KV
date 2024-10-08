import time
import random

print("\nVõitleja, kuna tegemist ei ole ajateenijakindla mänguga, on äärmiselt oluline, et kui mäng annab teatud vastusevariandid, kasutad sa täpselt neid. Vastasel juhul võib ilmneda tõrge.\n")
time.sleep(3)
  
eriala = input("\nMis eriala sa eelistad? (autojuht / sidemees / NAK) \n")
eriala_miks = input("\nKirjuta, miks sa just seda eriala eelistad? \n")
eriala_põhjendus = input("\nKirjuta, miks peaksid sellele erialale saama? \n")
  
time.sleep(0.5)
print("\nMõtlen, mis eriala määrata\n")
for i in range(1, 4):
      print(f"\n{i}/3\n")
      time.sleep(1)
print("\nPalju õnne, sa said nooremallohvitseride kursusele!\n")
  
time.sleep(1)
 
moraal = int(input("\n0-10, kui väga sa tahtsid kaitseväkke minna? \n"))
 
kapp_algus = input("\n1-5, kui hästi sa tavaliselt korda hoiad? \n")
kapp = int(kapp_algus)

kapp_algus = 5
kapp = 5
moraal = 10
hügieen = 10

def moraali_seis():
    global moraal
    print(f"\nSinu moraal on {moraal} / 10\n")

def check_morale():
    global moraal, kapp
    if kapp < 1:
        moraal -= 1
        print("\nSu kapp on korrast ära, sa ei leia oma snäkke üles. Moraal langeb.\n")
    elif kapp == 5:
        moraal += 1
        print("\nSu kapp on ideaalselt korras. Moraal tõuseb.\n")
    
    moraal = max(0, min(moraal, 10))
    
    if moraal == 0:
        end_game()

def kontrolli_sõjajumalat():
    global põranda_puhtus, moraal
    if põranda_puhtus == 0:
        if random.randint(1, 100) <= 100:  # 3% chance
            print("Põrand pole kunagi nii must olnud... Sõjajumal on vihane! Nakid koristavad terve kasarmu ära! Moraal langeb.")
            moraal -= 1
    if moraal == 0:
        end_game()

def end_game():
    print("\nSu moraal on langenud nullini...\n")
    time.sleep(3)
    print("\nKõik on läbi...\n")
    time.sleep(3)
    print("\nHüvasti, kaasvõitlejad...\n")
    time.sleep(5)
    print("\nMÄNGU LÕPP (sa kaotasid)\n")
    time.sleep(1)
    exit()

if moraal < 1:
    end_game()

e_keel = input("\nKas sa oskad eesti keelt? (jah/ei)? \n")
knows_estonian = e_keel.lower() != "ei"

def räägi_kaasvõitlejaga():
    with open("tsitaadid.txt", "r") as file:
        content = file.read()  
    return content.strip().split("\n\n")

def draw_quote(quotes, used_quotes, knows_estonian):
    available_quotes = [quote for quote in quotes if quote not in used_quotes]
    if not available_quotes: 
        return "\nSa oled oma kaasvõitlejatega liiga palju rääkinud. Nad ei vasta enam sulle.\n"
    quote = random.choice(available_quotes)  
    used_quotes.add(quote)  
    
    if not knows_estonian:
        quote = censor_random_words(quote)
    
    return quote  

def censor_random_words(quote):
    words = quote.split()
    num_words = len(words)
    min_censor = max(1, num_words // 2)
    max_censor = int(num_words * 0.9)
    num_words_to_censor = random.randint(min_censor, max_censor)
    words_to_censor = random.sample(words, num_words_to_censor)
    
    return " ".join('?' * len(word) if word in words_to_censor else word for word in words)

def suhtle(used_quotes, knows_estonian):
    quotes = räägi_kaasvõitlejaga()
    drawn_quote = draw_quote(quotes, used_quotes, knows_estonian)

    if drawn_quote:
        if not knows_estonian:
            print("\nKuulad oma kaasvõitlejate juttu, aga kuna sa ei oska eesti keelt, on sellest raske aru saada.\n")
        else:
            print("\nKuuled kaasvõitlejate juttu:\n")

        time.sleep(1)
        print(f'\n"{drawn_quote}"\n')
    else:
        print("\nSa oled oma kaasvõitlejatega liiga palju rääkinud. Nad ei vasta enam sulle.\n")
    time.sleep(1)

with open("varustus.txt", "r") as fail:
    algne_esemed = [rida.strip() for rida in fail.readlines()]
    esemed = algne_esemed.copy()

def ava_kapp():
    global kapp, esemed
    kapp -= 1 
    print("\nAvad kapi... kapp läheb veidi sassi!\n")
    if kapp < 0:
        kapp = 0
    if kapp == 0:
        kaotad_eseme()
    check_morale()

def kaotad_eseme():
    global esemed
    if esemed:
        kaotatud_eseme = random.choice(esemed)
        esemed.remove(kaotatud_eseme)
        print(f"\nVõimalik, et midagi kadus ära...\n")
    else:
        print("\nSu kapp on täiesti tühi.\n")

def korrasolek():
    print(f"\nKui korras su kapp on: {kapp} / 5\n")

def koristan():
    global kapp
    kapp += int(kapp_algus)
    if kapp > 5:
        kapp = 5
    print(f"\nSu kapp on nüüd {kapp} / 5 korras\n")
    check_morale()

def kapp_moodul():
    global kapp
    while True:
        print("\nSeisad oma kapi ees, mida sa teha tahad?")
        print("1. Ava kapp")
        print("2. Kui korras mu kapp on?")
        print("3. Varustusekontroll! Mis asjad mul kadunud on?")
        print("4. Koristan kappi")
        print("5. Mine kapi juurest eemale\n")
        
        valik = input("> ")

        if valik == "1":
            ava_kapp()
        elif valik == "2":
            korrasolek()
        elif valik == "3":
            alles_varustus()
        elif valik == "4":
            koristan()
        elif valik == "5":
            print("\nLähed kapi juurest eemale.\n")
            break
        else:
            print("\nPalun vali sobiv tegevus.\n")

väints_esemed = []

def kontrolli_väintsi():
    status = ["on kadunud", "on vist midagi ära kaotanud", "magas oma arstiaja maha"]
    väints_status = random.choice(status)
    
    print("\nKontrollid Väintsi...\n")
    time.sleep(1)

    if väints_status == "on kadunud":
        missing_places = ["puhkeruumis", "jõuksis", "teadmata kadunud", "rebaserajal", "toimkonna arvuti taga joonistamas"]
        location = random.choice(missing_places)
        print(f"\nSa ei suuda Väintsi leida. Teised arvavad, et ta on ilmselt {location}.\n")
    elif väints_status == "on vist midagi ära kaotanud":
        if random.choice([True, False]):
            kaotatud_eseme = random.choice(algne_esemed)
            väints_esemed.append(kaotatud_eseme)
            print(f"\nVäints on kaotanud järgneva eseme: {kaotatud_eseme}\n")
        else:
            print("\nVäints magab.\n")
    else:
        print(f"\nIlmnes, et Väints {väints_status}...\n")

def alles_varustus():
    kadunud = set(algne_esemed) - set(esemed)
    if kadunud:
        print("\nSinu kadunud esemed: " + ", ".join(kadunud) + "\n")
    else:
        print("\nSul pole kadunud esemeid.\n")

    if väints_esemed:
        print("\nVäintsi kadunud esemed: " + ", ".join(väints_esemed) + "\n")
    else:
        print("\nVäints ei ole (üllatuslikult) midagi kaotanud.\n")

    print("\nVoini kadunud esemed: kiiver\n")

def kes_on_toimkonnas():
    toimkond = ["Voini", "Maku", "Kiimstaar / Optimus Prime", "Šampa", "Tissu", "Närvihaige", "Lemmu", "PEDOFIIL", "Tambet"]
    toimkonnas = random.choice(toimkond)
    print(f"\nToimkonnas on {toimkonnas}\n")
    if toimkonnas == "Maku":
        print("\nValmistu katastroofiks...\n")

põranda_puhtus = 9
tupsud_kokku = 0

def kontrolli_põrandat():
    while True:
        global põranda_puhtus
        print("\nVaatad pingsalt põrandat. Mida soovid teha?")
        print("1. Kaabi põrandat")
        print("2. Mopi põrandat")
        print("3. Kaabi põrandat, seejärel mopi põrandat")
        print("4. Mitu tupsu on maas?")
        print("5. Looda, et äkki keegi teine tegeleb täna koristamisega")
        print("6. Kontrolli põranda puhtust")
        print("7. Ära keskendu enam põrandale\n")

        valik = input("> ")

        if valik == "6":
            global moraal
            põranda_puhtus -= random.randint(1,5)
            põranda_puhtus = max(0, põranda_puhtus)
            print(f"\nKontrollid põrandat, põrand on puhtuselt {põranda_puhtus}\n")
            if põranda_puhtus == 0:
                if random.randint(1, 100) <= 3:  # 3% chance
                    print("Põrand pole kunagi nii must olnud... Sõjajumal on vihane! Nakid koristavad täna õhtul terve kasarmu ära! Moraal langeb.")
                    moraal -= 1
                
            if moraal == 0:
                end_game()
        elif valik == "1":
            kaabi_põrandat()
        elif valik == "2":
            mopi_põrandat()
        elif valik == "3":
            kaabi_seejarel_mopi()
        elif valik == "4":
            global tupsud_kokku
            tupsud = random.randint(0,4)
            tupsud_kokku += tupsud 
            print(f"\nHetkel maas olevate tupsude arv on {tupsud}. Maas on kokku olnud {tupsud_kokku} tupsu.\n")
        elif valik == "5":
            print("\nSa tead väga hästi, et kui sina ei korista, ei korista mitte keegi.\n")
        elif valik == "7":
            break
        
        print("")

def kaabi_põrandat():
    global põranda_puhtus
    if põranda_puhtus < 8:
        puhtamaks = min(8, põranda_puhtus + kapp)
        print(f"\nKaabid põrandat, puhtus tõuseb {puhtamaks - põranda_puhtus} ühiku võrra.\n")
        põranda_puhtus = puhtamaks
    elif põranda_puhtus == 8 or põranda_puhtus == 9:
        print("\nPõrandal on monsuplekid, kaapimine ei aita enam.\n")
    else:
        print("\nPõrand on juba täiesti puhas.\n")
    print(f"\nPõrand on nüüd puhtuselt {põranda_puhtus} / 10.\n")

def mopi_põrandat():
    global põranda_puhtus
    mustemaks = 2  
    põranda_puhtus -= mustemaks
    põranda_puhtus = max(0, põranda_puhtus)
    print(f"\nEnne moppimist peab kaapima, see on SBK teadmine, muidu läheb põrand mustemaks! Põrand on nüüd puhtuselt {põranda_puhtus} / 10.\n")
    põrand_moraal()

def kaabi_seejarel_mopi():
    global põranda_puhtus
    põranda_puhtus = 10
    print("\nPõrand on nüüd täiesti puhas! 10 / 10.\n")
    põrand_moraal()

def põrand_moraal():
    global moraal, põranda_puhtus
    if põranda_puhtus < 1:
         if random.randint(1, 100) <= 50:
             moraal -= 1
             print("\nVeebel Õ on majas ja põrand on räpane...\n")
             time.sleep(3)
             print("\nSul tekib kananahk\n")
             time.sleep(3)
             print("\nSee on peaaegu hirmus kui see, kui lähed toimkonda üle võtma ja linnaku korrapidaja on kpt Naljapulk \n")
             time.sleep(3)
             print("\nSu moraal langeb\n")
    elif põranda_puhtus == 10:
        moraal += 1
        print("\nIme on sündinud, põrand on puhas! Su moraal tõuseb\n")
    moraal = max(0, min(moraal, 10))
    
    if moraal == 0:
        end_game()

autod_kokku = 0
sõdurid_kokku = 0

def aken():
    global autod_kokku, sõdurid_kokku
    autod = random.randint(0,30)
    sõdurid = random.randint(0,60)
    sõdurid_kokku += sõdurid
    autod_kokku += autod
    print("\nVaatad aknast välja")
    print(f"Hetkel on õues {autod} masinat ja {sõdurid} sõdurit.")
    print(f"Kokku on õues olnud {autod_kokku} masinat ja {sõdurid_kokku} sõdurit.")

def kraanikauss():
    while True:
        print("\nSeisad kraanikausi ees, mida sa teha tahad?")
        print("1. Vaata peeglisse")
        print("2. Pane vesi jooksma")
        print("3. Pane vesi kinni")
        print("4. Pese kraanikaussi")
        print("5. Pese peeglit")
        print("6. Mine kraanikausi juurest eemale\n")
        
        valik = input("> ")

        if valik == "1":
             print("\nVaatad peeglisse...")
             time.sleep(2)
             print("\nSulle vaatab vastu kurnatud paar silmi...")
             time.sleep(2)
             print("\nLootusetus võtab su hinges võimust...")
             time.sleep(2)
             print("\nPettumus matab hinge...")
             time.sleep(2)
        elif valik == "2":
            vesi_jooksma()
        elif valik == "3":
            vesi_kinni()
        elif valik == "4":
            print("\nPesed kraanikaussi")
            time.sleep(1)
            print("\nSellel ei ole mitte mingit mõju")
        elif valik == "5":
            print("\nPuhastad peeglit")
            time.sleep(1)
            print("\nSellel ei ole mitte mingit mõju.")
        elif valik == "6":
            print("\nLähed kapi juurest eemale\n")
            break
        else:
            print("\nPalun vali sobiv tegevus.\n")
    
vesi = False

def vesi_jooksma():
    global vesi
    if vesi == False:
        print("\nPaned vee jooksma (sa huligaan)")
        vesi = True
    elif vesi == True:
        print("\nVesi juba jookseb")

def vesi_kinni():
    global vesi
    if vesi == True:
        print("\nPanid vee kinni")
        vesi = False
    elif vesi == False:
        print("\nVesi on juba kinni")

taburet_põrandal = False


def taburet_põrandale():
    global taburet_põrandal
    if taburet_põrandal == True:
        print("\nTaburet juba on põrandal")
    elif taburet_põrandal == False:
        print("\nPanid tabureti põrandale")
        taburet_põrandal = True

def taburet_üleval():
    global taburet_põrandal
    if taburet_põrandal == True:
        print("\nPanid tabureti üles")
        taburet_põrandal = False
    elif taburet_põrandal == False:
        print("\nTaburet juba on üleval")

        
def istu():
    global taburet_põrandal, moraal
    if taburet_põrandal == True:
        print("\nIstusid taburetile")
    elif taburet_põrandal == False:
        print("\nProovisid taburetile istuda...")
        time.sleep(2)
        print("\n...kuid kuna taburet on üleval, näed totter välja.")
        time.sleep(2)
        print("\nOlles noor ja võrdlemisi hapra egoga, mõjub see su moraalile laastavalt")
        time.sleep(2)
        moraal -= 1
        
    if moraal == 0:
        end_game()


def taburet():
    while True:
        print("\nJõllitad oma taburetti. Mida soovid teha?")
        print("1. Pane taburet põrandale")
        print("2. Pane taburet üles")
        print("3. Istu taburetile")
        print("4. Jäta taburet sinnapaika\n")

        valik = input("> ")

        if valik == "1":
            taburet_põrandale()
        elif valik == "2":
            taburet_üleval()
        elif valik == "3":
            istu()
        elif valik == "4":
            print("\nJätad taburet sinnapaika.\n")
            break
        else:
            print("\nPalun vali sobiv tegevus.\n")

voodi_korras = True

def voodi_korda():
    global voodi_korras
    if voodi_korras == True:
        print("\nSu voodi juba on korras")
    elif voodi_korras == False:
        print("\nTeed oma voodi korda")
        voodi_korras = True
    
def voodi_laiali():
    global voodi_korras
    if voodi_korras == False:
        print("\nSu voodi juba on laiali tõmmatud")
    elif voodi_korras == True:
        print("\nViskad oma voodi laiali...")
        time.sleep(2)
        print("\nViskad OMA voodi laiali.......")
        time.sleep(2)
        print("\n...ohmoon")
        time.sleep(2)
        voodi_korras = False

def pikuta():
    global moraal, voodi_korras
    print("\nOh õnnis puhkus!")
    print("\nSu moraal tõuseb")
    moraal += 1
    
    moraal = max(0, min(moraal, 10))

def voodi():
    global voodi_korras
    while True:
        print("\nOled oma voodi juures. Mida soovid teha?")
        print("1. Kas mu voodi on korras?")
        print("2. Heida pikali")
        print("3. Tee voodi korda")
        print("4. Viska voodi laiali")
        print("0. Mine voodi juurest eemale ")
        
        valik = input("> ")
        
        if valik == "1":
            if voodi_korras == True:
                print("\nVoodi on korras")
            else:
                print("\nVoodi ei ole korras")
        elif valik == "2":
            pikuta()
        elif valik == "3":
            voodi_korda()
        elif valik == "4":
            voodi_laiali()
        elif valik == "0":
            print("\nLähed voodi juures minema\n")
            break
        else:
            print("\nPalun vali sobiv tegevus.\n")

def tool():
    while True:
        print("\nToas on tool, sa oled sellele natuke liiga lähedal")
        print("1. Istu toolile")
        print("2. Wtf, miks tooliga rohkem asju teha ei saa")
        print("3. Mine tooli juurest eemale")
        
        valik = input("> ")
        
        if valik == "1":
            istu_tool()
        if valik == "2":
            nilbe_tool()
        if valik == "3":
            print("\nLähed tooli juurest eemale")
            break


def nilbe_tool():
    print("\nKas sa tõesti tahad teada, mida tooliga veel teha saab?")
    otsus_1 = input("\n (jah / ei) \n")
    if otsus_1 == "jah":
        print("\nMa küsin igaks juhuks uuesti, oled sa kindel?")
        otsus_2 = input("\n (jah / ei) \n")
        if otsus_2 == "jah":
            print("\nViimane hoiatus. Kas sa tõesti tahad teada? Selle valiku pakkus rms PEDOFIIL, kes käis 14 aastaselt oma 15-aastase täditürtega")
            otsus_3 = input("\n (jah / ei) \n")
            if otsus_3 == "jah":
                print("\nTooli võib muidugimõista endale sisse istuda")

def istu_tool():
    global moraal
    tool_täis = random.randint(0,1)
    if tool_täis == 0:
        print("\nIstud toolile. See on veidi mugavam kui taburet")
        istud = True
        while istud == True:
            print("\nIstud toolil. Kas tahad püsti tõusta?")
            tõuse = input("\n1. Istu edasi \n2. Tõuse püsti\n")
            if tõuse == "2":
                istud = False
                print("Tõused püsti")                
    elif tool_täis == 1:
        print("\nSa ei saa toolile istuda, sest seal juba istub keegi. Moraal langeb")
        moraal -= 1
    
    if moraal == 0:
        end_game()

def main_loop():
    used_quotes = set()
    global moraal
    
    while True:
        if moraal <= 0:
            end_game()
        
        print("\nSeisad keset NAKi tuba.")
        print("\nMida soovid teha?")
        print("1. Mine kapi juurde")
        print("2. Keskendu põrandale")
        print("3. Kuula toas toimuvat juttu")
        print("4. Kuidas mul moraaliga lood on?")
        print("5. Kontrolli Väintsi")
        print("6. Kes on toimkonnas?")
        print("7. Vaata aknast välja")
        print("8. Mine kraanikausi juurde")
        print("9. Tee midagi oma taburetiga")
        print("10. Mine oma voodi juurde")
        print("11. Asjata tooliga")
        print("0. Välju mängust\n")

        valik = input("> ")

        if valik == "1":
            kapp_moodul()
        elif valik == "2":
            kontrolli_põrandat()
        elif valik == "3":
            suhtle(used_quotes, knows_estonian)
        elif valik == "4":
            moraali_seis()
        elif valik == "5":
            kontrolli_väintsi()
        elif valik == "6":
            kes_on_toimkonnas()
        elif valik == "7":
            aken()
        elif valik == "8":
            kraanikauss()
        elif valik == "9":
            taburet()
        elif valik == "10":
            voodi()
        elif valik == "11":
            tool()
        elif valik == "0":
            print("\nVäljud mängust.\n")
            break
        else:
            print("\nPalun vali sobiv tegevus.\n")

main_loop()
