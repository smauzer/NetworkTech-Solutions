# NetworkTech-Solutions Kft.

**⚠️A weboldal egy iskolai projekt részeként készült és csak egy fiktív céget mutat be!⚠️**

## Projekt készítése

**Projekt kezdete:** 2023.10.19

**Projekt határidő:** 2023.11.08

**Készítették:**
 - Smauzer Dávid
 - Nagy Noel
 - Tóth Barnabás
 - Baán Gyula

## Cég leírása

![NetworkTech-Solutions Logo](/default/static/default/img/nts-logo.png)

A cég szerverekkel, felhőszolgáltatások, illetve teljes hálózat megtervezésével és kivitelezésével foglalkozik. Ezeken túl a Web-oldalon hálózati eszközök is vásárolhatóak.
A NetworkTech Solutions Nyugat-Magyarország legnagyobb és legmodernebb vállalata. A legmodernebb, legkorszerűbb eszközökkel dolgozunk 400 kollégánkkal közel 15 telephelyen elosztva. Ennyi telephellyel az ország nyugati részének egészét lefedjük, később Kelet-Magyarországra, illetve Ausztria és Szlovákia felé is nyitni szeretnénk.

**A legfőbb telephelyünk:**

**Győr** belvárosában található a Vidanet mellett. Ez a legfőbb állomása a cégnek. Itt közel 50 emberünk dolgozik, mivel az Ügyfélszolgálati állomásunk és a Szerver farmunk is itt található.

**További 3 fontos telephely:**
 - Mosonmagyaróvár
 - Sopron
 - Veszprém

**Munkatársainkról:**
 - A 400 munkatársunk közül:
 - 25-en az ügyfélszolgálati csapatot erősíti
 - 10 a HR-osztályt
 - 10 rendszergazda, aki csak a telephelyeinken dolgozik
 - a többi kollégánk a terepen dolgozik, vagy valamilyen vezető

## Előkövetelmények

A webaplikáció futattásához egyedül python telepítésére van szükség!

Használt python verzió: **3.10.12**

A repository és python letöltése után a parancssorban a következő parancs lefuttatásával fel tudjuk telepíteni az összes szükséges kiegészítőt:

`pip install -r requirements.txt`

**A parancs lefuttatásakor a projekt mappájában kell lennünk a pranacssorban!** Ezt a `cd` parancs hazsnálatával tudjuk megtenni.

**A kiegészítők telepítését érdemes minden frissités után elvégezni, a későbbi problémák elkerülése érdekében.**

## Webaplikáció futtatása

**Ha az előkövetelmények fentállnak**, utána az aplikáció készen áll a futtatásra. A parancssorban navigáljunk a projekt főkönyvtárába és futtassuk le a következő parancsokat:

`python manage.py migrate`

`python manage.py runserver`

**Az első parancs lefuttatása csak a frissítések utáni első elindítás előtt szükséges.**