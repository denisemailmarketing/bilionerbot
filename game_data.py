# game_data.py — Oyun sahneleri ve finaller

# Her sahne yapısı:
# id: sahne numarası
# text: sahne metni (Türkçe)
# choices: seçenekler listesi
#   - text: seçenek metni
#   - effects: parametre değişimleri
#   - next: bir sonraki sahne id'si
#   - condition: koşullu geçiş (opsiyonel)

SCENES = {

    # ═══════════════════════════════════════
    # BÖLÜM 1: BAŞLANGIÇ
    # ═══════════════════════════════════════

    1: {
        "id": 1,
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "20 yaşındasın. Küçük bir evde yaşıyorsun ve cebinde sadece 500$ var.\n\n"
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
            "Küçük bir şirkette muhasebe asistanı oldun. Maaşın 1.200$ / ay.\n\n"
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
            "300$ harcadın malzemelere. İlk siparişin geldi! 80$ kazandın.\n\n"
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
            "Patron seni terfi ettirdi! Artık 2.500$ kazanıyorsun.\n\n"
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
            "Kemal Bey, yeni projesine yatırımcı arıyor. Seni ekibine almak istiyor ama hisse verecek.\n\n"
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
            "Bir tedarikçi teklif etti: Toplu sipariş verirsen fiyatı %40 düşürür.\n\n"
            "Ama bunun için 5.000$ gerekiyor. Yoksa..."
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
            "Ama tek başına yetiştirmek imkansız. Birini işe almanın vakti geldi mi?\n\n"
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
            "Ama hayalin hâlâ orada duruyor. Bir fırsat çıktı: Arkadaşın senden 2.000$ ortaklık istiyor.\n\n"
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
            "Artık 5.000$'ın var. Ama borçlulusun ve risk çok yüksek.\n\n"
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
                "text": "💼 Şirkete sataçak kişi bul",
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
            "Ama ortağın anlaşmazlık yaşıyorsunuz. Şirketi nasıl büyüteceğiniz konusunda fikir ayrılığı var."
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
                "text": "🤯 Şirketi sat ve yenile başla",
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
            "Ama alıcı, anlaşma sonrası bazı sorunlar çıkardı.\n\n"
            "Yarısını ödedi, kalanı için dava açtı. Ne yapıyorsun?"
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
            "Kahve bayilik işin çok iyi gidiyor! 3 şubeni var artık.\n\n"
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
                "text": "💰 Rakibe sat, kar et",
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
            "Üstelik yeni bir daire fırsatı çıktı. Çok cazip fiyat ama nakit sıkıntısın."
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
                "next": 31
            },
            {
                "text": "🇪🇺 Avrupa pazarına gir",
                "effects": {"money": -7000, "reputation": 20, "experience": 15, "risk": 15},
                "next": 31
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
                "next": 32
            },
            {
                "text": "🚀 Özel sektörde büy",
                "effects": {"money": 5000, "experience": 20, "reputation": 15},
                "next": 31
            }
        ]
    },

    28: {
        "id": 28,
        "chapter": "📖 Bölüm 6: Global Pazar",
        "text": (
            "Krizi atlattın ve güçlendin! Rakiplerin battı, sen hayatta kaldın.\n\n"
            "Artık sektörün en önemli isimlerinden birisin.\n\n"
            "Bir dev şirketten birleşme teklifi geldi: 200 milyon dolar."
        ),
        "choices": [
            {
                "text": "💰 Teklifi kabul et",
                "effects": {"money": 150000000, "reputation": 20, "risk": -20},
                "next": "final_check"
            },
            {
                "text": "🦅 Bağımsız kalmaya devam et",
                "effects": {"money": 5000, "reputation": 25, "risk": 10},
                "next": 33
            },
            {
                "text": "📈 Borsa'ya çık (IPO)",
                "effects": {"money": 80000000, "reputation": 30, "connections": 20},
                "next": "final_check"
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 7: İMPARATORLUK
    # ═══════════════════════════════════════

    29: {
        "id": 29,
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "Şirket imparatorluğun kuruldu! 10 farklı şirketin var.\n\n"
            "Ama büyük güç büyük sorumluluk getirir. Vergi makamları seni inceliyor.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "📋 Tam şeffaflıkla hareket et",
                "effects": {"reputation": 20, "risk": -20, "money": -5000},
                "next": 33
            },
            {
                "text": "🌍 Offshore yapılanmaya geç",
                "effects": {"money": 10000, "risk": 30},
                "next": 33
            },
            {
                "text": "⚖️ Hukuk ekibi kur",
                "effects": {"money": -8000, "risk": -15, "connections": 10},
                "next": 33
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
                "effects": {"connections": 30, "reputation": 25, "experience": 20},
                "next": 33
            },
            {
                "text": "🚀 Uzay/temiz enerji projesine gir",
                "effects": {"money": -20000000, "reputation": 30, "risk": 20},
                "next": "final_check"
            },
            {
                "text": "🏖️ Emekli ol, al-sat yap",
                "effects": {"money": 20000000, "risk": -30},
                "next": "final_check"
            }
        ]
    },

    # ═══════════════════════════════════════
    # BÖLÜM 8: FINAL ÖNCESI
    # ═══════════════════════════════════════

    31: {
        "id": 31,
        "chapter": "📖 Bölüm 8: Final",
        "text": (
            "Global pazarda güçlü bir konuma geldin.\n\n"
            "Artık kararın gelecek nesilleri etkileyecek düzeyde.\n\n"
            "Son büyük hamlen ne olacak?"
        ),
        "choices": [
            {
                "text": "🌍 Sosyal sorumluluk projesi kur",
                "effects": {"reputation": 30, "connections": 20, "money": -5000000},
                "next": "final_check"
            },
            {
                "text": "🤖 Yapay zeka şirketi kur",
                "effects": {"money": -10000000, "experience": 30, "risk": 20},
                "next": "final_check"
            },
            {
                "text": "💼 Her şeyi sat, devir",
                "effects": {"money": 500000000, "risk": -30},
                "next": "final_check"
            }
        ]
    },

    32: {
        "id": 32,
        "chapter": "📖 Bölüm 8: Final",
        "text": (
            "Gizli güç oldun. Sahne arkasında her şeyi yönetiyorsun.\n\n"
            "İsmin kimse tarafından bilinmiyor ama her büyük kararın arkasındasın.\n\n"
            "Son hamle: İtibarını mı inşa edeceksin, yoksa gizli kalmaya mı devam edeceksin?"
        ),
        "choices": [
            {
                "text": "🎭 Kamuya çık",
                "effects": {"reputation": 40, "risk": 15},
                "next": "final_check"
            },
            {
                "text": "🤫 Gizli kalmaya devam et",
                "effects": {"connections": 30, "risk": -10},
                "next": "final_check"
            },
            {
                "text": "🌏 Global güç olarak konumlan",
                "effects": {"money": 200000000, "connections": 40, "reputation": 20},
                "next": "final_check"
            }
        ]
    },

    33: {
        "id": 33,
        "chapter": "📖 Bölüm 8: Final",
        "text": (
            "Şirketin halka açıldı. Piyasa değeri 2 milyar dolar!\n\n"
            "Artık milyarder olmanın eşiğindesin.\n\n"
            "Son kararın: Hisselerini elinde tutacak mısın, yoksa satacak mısın?"
        ),
        "choices": [
            {
                "text": "💎 Hisseleri tut, büyümeye devam",
                "effects": {"money": 500000000, "risk": 15, "reputation": 20},
                "next": "final_check"
            },
            {
                "text": "💰 Hisselerin %30'unu sat",
                "effects": {"money": 300000000, "risk": -10},
                "next": "final_check"
            },
            {
                "text": "🏗️ Yeni sektöre yatır",
                "effects": {"money": 100000000, "experience": 20, "risk": 20},
                "next": "final_check"
            }
        ]
    }
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
            "Ama bu sonu değil. Deneyim kazandın.\n"
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
        "title": "📊 Yatırımcı",
        "text": (
            "📊 USTA YATIRIMCI!\n\n"
            "Kendi şirketini kurmak yerine doğru yerlere yatırım yaptın.\n"
            "Portföyündeki şirketler toplam 2 milyar dolar değerinde.\n\n"
            "Sen büyütüyorsun, onlar çalışıyor!\n\n"
            "💰 Servet: 400M+\n"
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
        "title": "🏖️ Her Şeyi Satıp Kaybolan Milyarder",
        "text": (
            "🏖️ HER ŞEYİ SATIP KAYBOLAN MİLYARDER!\n\n"
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

    # Öncelik sırasına göre kontrol
    if risk >= 90:
        return "tutuklanma"

    if money <= 0:
        return "iflas"

    if money >= 1000000000 and reputation > 50 and risk < 60:
        return "effsane_milyarder"

    if connections > 80 and reputation < 20:
        return "gizli_patron"

    if reputation > 80 and money >= 500000000:
        return "medya_yildizi" if money < 1000000000 else "effsane_milyarder"

    if experience > 80 and money > 500000000:
        return "teknoloji_devi"

    if money >= 1000000000 and reputation < 0:
        return "nefret_edilen_zengin"

    if connections > 80 and money >= 500000000:
        return "global_guc"

    if money >= 400000000 and connections > 60:
        return "yatirimci"

    if money >= 1000000000 and risk > 60:
        return "hepsini_satip_kaybolan"

    if money > 100000000:
        return "yatirimci"

    return "iflas"
