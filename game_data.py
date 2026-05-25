# game_data.py — Oyun sahneleri ve finaller (v2 — 40 sahne, 10 final)

SCENES = {

    # ═══════════════════════════════════════
    # BÖLÜM 1: BAŞLANGIÇ
    # ═══════════════════════════════════════

    1: {
        "id": 1,
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "20 yaşındasın. Küçük bir evde yaşıyorsun, cebinde sadece 500$ var.\n\n"
            "Milyarder olma hayalin var. Etrafın seni deli gibi görüyor ama sen eminsin.\n\n"
            "İlk adımın ne olacak?"
        ),
        "choices": [
            {
                "text": "💼 Normal bir işe gir",
                "effects": {"money": 300, "experience": 5, "risk": -2},
                "next": 2
            },
            {
                "text": "📦 Küçük bir online satış işi kur",
                "effects": {"money": -200, "experience": 10, "risk": 5},
                "next": 3
            },
            {
                "text": "📈 Tüm paranı kriptoya yatır",
                "effects": {"money": -500, "risk": 20},
                "next": 4
            }
        ]
    },

    2: {
        "id": 2,
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "Küçük bir şirkette muhasebe asistanı oldun. Maaşın 1.200$/ay.\n\n"
            "Patron seni fark etti ve ek proje teklif etti. Fazla mesai para getirir ama zamanını yer.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "⏰ Fazla mesaiyi kabul et",
                "effects": {"money": 500, "experience": 10, "reputation": 5},
                "next": 5
            },
            {
                "text": "📚 Boş vakitlerde online kurs al",
                "effects": {"money": -200, "experience": 20, "risk": -5},
                "next": 6
            },
            {
                "text": "🤝 İş arkadaşlarıyla networking yap",
                "effects": {"connections": 15, "reputation": 5},
                "next": 7
            }
        ]
    },

    3: {
        "id": 3,
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "E-ticaret mağazan açtın. İlk ürünün: el yapımı deri çantalar.\n\n"
            "300$ harcadın malzemelere. İlk siparişin geldi — 80$ kazandın!\n\n"
            "Şimdi ne yapacaksın?"
        ),
        "choices": [
            {
                "text": "💰 Kazancı tekrar işe yatır",
                "effects": {"money": -80, "experience": 15, "risk": 5},
                "next": 8
            },
            {
                "text": "📱 Sosyal medyada reklam ver",
                "effects": {"money": -150, "reputation": 10, "connections": 5},
                "next": 9
            },
            {
                "text": "🛑 Güvenli oynayıp para biriktir",
                "effects": {"money": 80, "risk": -5},
                "next": 10
            }
        ]
    },

    4: {
        "id": 4,
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "500$'ını kriptoya yatırdın. İki hafta sonra piyasa çöktü.\n\n"
            "Paranın %70'ini kaybettin. Elimde 150$ kaldı.\n\n"
            "Çaresiz ama umudunu kaybetmedin. Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "😤 Daha fazla yatırım yap (borç al)",
                "effects": {"money": -150, "risk": 30},
                "next": 11
            },
            {
                "text": "🔄 Her şeyden vazgeç, iş ara",
                "effects": {"money": 400, "experience": 5, "risk": -10},
                "next": 2
            },
            {
                "text": "📊 Kripto öğren ve bekle",
                "effects": {"experience": 20, "risk": 5},
                "next": 12
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 2: İLK PARA
    # ═══════════════════════════════════════

    5: {
        "id": 5,
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Patron seni terfi ettirdi! Artık 2.500$/ay kazanıyorsun.\n\n"
            "Ama bir startup fikrin var ve kafandan çıkmıyor: Yerel restoranlar için teslimat uygulaması.\n\n"
            "Riski göze alacak mısın?"
        ),
        "choices": [
            {
                "text": "🚀 İşi bırak, startup kur",
                "effects": {"money": -1000, "experience": 20, "risk": 25},
                "next": 13
            },
            {
                "text": "🌙 Gece vakitlerde geliştir",
                "effects": {"money": -300, "experience": 15, "risk": 10},
                "next": 14
            },
            {
                "text": "💼 Kararlı şekilde işte kal",
                "effects": {"money": 1000, "experience": 5, "reputation": 5},
                "next": 15
            }
        ]
    },

    6: {
        "id": 6,
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "6 ay boyunca programlama ve pazarlama kursları aldın.\n\n"
            "Artık temel kodlama biliyorsun. Bir SaaS ürünü fikrin var: küçük işletmeler için muhasebe yazılımı.\n\n"
            "Sonraki adımın ne?"
        ),
        "choices": [
            {
                "text": "💻 Ürünü kendin geliştir",
                "effects": {"money": -500, "experience": 25, "risk": 15},
                "next": 13
            },
            {
                "text": "🤝 Ortak bul ve birlikte kur",
                "effects": {"money": -200, "connections": 20, "risk": 10},
                "next": 16
            },
            {
                "text": "📋 Önce küçük freelance işler al",
                "effects": {"money": 800, "experience": 10},
                "next": 15
            }
        ]
    },

    7: {
        "id": 7,
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Bir iş yemeğinde zengin bir girişimciyle tanıştın: Kemal Bey.\n\n"
            "Kemal Bey, yeni projesine ortak arıyor. Seni ekibine almak istiyor ama hisse verecek.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "✅ Teklifi kabul et",
                "effects": {"connections": 25, "reputation": 10, "experience": 15},
                "next": 17
            },
            {
                "text": "🤔 Araştır, sonra karar ver",
                "effects": {"connections": 10, "risk": -5},
                "next": 17
            },
            {
                "text": "❌ Reddet, kendi işini kur",
                "effects": {"money": -300, "experience": 10, "risk": 15},
                "next": 13
            }
        ]
    },

    8: {
        "id": 8,
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "E-ticaret mağazan büyüyor! Artık ayda 2.000$ kazanıyorsun.\n\n"
            "Bir tedarikçi teklif etti: Toplu sipariş verirsen fiyatı %40 düşürür.\n"
            "Bunun için 5.000$ gerekiyor.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🏦 Bankadan kredi çek",
                "effects": {"money": 3000, "risk": 20},
                "next": 18
            },
            {
                "text": "👨‍👩‍👧 Aileden borç iste",
                "effects": {"money": 2000, "connections": -5, "risk": 10},
                "next": 18
            },
            {
                "text": "🐢 Yavaş ama güvenli büy",
                "effects": {"money": 500, "risk": -5},
                "next": 19
            }
        ]
    },

    9: {
        "id": 9,
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Instagram reklamın viral oldu! 500 yeni sipariş geldi.\n\n"
            "Ama tek başına yetiştirmek imkansız. Birini işe almanın vakti geldi mi?\n"
            "Aylık maliyetin 800$ artar."
        ),
        "choices": [
            {
                "text": "👷 Hemen işe al",
                "effects": {"money": -800, "experience": 10, "connections": 10},
                "next": 18
            },
            {
                "text": "🤖 Süreci otomatize et",
                "effects": {"money": -500, "experience": 20, "risk": 10},
                "next": 18
            },
            {
                "text": "😤 Siparişlerin bir kısmını reddet",
                "effects": {"money": 1000, "reputation": -10},
                "next": 19
            }
        ]
    },

    10: {
        "id": 10,
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Biriktirdiğin para 1.500$'a ulaştı. Küçük ama güvende hissediyorsun.\n\n"
            "Bir fırsat çıktı: Arkadaşın senden 2.000$ ortaklık istiyor.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🤝 Ortaklık teklifi kabul et",
                "effects": {"money": -1500, "connections": 20, "risk": 15},
                "next": 16
            },
            {
                "text": "📊 Kendi işini kur",
                "effects": {"money": -1000, "experience": 15, "risk": 20},
                "next": 13
            },
            {
                "text": "💤 Bekle, daha fazla biriktir",
                "effects": {"money": 500, "risk": -5},
                "next": 15
            }
        ]
    },

    11: {
        "id": 11,
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Borç alıp kriptoya yatırdın. Şans sende! Piyasa toparladı ve 3x kazandın.\n\n"
            "Artık 5.000$'ın var. Ama borçlusun ve risk çok yüksek.\n\n"
            "Şimdi ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "💸 Hepsini çek, borcu öde",
                "effects": {"money": 2000, "risk": -20},
                "next": 15
            },
            {
                "text": "📈 Yeniden yatır, daha büyük kazan",
                "effects": {"money": -3000, "risk": 30},
                "next": 20
            },
            {
                "text": "🏗️ İş kurmak için kullan",
                "effects": {"money": 3000, "experience": 10, "risk": -10},
                "next": 13
            }
        ]
    },

    12: {
        "id": 12,
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "6 ay kripto analizi öğrendin. Artık piyasayı daha iyi anlıyorsun.\n\n"
            "Küçük yatırımlarla 800$ biriktirdin. Bir kripto danışmanlık kanalı açabilirsin.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "📢 YouTube/Twitter kanalı aç",
                "effects": {"money": -100, "reputation": 15, "connections": 10},
                "next": 19
            },
            {
                "text": "💼 Kripto fonu kur",
                "effects": {"money": -500, "experience": 20, "risk": 25},
                "next": 20
            },
            {
                "text": "📖 Kitap yaz ve sat",
                "effects": {"money": 300, "reputation": 10, "experience": 10},
                "next": 15
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 3: BÜYÜME
    # ═══════════════════════════════════════

    13: {
        "id": 13,
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Startupın ilk ürünü hazır! Beta kullanıcılar memnun.\n\n"
            "Bir melek yatırımcı 50.000$ teklif etti, karşılığında %20 hisse istiyor.\n\n"
            "Teklife ne diyorsun?"
        ),
        "choices": [
            {
                "text": "✅ Teklifi kabul et",
                "effects": {"money": 40000, "connections": 20, "reputation": 15},
                "next": 21
            },
            {
                "text": "💬 Pazarlık yap, %10 teklif et",
                "effects": {"money": 25000, "connections": 10, "experience": 10},
                "next": 21
            },
            {
                "text": "❌ Reddet, kendi büyü",
                "effects": {"money": -2000, "experience": 15, "risk": 20},
                "next": 22
            }
        ]
    },

    14: {
        "id": 14,
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Geceleri kodladın, gündüzleri çalıştın. 6 ay sonra MVP hazır.\n\n"
            "İlk 10 müşterin var. Artık işi tam zamanlı yapmayı düşünüyorsun.\n\n"
            "Ama henüz kazanç yok. Güvenli mi olur?"
        ),
        "choices": [
            {
                "text": "🔥 İşi bırak, tam gaz",
                "effects": {"money": -1500, "experience": 20, "risk": 20},
                "next": 21
            },
            {
                "text": "📈 İşte kal, müşteri artır",
                "effects": {"money": 500, "connections": 10, "experience": 10},
                "next": 22
            },
            {
                "text": "💼 Şirketi satacak kişi bul",
                "effects": {"money": 5000, "reputation": 10},
                "next": 23
            }
        ]
    },

    15: {
        "id": 15,
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Durağan bir noktadasın. 3.000$ birikiminiz var.\n\n"
            "Bir franchise fırsatı çıktı: Ünlü bir kahve markasının bayiliği. 10.000$ sermaye gerekiyor.\n\n"
            "Seçimin ne?"
        ),
        "choices": [
            {
                "text": "☕ Franchise al",
                "effects": {"money": -8000, "experience": 15, "connections": 10, "risk": 15},
                "next": 24
            },
            {
                "text": "💻 Dijital işe odaklan",
                "effects": {"money": -1000, "experience": 20, "risk": 10},
                "next": 13
            },
            {
                "text": "🏠 Gayrimenkul yatırımı yap",
                "effects": {"money": -3000, "risk": 20, "connections": 5},
                "next": 25
            }
        ]
    },

    16: {
        "id": 16,
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Ortağınla işler başladı. O teknik, sen pazarlama.\n\n"
            "6 ay sonra aylık 15.000$ gelir elde ediyorsunuz.\n\n"
            "Ama ortağınla anlaşmazlık yaşıyorsunuz. Şirketi nasıl büyüteceğiniz konusunda fikir ayrılığı var."
        ),
        "choices": [
            {
                "text": "🤝 Uzlaş ve birlikte devam et",
                "effects": {"connections": 15, "reputation": 10, "experience": 10},
                "next": 21
            },
            {
                "text": "💰 Ortağın hissesini satın al",
                "effects": {"money": -5000, "risk": 10},
                "next": 22
            },
            {
                "text": "🤯 Şirketi sat ve yeniden başla",
                "effects": {"money": 20000, "experience": 15},
                "next": 26
            }
        ]
    },

    17: {
        "id": 17,
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Kemal Bey'in ekibindesin. Proje 2 milyon dolar yatırım aldı!\n\n"
            "Senin hissen: %5. Kağıt üzerinde 100.000$ değerinde.\n\n"
            "Ama projenin başarısı belirsiz. Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "📊 Aktif çalış, değeri artır",
                "effects": {"experience": 20, "connections": 20, "reputation": 10},
                "next": 21
            },
            {
                "text": "💸 Hisseni şimdi sat",
                "effects": {"money": 50000, "connections": -10},
                "next": 26
            },
            {
                "text": "🔍 Kendi startupını kurarak devam et",
                "effects": {"money": -2000, "experience": 15, "risk": 20},
                "next": 13
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 4: GÜÇ VE İTİBAR
    # ═══════════════════════════════════════

    18: {
        "id": 18,
        "chapter": "📖 Bölüm 4: Güç ve İtibar",
        "text": (
            "İşlerin büyüdü! Aylık ciron 50.000$'a ulaştı.\n\n"
            "Forbes 'Gelecek Vadeden Girişimciler' listesine girdin!\n\n"
            "Medya ilgisi arttı. Bir TV programı röportaj istiyor. Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "📺 Röportajı kabul et",
                "effects": {"reputation": 25, "connections": 15},
                "next": 26
            },
            {
                "text": "🤫 Sessiz kalmayı tercih et",
                "effects": {"risk": -10, "experience": 10},
                "next": 27
            },
            {
                "text": "✍️ Kendi blog/podcast aç",
                "effects": {"reputation": 15, "connections": 20, "money": 2000},
                "next": 26
            }
        ]
    },

    19: {
        "id": 19,
        "chapter": "📖 Bölüm 4: Güç ve İtibar",
        "text": (
            "Yavaş büyüdün ama sağlam temeller attın.\n\n"
            "Rakibinle rekabete girdin. Ama o daha büyük ve hızlı.\n\n"
            "Stratejin ne olacak?"
        ),
        "choices": [
            {
                "text": "⚔️ Fiyatları düşür, savaş",
                "effects": {"money": -3000, "reputation": 5, "risk": 20},
                "next": 27
            },
            {
                "text": "🤝 Rakiple ortak ol",
                "effects": {"connections": 25, "money": 5000},
                "next": 26
            },
            {
                "text": "🎯 Nişe odaklan, farklılaş",
                "effects": {"experience": 20, "reputation": 15, "money": 3000},
                "next": 26
            }
        ]
    },

    20: {
        "id": 20,
        "chapter": "📖 Bölüm 4: Güç ve İtibar",
        "text": (
            "Kripto piyasası yeniden yükseldi! Portföyün 3x büyüdü.\n\n"
            "Artık 20.000$'ın var. Ama piyasa çok volatil.\n\n"
            "Kazancını ne yapacaksın?"
        ),
        "choices": [
            {
                "text": "🏠 Gayrimenkule çevir",
                "effects": {"money": 15000, "risk": -10},
                "next": 25
            },
            {
                "text": "🚀 Startup'a yatır",
                "effects": {"money": 10000, "experience": 15, "risk": 15},
                "next": 13
            },
            {
                "text": "📊 Borsa ve tahvile çeşitle",
                "effects": {"money": 12000, "risk": -15, "experience": 10},
                "next": 26
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 5: KRİZ
    # ═══════════════════════════════════════

    21: {
        "id": 21,
        "chapter": "📖 Bölüm 5: Kriz",
        "text": (
            "Şirketin değeri 5 milyon dolara ulaştı!\n\n"
            "Ama beklenmedik bir kriz: Ekonomik durgunluk. Müşteriler ödemiyor, nakit akışı durdu.\n\n"
            "3 ay sonra iflas edebilirsin. Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "✂️ Masrafları kes, küçül",
                "effects": {"money": 5000, "reputation": -10, "risk": -15},
                "next": 28
            },
            {
                "text": "💊 Acil yatırımcı bul",
                "effects": {"money": 20000, "connections": 15, "risk": 10},
                "next": 29
            },
            {
                "text": "🏳️ Şirketi sat",
                "effects": {"money": 30000, "experience": 10},
                "next": 30
            }
        ]
    },

    22: {
        "id": 22,
        "chapter": "📖 Bölüm 5: Kriz",
        "text": (
            "Rakibin piyasaya girdi ve seni ezmeye çalışıyor. Fiyatları senin altına indirdi.\n\n"
            "Müşterilerinin %30'unu kaybettin. Çok zor bir dönem.\n\n"
            "Nasıl ayakta kalacaksın?"
        ),
        "choices": [
            {
                "text": "🔬 Yenilik yap, farklılaş",
                "effects": {"money": -5000, "experience": 25, "reputation": 15},
                "next": 28
            },
            {
                "text": "⚖️ Hukuki yola başvur",
                "effects": {"money": -3000, "risk": 15, "connections": -10},
                "next": 29
            },
            {
                "text": "🤝 Rakiple birleş",
                "effects": {"money": 10000, "connections": 20},
                "next": 30
            }
        ]
    },

    23: {
        "id": 23,
        "chapter": "📖 Bölüm 5: Kriz",
        "text": (
            "Şirketini 80.000$'a sattın. Büyük kazanç!\n\n"
            "Ama alıcı, anlaşma sonrası bazı sorunlar çıkardı. Yarısını ödedi, kalanı için dava açtı.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "⚖️ Mahkemeye ver",
                "effects": {"money": -5000, "risk": 20, "reputation": -5},
                "next": 30
            },
            {
                "text": "🤝 Uzlaşma teklif et",
                "effects": {"money": 10000, "risk": -10},
                "next": 30
            },
            {
                "text": "💼 Yeni işe odaklan",
                "effects": {"money": -2000, "experience": 15, "risk": -5},
                "next": 26
            }
        ]
    },

    24: {
        "id": 24,
        "chapter": "📖 Bölüm 5: Kriz",
        "text": (
            "Kahve bayilik işin çok iyi gidiyor! 3 şuben var artık.\n\n"
            "Ama bölgendeki büyük zincir kafeler seni sıkıştırıyor.\n\n"
            "Rakipler çok güçlü. Stratejin ne?"
        ),
        "choices": [
            {
                "text": "🌐 Online satışa geç",
                "effects": {"money": -2000, "experience": 15, "risk": 10},
                "next": 28
            },
            {
                "text": "📦 Franchise ağını genişlet",
                "effects": {"money": -5000, "connections": 20, "reputation": 15},
                "next": 29
            },
            {
                "text": "💰 Rakibe sat, kâr et",
                "effects": {"money": 50000, "experience": 10},
                "next": 30
            }
        ]
    },

    25: {
        "id": 25,
        "chapter": "📖 Bölüm 5: Kriz",
        "text": (
            "Gayrimenkul yatırımın var. 2 daire aldın.\n\n"
            "Kira getirisi güzel ama beklenmedik sorun: Kiracılar kirası ödemiyor, tahliye zor.\n\n"
            "Üstelik yeni bir daire fırsatı çıktı — çok cazip fiyat ama nakit sıkıntısındasın."
        ),
        "choices": [
            {
                "text": "🏦 Krediyle daire al",
                "effects": {"money": -2000, "risk": 20, "connections": 5},
                "next": 29
            },
            {
                "text": "📤 Mevcut daireleri sat",
                "effects": {"money": 25000, "experience": 10},
                "next": 30
            },
            {
                "text": "🏢 Ticari gayrimenkule geç",
                "effects": {"money": -10000, "connections": 15, "risk": 15},
                "next": 28
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 6: GLOBAL PAZAR
    # ═══════════════════════════════════════

    26: {
        "id": 26,
        "chapter": "📖 Bölüm 6: Global Pazar",
        "text": (
            "Şirketin değeri 50 milyon dolar! Artık uluslararası arenaya çıkma zamanı.\n\n"
            "Hangi pazara giriyorsun?"
        ),
        "choices": [
            {
                "text": "🇺🇸 ABD pazarına gir",
                "effects": {"money": -10000, "experience": 20, "risk": 25, "connections": 15},
                "next": 31
            },
            {
                "text": "🌏 Asya pazarına gir",
                "effects": {"money": -8000, "experience": 15, "connections": 25, "risk": 20},
                "next": 32
            },
            {
                "text": "🇪🇺 Avrupa pazarına gir",
                "effects": {"money": -7000, "reputation": 20, "experience": 15, "risk": 15},
                "next": 33
            }
        ]
    },

    27: {
        "id": 27,
        "chapter": "📖 Bölüm 6: Global Pazar",
        "text": (
            "Sessiz ama güçlü bir oyuncu oldun. Kimse seni tam bilmiyor ama etkilisin.\n\n"
            "Bir hükümet ihalesi çıktı: 100 milyon dolarlık proje.\n\n"
            "Katılacak mısın?"
        ),
        "choices": [
            {
                "text": "✅ İhaleye gir",
                "effects": {"money": -5000, "connections": 30, "risk": 20},
                "next": 31
            },
            {
                "text": "🤫 Arka planda ortak ol",
                "effects": {"money": 10000, "connections": 20, "risk": 10},
                "next": 34
            },
            {
                "text": "🚀 Özel sektörde büy",
                "effects": {"money": 5000, "experience": 20, "reputation": 15},
                "next": 32
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 7: İMPARATORLUK
    # ═══════════════════════════════════════

    28: {
        "id": 28,
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "Krizi atlattın ve güçlendin! Rakiplerin battı, sen hayatta kaldın.\n\n"
            "Artık sektörün en önemli isimlerinden birisin.\n\n"
            "Bir dev şirketten birleşme teklifi geldi: 200 milyon dolar."
        ),
        "choices": [
            {
                "text": "💰 Teklifi kabul et (200M$)",
                "effects": {"money": 200000000, "reputation": 20, "risk": -20},
                "next": 35
            },
            {
                "text": "🦅 Bağımsız kalmaya devam et",
                "effects": {"money": 5000000, "reputation": 25, "risk": 10},
                "next": 36
            },
            {
                "text": "📈 Borsa'ya çık (IPO)",
                "effects": {"money": 150000000, "reputation": 30, "connections": 20},
                "next": 35
            }
        ]
    },

    29: {
        "id": 29,
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "Yatırımcılar seni destekledi! Şirketin 100 milyon dolar değere ulaştı.\n\n"
            "Ama büyük güç büyük sorumluluk getirir. Vergi makamları seni inceliyor.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "📋 Tam şeffaflıkla hareket et",
                "effects": {"reputation": 20, "risk": -20, "money": -5000000},
                "next": 36
            },
            {
                "text": "🌍 Offshore yapılanmaya geç",
                "effects": {"money": 10000000, "risk": 30},
                "next": 36
            },
            {
                "text": "⚖️ Hukuk ekibi kur",
                "effects": {"money": -8000000, "risk": -15, "connections": 10},
                "next": 35
            }
        ]
    },

    30: {
        "id": 30,
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "Birçok çıkış yaptın ve toplamda 100 milyon dolar biriktirdin.\n\n"
            "Artık bir yatırımcısın. Portföyünde 15 startup var.\n\n"
            "Yeni nesil girişimcileri desteklemek mi, yoksa kendi mega projeye mi odaklanmak?"
        ),
        "choices": [
            {
                "text": "🌱 Ekosistemi geliştir",
                "effects": {"connections": 30, "reputation": 25, "experience": 20, "money": 20000000},
                "next": 36
            },
            {
                "text": "🚀 Uzay/temiz enerji projesine gir",
                "effects": {"money": -20000000, "reputation": 30, "risk": 20},
                "next": 37
            },
            {
                "text": "🏖️ Portföyü büyüt",
                "effects": {"money": 50000000, "risk": -10},
                "next": 35
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 8: GLOBAL GÜÇ
    # ═══════════════════════════════════════

    31: {
        "id": 31,
        "chapter": "📖 Bölüm 8: Global Güç",
        "text": (
            "ABD pazarında tutunmayı başardın! Şirketin değeri 500 milyon dolar.\n\n"
            "Silikon Vadisi'nde ofis açtın. Büyük teknoloji şirketleri seni rakip görüyor.\n\n"
            "Bir dev sana satın alma teklifi yaptı: 800 milyon dolar."
        ),
        "choices": [
            {
                "text": "💰 Sat ve özgürleş (800M$)",
                "effects": {"money": 800000000, "reputation": 20, "risk": -20},
                "next": 38
            },
            {
                "text": "🛡️ Reddet, halka aç (IPO)",
                "effects": {"money": 500000000, "reputation": 35, "connections": 25},
                "next": 39
            },
            {
                "text": "🤝 Ortak ol, %51 elinde kalsın",
                "effects": {"money": 300000000, "connections": 30, "reputation": 20},
                "next": 38
            }
        ]
    },

    32: {
        "id": 32,
        "chapter": "📖 Bölüm 8: Global Güç",
        "text": (
            "Asya pazarı patladı! Çin, Japonya ve Güneydoğu Asya'da güçlü konumdasın.\n\n"
            "Şirketin değeri 600 milyon dolar. Ama yerel hükümetler kısıtlama getirebilir.\n\n"
            "Stratejin ne?"
        ),
        "choices": [
            {
                "text": "🏛️ Yerel ortak bul",
                "effects": {"connections": 35, "risk": -15, "money": 100000000},
                "next": 38
            },
            {
                "text": "💪 Bağımsız büy, lobi yap",
                "effects": {"money": 200000000, "risk": 25, "reputation": 15},
                "next": 39
            },
            {
                "text": "🌐 Avrupa'ya da genişle",
                "effects": {"money": 150000000, "connections": 20, "experience": 15},
                "next": 39
            }
        ]
    },

    33: {
        "id": 33,
        "chapter": "📖 Bölüm 8: Global Güç",
        "text": (
            "Avrupa'da marka oldun. Sürdürülebilirlik projelerin büyük yankı uyandırdı.\n\n"
            "AB hükümetleri seni danışman olarak istiyor. Şirketin değeri 400 milyon dolar.\n\n"
            "Siyasete girmeyi düşünüyor musun?"
        ),
        "choices": [
            {
                "text": "🏛️ Danışmanlık kabul et",
                "effects": {"reputation": 35, "connections": 30, "money": 50000000},
                "next": 39
            },
            {
                "text": "🚫 Odaklan, siyasetten uzak dur",
                "effects": {"money": 200000000, "risk": -15},
                "next": 38
            },
            {
                "text": "📊 Şirketi sat, vakıf kur",
                "effects": {"money": 300000000, "reputation": 40, "risk": -20},
                "next": 40
            }
        ]
    },

    34: {
        "id": 34,
        "chapter": "📖 Bölüm 8: Global Güç",
        "text": (
            "Gizli güç oldun. Sahne arkasında her şeyi yönetiyorsun.\n\n"
            "İsmin kimse tarafından bilinmiyor ama her büyük kararın arkasındasın.\n\n"
            "Ülkelerin politikasını bile şekillendiriyorsun. Servetin 300 milyon dolar."
        ),
        "choices": [
            {
                "text": "🎭 Kamuya çık, marka ol",
                "effects": {"reputation": 40, "risk": 15, "money": 100000000},
                "next": 39
            },
            {
                "text": "🤫 Gizli kalmaya devam et",
                "effects": {"connections": 40, "risk": -10, "money": 200000000},
                "next": 40
            },
            {
                "text": "🌏 Global ağını genişlet",
                "effects": {"money": 300000000, "connections": 45, "reputation": 20},
                "next": 40
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 9: ZİRVE
    # ═══════════════════════════════════════

    35: {
        "id": 35,
        "chapter": "📖 Bölüm 9: Zirve",
        "text": (
            "Portföyünün toplam değeri 500 milyon doları geçti!\n\n"
            "Forbes listesinde adın var. Dünyanın her yerinden teklifler geliyor.\n\n"
            "Şimdi ne yapacaksın?"
        ),
        "choices": [
            {
                "text": "🤖 Yapay zeka şirketi kur",
                "effects": {"money": -50000000, "experience": 30, "risk": 20, "reputation": 20},
                "next": 38
            },
            {
                "text": "🏦 Kendi yatırım fonunu kur",
                "effects": {"money": 200000000, "connections": 30, "reputation": 15},
                "next": 39
            },
            {
                "text": "🌍 Sosyal sorumluluk projeleri",
                "effects": {"reputation": 40, "connections": 25, "money": -20000000},
                "next": 40
            }
        ]
    },

    36: {
        "id": 36,
        "chapter": "📖 Bölüm 9: Zirve",
        "text": (
            "Şirket imparatorluğun büyüdü. 10 farklı sektörde şirketin var.\n\n"
            "Toplam değer: 300 milyon dolar. Ama dağınık yapı yönetimi zorlaştırıyor.\n\n"
            "Nasıl organize oluyorsun?"
        ),
        "choices": [
            {
                "text": "🏗️ Holding yapısı kur",
                "effects": {"money": -10000000, "connections": 20, "reputation": 20, "risk": -10},
                "next": 38
            },
            {
                "text": "✂️ Kârsızları sat, odaklan",
                "effects": {"money": 150000000, "experience": 20, "risk": -15},
                "next": 39
            },
            {
                "text": "📊 Halka aç (IPO)",
                "effects": {"money": 400000000, "reputation": 30, "risk": 15},
                "next": 39
            }
        ]
    },

    37: {
        "id": 37,
        "chapter": "📖 Bölüm 9: Zirve",
        "text": (
            "Temiz enerji / uzay şirketin medyada gündem oldu!\n\n"
            "Elon Musk gibi isimlerle aynı sayfada anılmaya başladın.\n\n"
            "Hükümetler sana destek teklif ediyor. Anlaşmayı nasıl yapılandırıyorsun?"
        ),
        "choices": [
            {
                "text": "🏛️ Devlet ortaklığı kabul et",
                "effects": {"money": 300000000, "connections": 35, "risk": 15},
                "next": 39
            },
            {
                "text": "💼 Tamamen özel kal",
                "effects": {"money": 200000000, "reputation": 25, "risk": -10},
                "next": 38
            },
            {
                "text": "🌐 Uluslararası konsorsiyum kur",
                "effects": {"money": 400000000, "connections": 40, "reputation": 30},
                "next": 40
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 10: MİLYARDER SINIRI
    # ═══════════════════════════════════════

    38: {
        "id": 38,
        "chapter": "📖 Bölüm 10: Milyarder Sınırı",
        "text": (
            "Servetin 1 milyar dolara yaklaşıyor!\n\n"
            "Her sabah uyandığında gazete manşetlerinde adın var.\n"
            "Dünya liderleri seni arıyor, üniversiteler senden konuşma istiyor.\n\n"
            "Son büyük kararın ne olacak?"
        ),
        "choices": [
            {
                "text": "🏆 Büyük bir satın alma yap",
                "effects": {"money": 500000000, "connections": 20, "risk": 15},
                "next": "final_check"
            },
            {
                "text": "🌍 Global vakfını kur",
                "effects": {"reputation": 35, "connections": 30, "money": -100000000},
                "next": "final_check"
            },
            {
                "text": "📈 Şirketi borsada büyüt",
                "effects": {"money": 300000000, "reputation": 20, "risk": 10},
                "next": "final_check"
            }
        ]
    },

    39: {
        "id": 39,
        "chapter": "📖 Bölüm 10: Milyarder Sınırı",
        "text": (
            "Halka arzın büyük başarı oldu! Hisseler ilk günde %40 arttı.\n\n"
            "Servetin resmi olarak 1,2 milyar dolara ulaştı. Artık gerçek bir milyardersin.\n\n"
            "Bu serveti nasıl kullanacaksın?"
        ),
        "choices": [
            {
                "text": "🎓 Eğitim vakfı kur",
                "effects": {"reputation": 40, "connections": 25, "money": -50000000},
                "next": "final_check"
            },
            {
                "text": "🚀 Uzay şirketine yatır",
                "effects": {"money": -200000000, "experience": 30, "reputation": 30},
                "next": "final_check"
            },
            {
                "text": "💎 Lüks hayata geç",
                "effects": {"money": -300000000, "risk": 20, "reputation": -10},
                "next": "final_check"
            }
        ]
    },

    40: {
        "id": 40,
        "chapter": "📖 Bölüm 10: Milyarder Sınırı",
        "text": (
            "Artık sadece bir iş insanı değilsin — bir efsanesin.\n\n"
            "Servetin 2 milyar dolara yaklaşıyor. Ama bir şey eksik: mutluluk mu, anlam mı?\n\n"
            "Hayatının son büyük kararı:"
        ),
        "choices": [
            {
                "text": "🌱 Her şeyi bırak, insanlığa hizmet et",
                "effects": {"money": -1000000000, "reputation": 50, "connections": 40},
                "next": "final_check"
            },
            {
                "text": "👑 İmparatorluğu büyütmeye devam",
                "effects": {"money": 500000000, "risk": 20, "reputation": 10},
                "next": "final_check"
            },
            {
                "text": "🏝️ Her şeyi sat, adaya çekil",
                "effects": {"money": 1500000000, "risk": -50, "reputation": -20},
                "next": "final_check"
            }
        ]
    },
}

# ═══════════════════════════════════════
# FİNAL SONUÇLARI (10 farklı son)
# ═══════════════════════════════════════

ENDINGS = {
    "effsane_milyarder": {
        "title": "🏆 Efsane Milyarder",
        "text": (
            "🏆 TEBRİKLER! EFSANE MİLYARDER OLDUN!\n\n"
            "Sıfırdan başladın ve milyarlara ulaştın.\n"
            "İtibarın pırıl pırıl, hiçbir yasal sorunun yok.\n"
            "Forbes listesinde adın var.\n\n"
            "Sen gerçek anlamda bir efsanesin!\n\n"
            "💰 Servet: 1.000.000.000$+\n"
            "⭐ İtibar: Muhteşem\n"
            "⚠️ Risk: Düşük"
        )
    },
    "iflas": {
        "title": "💸 İflas Ettin",
        "text": (
            "💸 İFLAS!\n\n"
            "Riskler çok büyüktü ve her şeyi kaybettin.\n"
            "Borçların var, şirketin kapandı.\n\n"
            "Ama bu son değil. Deneyim kazandın.\n"
            "Birçok başarılı girişimci önce iflas etti.\n\n"
            "Yeniden dene!"
        )
    },
    "tutuklanma": {
        "title": "⚖️ Tutuklandın",
        "text": (
            "⚖️ TUTUKLAMA!\n\n"
            "Risk çok yüksekti ve yasaları çiğnedin.\n"
            "Vergi kaçakçılığı, dolandırıcılık veya rüşvet...\n\n"
            "Her yaptığın bir gün ortaya çıkar.\n"
            "Para varken hukuku da yanında tut.\n\n"
            "Bu sefere olmadı."
        )
    },
    "gizli_patron": {
        "title": "👑 Gizli Patron",
        "text": (
            "👑 GİZLİ PATRON!\n\n"
            "İsmini kimse bilmiyor ama sen her yerde etkilisin.\n"
            "Hükümetler sana danışıyor, şirketler sana bağlı.\n\n"
            "Güç, para değil... kontrol.\n\n"
            "💰 Servet: Muazzam ama gizli\n"
            "🤝 Bağlantılar: Efsanevi\n"
            "⭐ İtibar: Sıfır (kasıtlı)"
        )
    },
    "medya_yildizi": {
        "title": "🎤 Medya Yıldızı",
        "text": (
            "🎤 MEDYA YILDIZI!\n\n"
            "Para değil, etki kazandın.\n"
            "Milyonlarca takipçin var, kitapların best-seller.\n\n"
            "Zengin olmak için para gerekmiyor diyorsun artık...\n"
            "Ama banka hesabın da fena değil!\n\n"
            "⭐ İtibar: Efsanevi\n"
            "💰 Servet: 100M - 900M arası"
        )
    },
    "teknoloji_devi": {
        "title": "🚀 Teknoloji Devi",
        "text": (
            "🚀 TEKNOLOJİ DEVİ!\n\n"
            "Kurduğun teknoloji şirketi dünyayı değiştirdi.\n"
            "Elon, Jeff, Mark gibi isimlerle aynı sayfadasın.\n\n"
            "Geleceği kodladın!\n\n"
            "💻 Etki: Küresel\n"
            "💰 Servet: 500M+\n"
            "🧠 Tecrübe: Maksimum"
        )
    },
    "yatirimci": {
        "title": "📊 Usta Yatırımcı",
        "text": (
            "📊 USTA YATIRIMCI!\n\n"
            "Kendi şirketini kurmak yerine doğru yerlere yatırım yaptın.\n"
            "Portföyündeki şirketler toplam 2 milyar dolar değerinde.\n\n"
            "Sen büyütüyorsun, onlar çalışıyor!\n\n"
            "💰 Servet: 200M+\n"
            "🤝 Bağlantılar: Dev ağ\n"
            "⚠️ Risk: Dengeli"
        )
    },
    "nefret_edilen_zengin": {
        "title": "😈 Nefret Edilen Zengin",
        "text": (
            "😈 NEFRET EDİLEN ZENGİN!\n\n"
            "Çok para kazandın ama herkes senden nefret ediyor.\n"
            "Çalışanların şikayet ediyor, basın seni karalıyor.\n\n"
            "Para varken bile yalnız olunur.\n\n"
            "💰 Servet: 1B+\n"
            "⭐ İtibar: Negatif\n"
            "🤝 Bağlantılar: Düşmanlar"
        )
    },
    "global_guc": {
        "title": "🌍 Global Güç",
        "text": (
            "🌍 GLOBAL GÜÇ!\n\n"
            "Artık sadece bir iş insanı değilsin.\n"
            "Uluslararası politikayı etkiliyor, ülkelerle anlaşmalar yapıyorsun.\n\n"
            "Sınırları aşan bir güce sahipsin!\n\n"
            "💰 Servet: Sınırsız\n"
            "🤝 Bağlantılar: Liderler düzeyinde\n"
            "🌐 Etki: Küresel"
        )
    },
    "hepsini_satip_kaybolan": {
        "title": "🏝️ Her Şeyi Satıp Kaybolan Milyarder",
        "text": (
            "🏝️ HER ŞEYİ SATIP KAYBOLAN MİLYARDER!\n\n"
            "1 milyar dolar kazandın... ve hepsini harcadın.\n"
            "Adalar, yatlar, partiler, hayırseverlik...\n\n"
            "Bir gün uyandın ve hepsi gitmişti.\n"
            "Ama ne hikayeler anlatıyorsun!\n\n"
            "💰 Son durum: Sıfır\n"
            "📖 Hikaye: Efsane\n"
            "😄 Mutluluk: Tartışmalı"
        )
    }
}


def determine_ending(stats: dict) -> str:
    """Parametrelere göre final sonucunu belirle"""
    money = stats.get("money", 0)
    reputation = stats.get("reputation", 0)
    risk = stats.get("risk", 0)
    connections = stats.get("connections", 0)
    experience = stats.get("experience", 0)

    # 1. Kritik durumlar önce
    if risk >= 90:
        return "tutuklanma"

    if money <= 0:
        return "iflas"

    # 2. Milyarder finalleri
    if money >= 1_000_000_000:
        if reputation < 0:
            return "nefret_edilen_zengin"
        if risk > 60:
            return "hepsini_satip_kaybolan"
        if connections > 70:
            return "global_guc"
        return "effsane_milyarder"

    # 3. Orta seviye finaller
    if connections > 70 and reputation < 20:
        return "gizli_patron"

    if reputation > 70:
        return "medya_yildizi"

    if experience > 70 and money > 200_000_000:
        return "teknoloji_devi"

    if connections > 60 and money > 100_000_000:
        return "global_guc"

    if money > 100_000_000:
        return "yatirimci"

    if money > 10_000_000:
        return "yatirimci"

    # 4. Kötü ama değil iflas — küçük kazananlar
    if money > 0:
        return "yatirimci"

    return "iflas"
