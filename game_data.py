# game_data.py — ZERO → BILLION v3
# Экономика: эффекты масштабируются через множители,
# деньги в $ (реальные числа), логика финала пересмотрена.
#
# apply_effects в db.py применяет АБСОЛЮТНЫЕ суммы.
# Поэтому каждая глава использует суммы своего масштаба:
#   Гл.1-2: сотни / тысячи
#   Гл.3-4: десятки тысяч
#   Гл.5-6: миллионы
#   Гл.7-8: десятки миллионов
#   Гл.9-10: сотни миллионов / миллиарды

SCENES = {

    # ══════════════════════════════════════
    # BÖLÜM 1: BAŞLANGIÇ  (para: ~500$)
    # ══════════════════════════════════════

    1: {
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "20 yaşındasın. Cebinde 500$ var, sırtında büyük bir hayal.\n\n"
            "Sabah uyandın ve kendine sordun: Milyarder olmak istiyorum — nereden başlamalıyım?\n\n"
            "İlk adımın ne olacak?"
        ),
        "choices": [
            {
                "text": "💼 İş bul, tecrübe kazan",
                "effects": {"money": 1200, "experience": 8, "risk": -3},
                "next": 2
            },
            {
                "text": "📦 Online satış mağazası kur",
                "effects": {"money": -300, "experience": 12, "risk": 8},
                "next": 3
            },
            {
                "text": "📈 500$'ı kriptoya yatır",
                "effects": {"money": -500, "risk": 25},
                "next": 4
            }
        ]
    },

    2: {
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "Muhasebe firmasında asistan oldun. Maaş: 1.400$/ay.\n\n"
            "İlk ay bitti. Elinde 1.700$ var. Patron seni fark etti.\n"
            "'Hafta sonu da çalışabilir misin?' diye sordu. Ek ödeme: 600$/hafta sonu.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "⏰ Fazla mesaiye evet de",
                "effects": {"money": 600, "experience": 10, "reputation": 5},
                "next": 5
            },
            {
                "text": "📚 Hafta sonu online kurs al",
                "effects": {"money": -300, "experience": 20, "risk": -3},
                "next": 6
            },
            {
                "text": "🤝 Patronla öğle yemeği ye, ilişki kur",
                "effects": {"money": -50, "connections": 18, "reputation": 8},
                "next": 7
            }
        ]
    },

    3: {
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "El yapımı deri çanta mağazan açıldı. 300$ harcadın, ilk hafta 3 sipariş geldi.\n\n"
            "Toplam gelir: 240$. Kâr: -60$. Ama umut var.\n\n"
            "Nasıl büyüteceksin?"
        ),
        "choices": [
            {
                "text": "💰 Tüm kazancı yeniden yatır",
                "effects": {"money": 180, "experience": 15, "risk": 6},
                "next": 8
            },
            {
                "text": "📱 Instagram reklamına 200$ harca",
                "effects": {"money": -200, "reputation": 12, "connections": 8},
                "next": 9
            },
            {
                "text": "🐢 Yavaş git, para biriktir",
                "effects": {"money": 240, "risk": -4},
                "next": 10
            }
        ]
    },

    4: {
        "chapter": "📖 Bölüm 1: Başlangıç",
        "text": (
            "500$'ını kriptoya yatırdın. İlk hafta +40%. Sonra çöküş: -%70.\n\n"
            "Elinde 150$ kaldı. Bir hafta boyunca uyuyamadın.\n\n"
            "Şimdi ne yapacaksın?"
        ),
        "choices": [
            {
                "text": "😤 Borç alıp ikiye katla",
                "effects": {"money": -150, "risk": 35},
                "next": 11
            },
            {
                "text": "🔄 Her şeyden vazgeç, iş bul",
                "effects": {"money": 1400, "experience": 6, "risk": -10},
                "next": 2
            },
            {
                "text": "📊 Kripto analizi öğren, bekle",
                "effects": {"experience": 22, "risk": 5},
                "next": 12
            }
        ]
    },

    # ══════════════════════════════════════
    # BÖLÜM 2: İLK PARA  (para: ~2K-15K$)
    # ══════════════════════════════════════

    5: {
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "6 ay geçti. Fazla mesailerle birikimin 4.800$'a ulaştı.\n\n"
            "Patron seni muhasebe müdürü olmaya davet etti: 3.500$/ay.\n"
            "Ama bir startup fikrin var — yerel teslimat uygulaması.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🚀 İşi bırak, startup kur",
                "effects": {"money": -3000, "experience": 22, "risk": 28},
                "next": 13
            },
            {
                "text": "🌙 Geceleri startup geliştir, işte kal",
                "effects": {"money": 2100, "experience": 15, "risk": 10},
                "next": 14
            },
            {
                "text": "💼 Terfii kabul et, para biriktir",
                "effects": {"money": 7000, "experience": 8, "reputation": 8},
                "next": 15
            }
        ]
    },

    6: {
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "6 aylık kurs bitti. Artık Python ve dijital pazarlama biliyorsun.\n\n"
            "Elinde 3.200$ var ve iki seçenek:\n"
            "A) SaaS muhasebe yazılımı kur\n"
            "B) Freelance işler al, para biriktir\n\n"
            "Hangisi?"
        ),
        "choices": [
            {
                "text": "💻 SaaS yazılımı geliştir",
                "effects": {"money": -2500, "experience": 28, "risk": 18},
                "next": 13
            },
            {
                "text": "🤝 Ortak bul, birlikte kur",
                "effects": {"money": -800, "connections": 22, "risk": 12},
                "next": 16
            },
            {
                "text": "📋 Freelance ile 10K$ biriktir",
                "effects": {"money": 6800, "experience": 12},
                "next": 15
            }
        ]
    },

    7: {
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Patronunla öğle yemeğinde çok iyi anlaştınız.\n\n"
            "Sana sürpriz bir teklif: Şirketinin yeni dijital bölümünü kur, %15 hisse al.\n"
            "Maaşın sabit kalacak ama emek isteyecek.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "✅ Kabul et",
                "effects": {"money": 5000, "connections": 25, "reputation": 12, "experience": 15},
                "next": 17
            },
            {
                "text": "💬 Pazarlık yap — %25 iste",
                "effects": {"money": 3000, "connections": 15, "experience": 12},
                "next": 17
            },
            {
                "text": "❌ Reddet, kendi şirketini kur",
                "effects": {"money": -2000, "experience": 18, "risk": 20},
                "next": 13
            }
        ]
    },

    8: {
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Mağazan büyüdü! Aylık gelir: 2.400$, kâr: 900$.\n\n"
            "Bir tedarikçi toplu sipariş teklif etti: 5.000$ ver, maliyet %40 düşsün.\n"
            "Elinde 1.800$ var.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🏦 Bankadan 3.500$ kredi çek",
                "effects": {"money": 4200, "risk": 22},
                "next": 18
            },
            {
                "text": "👨‍👩‍👧 Aileden 3.000$ borç iste",
                "effects": {"money": 3000, "connections": -5, "risk": 12},
                "next": 18
            },
            {
                "text": "🐢 Yavaş büy, toplu sipariş yok",
                "effects": {"money": 900, "risk": -5},
                "next": 19
            }
        ]
    },

    9: {
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Instagram reklamın viral oldu! 500 sipariş geldi, 3 günde.\n\n"
            "Ama üretemiyorsun. Elinde 1.040$ var.\n"
            "Ya birini işe al (800$/ay) ya da siparişleri reddet.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "👷 Çalışan al, büyüt",
                "effects": {"money": -800, "experience": 12, "connections": 12},
                "next": 18
            },
            {
                "text": "🤖 Üretime ara ver, otomasyon araştır",
                "effects": {"money": -1200, "experience": 22, "risk": 10},
                "next": 18
            },
            {
                "text": "😤 500 siparişin 200'ünü reddet",
                "effects": {"money": 2400, "reputation": -12},
                "next": 19
            }
        ]
    },

    10: {
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Yavaş ama güvenli gidiyorsun. Birikimin 2.200$'a ulaştı.\n\n"
            "Eski arkadaşın Mert seni aradı: 'E-ticaret platformu kuruyorum, 2.000$ ortak ol!'\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🤝 Ortaklığı kabul et",
                "effects": {"money": -2000, "connections": 22, "risk": 15},
                "next": 16
            },
            {
                "text": "📊 Kendi platformunu kur",
                "effects": {"money": -1500, "experience": 18, "risk": 22},
                "next": 13
            },
            {
                "text": "💤 Reddet, biriktirmeye devam",
                "effects": {"money": 1800, "risk": -6},
                "next": 15
            }
        ]
    },

    11: {
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "Borç aldın ve yeniden yatırdın. Şans! Piyasa 3.2x arttı.\n\n"
            "Artık 4.800$ var. Ama borcun: 2.000$. Net: 2.800$.\n"
            "Risk hâlâ çok yüksek.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "💸 Çek, borcu öde, temiz başla",
                "effects": {"money": 2800, "risk": -22},
                "next": 15
            },
            {
                "text": "📈 Yeniden yatır — 10x için",
                "effects": {"money": -2800, "risk": 35},
                "next": 20
            },
            {
                "text": "🏗️ Çek ve şirket kur",
                "effects": {"money": 1500, "experience": 12, "risk": -8},
                "next": 13
            }
        ]
    },

    12: {
        "chapter": "📖 Bölüm 2: İlk Para",
        "text": (
            "6 ay kripto analizi öğrendin. Twitter'da 3.000 takipçin var.\n\n"
            "Elinde 150$ + kripto: toplam 1.200$.\n"
            "Kripto danışmanlık kanalı açmak ister misin?"
        ),
        "choices": [
            {
                "text": "📢 YouTube/Twitter kanalı aç",
                "effects": {"money": -200, "reputation": 18, "connections": 12},
                "next": 19
            },
            {
                "text": "💼 Ücretli kripto sinyalleri sat",
                "effects": {"money": 2800, "reputation": 8, "risk": 18},
                "next": 19
            },
            {
                "text": "📖 E-kitap yaz, pasif gelir",
                "effects": {"money": 600, "reputation": 12, "experience": 12},
                "next": 15
            }
        ]
    },

    # ══════════════════════════════════════
    # BÖLÜM 3: BÜYÜME  (para: ~10K-100K$)
    # ══════════════════════════════════════

    13: {
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Startupın ilk MVP'si hazır. 30 beta kullanıcın var ve hepsi memnun.\n\n"
            "Bir melek yatırımcı toplantıya geldi: '50.000$ karşılığı %20 hisse.'\n\n"
            "Ne diyorsun?"
        ),
        "choices": [
            {
                "text": "✅ Kabul et — hız önemli",
                "effects": {"money": 50000, "connections": 22, "reputation": 15},
                "next": 21
            },
            {
                "text": "💬 Pazarlık — %10 hisse için 40.000$",
                "effects": {"money": 40000, "connections": 12, "experience": 12},
                "next": 21
            },
            {
                "text": "❌ Reddet, bootstrap büyü",
                "effects": {"money": -5000, "experience": 18, "risk": 22},
                "next": 22
            }
        ]
    },

    14: {
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "8 ay geceleri çalıştın. Hem işte hem startupda.\n\n"
            "MVP hazır, 15 müşteri var, aylık 3.200$ gelir.\n"
            "Ama yoruldun. İşi bırakma vakti mi?\n\n"
            "Birikimin: 9.400$"
        ),
        "choices": [
            {
                "text": "🔥 İşi bırak, tam gaz",
                "effects": {"money": -3000, "experience": 22, "risk": 22},
                "next": 21
            },
            {
                "text": "📈 İşte kal, müşteri sayısını ikiye katla",
                "effects": {"money": 6400, "connections": 12, "experience": 12},
                "next": 22
            },
            {
                "text": "💼 Şirketi 30.000$'a sat",
                "effects": {"money": 30000, "reputation": 12},
                "next": 23
            }
        ]
    },

    15: {
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Birikimin 12.000$'a ulaştı.\n\n"
            "Üç fırsat önünde:\n"
            "A) Ünlü kahve markası franchise: 15.000$ giriş\n"
            "B) Dijital ajans kur\n"
            "C) Gayrimenkul — küçük bir daire al\n\n"
            "Hangisi?"
        ),
        "choices": [
            {
                "text": "☕ Franchise al",
                "effects": {"money": -15000, "experience": 15, "connections": 12, "risk": 15},
                "next": 24
            },
            {
                "text": "💻 Dijital ajans kur",
                "effects": {"money": -4000, "experience": 22, "risk": 12},
                "next": 13
            },
            {
                "text": "🏠 Daire al, kiraya ver",
                "effects": {"money": -12000, "risk": 18, "connections": 6},
                "next": 25
            }
        ]
    },

    16: {
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Ortağınla iyi başladınız. 6 ay sonra aylık 18.000$ ciro.\n\n"
            "Ama tartışma çıktı: Mert hızlı büyümek istiyor, sen sağlam temeller.\n"
            "Anlaşamıyorsunuz.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🤝 Uzlaş, birlikte devam",
                "effects": {"connections": 18, "reputation": 12, "experience": 12},
                "next": 21
            },
            {
                "text": "💰 Mert'in hissesini 25.000$'a satın al",
                "effects": {"money": -25000, "risk": 12},
                "next": 22
            },
            {
                "text": "🤯 Şirketi 80.000$'a sat",
                "effects": {"money": 80000, "experience": 18},
                "next": 26
            }
        ]
    },

    17: {
        "chapter": "📖 Bölüm 3: Büyüme",
        "text": (
            "Patronun şirketinde dijital bölüm kuruldu!\n\n"
            "1 yıl sonra bölümün şirket cirosunun %30'unu sağlıyor.\n"
            "Patronun sana 80.000$ nakit teklif etti — hisseni almak istiyor.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "💰 Hisseyi sat, 80.000$ al",
                "effects": {"money": 80000, "connections": -8},
                "next": 26
            },
            {
                "text": "📊 Reddet, şirketi bağımsız kurmaya zorla",
                "effects": {"money": 15000, "connections": 22, "risk": 15},
                "next": 21
            },
            {
                "text": "🚀 Kendi startupını kur, ayrıl",
                "effects": {"money": -5000, "experience": 18, "risk": 22},
                "next": 13
            }
        ]
    },

    # ══════════════════════════════════════
    # BÖLÜM 4: KRİZ  (para: ~50K-300K$)
    # ══════════════════════════════════════

    18: {
        "chapter": "📖 Bölüm 4: İlk Kriz",
        "text": (
            "İşler büyüdü! Aylık ciro 45.000$'a ulaştı.\n\n"
            "Sonra... müşterilerinin en büyüğü iflas etti. Sana borcu: 38.000$.\n"
            "O parayı hiç alamayabilirsin.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "⚖️ Hukuki takip başlat",
                "effects": {"money": -8000, "risk": 18, "reputation": -6},
                "next": 26
            },
            {
                "text": "✂️ Masrafları kes, hayatta kal",
                "effects": {"money": -15000, "reputation": -8, "risk": -12},
                "next": 26
            },
            {
                "text": "💊 Acil yatırımcı bul",
                "effects": {"money": 60000, "connections": 18, "risk": 12},
                "next": 27
            }
        ]
    },

    19: {
        "chapter": "📖 Bölüm 4: İlk Kriz",
        "text": (
            "Yavaş ama sağlam büyüdün. Aylık kâr 4.200$.\n\n"
            "Yeni bir rakip geldi — aynı ürünleri %30 ucuza satıyor.\n"
            "Müşterilerinin %40'ını kaybettin.\n\n"
            "Stratejin ne?"
        ),
        "choices": [
            {
                "text": "⚔️ Fiyatları düşür, savaş",
                "effects": {"money": -12000, "reputation": 6, "risk": 22},
                "next": 27
            },
            {
                "text": "🎯 Nişe odaklan, premium ol",
                "effects": {"money": 8000, "reputation": 18, "experience": 18},
                "next": 26
            },
            {
                "text": "🤝 Rakiple birleş",
                "effects": {"money": 35000, "connections": 22},
                "next": 27
            }
        ]
    },

    20: {
        "chapter": "📖 Bölüm 4: İlk Kriz",
        "text": (
            "Yeniden kripto yatırdın. Bu sefer piyasa daha da çöktü.\n\n"
            "Her şeyi kaybettin. 0$ kaldı.\n\n"
            "Ama vazgeçmiyorsun. Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "😤 Son kez borç al, yeniden dene",
                "effects": {"money": -500, "risk": 45},
                "next": 28
            },
            {
                "text": "🔄 Sıfırdan normal işe başla",
                "effects": {"money": 2800, "experience": 8, "risk": -20},
                "next": 5
            },
            {
                "text": "📖 Deneyimi anlat, influencer ol",
                "effects": {"money": 1200, "reputation": 15, "connections": 12},
                "next": 19
            }
        ]
    },

    21: {
        "chapter": "📖 Bölüm 4: Büyüme Ivmesi",
        "text": (
            "Şirketin değeri 500.000$'a ulaştı! Ekibinde 8 kişi var.\n\n"
            "Bir rakip şirket, müşterilerini çalmak için eski çalışanını işe aldı.\n"
            "İçeriden bilgi sızıyor.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🔒 Güvenlik sistemi kur, ekibi tara",
                "effects": {"money": -18000, "risk": -15, "reputation": 8},
                "next": 27
            },
            {
                "text": "⚖️ Dava aç",
                "effects": {"money": -22000, "risk": 18, "reputation": -6},
                "next": 27
            },
            {
                "text": "💡 Ürünü geliştir, rakibi geride bırak",
                "effects": {"money": -35000, "experience": 25, "reputation": 18},
                "next": 29
            }
        ]
    },

    22: {
        "chapter": "📖 Bölüm 4: Büyüme Ivmesi",
        "text": (
            "Bootstrap büyüyorsun. Yavaş ama senin.\n\n"
            "Aylık gelir 28.000$'a ulaştı. Kâr marjı %35.\n"
            "Bir accelerator programı seni seçti: 120.000$ + mentörlük, %8 hisse karşılığı.\n\n"
            "Kabul ediyor musun?"
        ),
        "choices": [
            {
                "text": "✅ Kabul et — hız ve mentörlük şart",
                "effects": {"money": 120000, "connections": 28, "reputation": 18},
                "next": 29
            },
            {
                "text": "💬 Pazarlık — %4 hisse için 80.000$",
                "effects": {"money": 80000, "connections": 18, "experience": 15},
                "next": 29
            },
            {
                "text": "❌ Reddet, kendi hızında büy",
                "effects": {"money": 28000, "experience": 18, "risk": -8},
                "next": 27
            }
        ]
    },

    23: {
        "chapter": "📖 Bölüm 4: Büyüme Ivmesi",
        "text": (
            "Şirketi sattın. 30.000$ veya 80.000$ elinde.\n\n"
            "Alıcı şimdi seni rakip görüyor. Aynı sektörde yeni şirket kurman yasak — 2 yıl.\n\n"
            "Geçici olarak ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🌐 Farklı sektörde şirket kur",
                "effects": {"money": -20000, "experience": 18, "risk": 15},
                "next": 27
            },
            {
                "text": "📊 2 yıl yatırım yap, portföy oluştur",
                "effects": {"money": 45000, "experience": 22, "connections": 15},
                "next": 29
            },
            {
                "text": "🏖️ 1 yıl tatil, sonra yenile başla",
                "effects": {"money": -15000, "risk": -15, "reputation": 8},
                "next": 27
            }
        ]
    },

    24: {
        "chapter": "📖 Bölüm 4: Büyüme Ivmesi",
        "text": (
            "Kahve şuben açıldı. İlk ay: 22.000$ ciro, 4.500$ kâr.\n\n"
            "6 ay sonra şuben çok iyi gidiyor. Marka sahibi 3. şube teklife geliyor.\n"
            "Her şube: 18.000$ giriş bedeli. Toplam 54.000$. Elinde 28.000$ var.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🏦 Kredi çek, 3 şube birden aç",
                "effects": {"money": -40000, "connections": 18, "reputation": 15, "risk": 22},
                "next": 29
            },
            {
                "text": "☕ Sadece 1 şube daha aç",
                "effects": {"money": -18000, "reputation": 12, "experience": 12},
                "next": 27
            },
            {
                "text": "💰 Rakibe tüm zinciri sat",
                "effects": {"money": 120000, "experience": 12},
                "next": 30
            }
        ]
    },

    25: {
        "chapter": "📖 Bölüm 4: Büyüme Ivmesi",
        "text": (
            "Gayrimenkul yatırımın var. Daire kirası: 850$/ay.\n\n"
            "Şehrin en hızlı büyüyen bölgesinde ticari mülk satışa çıktı.\n"
            "Fiyat: 85.000$. Bankadan %70 kredi çekebilirsin.\n\n"
            "Riski alıyor musun?"
        ),
        "choices": [
            {
                "text": "🏢 Ticari mülkü al",
                "effects": {"money": -25500, "risk": 22, "connections": 8},
                "next": 29
            },
            {
                "text": "📤 Daireyi sat, daha büyük al",
                "effects": {"money": 38000, "experience": 12},
                "next": 30
            },
            {
                "text": "🛑 Yavaş git, kiradan geç",
                "effects": {"money": 10200, "risk": -8},
                "next": 27
            }
        ]
    },

    # ══════════════════════════════════════
    # BÖLÜM 5: GERÇEK BÜYÜME  (para: ~200K-2M$)
    # ══════════════════════════════════════

    26: {
        "chapter": "📖 Bölüm 5: Milyon Yolu",
        "text": (
            "Şirketin yıllık cirosu 1.2 milyon dolara ulaştı.\n\n"
            "Bir PE fonu teklife geldi: '2.000.000$ karşılığı %40 hisse.'\n"
            "Bu para ile ülke geneline yayılabilirsin.\n\n"
            "Ne diyorsun?"
        ),
        "choices": [
            {
                "text": "✅ Anlaşmayı kabul et",
                "effects": {"money": 2000000, "connections": 28, "reputation": 18},
                "next": 31
            },
            {
                "text": "💬 Pazarlık — %25 hisse için 1.5M$",
                "effects": {"money": 1500000, "connections": 18, "experience": 15},
                "next": 31
            },
            {
                "text": "🦅 Reddet, organik büy",
                "effects": {"money": 400000, "reputation": 22, "risk": 15},
                "next": 32
            }
        ]
    },

    27: {
        "chapter": "📖 Bölüm 5: Milyon Yolu",
        "text": (
            "Zor dönemleri atlattın. Şirketin sağlam durumda.\n\n"
            "Elinde 180.000-350.000$ arası birikim var.\n"
            "Sektörün en büyük fuarında konuşmacı olman isteniyor.\n\n"
            "Medyaya çıkacak mısın?"
        ),
        "choices": [
            {
                "text": "📺 Evet — sahneye çık",
                "effects": {"reputation": 28, "connections": 22, "money": 15000},
                "next": 31
            },
            {
                "text": "🤫 Hayır — gizli kal, rakipler görmessin",
                "effects": {"risk": -12, "experience": 12},
                "next": 34
            },
            {
                "text": "✍️ Kendi podcast/blog serisini başlat",
                "effects": {"reputation": 22, "connections": 28, "money": 28000},
                "next": 31
            }
        ]
    },

    28: {
        "chapter": "📖 Bölüm 5: Milyon Yolu",
        "text": (
            "Son kripto kumarı her şeyi bitirdi. 0$ kaldı.\n\n"
            "Ama sektörde tanınan bir isimsin. Bir firma seni COO olarak işe almak istiyor.\n"
            "Maaş: 18.000$/ay + hisse opsiyonları.\n\n"
            "Kabul ediyor musun?"
        ),
        "choices": [
            {
                "text": "✅ COO ol, yeniden başla",
                "effects": {"money": 72000, "experience": 28, "connections": 22},
                "next": 31
            },
            {
                "text": "🔄 Reddet, kendi şirketini kur",
                "effects": {"money": -5000, "risk": 35, "experience": 18},
                "next": 13
            },
            {
                "text": "💼 Danışmanlık şirketi kur",
                "effects": {"money": 45000, "reputation": 15, "connections": 18},
                "next": 27
            }
        ]
    },

    29: {
        "chapter": "📖 Bölüm 5: Büyük Hamle",
        "text": (
            "Şirketin değeri 5 milyon dolara ulaştı!\n\n"
            "Vergi makamları seni incelemeye aldı. Muhaseben doğru ama zaman kaybı.\n"
            "Aynı anda: büyük bir müşteri 800.000$'lık anlaşma teklif etti.\n\n"
            "Önce ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "📋 Şeffaflıkla vergi sorununu çöz",
                "effects": {"money": -120000, "reputation": 22, "risk": -18},
                "next": 32
            },
            {
                "text": "💼 Anlaşmayı önce kapat",
                "effects": {"money": 800000, "risk": 18, "connections": 18},
                "next": 32
            },
            {
                "text": "🌍 Offshore yapı kur",
                "effects": {"money": 200000, "risk": 32},
                "next": 32
            }
        ]
    },

    30: {
        "chapter": "📖 Bölüm 5: Büyük Hamle",
        "text": (
            "Birkaç başarılı çıkış yaptın. Toplamda 400.000-600.000$ biriktirdin.\n\n"
            "Artık bir yatırımcısın. İki startup senden yatırım istiyor:\n"
            "A) Fintech — yüksek risk, yüksek potansiyel\n"
            "B) SaaS — düşük risk, istikrarlı büyüme\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "💳 Fintech'e 200.000$ yatır",
                "effects": {"money": -200000, "risk": 25, "connections": 15},
                "next": 32
            },
            {
                "text": "💻 SaaS'a 150.000$ yatır",
                "effects": {"money": -150000, "experience": 18, "connections": 18},
                "next": 31
            },
            {
                "text": "🌐 İkisine de 100.000$'ar yatır",
                "effects": {"money": -200000, "connections": 28, "risk": 15},
                "next": 32
            }
        ]
    },

    # ══════════════════════════════════════
    # BÖLÜM 6: GLOBAL PAZAR  (para: ~1M-20M$)
    # ══════════════════════════════════════

    31: {
        "chapter": "📖 Bölüm 6: Global Pazar",
        "text": (
            "Şirketin değeri 15 milyon dolar.\n\n"
            "Global genişleme zamanı. Üç pazar seçeneği var:\n"
            "🇺🇸 ABD — dev piyasa, çok rekabetçi\n"
            "🌏 Asya — hızlı büyüme, yerel zorluklar\n"
            "🇪🇺 Avrupa — düzenleyici ama prestijli\n\n"
            "Hangisine giriyorsun?"
        ),
        "choices": [
            {
                "text": "🇺🇸 ABD pazarı",
                "effects": {"money": -2500000, "experience": 22, "risk": 28, "connections": 18},
                "next": 35
            },
            {
                "text": "🌏 Asya pazarı",
                "effects": {"money": -1800000, "experience": 18, "connections": 28, "risk": 22},
                "next": 36
            },
            {
                "text": "🇪🇺 Avrupa pazarı",
                "effects": {"money": -1500000, "reputation": 22, "experience": 18, "risk": 15},
                "next": 37
            }
        ]
    },

    32: {
        "chapter": "📖 Bölüm 6: Global Pazar",
        "text": (
            "Şirketin global sahneye hazırlanıyor.\n\n"
            "Bir Körfez fonu seni aradı: 'Şirketine 30 milyon dolar yatırım yapalım.'\n"
            "Karşılığında: %15 hisse + 2 yönetim kurulu koltuğu.\n\n"
            "Ne diyorsun?"
        ),
        "choices": [
            {
                "text": "✅ Anlaşmayı imzala",
                "effects": {"money": 30000000, "connections": 32, "reputation": 22},
                "next": 35
            },
            {
                "text": "💬 Pazarlık — %8 hisse, 1 koltuk",
                "effects": {"money": 18000000, "connections": 22, "experience": 15},
                "next": 36
            },
            {
                "text": "❌ Reddet, halka arz hazırlığı yap",
                "effects": {"money": 5000000, "reputation": 28, "risk": 18},
                "next": 37
            }
        ]
    },

    33: {
        "chapter": "📖 Bölüm 6: Global Pazar",
        "text": (
            "Global sahnedesin. Elinde 8-25 milyon dolar arası.\n\n"
            "Forbes 'Yükselenler' listesine girdin. Bir kitap teklifi:\n"
            "'Hikayeni yaz, 500.000$ avans + dünya turuna çık.'\n\n"
            "Kabul ediyor musun?"
        ),
        "choices": [
            {
                "text": "📚 Kitabı yaz",
                "effects": {"money": 500000, "reputation": 35, "connections": 22},
                "next": 38
            },
            {
                "text": "🎙️ Podcast serisi başlat",
                "effects": {"money": 280000, "reputation": 28, "connections": 35},
                "next": 38
            },
            {
                "text": "🚀 Zamanı yok — işe odaklan",
                "effects": {"money": 2000000, "experience": 18, "risk": -8},
                "next": 35
            }
        ]
    },

    34: {
        "chapter": "📖 Bölüm 6: Gizli Oyuncu",
        "text": (
            "Gizli kalmayı seçtin. İsmin bilinmiyor ama etkin çok güçlü.\n\n"
            "Büyük bir hükümet ihalesi: 80 milyon dolarlık altyapı projesi.\n"
            "Ortakların seni öne sürüyor. Ama ismin ifşa olacak.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "✅ İhaleye gir",
                "effects": {"money": -3000000, "connections": 35, "risk": 22},
                "next": 38
            },
            {
                "text": "🤫 Arka planda kal, %20 al",
                "effects": {"money": 4500000, "connections": 28, "risk": 8},
                "next": 39
            },
            {
                "text": "🚀 Özel sektörde büyümeye devam et",
                "effects": {"money": 6000000, "experience": 22, "reputation": 18},
                "next": 38
            }
        ]
    },

    # ══════════════════════════════════════
    # BÖLÜM 7: İMPARATORLUK  (para: ~20M-200M$)
    # ══════════════════════════════════════

    35: {
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "ABD'de tutunmayı başardın! Şirketin değeri 80 milyon dolar.\n\n"
            "Amazon ve Google aynı anda seni kopyalıyor. Devlere karşı savaş mı, yoksa satış mı?\n\n"
            "Elinde 12 milyon dolar var."
        ),
        "choices": [
            {
                "text": "⚔️ Savaş — nişe odaklan",
                "effects": {"money": -8000000, "experience": 28, "reputation": 22},
                "next": 40
            },
            {
                "text": "💰 Google'a sat — 150 milyon dolar",
                "effects": {"money": 150000000, "reputation": 18, "risk": -22},
                "next": 41
            },
            {
                "text": "📈 Halka arz (IPO) — 200 milyon dolar topla",
                "effects": {"money": 200000000, "reputation": 35, "connections": 22},
                "next": 41
            }
        ]
    },

    36: {
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "Asya pazarı patladı! Çin, Japonya ve Güneydoğu Asya'da güçlüsün.\n\n"
            "Şirketin değeri 120 milyon dolar. Ama Çin hükümeti kısıtlama getirebilir.\n\n"
            "Stratejin ne?"
        ),
        "choices": [
            {
                "text": "🏛️ Yerel ortak bul, riski azalt",
                "effects": {"money": 18000000, "connections": 35, "risk": -18},
                "next": 40
            },
            {
                "text": "💪 Bağımsız büy, lobi yap",
                "effects": {"money": 45000000, "risk": 28, "reputation": 18},
                "next": 41
            },
            {
                "text": "🌐 Avrupa'ya da aynı anda genişle",
                "effects": {"money": -15000000, "connections": 22, "experience": 18},
                "next": 40
            }
        ]
    },

    37: {
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "Avrupa'da büyük başarı! Sürdürülebilirlik projelerin AB medyasında gündem.\n\n"
            "Şirketin değeri 90 milyon dolar.\n"
            "AB hükümetleri seni danışman istiyor. Politikaya yakın olmak şanslar açar ama riskler de.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🏛️ Resmi danışman ol",
                "effects": {"reputation": 35, "connections": 32, "money": 12000000},
                "next": 41
            },
            {
                "text": "🚫 Politikadan uzak dur, odaklan",
                "effects": {"money": 55000000, "risk": -18},
                "next": 40
            },
            {
                "text": "📊 Şirketi sat, vakıf kur",
                "effects": {"money": 80000000, "reputation": 40, "risk": -22},
                "next": 42
            }
        ]
    },

    38: {
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "Medyada ünlüsün. Elinde 30-80 milyon dolar var.\n\n"
            "Sektörün en büyük rakibini satın alma fırsatı doğdu.\n"
            "Rakibin batıyor. Değeri: 40 milyon dolar. Gerçek değeri: 120 milyon dolar.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🏗️ Satın al — 40M$ öde",
                "effects": {"money": -40000000, "connections": 22, "reputation": 22, "experience": 15},
                "next": 41
            },
            {
                "text": "🤝 Ortak ol — 20M$ ver, %30 al",
                "effects": {"money": -20000000, "connections": 28, "risk": 12},
                "next": 41
            },
            {
                "text": "🦅 Hayır — kendi büyümeye devam",
                "effects": {"money": 25000000, "experience": 18, "risk": -8},
                "next": 40
            }
        ]
    },

    39: {
        "chapter": "📖 Bölüm 7: Gizli İmparator",
        "text": (
            "Gizli güç oldun. İsmin bilinmiyor ama etkini her yerde hissettiriyorsun.\n\n"
            "Servetin 100-200 milyon dolar. Ülkelerin politikasını şekillendiriyorsun.\n\n"
            "Son hamle: Kamuya çıkmak mı yoksa gizli kalmak mı?"
        ),
        "choices": [
            {
                "text": "🎭 Kamuya çık, marka ol",
                "effects": {"reputation": 42, "risk": 18, "money": 50000000},
                "next": 41
            },
            {
                "text": "🤫 Gizli kal, ağı genişlet",
                "effects": {"connections": 42, "risk": -12, "money": 120000000},
                "next": 42
            },
            {
                "text": "🌏 Global ağını kilitleyen hamleyi yap",
                "effects": {"money": 200000000, "connections": 48, "reputation": 22},
                "next": 42
            }
        ]
    },

    40: {
        "chapter": "📖 Bölüm 7: İmparatorluk",
        "text": (
            "Şirket imparatorluğun kuruldu. 8 farklı sektörde şirketin var.\n\n"
            "Toplam değer: 250-400 milyon dolar.\n"
            "Yönetim zor. Bir danışman şirketi önerdi: Holding yapısı kur.\n\n"
            "Ne yapıyorsun?"
        ),
        "choices": [
            {
                "text": "🏗️ Holding kur, profesyonel yönetim",
                "effects": {"money": -15000000, "connections": 22, "reputation": 22, "risk": -12},
                "next": 41
            },
            {
                "text": "✂️ Kârsızları sat, odaklan",
                "effects": {"money": 80000000, "experience": 22, "risk": -18},
                "next": 42
            },
            {
                "text": "📊 Tümünü halka aç (IPO)",
                "effects": {"money": 350000000, "reputation": 32, "risk": 18},
                "next": 42
            }
        ]
    },

    # ══════════════════════════════════════
    # BÖLÜM 8: MİLYARDER EŞİĞİ  (para: ~200M-1B$)
    # ══════════════════════════════════════

    41: {
        "chapter": "📖 Bölüm 8: Milyarder Eşiği",
        "text": (
            "Servetin 300-600 milyon dolara ulaştı.\n\n"
            "Forbes listesinde adın var. Dünyanın her yerinden teklif geliyor.\n"
            "Bir Japon holdingi sana 800 milyon dolar teklif etti — her şeyin için.\n\n"
            "Son büyük kararın:"
        ),
        "choices": [
            {
                "text": "💰 Sat — 800 milyon dolar al",
                "effects": {"money": 800000000, "reputation": 22, "risk": -25},
                "next": "final_check"
            },
            {
                "text": "🦅 Reddet — milyarder ol kendi yolunda",
                "effects": {"money": 200000000, "reputation": 28, "risk": 15},
                "next": 43
            },
            {
                "text": "📈 Halka arz — piyasa değeri 2 milyar",
                "effects": {"money": 600000000, "reputation": 38, "connections": 22},
                "next": 43
            }
        ]
    },

    42: {
        "chapter": "📖 Bölüm 8: Milyarder Eşiği",
        "text": (
            "Gizli veya açık, artık küresel bir güçsün.\n\n"
            "Servetin 400-700 milyon dolar.\n"
            "Bir teknoloji konsorsiumu kurma teklife geldi: 5 ülkenin en büyük şirketleri beraber.\n\n"
            "Liderliği alıyor musun?"
        ),
        "choices": [
            {
                "text": "👑 Evet — konsorsiyumu yönet",
                "effects": {"money": 300000000, "connections": 48, "reputation": 32},
                "next": "final_check"
            },
            {
                "text": "🌱 Hayır — sosyal sorumluluk vakfı kur",
                "effects": {"money": -100000000, "reputation": 48, "connections": 35},
                "next": "final_check"
            },
            {
                "text": "🚀 Uzay / temiz enerji şirketi kur",
                "effects": {"money": -200000000, "reputation": 38, "experience": 32},
                "next": 43
            }
        ]
    },

    # ══════════════════════════════════════
    # BÖLÜM 9: ZİRVE  (para: ~500M-2B$)
    # ══════════════════════════════════════

    43: {
        "chapter": "📖 Bölüm 9: Zirve",
        "text": (
            "Servetin 500 milyon – 1 milyar dolar arasında.\n\n"
            "Milyarder olmanın eşiğindesin. Hisseler yükseliyor, medya seni konuşuyor.\n"
            "Büyük bir satın alma fırsatı: Bir rakibin değeri 300 milyon. Pazar değeri: 900 milyon.\n\n"
            "Son hamle:"
        ),
        "choices": [
            {
                "text": "🏆 Rakibi satın al — 300M$ öde",
                "effects": {"money": -300000000, "connections": 28, "reputation": 28, "experience": 18},
                "next": "final_check"
            },
            {
                "text": "🌍 Global vakıf kur, insanlığa hizmet",
                "effects": {"reputation": 48, "connections": 35, "money": -150000000},
                "next": "final_check"
            },
            {
                "text": "💎 Hisseleri tut, büyümeye devam",
                "effects": {"money": 500000000, "risk": 15, "reputation": 22},
                "next": "final_check"
            }
        ]
    },

}

# ══════════════════════════════════════════════════════
# FİNAL SONUÇLARI
# ══════════════════════════════════════════════════════

ENDINGS = {
    "effsane_milyarder": {
        "title": "🏆 Efsane Milyarder",
        "text": (
            "🏆 TEBRİKLER — EFSANE MİLYARDER!\n\n"
            "Sıfırdan başladın, 500$ ile yola çıktın.\n"
            "Bugün milyardersin — hem servette hem itibarda.\n"
            "Forbes listesinde adın var. Dünyanın her köşesinde seni tanıyorlar.\n\n"
            "💰 Servet: 1.000.000.000$+\n"
            "⭐ İtibar: Efsane\n"
            "⚠️ Risk: Kontrollü"
        )
    },
    "iflas": {
        "title": "💸 İflas",
        "text": (
            "💸 İFLAS!\n\n"
            "Her şeyi kaybettin.\n"
            "Ama bu son değil — bu başlangıç.\n"
            "Jobs, Musk, Disney... hepsi önce iflas etti.\n\n"
            "Yeniden dene. Bu sefer daha akıllısın."
        )
    },
    "tutuklanma": {
        "title": "⚖️ Tutuklandın",
        "text": (
            "⚖️ TUTUKLAMA!\n\n"
            "Risk çok yüksekti.\n"
            "Vergi kaçakçılığı veya dolandırıcılık.\n\n"
            "Her şey bir gün ortaya çıkar.\n"
            "Para kazanırken hukuku yanında tut."
        )
    },
    "gizli_patron": {
        "title": "👑 Gizli Patron",
        "text": (
            "👑 GİZLİ PATRON!\n\n"
            "İsmin kimse bilmiyor ama sen her yeri yönetiyorsun.\n"
            "Hükümetler sana danışıyor, şirketler sana bağlı.\n\n"
            "Güç paradır diyenlere katılmıyorsun:\n"
            "Güç, kontrol.\n\n"
            "💰 Servet: Çok büyük ama gizli\n"
            "🤝 Bağlantılar: Efsane\n"
            "⭐ İtibar: Sıfır (kasıtlı)"
        )
    },
    "medya_yildizi": {
        "title": "🎤 Medya Yıldızı",
        "text": (
            "🎤 MEDYA YILDIZI!\n\n"
            "Milyonlarca takipçin, best-seller kitapların var.\n"
            "Her konuşman 200.000$ getiriyor.\n\n"
            "Para mı etki mi? Sen ikisine de sahipsin.\n\n"
            "⭐ İtibar: Efsane\n"
            "💰 Servet: 100M - 900M"
        )
    },
    "teknoloji_devi": {
        "title": "🚀 Teknoloji Devi",
        "text": (
            "🚀 TEKNOLOJİ DEVİ!\n\n"
            "Şirketin dünyayı değiştirdi.\n"
            "Elon, Jeff, Mark ile aynı sayfadasın.\n\n"
            "Geleceği sen şekillendirdin.\n\n"
            "💻 Etki: Küresel\n"
            "💰 Servet: 500M+\n"
            "🧠 Tecrübe: Maksimum"
        )
    },
    "yatirimci": {
        "title": "📊 Usta Yatırımcı",
        "text": (
            "📊 USTA YATIRIMCI!\n\n"
            "Kendi şirketi değil, doğru şirketlere yatırım yaptın.\n"
            "Portföyün 1 milyar dolar değerinde.\n\n"
            "Sen büyütüyorsun, onlar çalışıyor.\n\n"
            "💰 Servet: 200M+\n"
            "🤝 Bağlantılar: Dev ağ"
        )
    },
    "nefret_edilen_zengin": {
        "title": "😈 Nefret Edilen Zengin",
        "text": (
            "😈 NEFRET EDİLEN ZENGİN!\n\n"
            "Para kazandın ama herkes senden nefret ediyor.\n"
            "Çalışanların şikayet ediyor, basın seni karalıyor.\n\n"
            "Para varken bile yalnız olunur.\n\n"
            "💰 Servet: 1B+\n"
            "⭐ İtibar: Negatif"
        )
    },
    "global_guc": {
        "title": "🌍 Global Güç",
        "text": (
            "🌍 GLOBAL GÜÇ!\n\n"
            "Artık sadece iş insanı değilsin.\n"
            "Ülkeler seninle anlaşma masasına oturuyor.\n"
            "Politika, ekonomi, teknoloji — hepsinde etkilisin.\n\n"
            "💰 Servet: 500M+\n"
            "🌐 Etki: Küresel\n"
            "🤝 Bağlantılar: Liderler seviyesi"
        )
    },
    "hepsini_satip_kaybolan": {
        "title": "🏝️ Her Şeyi Satıp Kaybolan",
        "text": (
            "🏝️ HER ŞEYİ SATIP KAYBOLAN MİLYARDER!\n\n"
            "1 milyar dolar kazandın... ve harcadın.\n"
            "Adalar, yatlar, partiler...\n\n"
            "Bir gün uyandın: hesapta 0.\n"
            "Ama ne hikayeler var anlatacak!\n\n"
            "💰 Son durum: Sıfır\n"
            "😄 Efsane: Kesin"
        )
    }
}


def determine_ending(stats: dict) -> str:
    money     = stats.get("money", 0)
    reputation = stats.get("reputation", 0)
    risk      = stats.get("risk", 0)
    connections = stats.get("connections", 0)
    experience  = stats.get("experience", 0)

    # --- Kritik haller ---
    if risk >= 90:
        return "tutuklanma"
    if money <= 0:
        return "iflas"

    # --- Milyarder ($1B+) ---
    if money >= 1_000_000_000:
        if reputation < 0:
            return "nefret_edilen_zengin"
        if risk > 65:
            return "hepsini_satip_kaybolan"
        if connections >= 65:
            return "global_guc"
        return "effsane_milyarder"

    # --- 500M - 1B arası ---
    if money >= 500_000_000:
        if connections >= 55 and reputation < 20:
            return "gizli_patron"
        if reputation >= 65:
            return "medya_yildizi"
        if experience >= 65:
            return "teknoloji_devi"
        if connections >= 55:
            return "global_guc"
        return "yatirimci"

    # --- 100M - 500M ---
    if money >= 100_000_000:
        if connections >= 60 and reputation < 20:
            return "gizli_patron"
        if reputation >= 55:
            return "medya_yildizi"
        if experience >= 60:
            return "teknoloji_devi"
        return "yatirimci"

    # --- 10M - 100M ---
    if money >= 10_000_000:
        return "yatirimci"

    # --- 0 - 10M ---
    return "yatirimci"
