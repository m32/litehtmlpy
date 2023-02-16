<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tns="http://crd.gov.pl/wzor/2022/11/09/11890/" version="1.0">
    <xsl:import href="http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/03/15/eD/DefinicjeSzablony/Posredni_wspolne_v13-0E.xsl"/>
    <xsl:import href="http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/03/15/eD/PITR/PIT-R(21)_Z_v1-0E.xsl"/>
    <xsl:import href="http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/03/15/eD/ORDZU/ORD-ZU(3)_v11-0E.xsl"/>
    <xsl:output method="html" encoding="UTF-8" indent="yes" version="4.01" doctype-public="-//W3C//DTD HTML 4.01//EN" doctype-system="http://www.w3.org/TR/html4/strict.dtd"/>
    <xsl:template name="TytulDokumentu">
    INFORMACJA O PRZYCHODACH Z INNYCH ŹRÓDEŁ ORAZ O DOCHODACH
    I POBRANYCH ZALICZKACH NA PODATEK DOCHODOWY
    </xsl:template>
    <xsl:template name="StyleDlaFormularza">
        <style type="text/css">
      .tlo-formularza { background-color:#D3D3D3; font-size:1.0em; }
      .rowdiv { height: 2em }
      .opis-tekstowy { font-weight: normal}
      .niewypelnianeopisy {font-weight: bold}
      .obok-daty {width: 100%}
      .pogrubiane { border: 3px solid black;}
        </style>
    </xsl:template>
    <xsl:template match="tns:Deklaracja">
        <div class="deklaracja">
            <!-- m32
            <xsl:call-template name="NaglowekTechniczny">
                <xsl:with-param name="naglowek" select="tns:Naglowek"/>
                <xsl:with-param name="uzycie" select="'deklaracja'"/>
            </xsl:call-template>
-->
            <xsl:call-template name="NaglowekTytulowy">
                <xsl:with-param name="uzycie" select="'deklaracja'"/>
                <xsl:with-param name="nazwa">
          PIT-11(29) INFORMACJA O PRZYCHODACH Z INNYCH ŹRÓDEŁ ORAZ O DOCHODACH
          I POBRANYCH ZALICZKACH NA PODATEK DOCHODOWY
                    <div>
                        <span class="opis-tekstowy"> w roku<sup>2)</sup>
                            <xsl:apply-templates select="*[local-name()='Naglowek']/*[local-name()='Rok']"/>
                        </span>
                    </div>
                </xsl:with-param>
            </xsl:call-template>
            <xsl:call-template name="PodNaglowkiemPIT11"/>
            <xsl:call-template name="MiejsceICel">
                <xsl:with-param name="sekcja">A.</xsl:with-param>
            </xsl:call-template>
            <xsl:call-template name="Skladajacy">
                <xsl:with-param name="sekcja">B.</xsl:with-param>
            </xsl:call-template>
            <xsl:call-template name="DaneIdentyfikacyjne">
                <xsl:with-param name="sekcja">C.</xsl:with-param>
            </xsl:call-template>
            <!-- m32
            <div class="lamstrone"></div>
-->
            <xsl:call-template name="KosztyUzyskaniaPrzychodu">
                <xsl:with-param name="sekcja">D.</xsl:with-param>
            </xsl:call-template>
            <xsl:call-template name="DochodyPodatnika">
                <xsl:with-param name="sekcja">E.</xsl:with-param>
            </xsl:call-template>
            <xsl:call-template name="InformacjaOPrzychodach1">
                <xsl:with-param name="sekcja">F.</xsl:with-param>
            </xsl:call-template>
            <!-- m32
            <div class="lamstrone"></div>
-->
            <xsl:call-template name="InformacjaOPrzychodach2">
                <xsl:with-param name="sekcja">G.</xsl:with-param>
            </xsl:call-template>
            <!-- m32
            <xsl:call-template name="ObjasnieniaPit11"/>
            <xsl:call-template name="Pouczenie"/>
-->
        </div>
        <xsl:apply-templates select="tns:Zalaczniki"/>
    </xsl:template>
    <xsl:template name="PodNaglowkiemPIT11">
        <!-- m32
        <div class="tlo-formularza">
            <table style="width: 100%">
                <tr style="height: 10px"/>
                <tr style="width: 100%">
                    <td style="width: 45%"/>
                    <td/>
                    <td style="width: 55%">
                        <span class="data">
                            <span class="opisrubryki">
                5. Nr informacji<sup>3)</sup>  
              </span>
                            <xsl:value-of select="tns:PozycjeSzczegolowe/tns:P_5"/>
                        </span>
                    </td>
                </tr>
                <tr style="height: 10px"/>
            </table>
        </div>
-->
        <div class="prawne">
            <table>
                <tr>
                    <td class="etykieta" style="width: 15%" valign="top">Podstawa prawna:</td>
                    <td class="wartosc">
            Art. 35 ust. 6<sup>4)</sup>, art. 39 ust. 1, art. 42 ust. 2 pkt 1, art. 42a ust. 1, art. 42e ust. 6 ustawy z dnia 26 lipca 1991 r. o podatku dochodowym od osób fizycznych (Dz. U. z 2021 r. poz. 1128, z późn. zm.), zwanej dalej „ustawą”; art. 35a ust. 5 ustawy, w brzmieniu obowiązującym przed dniem 26 października 2007 r.<sup>5)</sup>
                    </td>
                </tr>
                <tr>
                    <td class="etykieta" style="width: 15%" valign="top">Składający:</td>
                    <td class="wartosc">
            Płatnicy podatku dochodowego od osób fizycznych, a także niebędący płatnikami: rolnicy, osoby fizyczne prowadzące działalność gospodarczą, osoby prawne i ich jednostki organizacyjne oraz jednostki organizacyjne niemające osobowości prawnej.
                    </td>
                </tr>
                <tr>
                    <td class="etykieta" style="width: 15%" valign="top">Terminy składania:</td>
                    <td class="wartosc">
            Do końca stycznia roku następującego po roku podatkowym<sup>5)</sup> – dla informacji składanych urzędowi skarbowemu; do końca lutego roku następującego po roku podatkowym – dla informacji przesyłanych podatnikowi; w terminie 14 dni od złożenia pisemnego wniosku przez podatnika – w przypadku gdy w trakcie roku podatkowego ustał obowiązek poboru zaliczki przez płatników, o których mowa w art. 39 ust. 1 ustawy; do dnia zaprzestania działalności<sup>6)</sup> – w przypadku gdy składający zaprzestali działalności przed końcem stycznia lub odpowiednio przed końcem lutego roku następującego po roku podatkowym.
                    </td>
                </tr>
                <tr>
                    <td class="etykieta" style="width: 15%" valign="top">Otrzymuje:</td>
                    <td class="wartosc">
            Podatnik oraz urząd skarbowy według miejsca zamieszkania podatnika, a w przypadku podatników, o których mowa w art. 3 ust. 2a ustawy, urząd skarbowy w sprawach opodatkowania osób zagranicznych.
                    </td>
                </tr>
            </table>
        </div>
    </xsl:template>
    <xsl:template name="MiejsceICel">
        <xsl:param name="sekcja"/>
        <h2 class="tytul-sekcja-blok">
            <xsl:value-of select="$sekcja"/>
 MIEJSCE I CEL SKŁADANIA INFORMACJI
        </h2>
        <table class="normalna">
            <tr>
                <td class="niewypelnianeopisy" style="width:33%">
          Urząd skarbowy, do którego adresowana jest informacja<sup>7)</sup>
                </td>
                <td class="wypelniane" style="width:auto">
                    <div>
                        <xsl:apply-templates select="*[local-name()='Naglowek']/*[local-name()='KodUrzedu']"/>
                    </div>
                </td>
            </tr>
            <tr>
                <td class="niewypelnianeopisy">Cel złożenia formularza:</td>
                <td class="wypelniane">
                    <xsl:choose>
                        <xsl:when test="*[local-name()='Naglowek']/*[local-name()='CelZlozenia'] = 1">
                            <input type="checkbox" checked="checked" disabled="disabled"/>
1. złożenie informacji
                        </xsl:when>
                        <xsl:when test="*[local-name()='Naglowek']/*[local-name()='CelZlozenia'] = 2">
                            <input type="checkbox" checked="checked" disabled="disabled"/>
2. korekta informacji<sup>8)</sup>
                        </xsl:when>
                    </xsl:choose>
                </td>
            </tr>
        </table>
    </xsl:template>
    <xsl:template name="Skladajacy">
        <xsl:param name="sekcja"/>
        <h2 class="tytul-sekcja-blok">
            <xsl:value-of select="$sekcja"/>
 DANE IDENTYFIKACYJNE SKŁADAJĄCEGO<br/>
        <span class="opis-tekstowy">* - dotyczy składającego niebędącego osobą fizyczną, ** - dotyczy składającego będącego osobą fizyczną  
        </span>
    </h2>
    <table class="normalna">
        <xsl:if test="count(tns:Podmiot1/*[local-name()='OsobaFizyczna']) &gt; 0">
            <xsl:for-each select="tns:Podmiot1/*[local-name()='OsobaFizyczna']">
                <tr>
                    <td class="wypelniane">
                        <div class="opisrubryki">Identyfikator podatkowy NIP<sup>1)</sup> / numer PESEL składającego</div>
                        <xsl:if test="*[local-name()='NIP' ]">
                            <xsl:value-of select="*[local-name() = 'NIP']"/>
                        </xsl:if>
                        <xsl:if test="not(*[local-name()='NIP'])">
                            <xsl:apply-templates select="*[local-name() = 'PESEL']"/>
                        </xsl:if>
                    </td>
                </tr>
                <tr>
                    <td class="wypelniane" style="width: 100%">
                        <div class="opisrubryki">8. Rodzaj składającego</div>
                        <input type="checkbox" checked="checked" disabled="disabled"/>
2. osoba fizyczna
                    </td>
                </tr>
                <tr>
                    <td class="wypelniane">
                        <div class="opisrubryki">
                10. Nazwisko, pierwsze imię, data urodzenia<font style="font-weight: normal">
                            <sup>9)</sup>
                        </font>
                    </div>
                    <xsl:value-of select="*[local-name() = 'Nazwisko']"/>
                    <xsl:value-of select="*[local-name() = 'ImiePierwsze']"/>
                    <xsl:value-of select="*[local-name() = 'DataUrodzenia']"/>
                </td>
            </tr>
        </xsl:for-each>
    </xsl:if>
    <xsl:if test="count(tns:Podmiot1/*[local-name()='OsobaNiefizyczna']) &gt; 0">
        <xsl:for-each select="tns:Podmiot1/*[local-name()='OsobaNiefizyczna']">
            <tr>
                <td class="wypelniane">
                    <div class="opisrubryki">Identyfikator podatkowy NIP / numer PESEL składającego</div>
                    <xsl:if test="*[local-name()='NIP' ]">
                        <xsl:value-of select="*[local-name() = 'NIP']"/>
                    </xsl:if>
                    <xsl:if test="not(*[local-name()='NIP'])">
                        <xsl:apply-templates select="*[local-name() = 'PESEL']"/>
                    </xsl:if>
                </td>
            </tr>
            <tr>
                <td class="wypelniane" style="width: 100%">
                    <div class="opisrubryki">8. Rodzaj składającego</div>
                    <input type="checkbox" checked="checked" disabled="disabled"/>
1. składający niebędący osobą fizyczną
                </td>
            </tr>
            <tr>
                <td class="wypelniane">
                    <div class="opisrubryki">9. Nazwa pełna</div>
                    <xsl:apply-templates select="*[local-name() = 'PelnaNazwa']"/>
                </td>
            </tr>
        </xsl:for-each>
    </xsl:if>
</table>
</xsl:template>
<xsl:template name="DaneIdentyfikacyjne">
<xsl:param name="sekcja"/>
<h2 class="tytul-sekcja-blok">
    <xsl:value-of select="$sekcja"/>
 DANE IDENTYFIKACYJNE I ADRES ZAMIESZKANIA PODATNIKA
</h2>
<xsl:for-each select="tns:PozycjeSzczegolowe">
    <table class="normalna">
        <tr>
            <td class="wypelniane" style="width: 100%">
                <div class="opisrubryki">11. Rodzaj obowiązku podatkowego podatnika</div>
                <xsl:choose>
                    <xsl:when test="tns:P_11 =1">
                        <input type="checkbox" checked="checked" disabled="disabled"/>
1. nieograniczony
                obowiązek podatkowy (rezydent)
                    </xsl:when>
                    <xsl:when test="tns:P_11 =2">
                        <input type="checkbox" checked="checked" disabled="disabled"/>
2. ograniczony obowiązek podatkowy (nierezydent)<sup>10)</sup>
                    </xsl:when>
                </xsl:choose>
            </td>
        </tr>
    </table>
</xsl:for-each>
<xsl:for-each select="tns:Podmiot2">
    <table class="normalna">
        <xsl:for-each select="*[local-name()='OsobaFizyczna']">
            <tr>
                <td class="wypelniane" style="width: 50%">
                    <div class="opisrubryki">12. Identyfikator podatkowy NIP / numer PESEL</div>
                    <xsl:if test="*[local-name()='NIP' ]">
                        <xsl:value-of select="*[local-name() = 'NIP']"/>
                    </xsl:if>
                    <xsl:if test="not(*[local-name()='NIP'])">
                        <xsl:apply-templates select="*[local-name() = 'PESEL']"/>
                    </xsl:if>
                </td>
                <td class="wypelniane" style="width: 50%">
                    <div class="rowdiv">
                        <div class="opisrubryki">
                  13. Zagraniczny numer identyfikacyjny podatnika <font style="font-weight: normal">(numer dokumentu stwierdzającego tożsamość)<sup>11)</sup>
                        </font>
                    </div>
                    <xsl:value-of select="tns:NrId"/>
                </div>
            </td>
        </tr>
    </xsl:for-each>
    <tr>
        <td class="wypelniane" style="width: 50%">
            <div class="rowdiv">
                <div class="opisrubryki">
                  14. Rodzaj numeru identyfikacyjnego (dokumentu stwierdzającego
                  tożsamość)<font style="font-weight: normal">
                    <sup>12)</sup>
                </font>
            </div>
            <xsl:for-each select="*[local-name()='OsobaFizyczna']">
                <xsl:choose>
                    <xsl:when test="//tns:RodzajNrId=1">
                        <input type="checkbox" checked="checked" disabled="disabled"/>
1. numer
                    identyfikacyjny
                    TIN
                    </xsl:when>
                    <xsl:when test="//tns:RodzajNrId=2">
                        <input type="checkbox" checked="checked" disabled="disabled"/>
2. numer
                    ubezpieczeniowy
                    </xsl:when>
                    <xsl:when test="//tns:RodzajNrId= 3">
                        <input type="checkbox" checked="checked" disabled="disabled"/>
3. paszport
                    </xsl:when>
                    <xsl:when test="//tns:RodzajNrId=4">
                        <input type="checkbox" checked="checked" disabled="disabled"/>
4. urzędowy
                    dokument
                    stwierdzający tożsamość
                    </xsl:when>
                    <xsl:when test="//tns:RodzajNrId=8">
                        <input type="checkbox" checked="checked" disabled="disabled"/>
8. inny rodzaj
                    identyfikacji podatkowej
                    </xsl:when>
                    <xsl:when test="//tns:RodzajNrId=9">
                        <input type="checkbox" checked="checked" disabled="disabled"/>
9. inny dokument
                    potwierdzający tożsamość
                    </xsl:when>
                </xsl:choose>
            </xsl:for-each>
        </div>
    </td>
    <td class="wypelniane" style="width: 50%">
        <div class="rowdiv">
            <div class="opisrubryki">
                15. Kraj wydania numeru identyfikacyjnego (dokumentu stwierdzającego tożsamość)
                <font style="font-weight: normal">
                    <sup>12)</sup>
                </font>
            </div>
            <xsl:apply-templates select="*[local-name()='AdresZamieszkania']/*[local-name()='KodKraju']"/>
        </div>
    </td>
</tr>
</table>
<table class="normalna">
<tr>
    <td class="wypelniane" style="width: 33%">
        <div class="opisrubryki">16. Nazwisko</div>
        <div class="wypełniane">
            <xsl:value-of select="*[local-name()='OsobaFizyczna']/*[local-name()='Nazwisko']"/>
        </div>
    </td>
    <td class="wypelniane" style="width: 33%">
        <div class="opisrubryki">17. Pierwsze Imię</div>
        <div class="wypełniane">
            <xsl:value-of select="*[local-name()='OsobaFizyczna']/*[local-name()='ImiePierwsze']"/>
        </div>
    </td>
    <td class="wypelniane" style="width: 34%">
        <div class="opisrubryki">18. Data urodzenia</div>
        <div class="wypełniane">
            <xsl:value-of select="*[local-name()='OsobaFizyczna']/*[local-name()='DataUrodzenia']"/>
        </div>
    </td>
</tr>
</table>
<table class="normalna">
<tr>
    <td class="wypelniane" style="width:20%">
        <div class="opisrubryki">19. Kraj</div>
        <xsl:for-each select="*[local-name()='AdresZamieszkania']/*[local-name()='KodKraju']">
            <xsl:call-template name="PokazKodKraju"/>
        </xsl:for-each>
    </td>
    <td class="wypelniane" style="width:40%">
        <div class="opisrubryki">20. Województwo</div>
        <xsl:value-of select="*[local-name()='AdresZamieszkania']/*[local-name()='Wojewodztwo']"/>
    </td>
    <td class="wypelniane" style="width:40%">
        <div class="opisrubryki">21. Powiat</div>
        <xsl:value-of select="*[local-name()='AdresZamieszkania']/*[local-name()='Powiat']"/>
    </td>
</tr>
</table>
<table class="normalna">
<tr>
    <td class="wypelniane" style="width:35%">
        <div class="opisrubryki">22. Gmina</div>
        <xsl:value-of select="*[local-name()='AdresZamieszkania']/*[local-name()='Gmina']"/>
    </td>
    <td class="wypelniane" style="width:45%">
        <div class="opisrubryki">23. Ulica</div>
        <xsl:value-of select="*[local-name()='AdresZamieszkania']/*[local-name()='Ulica']"/>
    </td>
    <td class="wypelniane" style="width:10%">
        <div class="opisrubryki">24. Numer domu</div>
        <xsl:value-of select="*[local-name()='AdresZamieszkania']/*[local-name()='NrDomu']"/>
    </td>
    <td class="wypelniane" style="width:10%">
        <div class="opisrubryki">25. Numer lokalu</div>
        <xsl:value-of select="*[local-name()='AdresZamieszkania']/*[local-name()='NrLokalu']"/>
    </td>
</tr>
</table>
<table class="normalna">
<tr>
    <td class="wypelniane" style="width:70%">
        <div class="opisrubryki">26. Miejscowość</div>
        <xsl:value-of select="*[local-name()='AdresZamieszkania']/*[local-name()='Miejscowosc']"/>
    </td>
    <td class="wypelniane" style="width:30%">
        <div class="opisrubryki">27. Kod pocztowy</div>
        <xsl:value-of select="*[local-name()='AdresZamieszkania']/*[local-name()='KodPocztowy']"/>
    </td>
</tr>
</table>
</xsl:for-each>
</xsl:template>
<xsl:template name="KosztyUzyskaniaPrzychodu">
<xsl:param name="sekcja"/>
<xsl:for-each select="tns:PozycjeSzczegolowe">
<h2 class="tytul-sekcja-blok">
<xsl:value-of select="$sekcja"/>
 INFORMACJA O KOSZTACH UZYSKANIA PRZYCHODU
<font style="font-size: 0.8em">
          Z TYTUŁU STOSUNKU SŁUŻBOWEGO,
          STOSUNKU PRACY, SPÓŁDZIELCZEGO STOSUNKU PRACY ORAZ PRACY NAKŁADCZEJ
</font>
</h2>
<!-- m32 -->
<div class="lamstrone"></div>
<table class="normalna">
<tr>
    <td class="wypelniane" style="width:50%">
        <div class="opisrubryki">
              28. Koszty uzyskania przychodów, wykazane w poz. 30, zostały
              uwzględnione do wysokości przysługującej podatnikowi
        </div>
        <xsl:choose>
            <xsl:when test="//tns:P_28 = 1">
                <input type="checkbox" checked="checked" disabled="disabled"/>
1. z jednego stosunku pracy (stosunków pokrewnych)
            </xsl:when>
            <xsl:when test="//tns:P_28 = 2">
                <input type="checkbox" checked="checked" disabled="disabled"/>
2. z więcej niż jednego stosunku pracy (stosunków pokrewnych)
            </xsl:when>
            <xsl:when test="//tns:P_28 = 3">
                <input type="checkbox" checked="checked" disabled="disabled"/>
3. z jednego stosunku pracy (stosunków pokrewnych), podwyższone w związku z zamieszkiwaniem podatnika poza miejscowością, w której znajduje się zakład pracy
            </xsl:when>
            <xsl:when test="//tns:P_28 = 4">
                <input type="checkbox" checked="checked" disabled="disabled"/>
4. z więcej niż jednego stosunku pracy (stosunków pokrewnych), podwyższone w związku z zamieszkiwaniem podatnika poza miejscowością, w której znajduje się zakład pracy
            </xsl:when>
        </xsl:choose>
    </td>
</tr>
</table>
</xsl:for-each>
</xsl:template>
<xsl:template name="DochodyPodatnika">
<xsl:param name="sekcja"/>
<xsl:for-each select="tns:PozycjeSzczegolowe">
<h2 class="tytul-sekcja-blok">
<xsl:value-of select="$sekcja"/>
 DOCHODY PODATNIKA, POBRANE ZALICZKI ORAZ POBRANE SKŁADKI NA UBEZPIECZENIA SPOŁECZNE
<div class="opis-tekstowy">
          (część tę wypełniają składający będący płatnikami)
</div>
</h2>
<table class="normalna">
<tr>
    <td class="niewypelniane" style="width: 35%">
        <b/>
Źródła przychodów
    </td>
    <td class="niewypelniane" style="width: 12%">
            Przychód<font style="font-weight: normal">
        <sup>13)</sup>
    </font>
</td>
<td class="niewypelniane" style="width: 12%">
            Koszty uzyskania przychodów<font style="font-weight: normal">
    <sup>14)</sup>
</font>
</td>
<td class="niewypelniane" style="width: 12%">
            Dochód<br/>
(b - c)
</td>
<td class="niewypelniane" style="width: 12%">
            Dochód zwolniony od podatku<font style="font-weight: normal">
<sup>13)</sup>
</font>
</td>
<td class="niewypelniane" style="width: 12%">
            Zaliczka pobrana przez płatnika<font style="font-weight: normal">
<sup>15)</sup>
</font>
</td>
</tr>
<tr>
<td class="niewypelniane" style="width: 35%">a</td>
<td class="niewypelniane" style="width: 12%">b</td>
<td class="niewypelniane" style="width: 12%">c</td>
<td class="niewypelniane" style="width: 12%">d</td>
<td class="niewypelniane" style="width: 12%">e</td>
<td class="niewypelniane" style="width: 12%">f</td>
</tr>
<tr>
<td class="niewypelnianeopisy" rowspan="2">
            1. Należności ze stosunku: pracy, służbowego, spółdzielczego i z pracy nakładczej, wypłacone przez zakład pracy oraz płatników, o których mowa w art. 42e ust. 1 ustawy, z wyjątkiem należności wykazanych w wierszu 2 albo 3<font style="font-weight: normal">
<sup>16)</sup>
</font>
<div class="opis-tekstowy">
              W poz. 34 należy wykazać przychody, do których zastosowano odliczenie kosztów uzyskania przychodów na podstawie art. 22 ust. 9 pkt 3 ustawy.
</div>
</td>
<td class="wypelniane">
<div class="opisrubryki">29.</div>
<div class="kwota">
<xsl:value-of select="tns:P_29"/>
</div>
</td>
<td class="wypelniane pogrubiane" style="width: 12%">
<div class="opisrubryki">30.</div>
<div class="kwota">
<xsl:value-of select="tns:P_30"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">31.</div>
<div class="kwota">
<xsl:value-of select="tns:P_31"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">32.</div>
<div class="kwota">
<xsl:value-of select="tns:P_32"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">33.</div>
<div class="kwota">
<xsl:value-of select="tns:P_33"/>
</div>
</td>
</tr>
<tr>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">34.</div>
<div class="kwota">
<xsl:value-of select="tns:P_34"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">35.</div>
<div class="kwota">
<xsl:value-of select="tns:P_35"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" rowspan="2">
            2. Należności z tytułów wymienionych w wierszu 1, otrzymane przez podatników do ukończenia 26. roku życia<font style="font-weight: normal">
<sup>17)</sup>
</font>
<div class="opis-tekstowy">
              W poz. 41 należy wykazać przychody, do których zastosowano odliczenie kosztów uzyskania przychodów na podstawie art. 22 ust. 9 pkt 3 ustawy.
</div>
</td>
<td class="wypelniane">
<div class="opisrubryki">36.</div>
<div class="kwota">
<xsl:value-of select="tns:P_36"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">37.</div>
<div class="kwota">
<xsl:value-of select="tns:P_37"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">38.</div>
<div class="kwota">
<xsl:value-of select="tns:P_38"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">39.</div>
<div class="kwota">
<xsl:value-of select="tns:P_39"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">40.</div>
<div class="kwota">
<xsl:value-of select="tns:P_40"/>
</div>
</td>
</tr>
<tr>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">41.</div>
<div class="kwota">
<xsl:value-of select="tns:P_41"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">42.</div>
<div class="kwota">
<xsl:value-of select="tns:P_42"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" rowspan="2">
            3. Należności z tytułów wymienionych w wierszu 1, otrzymane przez podatników od ukończenia wieku emerytalnego<font style="font-weight: normal">
<sup>18)</sup>
</font>
<div class="opis-tekstowy">
              W poz. 48 należy wykazać przychody, do których zastosowano odliczenie kosztów uzyskania przychodów na podstawie art. 22 ust. 9 pkt 3 ustawy.
</div>
</td>
<td class="wypelniane">
<div class="opisrubryki">43.</div>
<div class="kwota">
<xsl:value-of select="tns:P_43"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">44.</div>
<div class="kwota">
<xsl:value-of select="tns:P_44"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">45.</div>
<div class="kwota">
<xsl:value-of select="tns:P_45"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">46.</div>
<div class="kwota">
<xsl:value-of select="tns:P_46"/>
</div>
</td>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">47.</div>
<div class="kwota">
<xsl:value-of select="tns:P_47"/>
</div>
</td>
</tr>
<tr>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">48.</div>
<div class="kwota">
<xsl:value-of select="tns:P_48"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">49.</div>
<div class="kwota">
<xsl:value-of select="tns:P_49"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">4. Emerytury - renty zagraniczne</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">50.</div>
<div class="kwota">
<xsl:value-of select="tns:P_50"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">51.</div>
<div class="kwota">
<xsl:value-of select="tns:P_51"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">52.</div>
<div class="kwota">
<xsl:value-of select="tns:P_52"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">53.</div>
<div class="kwota">
<xsl:value-of select="tns:P_53"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            5. Działalność wykonywana osobiście, o której mowa w art. 13 pkt 2, 4-9 ustawy, w tym z umowy o dzieło oraz czynności związane z pełnieniem obowiązków społecznych lub obywatelskich, z wyjątkiem należności wykazanych w wierszach 6 i 7 albo 8
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">54.</div>
<div class="kwota">
<xsl:value-of select="tns:P_54"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">55.</div>
<div class="kwota">
<xsl:value-of select="tns:P_55"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">56.</div>
<div class="kwota">
<xsl:value-of select="tns:P_56"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">57.</div>
<div class="kwota">
<xsl:value-of select="tns:P_57"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            6. Należności z tytułu umowy zlecenia, o której mowa w art. 13 pkt 8 ustawy, z wyjątkiem należności wykazanych w wierszu 7 albo 8
<font style="font-weight: normal">
<sup>16)</sup>
</font>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">58.</div>
<div class="kwota">
<xsl:value-of select="tns:P_58"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">59.</div>
<div class="kwota">
<xsl:value-of select="tns:P_59"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">60.</div>
<div class="kwota">
<xsl:value-of select="tns:P_60"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">61.</div>
<div class="kwota">
<xsl:value-of select="tns:P_61"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            7. Należności z tytułu wymienionego w wierszu 6, otrzymane przez podatników do ukończenia 26. roku życia<font style="font-weight: normal">
<sup>17)</sup>
</font>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">62.</div>
<div class="kwota">
<xsl:value-of select="tns:P_62"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">63.</div>
<div class="kwota">
<xsl:value-of select="tns:P_63"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">64.</div>
<div class="kwota">
<xsl:value-of select="tns:P_64"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">65.</div>
<div class="kwota">
<xsl:value-of select="tns:P_65"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            8. Należności z tytułu wymienionego w wierszu 6, otrzymane przez podatników od ukończenia wieku emerytalnego<font style="font-weight: normal">
<sup>18)</sup>
</font>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">66.</div>
<div class="kwota">
<xsl:value-of select="tns:P_66"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">67.</div>
<div class="kwota">
<xsl:value-of select="tns:P_67"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">68.</div>
<div class="kwota">
<xsl:value-of select="tns:P_68"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">69.</div>
<div class="kwota">
<xsl:value-of select="tns:P_69"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" rowspan="2">
            9. Prawa autorskie i inne prawa, o których mowa w art. 18 ustawy<br/>
<div class="opis-tekstowy">
              W poz. 73 należy wykazać przychody, do których zastosowano koszty uzyskania przychodów na podstawie art. 22 ust. 9 pkt 1-3 ustawy.
</div>
</td>
<td class="wypelniane">
<div class="opisrubryki">70.</div>
<div class="kwota">
<xsl:value-of select="tns:P_70"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">71.</div>
<div class="kwota">
<xsl:value-of select="tns:P_71"/>
</div>
</td>
<td class="puste" rowspan="2"/>
<td class="wypelniane" style="width: 12%" rowspan="2">
<div class="opisrubryki">72.</div>
<div class="kwota">
<xsl:value-of select="tns:P_72"/>
</div>
</td>
</tr>
<tr>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">73.</div>
<div class="kwota">
<xsl:value-of select="tns:P_73"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">74.</div>
<div class="kwota">
<xsl:value-of select="tns:P_74"/>
</div>
</td>
</tr>
<!-- m32
</table>
            <div class="lamstrone"></div>
<table>
-->
<tr>
<td class="niewypelnianeopisy">
            10. Należności z tytułu praktyk absolwenckich lub staży uczniowskich, z wyjątkiem należności wykazanych w wierszu 11
</td>
<td class="wypelniane">
<div class="opisrubryki">75.</div>
<div class="kwota">
<xsl:value-of select="tns:P_75"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">76.</div>
<div class="kwota">
<xsl:value-of select="tns:P_76"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">77.</div>
<div class="kwota">
<xsl:value-of select="tns:P_77"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            11. Należności z tytułu wymienionego w wierszu 10, otrzymane przez podatników do ukończenia 26. roku życia<font style="font-weight: normal">
<sup>17)</sup>
</font>
</td>
<td class="wypelniane">
<div class="opisrubryki">78.</div>
<div class="kwota">
<xsl:value-of select="tns:P_78"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">79.</div>
<div class="kwota">
<xsl:value-of select="tns:P_79"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">80.</div>
<div class="kwota">
<xsl:value-of select="tns:P_80"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            12. Zasiłki macierzyńskie, z wyjątkiem zasiłków wykazanych w wierszu 13 albo 14
</td>
<td class="wypelniane">
<div class="opisrubryki">81.</div>
<div class="kwota">
<xsl:value-of select="tns:P_81"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">82.</div>
<div class="kwota">
<xsl:value-of select="tns:P_82"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">83.</div>
<div class="kwota">
<xsl:value-of select="tns:P_83"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            13. Zasiłki macierzyńskie otrzymane przez podatników do ukończenia 26. roku życia<font style="font-weight: normal">
<sup>17)</sup>
</font>
</td>
<td class="wypelniane">
<div class="opisrubryki">84.</div>
<div class="kwota">
<xsl:value-of select="tns:P_84"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">85.</div>
<div class="kwota">
<xsl:value-of select="tns:P_85"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">86.</div>
<div class="kwota">
<xsl:value-of select="tns:P_86"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            14. Zasiłki macierzyńskie otrzymane przez podatników od ukończenia wieku emerytalnego<font style="font-weight: normal">
<sup>18)</sup>
</font>
</td>
<td class="wypelniane">
<div class="opisrubryki">87.</div>
<div class="kwota">
<xsl:value-of select="tns:P_87"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">88.</div>
<div class="kwota">
<xsl:value-of select="tns:P_88"/>
</div>
</td>
<td class="puste"/>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">89.</div>
<div class="kwota">
<xsl:value-of select="tns:P_89"/>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            15. Inne źródła<font style="font-weight: normal">
<sup>19)</sup>
</font>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">90.</div>
<div class="kwota">
<xsl:value-of select="tns:P_90"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">91.</div>
<div class="kwota">
<xsl:value-of select="tns:P_91"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">92.</div>
<div class="kwota">
<xsl:value-of select="tns:P_92"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">93.</div>
<div class="kwota">
<xsl:value-of select="tns:P_93"/>
</div>
</td>
<td class="wypelniane" style="width: 12%">
<div class="opisrubryki">94.</div>
<div class="kwota">
<xsl:value-of select="tns:P_94"/>
</div>
</td>
</tr>
</table>
<table class="normalna">
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Składki na ubezpieczenia społeczne, o których mowa w przepisach ustawy, podlegające odliczeniu od dochodu<font style="font-weight: normal">
<sup>20)</sup>
</font>, w tym zagraniczne, o których mowa w art. 26 ust. 1 pkt 2a ustawy, z wyjątkiem wykazanych w poz. 96
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">95.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_95)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Składki na ubezpieczenia społeczne, o których mowa w przepisach ustawy<font style="font-weight: normal">
<sup>20)</sup>
</font>,   
            w tym zagraniczne, o których mowa w art. 26 ust. 1 pkt 2a ustawy, których podstawę wymiaru stanowi przychód wymieniony w wierszach 2, 3, 7, 8 i 11 części E
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">96.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_96)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Składki na ubezpieczenia społeczne, o których mowa w przepisach ustawy, których podstawę wymiaru stanowi przychód zwolniony na podstawie art. 21 ust. 1 pkt 148 oraz 152-154 ustawy, wykazane odpowiednio w poz. 110, 111, 112, 115 i 116
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">97.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_97)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
</table>
</xsl:for-each>
</xsl:template>
<xsl:template name="InformacjaOPrzychodach1">
<xsl:param name="sekcja"/>
<xsl:for-each select="tns:PozycjeSzczegolowe">
<div class="tytul-sekcja-blok">
<h2>
<xsl:value-of select="$sekcja"/>
 INFORMACJA O WYSOKOŚCI PRZYCHODÓW, O KTÓRYCH MOWA W ART. 20 UST. 1 USTAWY
<div class="opis-tekstowy">
            (część tę wypełniają składający niebędący płatnikami, o których mowa w art.
            42a ustawy, w tym rolnicy)
</div>
</h2>
</div>
<table class="normalna">
<tr>
<td class="niewypelnianeopisy" style="width: 75%; text-align: center">Rodzaj przychodu</td>
<td class="niewypelnianeopisy" style="width: 25%; text-align: center">Przychód</td>
</tr>
<tr>
<td class="niewypelnianeopisy">Wynagrodzenie z tytułu umowy o pomocy przy zbiorach</td>
<td class="wypelniane">
<div class="opisrubryki">98.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_98)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="wypelniane">
<div class="opisrubryki">99.</div>
<xsl:value-of select="tns:P_99"/>
</td>
<td class="wypelniane">
<div class="opisrubryki">100.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_100)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="wypelniane">
<div class="opisrubryki">101.</div>
<xsl:value-of select="tns:P_101"/>
</td>
<td class="wypelniane">
<div class="opisrubryki">102.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_102)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="wypelniane">
<div class="opisrubryki">103.</div>
<xsl:value-of select="tns:P_103"/>
</td>
<td class="wypelniane">
<div class="opisrubryki">104.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_104)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy">
            Razem
<div class="opis-tekstowy">Suma kwot z poz.: 98, 100, 102 i 104.</div>
</td>
<td class="wypelniane">
<div class="opisrubryki">105.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_105)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
</table>
</xsl:for-each>
</xsl:template>
<xsl:template name="InformacjaOPrzychodach2">
<xsl:param name="sekcja"/>
<xsl:for-each select="tns:PozycjeSzczegolowe">
<div class="tytul-sekcja-blok">
<h2>
<xsl:value-of select="$sekcja"/>
 INFORMACJA O PRZYCHODACH ZWOLNIONYCH OD PODATKU, ZAŁĄCZNIKU ORAZ O POBRANYCH PRZEZ PŁATNIKA SKŁADKACH: NA UBEZPIECZENIE ZDROWOTNE ORAZ CZŁONKOWSKICH NA RZECZ ZWIĄZKÓW ZAWODOWYCH
<div class="opis-tekstowy">
            (część tę wypełniają składający będący płatnikami)
</div>
</h2>
</div>
<table class="normalna">
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Przychody z tytułu stypendium, o którym mowa w art. 21 ust. 1 pkt 40b ustawy
<div class="opis-tekstowy">Należy wykazać kwotę stypendium, do wysokości limitu zwolnienia<sup>21)</sup>.
</div>
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">106.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_106)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Przychody otrzymywane z zagranicy, o których mowa w art. 21 ust. 1 pkt 74 ustawy, między innymi renty inwalidzkie z tytułu inwalidztwa wojennego
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">107.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_107)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Przychody pochodzące ze środków bezzwrotnej pomocy zagranicznej, o których mowa w art. 21 ust. 1 pkt 46 ustawy
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">108.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_108)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Przychody ze stosunku pracy i stosunków pokrewnych, z umów zlecenia, praktyk absolwenckich lub staży uczniowskich oraz z zasiłków macierzyńskich, o których mowa w art. 21 ust. 1 pkt 148 ustawy<font style="font-weight: normal">
<div class="opis-tekstowy">Należy wykazać kwotę przychodu, do wysokości limitu zwolnienia<sup>22)</sup>.
</div>
</font>
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">109.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_109)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
</table>
<table class="normalna">
<tr>
<td class="niewypelnianeopisy" rowspan="5" style="width:5%">
                        w tym:
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 70%">
            przychody ze stosunku pracy i stosunków pokrewnych
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">110.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_110)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 70%">
            przychody z umów zlecenia
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">111.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_111)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 70%">
            przychody z tytułu praktyk absolwenckich lub staży uczniowskich
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">112.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_112)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 70%">
            przychody z zasiłków macierzyńskich
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">113.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_113)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
</table>
<table class="normalna">
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Przychody ze stosunku pracy i stosunków pokrewnych, z umów zlecenia oraz z zasiłków macierzyńskich o których mowa w art. 21 ust. 1 pkt 152-154 ustawy<font style="font-weight: normal">
<div class="opis-tekstowy">Należy wykazać kwotę przychodu, do wysokości limitu zwolnienia<sup>22)</sup>.
</div>
</font>
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">114.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_114)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
</table>
<table class="normalna">
<tr>
<td class="niewypelnianeopisy" rowspan="4" style="width:5%">
                        w tym:
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 70%">
            przychody ze stosunku pracy i stosunków pokrewnych
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">115.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_115)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 70%">
            przychody z umów zlecenia
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">116.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_116)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 70%">
            przychody z zasiłków macierzyńskich
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">117.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_117)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
</table>
<table class="normalna">
<tr>
<td class="wypelniane" style="width:25%" colspan="2">
<div class="opisrubryki">Rodzaj (podstawa prawna) przychodu zwolnionego od podatku, wykazanego w poz. 114</div>
<xsl:choose>
<xsl:when test="tns:P_118 = 1">118. <input type="checkbox" checked="checked" disabled="disabled"/>
art. 21 ust. 1 pkt 152 ustawy<br/>
</xsl:when>
<xsl:otherwise>
                                118. <input type="checkbox" disabled="disabled"/>
 art. 21 ust. 1 pkt 152 ustawy<br/>
</xsl:otherwise>
</xsl:choose>
<xsl:choose>
<xsl:when test="tns:P_119 = 1">119. <input type="checkbox" checked="checked" disabled="disabled"/>
 art. 21 ust. 1 pkt 153 ustawy<br/>
</xsl:when>
<xsl:otherwise>
                                119. <input type="checkbox" disabled="disabled"/>
 art. 21 ust. 1 pkt 153 ustawy<br/>
</xsl:otherwise>
</xsl:choose>
<xsl:choose>
<xsl:when test="tns:P_120 = 1">120. <input type="checkbox" checked="checked" disabled="disabled"/>
 art. 21 ust. 1 pkt 154 ustawy<br/>
</xsl:when>
<xsl:otherwise>
                                120. <input type="checkbox" disabled="disabled"/>
 art. 21 ust. 1 pkt 154 ustawy
</xsl:otherwise>
</xsl:choose>
</td>
</tr>
<tr>
<td class="wypelniane" style="width:25%" colspan="2">
<div class="opisrubryki">121. Do niniejszej informacji dołączono informację PIT-R</div>
<xsl:if test="tns:P_121 = 1">
<input type="checkbox" checked="checked" disabled="disabled"/>
1. tak
</xsl:if>
<xsl:if test="tns:P_121 = 2">
<input type="checkbox" checked="checked" disabled="disabled"/>
2. nie
</xsl:if>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Składki na ubezpieczenie zdrowotne pobrane przez płatnika do wysokości 9% podstawy jej wymiaru
<font style="font-weight: normal">
<sup>23)</sup>
</font>
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">122.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_122)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
<tr>
<td class="niewypelnianeopisy" style="width: 75%">
            Składki członkowskie na rzecz związków zawodowych pobrane przez płatnika, podlegające odliczeniu od dochodu, o których mowa w art. 26 ust. 1 pkt 2c ustawy
</td>
<td class="wypelniane" style="width:25%">
<div class="opisrubryki">123.</div>
<div class="kwota">
<xsl:call-template name="TransformataKwoty">
<xsl:with-param name="kwota" select="string(tns:P_123)"/>
<xsl:with-param name="czyKwotaZaokraglona" select="0"/>
</xsl:call-template>
</div>
</td>
</tr>
</table>
</xsl:for-each>
</xsl:template>
<xsl:template name="ObjasnieniaPit11">
<h2 class="tekst">Objaśnienia</h2>
<h3 align="justify">
<font size="2pt">
<div class="objaśnienia" style="width: 100%" align="justify">
<sup>1)</sup> W przypadku przedsiębiorstwa w spadku należy podać identyfikator podatkowy NIP zmarłego przedsiębiorcy.
<br/>
<sup>2)</sup> Jeżeli w odniesieniu do dochodów (przychodów) osoby fizycznej uzyskanych w roku, o którym mowa w poz. 4, składający sporządza i przesyła więcej niż jedną informację PIT-11 (niebędącą korektą poprzedniej), w informacji tej nie uwzględnia się kwot wykazanych w uprzednio przesłanych informacjach (nie sumuje się ich). W przypadku gdy sporządzone i przesłane w trakcie roku podatkowego informacje PIT-11 zawierają kompletne dane niezbędne do sporządzenia zeznania podatkowego, płatnik nie przesyła informacji PIT-11 po zakończeniu roku.
<br/>
<sup>3)</sup> Jeżeli w odniesieniu do dochodów (przychodów) osoby fizycznej uzyskanych w roku, o którym mowa w poz. 4, składający sporządza i przesyła więcej niż jedną informację PIT-11 (niebędącą korektą poprzedniej), należy podać kolejny numer składanej informacji dotyczącej tego roku podatkowego.
<br/>
<sup>4)</sup> Od 1 stycznia 2023 r. art. 35 ust. 6 ustawy zastępuje dotychczasowy art. 35 ust. 10 ustawy. Przepis art. 35 ust. 6 ustawy ma zastosowanie do dochodów (przychodów) uzyskanych od 1 stycznia 2023 r.
<br/>
<sup>5)</sup> Art. 35a ustawy został uchylony z dniem 26 października 2007 r. ustawą z dnia 24 sierpnia 2007 r. o zmianie ustawy o promocji zatrudnienia i instytucjach rynku pracy oraz o zmianie niektórych innych ustaw (Dz. U. poz. 1243). Uchylony przepis na mocy art. 7 ust. 7 powołanej ustawy ma zastosowanie do płatników do czasu obowiązywania umowy aktywizacyjnej zawartej przed dniem 26 października 2007 r. W tym przypadku płatnik przekazuje informację podatnikowi i urzędowi skarbowemu w terminie do końca lutego roku następującego po roku podatkowym.
<br/>
<sup>6)</sup> W przypadku przedsiębiorstwa w spadku za dzień zaprzestania działalności uważa się dzień wygaśnięcia zarządu sukcesyjnego albo wygaśnięcia uprawnienia do powołania zarządcy sukcesyjnego, jeżeli zarząd sukcesyjny nie został ustanowiony i dokonano zgłoszenia, o którym mowa w art. 12 ust. 1c ustawy z dnia 13 października 1995 r. o zasadach ewidencji i identyfikacji podatników i płatników (Dz. U. z 2022 r. poz. 166).
<br/>
<sup>7)</sup> Ilekroć w informacji jest mowa o urzędzie skarbowym, w tym o urzędzie skarbowym, do którego adresowana jest informacja – oznacza to urząd skarbowy, przy pomocy którego właściwy dla podatnika naczelnik urzędu skarbowego wykonuje swoje zadania.
<br/>
<sup>8)</sup> Zgodnie z art. 81 ustawy z dnia 29 sierpnia 1997 r. – Ordynacja podatkowa (Dz. U. z 2021 r. poz. 1540, z późn. zm.), zwanej dalej „Ordynacją podatkową”.
<br/>
<sup>9)</sup> W przypadku przedsiębiorstwa w spadku należy podać dane identyfikacyjne zmarłego przedsiębiorcy.
<br/>
<sup>10)</sup> W przypadku zaznaczenia kwadratu nr 2 w poz. 19-27 należy podać kraj inny niż Rzeczypospolita Polska oraz adres zamieszkania za granicą; dodatkowo kod kraju wydania dokumentu powinien być zgodny z krajem adresu zamieszkania.
<br/>
<sup>11)</sup> W poz. 13 należy podać numer służący identyfikacji do celów podatkowych lub ubezpieczeń społecznych uzyskany w państwie, w którym podatnik ma miejsce zamieszkania. W przypadku braku takiego numeru w poz. 13 należy podać numer dokumentu stwierdzającego tożsamość podatnika, uzyskanego w tym państwie.
<br/>
<sup>12)</sup> Poz. 14 i 15 należy wypełnić, jeżeli w poz. 13 podano zagraniczny numer identyfikacyjny podatnika lub numer dokumentu stwierdzającego tożsamość podatnika.
<br/>
<sup>13)</sup> W kwocie przychodów, w części E, nie uwzględnia się przychodów wolnych od podatku na podstawie przepisów ustawy oraz przychodów, od których na podstawie przepisów Ordynacji podatkowej zaniechano poboru podatku; jednakże w kolumnie e należy wykazać dochody zwolnione od podatku na podstawie umów o unikaniu podwójnego opodatkowania lub innych umów międzynarodowych.
<br/>
<sup>14)</sup> W kwocie kosztów uzyskania przychodów wykazuje się koszty faktycznie uwzględnione przez płatnika przy poborze zaliczek na podatek.
<br/>
<sup>15)</sup> W przypadku gdy zakład pracy pobierał zaliczki na podatek zarówno od należności ze stosunku: pracy, służbowego, spółdzielczego i z pracy nakładczej, o których mowa w art. 12 ust. 1 ustawy, jak i zasiłków pieniężnych z ubezpieczenia społecznego, o których mowa w art. 20 ust. 1 ustawy, łączną kwotę zaliczek pobranych z tych źródeł wykazuje tylko raz. Kwotę tę płatnik może wykazać w wierszu 1, odpowiednio w wierszach 2, 3, 12, 13, 14 albo 15 części E.
<br/>
<sup>16)</sup> W wierszu 1 i odpowiednio wierszu 6 części E wykazuje się również przychody z wymienionych tam tytułów otrzymane przez podatników, którzy przenieśli miejsce zamieszkania na terytorium Rzeczypospolitej Polskiej (tzw. ulga na powrót) oraz otrzymane przez podatników, którzy w roku podatkowym wychowywali co najmniej czworo dzieci (tzw. ulga dla rodzin 4+), jeśli płatnik w trakcie roku pobierał od tych przychodów zaliczki na podatek w sytuacji gdy podatnik nie złożył płatnikowi oświadczenia o spełnieniu warunków do stosowania zwolnień od podatku, o których mowa w art. 21 ust. 1 pkt 152 i 153 ustawy, albo z powodu przekroczenia limitu przychodu zwolnionego od podatku (sumy kwot wykazanych w poz. 109 i 114), gdy zwolnienie było stosowane w trakcie roku. W wierszach tych należy odpowiednio wykazać przychody uzyskane przez podatników wraz z kwotą kosztów uzyskania przychodów oraz sumą zaliczek na podatek pobranych przez płatnika.
<br/>
<sup>17)</sup> Wiersze 2, 7, 11 i 13 części E wypełnia się, jeśli płatnik w trakcie roku pobierał od tych przychodów zaliczki na podatek w związku ze złożeniem przez podatnika oświadczenia o rezygnacji ze stosowania w trakcie roku zwolnienia od podatku, o którym mowa w art. 21 ust. 1 pkt 148 ustawy (tzw. ulga dla młodych) albo z powodu przekroczenia limitu przychodu zwolnionego od podatku (sumy kwot wykazanych w poz. 109 i 114), gdy zwolnienie było stosowane w trakcie roku. W wierszach tych należy odpowiednio wykazać przychody uzyskane przez podatników do ukończenia 26. roku życia wraz z kwotą kosztów uzyskania przychodów oraz sumą zaliczek na podatek pobranych przez płatnika. Przychody ze stosunku pracy i stosunków pokrewnych uzyskane przez podatnika po dniu ukończenia 26. roku życia płatnik wykazuje w wierszu 1, odpowiednio przychody z umów zlecenia, o których mowa w art. 13 pkt 8 ustawy, płatnik wykazuje w wierszu 6, przychody z praktyk absolwenckich lub staży uczniowskich, płatnik wykazuje w wierszu 10, a przychody z zasiłków macierzyńskich płatnik wykazuje w wierszu 12.
<br/>
<sup>18)</sup> Wiersze 3, 8 i 14 części E wypełnia się, jeśli płatnik w trakcie roku pobierał od tych przychodów zaliczki na podatek w sytuacji gdy podatnik nie złożył płatnikowi oświadczenia o spełnieniu warunków do stosowania zwolnienia od podatku, o którym mowa w art. 21 ust. 1 pkt 154 ustawy (tzw. ulgi dla seniora) albo z powodu przekroczenia limitu przychodu zwolnionego od podatku (sumy kwot wykazanych w poz. 109 i 114), gdy zwolnienie było stosowane w trakcie roku. W wierszach tych należy odpowiednio wykazać przychody uzyskane przez podatników po ukończeniu 60. roku życia w przypadku kobiety i 65. roku życia w przypadku mężczyzny, pod warunkiem że podatnik podlega z tytułu uzyskania tych przychodów ubezpieczeniom społecznym w rozumieniu ustawy z dnia 13 października 1998 r. o systemie ubezpieczeń społecznych (Dz. U. z 2022 r. poz. 1009, z późn. zm.). W wierszach tych należy odpowiednio wykazać kwoty kosztów uzyskania przychodów oraz sumy zaliczek na podatek pobranych przez płatnika. Przychody ze stosunku pracy i stosunków pokrewnych uzyskane przez podatnika przed ukończeniem ww. wieku płatnik wykazuje w wierszu 1, odpowiednio przychody z umów zlecenia, o których mowa w art. 13 pkt 8 ustawy płatnik wykazuje w wierszu 6, a z zasiłków macierzyńskich – w wierszu 12.
<br/>
<sup>19)</sup> W wierszu 15 części E wykazuje się m.in. zasiłki pieniężne z ubezpieczenia społecznego wypłacone przez zakład pracy, z wyjątkiem zasiłków macierzyńskich wykazanych w wierszach 12, 13 i 14, należności z tytułu członkostwa w rolniczej spółdzielni produkcyjnej, należności za pracę przypadające tymczasowo aresztowanym lub skazanym, świadczenia wypłacone z Funduszów: Pracy i Gwarantowanych Świadczeń Pracowniczych, należności wynikające z umowy aktywizacyjnej, a także kwotę stypendium, o którym mowa w art. 21 ust. 1 pkt 40b ustawy, w wysokości przekraczającej kwotę zwolnioną od podatku (wykazaną w poz. 106).
<br/>
<sup>20)</sup> W poz. 95 i 96 nie wykazuje się składek, których podstawę wymiaru stanowi dochód (przychód) zwolniony od podatku na podstawie ustawy, oraz składek, których podstawę wymiaru stanowi dochód, od którego na podstawie przepisów Ordynacji podatkowej zaniechano poboru podatku, a w przypadku składek zagranicznych, których podstawę wymiaru stanowi dochód (przychód) zwolniony od podatku na podstawie umów o unikaniu podwójnego opodatkowania.
<br/>
<sup>21)</sup> Limit zwolnienia od podatku wynosi 3 800 zł w roku podatkowym.
<br/>
<sup>22)</sup> Limit zwolnienia od podatku przychodów wykazanych w poz. 109 i 114 wynosi łącznie 85 528 zł w roku podatkowym.
<br/>
<sup>23)</sup> W poz. 122 wykazuje się składki na ubezpieczenie zdrowotne, o których mowa w ustawie z dnia 27 sierpnia 2004 r. o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych (Dz. U. z 2021 r. poz. 1285, z późn. zm.). Składki wykazane w poz. 122 są uwzględniane w kwocie składek do obliczenia w zeznaniu podatkowym dodatkowego zwrotu z tytułu ulgi na dzieci, zgodnie z art. 27f ust. 9 ustawy.
</div>
</font>
</h3>
</xsl:template>
<xsl:template name="Pouczenie">
<h2 class="tekst">Pouczenie</h2>
    Za uchybienie obowiązkom płatnika / składającego niebędącego płatnikiem, grozi odpowiedzialność przewidziana w Kodeksie karnym skarbowym.
</xsl:template>
<xsl:template name="NaglowekTytulowy">
<xsl:param name="naglowek"/>
<xsl:param name="nazwa"/>
<xsl:param name="objasnienie"/>
<xsl:param name="podstawy-prawne"/>
<xsl:param name="uzycie"/>
<xsl:param name="nad-data"/>
<xsl:param name="przed-data"/>
<xsl:param name="po-dacie"/>
<!-- deklaracja | zalacznik -->
<div>
<xsl:choose>
<xsl:when test="$uzycie = 'deklaracja'">
<xsl:attribute name="class">tlo-formularza</xsl:attribute>
</xsl:when>
<xsl:when test="$uzycie = 'zalacznik'">
<xsl:attribute name="class">tlo-zalacznika</xsl:attribute>
</xsl:when>
</xsl:choose>
<xsl:if test="$nazwa">
<h1 class="nazwa">
<xsl:copy-of select="$nazwa"/>
</h1>
</xsl:if>
<xsl:copy-of select="$nad-data"/>
<xsl:if test="$naglowek">
<div class="okres">
<xsl:if test="$przed-data or $po-dacie">
<span class="obok-daty">
<xsl:copy-of select="$przed-data"/>
</span>
</xsl:if>
<xsl:apply-templates select="$naglowek/*[local-name()='Miesiac'] | $naglowek/*[local-name()='Kwartal']"/>
<xsl:apply-templates select="$naglowek/*[local-name()='OkresOd']"/>
<xsl:apply-templates select="$naglowek/*[local-name()='OkresDo']"/>
<xsl:apply-templates select="$naglowek/*[local-name()='Data']"/>
<xsl:if test="$przed-data or $po-dacie">
<span class="obok-daty">
<xsl:copy-of select="$po-dacie"/>
</span>
</xsl:if>
</div>
</xsl:if>
<xsl:if test="$objasnienie">
<div class="objasnienie">
<xsl:copy-of select="$objasnienie"/>
</div>
</xsl:if>
</div>
<xsl:if test="$podstawy-prawne">
<div class="prawne">
<xsl:copy-of select="$podstawy-prawne"/>
</div>
</xsl:if>
</xsl:template>
<xsl:template name="TransformataKwoty">
<xsl:param name="kwota"/>
<xsl:param name="czyKwotaZaokraglona"/>
<xsl:choose>
<xsl:when test="$kwota = ''">
<xsl:choose>
<xsl:when test="$czyKwotaZaokraglona">
            zł
</xsl:when>
<xsl:otherwise>
            zł,   gr
</xsl:otherwise>
</xsl:choose>
</xsl:when>
<xsl:when test="contains($kwota, '.')">
<xsl:value-of select="substring-before($kwota,'.')"/>
 zł, <xsl:value-of select="substring-after($kwota,'.')"/>
 gr
</xsl:when>
<xsl:otherwise>
<xsl:choose>
<xsl:when test="$czyKwotaZaokraglona">
<xsl:value-of select="$kwota"/>
 zł
</xsl:when>
<xsl:otherwise>
<xsl:value-of select="$kwota"/>
 zł, 00 gr
</xsl:otherwise>
</xsl:choose>
</xsl:otherwise>
</xsl:choose>
</xsl:template>
</xsl:stylesheet>