# -*- coding: utf-8 -*-
"""
Unit 8 Data Definition - IELTS Foundation Stage 2 (Band 4.0 - 4.5)
Topic: Transport, Traffic Congestion & Public Transit
"""

UNIT_CONFIG = {
    "unit_id": "08",
    "unit_num": 8,
    "title": "Unit 8: Transport, Traffic Congestion & Public Transit",
    "badge": "My IELTS journey",
    "audio_dir": "audio/unit08",
    "reading_title": "Solving Urban Gridlock: Why Investing in Public Transit Networks Matters",
    "reading_word_count": "~340 words • IELTS Foundation Stage 2",
}

VOCAB_LIST = [
    {
        "word": "congestion",
        "pos": "n",
        "ipa": "/kənˈdʒestʃən/",
        "meaning": "sự ùn tắc giao thông, nạn kẹt xe",
        "colloc": "severe traffic congestion, reduce road congestion",
        "example": "Expanding the underground metro is the best way to reduce severe traffic congestion."
    },
    {
        "word": "commute",
        "pos": "v/n",
        "ipa": "/kəˈmjuːt/",
        "meaning": "đi lại hằng ngày giữa nhà và nơi làm việc/học tập",
        "colloc": "commute to work, daily morning commute",
        "example": "Thousands of suburban residents commute to the city centre by train every morning."
    },
    {
        "word": "passenger",
        "pos": "n",
        "ipa": "/ˈpæsɪndʒə(r)/",
        "meaning": "hành khách (đi tàu, xe buýt, máy bay)",
        "colloc": "rail passenger, passenger safety",
        "example": "Electric buses can carry up to eighty passengers comfortably and quietly."
    },
    {
        "word": "vehicle",
        "pos": "n",
        "ipa": "/ˈviːəkl/",
        "meaning": "phương tiện giao thông, xe cộ",
        "colloc": "private vehicle, electric vehicle (EV)",
        "example": "Banning private vehicles from narrow historic streets helps improve air quality."
    },
    {
        "word": "infrastructure",
        "pos": "n",
        "ipa": "/ˈɪnfrəstrʌktʃə(r)/",
        "meaning": "cơ sở hạ tầng (cầu đường, bến bãi, mạng lưới điện/giao thông)",
        "colloc": "transport infrastructure, upgrade infrastructure",
        "example": "The government is investing billions of dollars in modern transport infrastructure."
    },
    {
        "word": "railway",
        "pos": "n",
        "ipa": "/ˈreɪlweɪ/",
        "meaning": "đường sắt, hệ thống tàu hỏa",
        "colloc": "high-speed railway, national railway network",
        "example": "A new high-speed railway now links the capital with major coastal ports."
    },
    {
        "word": "reliable",
        "pos": "adj",
        "ipa": "/rɪˈlaɪəbl/",
        "meaning": "đáng tin cậy, hoạt động ổn định",
        "colloc": "reliable public transport, safe and reliable",
        "example": "People will drive less if the city provides a cheap and reliable bus service."
    },
    {
        "word": "punctual",
        "pos": "adj",
        "ipa": "/ˈpʌŋktʃuəl/",
        "meaning": "đúng giờ (không bị trễ chuyến)",
        "colloc": "punctual train service, always punctual",
        "example": "Japanese bullet trains are world-famous for being extremely punctual."
    },
    {
        "word": "cyclist",
        "pos": "n",
        "ipa": "/ˈsaɪklɪst/",
        "meaning": "người đi xe đạp",
        "colloc": "dedicated lane for cyclists, protect cyclists",
        "example": "Building separate bike lanes protects cyclists from heavy trucks and cars."
    },
    {
        "word": "delay",
        "pos": "n/v",
        "ipa": "/dɪˈleɪ/",
        "meaning": "sự chậm trễ, sự trì hoãn chuyến đi",
        "colloc": "long traffic delay, cause a two-hour delay",
        "example": "Heavy snow caused a two-hour delay on the morning commuter railway line."
    },
    {
        "word": "subsidize",
        "pos": "v",
        "ipa": "/ˈsʌbsɪdaɪz/",
        "meaning": "trợ giá, hỗ trợ kinh phí từ ngân sách nhà nước",
        "colloc": "subsidize bus fares, heavily subsidized",
        "example": "Local authorities should subsidize public transit so low-income workers can afford it."
    },
    {
        "word": "convenient",
        "pos": "adj",
        "ipa": "/kənˈviːniənt/",
        "meaning": "thuận tiện, tiện lợi",
        "colloc": "fast and convenient, convenient location",
        "example": "Paying for metro tickets with a smartphone app is fast and convenient."
    },
    {
        "word": "alternative",
        "pos": "n/adj",
        "ipa": "/ɔːlˈtɜːnətɪv/",
        "meaning": "giải pháp thay thế, phương án lựa chọn khác",
        "colloc": "eco-friendly alternative, alternative transport",
        "example": "Cycling is a healthy and eco-friendly alternative to driving a private car."
    },
    {
        "word": "exhaust",
        "pos": "n",
        "ipa": "/ɪɡˈzɔːst/",
        "meaning": "khí thải độc hại từ ống xả động cơ xe",
        "colloc": "toxic exhaust fumes, car exhaust",
        "example": "Breathing toxic exhaust fumes from diesel trucks can damage human lungs."
    },
    {
        "word": "network",
        "pos": "n",
        "ipa": "/ˈnetwɜːk/",
        "meaning": "mạng lưới (tuyến xe buýt, tàu điện, đường bộ)",
        "colloc": "underground metro network, extensive road network",
        "example": "London has an extensive underground metro network that serves millions daily."
    }
]

GRAMMAR_THEORY = {
    "tier1": {
        "title": "🟢 Tầng 1: Căn Bản (Phân Biệt Because/Since + Mệnh Đề vs. Because of/Due to + Cụm Danh Từ)",
        "content": [
            "• <b>Nhóm đi với Mệnh đề (S + V):</b> <code>because / since / as + S + V</code><br>&nbsp;&nbsp;<i>Ví dụ:</i> Many commuters prefer the metro <b>because</b> <u>it is punctual and convenient</u>.",
            "• <b>Nhóm đi với Cụm danh từ hoặc V-ing:</b> <code>because of / due to / owing to + Noun Phrase / V-ing</code><br>&nbsp;&nbsp;<i>Ví dụ:</i> Flights were cancelled <b>due to</b> <u>severe weather delays</u> (<i>không có động từ chia thì sau due to</i>)."
        ]
    },
    "tier2": {
        "title": "🔵 Tầng 2: Nâng Cao (Từ Nối Chỉ Hệ Quả Học Thuật: Therefore, Consequently, As a result)",
        "content": [
            "• <b>Công thức nối 2 câu độc lập (hoặc sau dấu chấm phẩy):</b><br>&nbsp;&nbsp;<code>Mệnh đề nguyên nhân. Therefore, / Consequently, / As a result, + Mệnh đề kết quả.</code><br>&nbsp;&nbsp;<i>Ví dụ:</i> Too many people drive private vehicles during rush hour. <b>Consequently,</b> city centres suffer from severe traffic congestion and toxic exhaust fumes.",
            "• <b>Động từ chỉ nguyên nhân - kết quả trực tiếp (Band 7.0+):</b> <code>lead to / result in / cause + Noun Phrase</code><br>&nbsp;&nbsp;<i>Ví dụ:</i> Investing in railway infrastructure <b>leads to</b> faster daily commutes."
        ]
    }
}

VOCAB_QUESTIONS = [
    {
        "q": "1. During rush hour, thousands of cars enter the city centre and cause severe traffic ________.",
        "opts": ["congestion", "hospitality", "upbringing", "adolescence"],
        "ans": 0,
        "exp": "<b>traffic congestion</b>: sự ùn tắc giao thông, kẹt xe."
    },
    {
        "q": "2. Instead of driving, my father takes the underground train to ________ to his office every day.",
        "opts": ["commute", "demolish", "nurture", "renovate"],
        "ans": 0,
        "exp": "<b>commute to work/office</b> (v): đi làm hằng ngày từ nhà tới chỗ làm."
    },
    {
        "q": "3. The government should ________ bus and train fares so that students and workers pay less.",
        "opts": ["subsidize", "congest", "delay", "demolish"],
        "ans": 0,
        "exp": "<b>subsidize</b> (v): trợ giá từ ngân sách nhà nước."
    },
    {
        "q": "4. High-speed trains are a clean and fast ________ to short domestic flights.",
        "opts": ["alternative", "exhaust", "cyclist", "passenger"],
        "ans": 0,
        "exp": "<b>alternative (to)</b> (n): phương án thay thế."
    },
    {
        "q": "5. Old petrol cars release toxic ________ fumes that pollute the air in crowded streets.",
        "opts": ["exhaust", "infrastructure", "network", "suburb"],
        "ans": 0,
        "exp": "<b>exhaust fumes</b>: khí thải từ ống xả xe cộ."
    },
    {
        "q": "6. A modern city needs strong transport ________, including bridges, tunnels, and metro lines.",
        "opts": ["infrastructure", "adolescence", "sibling", "obesity"],
        "ans": 0,
        "exp": "<b>transport infrastructure</b>: cơ sở hạ tầng giao thông."
    },
    {
        "q": "7. Every ________ on the express bus must wear a seatbelt for safety.",
        "opts": ["passenger", "vehicle", "railway", "skyscraper"],
        "ans": 0,
        "exp": "<b>passenger</b> (n): hành khách."
    },
    {
        "q": "8. The city has painted green bike lanes along the river to keep ________ safe from heavy traffic.",
        "opts": ["cyclists", "skyscrapers", "households", "devices"],
        "ans": 0,
        "exp": "<b>cyclists</b> (n): những người đi xe đạp."
    },
    {
        "q": "9. Swiss trains are famous for being extremely ________; they almost never arrive late.",
        "opts": ["punctual", "nuclear", "extended", "sedentary"],
        "ans": 0,
        "exp": "<b>punctual</b> (adj): đúng giờ."
    },
    {
        "q": "10. Because the metro station is right next to my flat, taking the train is very ________.",
        "opts": ["convenient", "artificial", "endangered", "virtual"],
        "ans": 0,
        "exp": "<b>convenient</b> (adj): thuận tiện, tiện lợi."
    },
    {
        "q": "11. An accident on the highway caused a forty-minute ________ for morning commuters.",
        "opts": ["delay", "bond", "harmony", "breakthrough"],
        "ans": 0,
        "exp": "<b>delay</b> (n): sự chậm trễ."
    },
    {
        "q": "12. Electric ________ produce zero tailpipe emissions and are much quieter than diesel trucks.",
        "opts": ["vehicles", "pedestrians", "siblings", "suburbs"],
        "ans": 0,
        "exp": "<b>electric vehicles (EVs)</b>: các phương tiện giao thông chạy điện."
    },
    {
        "q": "13. Citizens will only give up their cars if the public bus system is frequent and ________.",
        "opts": ["reliable", "nuclear", "influential", "adjacent"],
        "ans": 0,
        "exp": "<b>reliable</b> (adj): đáng tin cậy, hoạt động ổn định."
    },
    {
        "q": "14. Engineers are building a high-speed ________ that connects the airport with the city centre.",
        "opts": ["railway", "upbringing", "accommodation", "privacy"],
        "ans": 0,
        "exp": "<b>high-speed railway</b>: tuyến đường sắt cao tốc."
    },
    {
        "q": "15. Expanding the underground metro ________ will allow millions of people to travel easily.",
        "opts": ["network", "conflict", "exhaust", "addiction"],
        "ans": 0,
        "exp": "<b>metro network</b>: mạng lưới tàu điện ngầm."
    },
    {
        "q": "16. [Ôn tập Unit 7] The central shopping street has been turned into a car-free ________ zone.",
        "opts": ["pedestrian", "passenger", "nuclear", "virtual"],
        "ans": 0,
        "exp": "<b>pedestrian zone</b> (Unit 7): khu phố dành riêng cho người đi bộ."
    },
    {
        "q": "17. [Ôn tập Unit 7] The old bus depot was ________ to make way for a modern railway station.",
        "opts": ["demolished", "nurtured", "communicated", "revised"],
        "ans": 0,
        "exp": "<b>demolished</b> (Unit 7): bị phá dỡ."
    },
    {
        "q": "18. [Ôn tập Unit 6] In a modern ________ family, both parents often commute to work every day.",
        "opts": ["nuclear", "extended", "spacious", "renewable"],
        "ans": 0,
        "exp": "<b>nuclear family</b> (Unit 6): gia đình hạt nhân."
    },
    {
        "q": "19. [Ôn tập Unit 5] Commuters can buy digital train tickets on a smartphone ________.",
        "opts": ["platform", "habitat", "sibling", "stamina"],
        "ans": 0,
        "exp": "<b>digital platform</b> (Unit 5): nền tảng số."
    },
    {
        "q": "20. [Ôn tập Unit 3] Switching from petrol cars to electric trains helps cut carbon ________.",
        "opts": ["emissions", "assignments", "conflicts", "bonds"],
        "ans": 0,
        "exp": "<b>carbon emissions</b> (Unit 3): khí thải carbon."
    }
]

GRAMMAR_QUESTIONS = [
    {
        "q": "1. Morning trains were delayed for thirty minutes ________ heavy fog on the railway tracks.",
        "opts": ["because", "due to", "since", "therefore"],
        "ans": 1,
        "exp": "Sau chỗ trống là cụm danh từ 'heavy fog on the railway tracks' (không có động từ chia thì) -> Dùng <b>due to</b>."
    },
    {
        "q": "2. Many office workers prefer taking the metro ________ it is punctual and avoids road congestion.",
        "opts": ["because of", "owing to", "because", "consequently"],
        "ans": 2,
        "exp": "Sau chỗ trống là mệnh đề đầy đủ 'it is punctual...' (S + V) -> Dùng liên từ <b>because</b>."
    },
    {
        "q": "3. The city council heavily subsidized bus fares. ________, the number of bus passengers increased by 40%.",
        "opts": ["Because", "Consequently", "Due to", "Although"],
        "ans": 1,
        "exp": "Đứng đầu câu mới, trước dấu phẩy để chỉ kết quả của câu trước -> <b>Consequently</b> (Do đó / Kết quả là)."
    },
    {
        "q": "4. Severe traffic congestion ________ a lack of reliable public transport in rapidly growing cities.",
        "opts": ["results from", "results in", "therefore", "because"],
        "ans": 0,
        "exp": "<b>results from + nguyên nhân</b>: bắt nguồn từ sự thiếu hụt giao thông công cộng đáng tin cậy."
    },
    {
        "q": "5. Breathing toxic exhaust fumes every day can ________ serious respiratory illnesses.",
        "opts": ["lead to", "due to", "because of", "as a result"],
        "ans": 0,
        "exp": "Sau động từ khuyết thiếu 'can' cần động từ nguyên mẫu: <b>lead to + Noun</b> (dẫn đến)."
    },
    {
        "q": "6. ________ the high cost of city-centre parking, most commuters now leave their private vehicles at home.",
        "opts": ["Because", "Owing to", "Since", "Therefore"],
        "ans": 1,
        "exp": "Đi với cụm danh từ 'the high cost of city-centre parking' -> <b>Owing to</b> (= Because of / Due to)."
    },
    {
        "q": "7. Dedicated bike lanes are very safe. ________, more students are cycling to university.",
        "opts": ["As a result", "Because of", "Due to", "Since"],
        "ans": 0,
        "exp": "Cụm trạng từ nối chỉ kết quả đứng đầu câu trước dấu phẩy -> <b>As a result</b>."
    },
    {
        "q": "8. ________ the new express railway opened last month, daily commuting time has dropped by half.",
        "opts": ["Since", "Due to", "Because of", "Therefore"],
        "ans": 0,
        "exp": "Đi với mệnh đề 'the new express railway opened last month' -> <b>Since</b>."
    },
    {
        "q": "9. Poor road infrastructure ________ long traffic delays during the rainy season.",
        "opts": ["causes", "because", "due to", "consequently"],
        "ans": 0,
        "exp": "Câu thiếu động từ chính chia theo chủ ngữ số ít 'Poor road infrastructure' -> <b>causes</b> (gây ra)."
    },
    {
        "q": "10. Electric buses are quiet and clean; ________, they are an ideal alternative for modern cities.",
        "opts": ["therefore", "because", "due to", "owing to"],
        "ans": 0,
        "exp": "Sau dấu chấm phẩy (;), trước dấu phẩy (,) dùng trạng từ liên kết chỉ kết quả -> <b>therefore</b>."
    }
]

DIALOGUE_LINES = [
    {
        "speaker": "Transit Clerk",
        "text": "Good morning, Metro Customer Service! How can I help you with your travel pass today?",
        "hint": ""
    },
    {
        "speaker": "Commuter",
        "text": "Hello! I just moved to the northern suburb, and I need a reliable way to commute to the city centre.",
        "hint": ""
    },
    {
        "speaker": "Transit Clerk",
        "text": "You should definitely apply for our Monthly Smart Commuter Card. It covers both the railway and electric buses.",
        "hint": ""
    },
    {
        "speaker": "Commuter",
        "text": "That sounds very convenient! How long does the express train take from North Station to Central Plaza?",
        "hint": ""
    },
    {
        "speaker": "Transit Clerk",
        "text": "Driving a car takes nearly an hour due to congestion, but the express train takes only 22 minutes.",
        "hint": "💡 Đáp án câu 1: 22 / 22 minutes"
    },
    {
        "speaker": "Commuter",
        "text": "Wow, 22 minutes is super fast! What if I want to bring my bicycle to the station?",
        "hint": ""
    },
    {
        "speaker": "Transit Clerk",
        "text": "We have a free secure parking area for cyclists right next to Platform 1.",
        "hint": "💡 Đáp án câu 2: Platform 1"
    },
    {
        "speaker": "Commuter",
        "text": "How much does the Monthly Smart Commuter Card cost for full-time workers?",
        "hint": ""
    },
    {
        "speaker": "Transit Clerk",
        "text": "The normal price is 90 pounds, but because the city council subsidizes green travel, it is now 65 pounds.",
        "hint": "💡 Bẫy giá cũ vs giá đã trợ giá câu 3: 65"
    },
    {
        "speaker": "Commuter",
        "text": "Great! Can I also use the card on the weekend airport shuttle?",
        "hint": ""
    },
    {
        "speaker": "Transit Clerk",
        "text": "Yes, all cardholders get free rides on the Green Express bus network on Saturdays and Sundays.",
        "hint": "💡 Đáp án câu 4: Green Express"
    },
    {
        "speaker": "Commuter",
        "text": "Let's register! My surname is Henderson. That is spelled H - E - N - D - E - R - S - O - N.",
        "hint": "💡 Đáp án đánh vần câu 5: HENDERSON"
    },
    {
        "speaker": "Transit Clerk",
        "text": "Thank you, Mr. Henderson. What document do you have to verify your home address?",
        "hint": ""
    },
    {
        "speaker": "Commuter",
        "text": "I brought my electricity bill and my driving licence.",
        "hint": "💡 Đáp án câu 6: driving licence / electricity bill"
    },
    {
        "speaker": "Transit Clerk",
        "text": "Perfect! Here is your new Smart Commuter Card. Have a punctual and pleasant journey!",
        "hint": ""
    }
]

LISTENING_QUESTIONS = [
    {
        "id": "l1",
        "label": "1. Express train journey time to Central Plaza (minutes):",
        "placeholder": "Nhập con số / mốc thời gian nghe được...",
        "answers": ["22", "22 minutes", "twenty-two"]
    },
    {
        "id": "l2",
        "label": "2. Free secure bike parking for cyclists is next to:",
        "placeholder": "Nhập con số / mốc thời gian nghe được...",
        "answers": ["platform 1", "platform one"]
    },
    {
        "id": "l3",
        "label": "3. Subsidized monthly price of the Smart Commuter Card (£):",
        "placeholder": "Nhập con số / mốc thời gian nghe được...",
        "answers": ["65", "65 pounds"]
    },
    {
        "id": "l4",
        "label": "4. Name of the weekend airport bus network: the ________ Express",
        "placeholder": "Nhập tên riêng được đánh vần...",
        "answers": ["green", "green express"]
    },
    {
        "id": "l5",
        "label": "5. Commuter's surname: Mr.",
        "placeholder": "Nhập tên riêng được đánh vần...",
        "answers": ["henderson"]
    },
    {
        "id": "l6",
        "label": "6. Document provided with the electricity bill: his ________",
        "placeholder": "Nhập từ/cụm từ nghe được (1-2 từ)...",
        "answers": ["driving licence", "driving license", "licence", "license"]
    }
]

READING_PASSAGE = {
    "title": "Solving Urban Gridlock: Why Investing in Public Transit Networks Matters",
    "paragraphs": [
        {
            "label": "Paragraph A - The High Cost of Private Vehicles",
            "content": "In many rapidly growing cities, millions of residents rely on private <b>vehicles</b> for their daily <b>commute</b>. Due to the overwhelming number of cars on narrow roads, city centres suffer from severe traffic <b>congestion</b> and long <b>delays</b>. Not only does this waste valuable working hours, but toxic <b>exhaust</b> fumes from petrol engines also damage public health and the urban environment."
        },
        {
            "label": "Paragraph B - Building a Reliable Transit Network",
            "content": "Urban planners agree that the most effective solution is to upgrade public transport <b>infrastructure</b>. When a city expands its underground metro and high-speed <b>railway</b> <b>network</b>, thousands of <b>passengers</b> can travel simultaneously without roadblocks. Because modern electric trains are <b>punctual</b>, safe, and <b>convenient</b>, commuters willingly leave their cars at home."
        },
        {
            "label": "Paragraph C - Subsidies and Green Alternatives",
            "content": "Furthermore, governments should <b>subsidize</b> ticket prices so that public transit remains affordable for every citizen. Cities can also create dedicated lanes for <b>cyclists</b> and electric buses, offering an eco-friendly <b>alternative</b> for short trips. Consequently, investing in a <b>reliable</b> public transit system reduces pollution and makes urban life far more enjoyable."
        }
    ]
}

READING_QUESTIONS = [
    {
        "id": "r1",
        "label": "1. How underground metro and railway networks move passengers without roadblocks: (Paragraph A, B or C)",
        "placeholder": "Nhập chữ cái A, B hoặc C...",
        "answers": ["b", "paragraph b"]
    },
    {
        "id": "r2",
        "label": "2. Government ticket subsidies and dedicated lanes for cyclists: (Paragraph A, B or C)",
        "placeholder": "Nhập chữ cái A, B hoặc C...",
        "answers": ["c", "paragraph c"]
    },
    {
        "id": "r3",
        "label": "3. The problems caused by too many private cars and toxic exhaust fumes: (Paragraph A, B or C)",
        "placeholder": "Nhập chữ cái A, B hoặc C...",
        "answers": ["a", "paragraph a"]
    },
    {
        "id": "r4",
        "label": "4. What do petrol engines release that damages public health? Toxic ________. (NO MORE THAN TWO WORDS)",
        "placeholder": "Nhập từ/cụm từ trích từ đoạn A...",
        "answers": ["exhaust fumes", "exhaust"]
    },
    {
        "id": "r5",
        "label": "5. Why do commuters willingly leave their cars at home? Because electric trains are punctual, safe, and ________. (ONE WORD)",
        "placeholder": "Nhập từ/cụm từ trích từ đoạn B...",
        "answers": ["convenient"]
    },
    {
        "id": "r6",
        "label": "6. Who should governments build dedicated lanes for besides electric buses? (ONE WORD)",
        "placeholder": "Nhập từ/cụm từ trích từ đoạn C...",
        "answers": ["cyclists"]
    }
]

WRITING_TASK = {
    "topic": "✍️ Academic Writing Lab (Task 2 Problem & Solution): Giải Quyết Nạn Kẹt Xe Đô Thị",
    "prompt": "Write a short paragraph (65 - 85 words) explaining the main cause of urban traffic congestion and suggesting how governments can encourage people to use public transport.",
    "criteria": "Tiêu chuẩn: Sử dụng cấu trúc Nguyên nhân – Kết quả (due to / because / therefore / consequently / lead to), và ít nhất 4 từ vựng Unit 8 (congestion, commute, vehicle, infrastructure, railway, reliable, punctual, subsidize, alternative, exhaust, network...).",
    "target_words": 75,
    "unit_vocab": ["congestion", "commute", "passenger", "vehicle", "infrastructure", "railway", "reliable", "punctual", "cyclist", "delay", "subsidize", "convenient", "alternative", "exhaust", "network"],
    "model_essay": "In many major cities, severe traffic congestion occurs mainly due to the excessive use of private vehicles during the morning commute. This not only causes long delays for passengers but also releases toxic exhaust fumes into the air. To solve this problem, governments should invest heavily in modern transport infrastructure, such as expanding the underground railway network and building safe lanes for cyclists. Furthermore, if authorities subsidize ticket fares to make buses more punctual, reliable, and convenient, citizens will gladly choose public transit as an eco-friendly alternative.",
    "model_analysis": [
        "<b>Câu 1 & 2 (Nêu nguyên nhân & Hệ quả - Cause & Effect):</b> Dùng cụm giới từ học thuật <code>mainly due to the excessive use of private vehicles</code> kết hợp <code>traffic congestion</code>, <code>commute</code>, <code>delays</code> và <code>toxic exhaust fumes</code>.",
        "<b>Câu 3 (Giải pháp hạ tầng - Solution 1):</b> Đề xuất <code>invest heavily in modern transport infrastructure</code>, <code>railway network</code> và <code>safe lanes for cyclists</code>.",
        "<b>Câu 4 (Giải pháp chính sách - Solution 2):</b> Khai thác động từ <code>subsidize ticket fares</code> cùng bộ 3 tính từ <code>punctual, reliable, and convenient</code> + <code>eco-friendly alternative</code>."
    ],
    "model_translation": "Tại nhiều thành phố lớn, tình trạng ùn tắc giao thông nghiêm trọng xảy ra chủ yếu do việc sử dụng quá mức các phương tiện cá nhân trong giờ đi làm buổi sáng. Điều này không chỉ gây ra sự chậm trễ kéo dài cho hành khách mà còn thải ra khí thải độc hại vào không khí. Để giải quyết vấn đề này, chính phủ nên đầu tư mạnh vào cơ sở hạ tầng giao thông hiện đại, chẳng hạn như mở rộng mạng lưới đường sắt ngầm và xây dựng làn đường an toàn cho người đi xe đạp. Hơn nữa, nếu chính quyền trợ giá vé để xe buýt đúng giờ, đáng tin cậy và thuận tiện hơn, người dân sẽ sẵn lòng chọn giao thông công cộng như một giải pháp thay thế thân thiện với môi trường."
}

SPEAKING_TASK = {
    "title": "🗣️ Speaking Lab: Phỏng Vấn Về Giao Thông Đô Thị & Phương Tiện Đi Lại",
    "questions": [
        {
            "id": "q1",
            "text": "Q1: How do you usually commute to school or work every day?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Nêu phương tiện đi lại (electric bus / metro railway / bicycle) + Giải thích lý do bằng because/due to (convenient, punctual, helps avoid traffic congestion).",
            "sample_answer": "Every morning, I commute to university by electric bus because it is affordable and convenient. Since the city created dedicated bus lanes last year, the service has become much more punctual and helps me avoid rush-hour traffic delays.",
            "sample_audio_key": "speaking_q1"
        },
        {
            "id": "q2",
            "text": "Q2: What is the biggest traffic problem in your city at the moment?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Nêu vấn đề (severe rush-hour congestion and toxic exhaust fumes) + Chỉ ra nguyên nhân (too many private vehicles and narrow road infrastructure).",
            "sample_answer": "The biggest challenge in my city is severe traffic congestion due to the overwhelming number of private vehicles. During peak hours, millions of motorbikes and cars cause long delays and release toxic exhaust fumes into the air.",
            "sample_audio_key": "speaking_q2"
        },
        {
            "id": "q3",
            "text": "Q3: How can the government encourage more people to use public transport?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Nêu 2 giải pháp (upgrade the metro network to make it more reliable + subsidize ticket prices for passengers and cyclists).",
            "sample_answer": "To encourage people to leave their cars at home, the government should upgrade transport infrastructure and expand the underground railway network. Furthermore, authorities ought to subsidize ticket fares so that public transit becomes a reliable alternative for every passenger.",
            "sample_audio_key": "speaking_q3"
        }
    ],
    "targeted_sounds": [
        {"word": "congestion", "sound": "/kənˈdʒestʃən/", "note": "Nhấn âm tiết thứ 2: -GES- (/ˈdʒestʃən/)"},
        {"word": "infrastructure", "sound": "/ˈɪnfrəstrʌktʃə(r)/", "note": "Nhấn âm tiết đầu tiên: IN-fra-struc-ture"},
        {"word": "vehicle", "sound": "/ˈviːəkl/", "note": "Âm 'h' câm, nhấn âm đầu: VEE-uh-kl"},
        {"word": "punctual", "sound": "/ˈpʌŋktʃuəl/", "note": "Nhấn âm đầu tiên: PUNC-tchu-al"},
        {"word": "exhaust", "sound": "/ɪɡˈzɔːst/", "note": "Âm 'ex-' phát âm là /ɪɡˈz/, 'h' câm"}
    ],
    "lexical_words": ["congestion", "commute", "passenger", "vehicle", "infrastructure", "railway", "reliable", "punctual", "cyclist", "delay", "subsidize", "convenient", "alternative", "exhaust", "network"]
}
