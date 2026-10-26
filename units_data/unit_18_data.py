# -*- coding: utf-8 -*-
"""
Unit 18 Data Definition - IELTS Foundation Stage 4 (Band 5.0)
Topic: Agriculture, Food Security, Organic Farming & Genetic Engineering
"""

UNIT_CONFIG = {
    "unit_id": "18",
    "unit_num": 18,
    "title": "Unit 18: Agriculture, Food Security, Organic Farming & Genetic Engineering",
    "badge": "My IELTS journey",
    "audio_dir": "audio/unit18",
    "reading_title": "Feeding Ten Billion People: Organic Farming versus Genetic Engineering",
    "reading_word_count": "~390 words • IELTS Foundation Stage 4",
}

VOCAB_LIST = [
    {
        "word": "agriculture",
        "pos": "n",
        "ipa": "/ˈæɡrɪkʌltʃə(r)/",
        "meaning": "ngành nông nghiệp (adj: agricultural — thuộc nông nghiệp)",
        "colloc": "intensive agriculture, sustainable agriculture, modern agriculture",
        "example": "Approximately seventy percent of the world's freshwater supply is consumed by agriculture."
    },
    {
        "word": "cultivate",
        "pos": "v",
        "ipa": "/ˈkʌltɪveɪt/",
        "meaning": "canh tác, trồng trọt (cây lương thực hoặc đất đai)",
        "colloc": "cultivate crops, cultivate land, cultivate wet rice",
        "example": "Local farmers have begun to cultivate drought-tolerant varieties of wheat to cope with climate change."
    },
    {
        "word": "harvest",
        "pos": "n/v",
        "ipa": "/ˈhɑːvɪst/",
        "meaning": "vụ mùa thu hoạch; thu hoạch nông sản",
        "colloc": "abundant harvest, poor harvest, harvest ripe crops",
        "example": "Severe flooding in the delta destroyed nearly half of this year's autumn rice harvest."
    },
    {
        "word": "irrigation",
        "pos": "n",
        "ipa": "/ˌɪrɪˈɡeɪʃn/",
        "meaning": "hệ thống tưới tiêu thủy lợi",
        "colloc": "drip irrigation system, agricultural irrigation canals",
        "example": "Installing modern drip irrigation systems allows farmers to water their fields without wasting groundwater."
    },
    {
        "word": "fertilizer",
        "pos": "n",
        "ipa": "/ˈfɜːtəlaɪzə(r)/",
        "meaning": "phân bón (hóa học hoặc hữu cơ)",
        "colloc": "chemical fertilizers, synthetic fertilizers, natural fertilizer",
        "example": "The excessive use of chemical fertilizers has degraded soil quality and polluted nearby rivers."
    },
    {
        "word": "pesticide",
        "pos": "n",
        "ipa": "/ˈpestɪsaɪd/",
        "meaning": "thuốc trừ sâu, hóa chất diệt côn trùng gây hại",
        "colloc": "spray toxic pesticides, harmful pesticide residues",
        "example": "Consumers wash fruit and vegetables thoroughly to remove harmful pesticide residues."
    },
    {
        "word": "organic",
        "pos": "adj",
        "ipa": "/ɔːˈɡænɪk/",
        "meaning": "hữu cơ (canh tác tự nhiên không sử dụng phân bón hay thuốc trừ sâu hóa học)",
        "colloc": "organic farming, certified organic produce, organic vegetables",
        "example": "Although organic vegetables are free from synthetic chemicals, they are often more expensive."
    },
    {
        "word": "livestock",
        "pos": "n",
        "ipa": "/ˈlaɪvstɒk/",
        "meaning": "gia súc, vật nuôi trang trại (bò, cừu, lợn — luôn chia động từ số nhiều)",
        "colloc": "raise livestock, intensive livestock farming",
        "example": "Raising livestock such as cattle produces a large amount of methane, a potent greenhouse gas."
    },
    {
        "word": "famine",
        "pos": "n",
        "ipa": "/ˈfæmɪn/",
        "meaning": "nạn đói diện rộng",
        "colloc": "widespread famine, prevent severe famine",
        "example": "High-yield crop varieties have helped prevent widespread famine in developing nations."
    },
    {
        "word": "yield",
        "pos": "n/v",
        "ipa": "/jiːld/",
        "meaning": "năng suất, sản lượng cây trồng thu được trên mỗi đơn vị diện tích",
        "colloc": "boost crop yields, high-yield seeds, average yield per hectare",
        "example": "Advancements in agricultural science have doubled average grain yields over the past fifty years."
    },
    {
        "word": "sustainable",
        "pos": "adj",
        "ipa": "/səˈsteɪnəbl/",
        "meaning": "bền vững (thân thiện với môi trường, không làm cạn kiệt tài nguyên cho tương lai)",
        "colloc": "sustainable farming practices, environmentally sustainable",
        "example": "Governments must subsidize sustainable farming methods to protect the ecosystem for future generations."
    },
    {
        "word": "modify",
        "pos": "v",
        "ipa": "/ˈmɒdɪfaɪ/",
        "meaning": "biến đổi, chỉnh sửa (đặc biệt là biến đổi gen — genetically modified crops)",
        "colloc": "genetically modified (GM) crops, modify plant genetics",
        "example": "Scientists can modify the genetic structure of maize so that it can resist insect attacks naturally."
    },
    {
        "word": "soil",
        "pos": "n",
        "ipa": "/sɔɪl/",
        "meaning": "đất trồng, thổ nhưỡng",
        "colloc": "fertile soil, soil erosion, soil degradation",
        "example": "Over-farming without crop rotation strips essential nutrients from the soil and causes erosion."
    },
    {
        "word": "drought",
        "pos": "n",
        "ipa": "/draʊt/",
        "meaning": "hạn hán kéo dài",
        "colloc": "prolonged drought, severe drought, drought-tolerant seeds",
        "example": "A prolonged drought in the region has dried up rivers and devastated local rice harvests."
    },
    {
        "word": "shortage",
        "pos": "n",
        "ipa": "/ˈʃɔːtɪdʒ/",
        "meaning": "sự thiếu hụt, sự khan hiếm (lương thực, nước ngọt, lao động)",
        "colloc": "acute food shortage, severe water shortage, labour shortage",
        "example": "Extreme weather events and prolonged droughts could trigger global food shortages in the future."
    }
]

GRAMMAR_THEORY = {
    "tier1": {
        "title": "🟢 Tầng 1: Hiện Tại Hoàn Thành (have/has V3) vs. Hiện Tại Hoàn Thành Tiếp Diễn (have/has been V-ing)",
        "content": [
            "• <b>Present Perfect (<code>have/has + V3/ed</code>):</b> Nhấn mạnh vào <b>kết quả đã hoàn tất hoặc con số định lượng</b> tính đến hiện tại (thường đi với <i>over the past 50 years, since the 1960s</i>).<br>&nbsp;&nbsp;<i>Ví dụ:</i> High-yield seeds <b>have doubled</b> global grain production and <b>prevented</b> widespread famine.",
            "• <b>Present Perfect Passive (<code>have/has + been + V3/ed</code>):</b> Nhấn mạnh hậu quả môi trường đã xảy ra.<br>&nbsp;&nbsp;<i>Ví dụ:</i> Millions of hectares of fertile soil <b>have been degraded</b> by chemical fertilizers.",
            "• <b>Present Perfect Continuous (<code>have/has + been + V-ing</code>):</b> Nhấn mạnh <b>quá trình liên tục</b> bắt đầu trong quá khứ và vẫn đang tiếp diễn.<br>&nbsp;&nbsp;<i>Ví dụ:</i> Scientists <b>have been modifying</b> plant genetics for decades to combat severe droughts."
        ]
    },
    "tier2": {
        "title": "🔵 Tầng 2: Cụm Động Từ Nhân - Quả Học Thuật (Academic Cause-and-Effect Verbs)",
        "content": [
            "• <b>Thay thế 'make / because' bằng 4 cấu trúc Nhân - Quả chuẩn C1 trong Writing Task 2:</b><br>&nbsp;&nbsp;1. <b><code>lead to / result in + Noun / V-ing</code> (Dẫn đến hậu quả là...):</b><br>&nbsp;&nbsp;&nbsp;&nbsp;<i>Ví dụ:</i> Prolonged droughts often <b>result in</b> acute food shortages.<br>&nbsp;&nbsp;2. <b><code>contribute (significantly) to + Noun / V-ing</code> (Góp phần gây ra...):</b><br>&nbsp;&nbsp;&nbsp;&nbsp;<i>Ví dụ:</i> Intensive livestock farming <b>contributes significantly to</b> global warming.<br>&nbsp;&nbsp;3. <b><code>stem from / result from + Nguyên nhân</code> (Bắt nguồn từ nguyên nhân...):</b><br>&nbsp;&nbsp;&nbsp;&nbsp;<i>Ví dụ:</i> Severe soil degradation largely <b>stems from</b> the overuse of synthetic pesticides."
        ]
    }
}

VOCAB_QUESTIONS = [
    {
        "q": "1. Modern ________ relies heavily on machinery and scientific irrigation to feed eight billion people.",
        "opts": ["agriculture", "apparatus", "legislation", "turbine"],
        "ans": 0,
        "exp": "<b>agriculture</b> (n): ngành nông nghiệp."
    },
    {
        "q": "2. Farmers in mountainous regions build terraced fields on steep slopes in order to ________ wet rice.",
        "opts": ["cultivate", "modify", "filter", "transmit"],
        "ans": 0,
        "exp": "<b>cultivate</b> (v): canh tác, trồng trọt cây lương thực."
    },
    {
        "q": "3. Favourable weather conditions throughout the spring resulted in an abundant wheat ________ this autumn.",
        "opts": ["harvest", "drought", "famine", "shortage"],
        "ans": 0,
        "exp": "<b>abundant harvest</b> (n): vụ mùa thu hoạch bội thu."
    },
    {
        "q": "4. By switching to drip ________, the vegetable farm reduced its water consumption by 60%.",
        "opts": ["irrigation", "pesticide", "fertilizer", "livestock"],
        "ans": 0,
        "exp": "<b>drip irrigation</b> (n): hệ thống tưới nhỏ giọt tiết kiệm nước."
    },
    {
        "q": "5. When rain washes excess chemical ________ from farmlands into rivers, it causes water pollution.",
        "opts": ["fertilizers", "yields", "droughts", "shortages"],
        "ans": 0,
        "exp": "<b>chemical fertilizers</b> (n): phân bón hóa học."
    },
    {
        "q": "6. Spraying synthetic ________ kills destructive insects, but it also harms honeybees.",
        "opts": ["pesticides", "harvests", "soils", "turbines"],
        "ans": 0,
        "exp": "<b>pesticides</b> (n): thuốc trừ sâu."
    },
    {
        "q": "7. Demand for ________ fruit and vegetables has grown rapidly as consumers worry about chemical residues.",
        "opts": ["organic", "solar", "sedentary", "chronic"],
        "ans": 0,
        "exp": "<b>organic</b> (adj): hữu cơ (không dùng hóa chất tổng hợp)."
    },
    {
        "q": "8. Vast areas of tropical forest have been cleared to create grazing land for cattle and other ________.",
        "opts": ["livestock", "famine", "yield", "soil"],
        "ans": 0,
        "exp": "<b>livestock</b> (n): gia súc, vật nuôi trang trại."
    },
    {
        "q": "9. International aid agencies delivered emergency grain supplies to prevent a catastrophic ________.",
        "opts": ["famine", "harvest", "yield", "irrigation"],
        "ans": 0,
        "exp": "<b>famine</b> (n): nạn đói diện rộng."
    },
    {
        "q": "10. Genetically engineered seeds can produce a much higher ________ per hectare than traditional varieties.",
        "opts": ["yield", "shortage", "drought", "pesticide"],
        "ans": 0,
        "exp": "<b>crop yield</b> (n): năng suất, sản lượng thu hoạch."
    },
    {
        "q": "11. Crop rotation and natural composting are key elements of ________ agriculture that protect nature.",
        "opts": ["sustainable", "infectious", "continuous", "juvenile"],
        "ans": 0,
        "exp": "<b>sustainable agriculture</b>: nền nông nghiệp bền vững."
    },
    {
        "q": "12. Biotechnologists can ________ the DNA of rice plants to make them resistant to pests and salty water.",
        "opts": ["modify", "cultivate", "harvest", "filter"],
        "ans": 0,
        "exp": "<b>modify</b> (v): biến đổi, chỉnh sửa gen."
    },
    {
        "q": "13. Planting cover crops during the winter prevents heavy rain from washing away fertile ________.",
        "opts": ["soil", "grid", "livestock", "famine"],
        "ans": 0,
        "exp": "<b>fertile soil</b> (n): lớp đất trồng màu mỡ."
    },
    {
        "q": "14. After three consecutive years without rainfall, the province suffered its worst ________ in a century.",
        "opts": ["drought", "harvest", "irrigation", "yield"],
        "ans": 0,
        "exp": "<b>prolonged / severe drought</b> (n): hạn hán kéo dài."
    },
    {
        "q": "15. Rising temperatures and crop failures could lead to an acute food ________ in many poor nations.",
        "opts": ["shortage", "fertilizer", "turbine", "vaccine"],
        "ans": 0,
        "exp": "<b>acute food shortage</b> (n): sự thiếu hụt lương thực trầm trọng."
    },
    {
        "q": "16. [Ôn tập Unit 17] In a geothermal plant, mechanical motion is ________ into electrical current by a generator.",
        "opts": ["converted", "cultivated", "harvested", "diagnosed"],
        "ans": 0,
        "exp": "<b>convert A into B</b> (Unit 17): chuyển đổi năng lượng."
    },
    {
        "q": "17. [Ôn tập Unit 17] Before being injected underground, cold water must ________ basic filtration.",
        "opts": ["undergo", "generate", "transmit", "distribute"],
        "ans": 0,
        "exp": "<b>undergo</b> (Unit 17): trải qua quá trình xử lý."
    },
    {
        "q": "18. [Ôn tập Unit 16] Taking antibiotics without a doctor's ________ can create drug-resistant bacteria.",
        "opts": ["prescription", "apparatus", "surveillance", "verdict"],
        "ans": 0,
        "exp": "<b>prescription</b> (Unit 16): đơn thuốc của bác sĩ."
    },
    {
        "q": "19. [Ôn tập Unit 15] Prisons should provide vocational training to ________ offenders and reduce repeat crime.",
        "opts": ["rehabilitate", "enforce", "extract", "cultivate"],
        "ans": 0,
        "exp": "<b>rehabilitate</b> (Unit 15): cải tạo, phục hồi cho người lầm lỗi."
    },
    {
        "q": "20. [Ôn tập Unit 13] Misleading advertisements often try to ________ consumers into buying unhealthy snacks.",
        "opts": ["manipulate", "generate", "filter", "immunize"],
        "ans": 0,
        "exp": "<b>manipulate</b> (Unit 13): thao túng, lôi kéo người tiêu dùng."
    }
]

GRAMMAR_QUESTIONS = [
    {
        "q": "1. Over the past three decades, the excessive use of chemical fertilizers ________ the quality of arable soil.",
        "opts": ["degrades", "degraded", "has degraded", "is degrading"],
        "ans": 2,
        "exp": "Cụm thời gian 'Over the past three decades' -> chia Hiện tại Hoàn thành: <b>has degraded</b>."
    },
    {
        "q": "2. Agricultural scientists ________ drought-tolerant crop varieties for years, and their trials are still ongoing.",
        "opts": ["developed", "have been developing", "are developed", "were developing"],
        "ans": 1,
        "exp": "Hành động kéo dài nhiều năm ('for years') và vẫn đang tiếp diễn ('still ongoing') -> HTHT Tiếp diễn: <b>have been developing</b>."
    },
    {
        "q": "3. Severe declines in wild honeybee populations largely stem ________ the widespread spraying of toxic pesticides.",
        "opts": ["to", "in", "from", "with"],
        "ans": 2,
        "exp": "Cấu trúc Nhân - Quả C1: <code>stem from + Nguyên nhân</code> (bắt nguồn từ...) -> <b>from</b>."
    },
    {
        "q": "4. Clearing forests to raise livestock contributes significantly ________ global greenhouse gas emissions.",
        "opts": ["from", "in", "to", "for"],
        "ans": 2,
        "exp": "Cấu trúc: <code>contribute (significantly) to + Noun / V-ing</code> (góp phần dẫn đến...) -> <b>to</b>."
    },
    {
        "q": "5. Prolonged droughts combined with poor irrigation have resulted ________ acute food shortages across the region.",
        "opts": ["in", "from", "to", "at"],
        "ans": 0,
        "exp": "Cấu trúc: <code>result in + Kết quả</code> (dẫn đến hậu quả là...) -> <b>in</b>."
    },
    {
        "q": "6. Since the Green Revolution began in the 1960s, global grain yields ________ more than threefold.",
        "opts": ["increased", "have increased", "have been increasing", "increase"],
        "ans": 1,
        "exp": "Mốc thời gian 'Since + QKĐ' và có con số kết quả định lượng ('more than threefold') -> Hiện tại Hoàn thành: <b>have increased</b>."
    },
    {
        "q": "7. Large herds of livestock ________ in cramped factory farms, which increases the risk of infectious diseases.",
        "opts": ["is raised", "are raised", "has raised", "have been raising"],
        "ans": 1,
        "exp": "Danh từ 'livestock' (gia súc) luôn mang nghĩa số nhiều -> Bị động Hiện tại đơn số nhiều: <b>are raised</b>."
    },
    {
        "q": "8. ________ genetically modified seeds can boost crop yields, critics worry about their long-term ecological impact.",
        "opts": ["Despite", "Although", "Because of", "However"],
        "ans": 1,
        "exp": "Đứng trước một mệnh đề đầy đủ (S + V) chỉ sự nhượng bộ -> dùng liên từ <b>Although</b>."
    },
    {
        "q": "9. Millions of tonnes of edible food ________ every year in wealthy nations while poorer countries face famine.",
        "opts": ["waste", "is wasted", "are wasted", "have wasted"],
        "ans": 2,
        "exp": "Chủ ngữ 'Millions of tonnes of...' là số nhiều chịu tác động -> Bị động số nhiều: <b>are wasted</b>."
    },
    {
        "q": "10. Switching to sustainable organic farming helps prevent fertile soil from ________ by heavy seasonal rains.",
        "opts": ["eroding", "being eroded", "eroded", "to erode"],
        "ans": 1,
        "exp": "Sau <code>prevent + O + from + V-ing</code>, có tác nhân bị động 'by heavy seasonal rains' -> dùng <b>being eroded</b>."
    }
]

DIALOGUE_LINES = [
    {
        "speaker": "Workshop Director",
        "text": "Good afternoon, GreenValley Sustainable Agriculture Centre, Arthur speaking. How can I help you?",
        "hint": ""
    },
    {
        "speaker": "Young Farmer",
        "text": "Hello Arthur! My name is Hannah Dawson. I recently inherited a vegetable farm and would like to register for your Organic Farming Workshop.",
        "hint": ""
    },
    {
        "speaker": "Workshop Director",
        "text": "Welcome, Hannah! Before I check availability, could you spell your surname for me?",
        "hint": ""
    },
    {
        "speaker": "Young Farmer",
        "text": "Sure, it is Dawson. D - A - W - S - O - N.",
        "hint": "💡 Đáp án câu 1 (Họ học viên): DAWSON"
    },
    {
        "speaker": "Workshop Director",
        "text": "Thank you. What is the main challenge you are facing on your farm right now?",
        "hint": ""
    },
    {
        "speaker": "Young Farmer",
        "text": "Years of chemical fertilizers have damaged my land, so my crop yields are falling.",
        "hint": ""
    },
    {
        "speaker": "Workshop Director",
        "text": "Then Saturday morning is ideal for you. Our first session focuses on Soil Restoration using natural compost instead of synthetic pesticides.",
        "hint": "💡 Đáp án câu 2 (Chủ đề sáng thứ Bảy): Soil"
    },
    {
        "speaker": "Young Farmer",
        "text": "That is exactly what I need! What about water management? We suffered a severe drought last summer.",
        "hint": ""
    },
    {
        "speaker": "Workshop Director",
        "text": "On Saturday afternoon, our engineers demonstrate how to install a drip irrigation system.",
        "hint": "💡 Đáp án câu 3 (Hệ thống tưới nhỏ giọt): irrigation"
    },
    {
        "speaker": "Young Farmer",
        "text": "How much water does that drip system save compared to traditional open canals?",
        "hint": ""
    },
    {
        "speaker": "Workshop Director",
        "text": "Traditional sprinklers save about 25%, but our drip irrigation system cuts water waste by 60%.",
        "hint": "💡 Bẫy % câu 4: 60"
    },
    {
        "speaker": "Young Farmer",
        "text": "Sixty percent savings would save my harvest! How much does the two-day workshop cost?",
        "hint": ""
    },
    {
        "speaker": "Workshop Director",
        "text": "The full registration fee is 115 pounds, which includes organic lunches and a starter pack of drought-tolerant seeds.",
        "hint": "💡 Đáp án câu 5 (Học phí): 115"
    },
    {
        "speaker": "Young Farmer",
        "text": "One hundred and fifteen pounds is great value. Where is your training farm located?",
        "hint": ""
    },
    {
        "speaker": "Workshop Director",
        "text": "We are located on Meadow Lane, just ten minutes north of the railway station. See you on Saturday!",
        "hint": "💡 Đáp án câu 6 (Tên đường): Meadow"
    }
]

LISTENING_QUESTIONS = [
    {
        "id": "l1",
        "label": "1. Participant's surname: Hannah",
        "placeholder": "Nhập tên riêng được đánh vần...",
        "answers": ["dawson"]
    },
    {
        "id": "l2",
        "label": "2. Saturday morning session topic: ________ Restoration (using natural compost)",
        "placeholder": "Nhập từ/cụm từ nghe được (1-2 từ)...",
        "answers": ["soil"]
    },
    {
        "id": "l3",
        "label": "3. Saturday afternoon practical demo: installing a drip ________ system",
        "placeholder": "Nhập từ/cụm từ nghe được (1-2 từ)...",
        "answers": ["irrigation"]
    },
    {
        "id": "l4",
        "label": "4. Percentage of water saved by the drip system: ________%",
        "placeholder": "Nhập con số / mốc thời gian nghe được...",
        "answers": ["60", "sixty"]
    },
    {
        "id": "l5",
        "label": "5. Total registration fee for the two-day workshop: £________",
        "placeholder": "Nhập con số / mốc thời gian nghe được...",
        "answers": ["115", "one hundred and fifteen"]
    },
    {
        "id": "l6",
        "label": "6. Location of the training farm: on ________ Lane",
        "placeholder": "Nhập từ/cụm từ nghe được (1-2 từ)...",
        "answers": ["meadow", "meadow lane"]
    }
]

READING_PASSAGE = {
    "title": "Feeding Ten Billion People: Organic Farming versus Genetic Engineering",
    "paragraphs": [
        {
            "label": "Paragraph A - The Ecological Cost of Intensive Chemical Agriculture",
            "content": "By 2050, the global population is projected to reach nearly ten billion, placing immense pressure on modern <b>agriculture</b>. Over the past half-century, the Green Revolution has prevented widespread <b>famine</b> by introducing high-<b>yield</b> crop varieties, mechanized <b>irrigation</b>, and chemical <b>fertilizers</b>. However, these intensive methods have come at a heavy ecological cost. Decades of spraying synthetic <b>pesticides</b> have degraded fertile <b>soil</b>, polluted rivers, and harmed beneficial insects, while intensive <b>livestock</b> farming has accelerated global warming."
        },
        {
            "label": "Paragraph B - The Benefits and Limitations of Organic Farming",
            "content": "In response to this crisis, many environmentalists advocate a transition towards <b>organic</b> and <b>sustainable</b> farming. <b>Organic</b> farmers <b>cultivate</b> crops without synthetic chemicals, using natural compost and crop rotation to maintain <b>soil</b> fertility. While <b>organic</b> methods protect biodiversity and produce chemical-free food, they suffer from a major limitation: on average, <b>organic</b> farms produce 25% lower <b>yields</b> per hectare. Relying solely on <b>organic</b> farming would require clearing more forests for farmland and could lead to acute food <b>shortages</b>."
        },
        {
            "label": "Paragraph C - Integrating Biotechnology and Sustainable Practices",
            "content": "Consequently, many agricultural scientists argue that biotechnology must be combined with eco-friendly farming. Through genetic engineering, researchers have been <b>modifying</b> the DNA of staple crops like rice and wheat to make them resilient to climate extremes. Newly developed <b>drought</b>-tolerant seeds allow farmers in arid regions to secure a reliable <b>harvest</b> during water <b>shortages</b>, while pest-resistant crops reduce the need for toxic <b>pesticides</b>."
        }
    ]
}

READING_QUESTIONS = [
    {
        "id": "r1",
        "label": "1. Why relying solely on organic farming could lead to lower yields and food shortages: (Paragraph A, B or C)",
        "placeholder": "Nhập chữ cái A, B hoặc C...",
        "answers": ["b", "paragraph b"]
    },
    {
        "id": "r2",
        "label": "2. How chemical fertilizers, pesticides and livestock farming have damaged the environment: (Paragraph A, B or C)",
        "placeholder": "Nhập chữ cái A, B hoặc C...",
        "answers": ["a", "paragraph a"]
    },
    {
        "id": "r3",
        "label": "3. How genetically modified seeds help farmers survive droughts and reduce pesticide use: (Paragraph A, B or C)",
        "placeholder": "Nhập chữ cái A, B hoặc C...",
        "answers": ["c", "paragraph c"]
    },
    {
        "id": "r4",
        "label": "4. What crisis did the Green Revolution successfully prevent over the past half-century? Widespread ________. (ONE WORD from Para A)",
        "placeholder": "Nhập từ/cụm từ trích từ đoạn A...",
        "answers": ["famine"]
    },
    {
        "id": "r5",
        "label": "5. On average, organic farms produce 25% lower ________ per hectare than conventional farms. (ONE WORD from Para B)",
        "placeholder": "Nhập từ/cụm từ trích từ đoạn B...",
        "answers": ["yields", "yield"]
    },
    {
        "id": "r6",
        "label": "6. What type of newly developed seeds allow farmers in arid regions to secure a reliable harvest? ________-tolerant seeds. (ONE WORD from Para C)",
        "placeholder": "Nhập từ/cụm từ trích từ đoạn C...",
        "answers": ["drought"]
    }
]

WRITING_TASK = {
    "topic": "✍️ Academic Writing Lab (Task 2 Discussion): Nông Nghiệp Thâm Canh Hóa Chất & Biến Đổi Gen vs. Nông Nghiệp Hữu Cơ Bền Vững",
    "prompt": "Some people argue that modern intensive agriculture using chemical fertilizers, pesticides, and genetically modified crops is the only way to prevent global food shortages. Others believe that we must switch to organic and sustainable farming to protect the environment. Discuss both views and give your opinion (90 - 120 words).",
    "criteria": "Tiêu chuẩn: Sử dụng thì Hiện tại Hoàn thành (have doubled / have degraded / have been modifying), cụm động từ Nhân - Quả (result in / lead to / contribute to) và ít nhất 6 từ vựng Unit 18.",
    "target_words": 100,
    "unit_vocab": ["agriculture", "cultivate", "harvest", "irrigation", "fertilizer", "pesticide", "organic", "livestock", "famine", "yield", "sustainable", "modify", "soil", "drought", "shortage"],
    "model_essay": "While some people maintain that chemical-intensive agriculture is indispensable for preventing global food shortages, others advocate a transition towards organic and sustainable farming. On the one hand, modern agricultural technologies have doubled crop yields over the past fifty years and prevented widespread famine. Furthermore, scientists have been modifying plant genetics to create drought-tolerant seeds, allowing farmers to secure a reliable harvest during severe water shortages. On the other hand, the excessive use of chemical fertilizers and toxic pesticides has degraded fertile soil and polluted rivers, while intensive livestock farming contributes significantly to global warming. In conclusion, I believe governments should combine organic soil management and smart drip irrigation with safe, climate-resilient seeds to ensure both food security and environmental protection.",
    "model_analysis": [
        "<b>Câu 1 (Topic Sentence nêu 2 luồng quan điểm đối lập):</b> <code>While some people maintain that chemical-intensive agriculture is indispensable for preventing global food shortages, others advocate...</code>",
        "<b>Câu 2 & 3 (Vế 1 — Hiện tại Hoàn thành & HTHT Tiếp diễn):</b> <code>have doubled crop yields... and prevented widespread famine</code> + <code>scientists have been modifying plant genetics to create drought-tolerant seeds...</code>",
        "<b>Câu 4 & 5 (Vế 2 + Kết luận dung hòa với Cụm động từ Nhân - Quả):</b> <code>has degraded fertile soil</code> + <code>contributes significantly to global warming</code>, chốt lại giải pháp kết hợp bền vững."
    ],
    "model_translation": "Trong khi một số người cho rằng nông nghiệp thâm canh sử dụng hóa chất là không thể thiếu để ngăn chặn tình trạng thiếu hụt lương thực toàn cầu, những người khác lại ủng hộ việc chuyển dịch sang canh tác hữu cơ và bền vững. Một mặt, các công nghệ nông nghiệp hiện đại đã làm tăng gấp đôi năng suất cây trồng trong 50 năm qua và ngăn chặn nạn đói diện rộng. Hơn nữa, các nhà khoa học đã và đang biến đổi di truyền thực vật để tạo ra các hạt giống chịu hạn, cho phép nông dân đảm bảo vụ mùa thu hoạch ổn định trong những đợt thiếu nước gay gắt. Mặt khác, việc lạm dụng phân bón hóa học và thuốc trừ sâu độc hại đã làm suy thoái đất trồng màu mỡ và gây ô nhiễm sông ngòi, trong khi chăn nuôi gia súc thâm canh góp phần đáng kể vào sự nóng lên toàn cầu. Tóm lại, tôi tin rằng chính phủ nên kết hợp quản lý đất hữu cơ và tưới nhỏ giọt thông minh với các giống cây trồng thích ứng khí hậu an toàn để đảm bảo cả an ninh lương thực lẫn bảo vệ môi trường."
}

SPEAKING_TASK = {
    "title": "🗣️ Speaking Lab: Phỏng Vấn Chủ Đề Thực Phẩm Hữu Cơ, Nông Nghiệp & Biến Đổi Khí Hậu",
    "questions": [
        {
            "id": "q1",
            "text": "Q1: Do you prefer buying organic fruit and vegetables, or regular produce at the market?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Nêu sở thích ưu tiên thực phẩm hữu cơ (certified organic vegetables) + Giải thích lý do lo ngại dư lượng thuốc trừ sâu (pesticide residues & chemical fertilizers).",
            "sample_answer": "Whenever my budget allows, I definitely prefer buying certified organic vegetables from reputable supermarkets. Many consumers in my country are deeply concerned about harmful pesticide residues and chemical fertilizers used in conventional agriculture, so buying organic produce helps protect my family's health.",
            "sample_audio_key": "speaking_q1"
        },
        {
            "id": "q2",
            "text": "Q2: What is the most important agricultural crop cultivated in your country?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Chọn lúa nước (wet rice in the Mekong Delta) + Mô tả điều kiện fertile soil, irrigation canals và cách nông dân ứng phó với prolonged droughts.",
            "sample_answer": "Wet rice is by far the most vital crop cultivated in Vietnam, especially in the Mekong River Delta. Thanks to fertile alluvial soil and an extensive network of irrigation canals, farmers can harvest up to three rice crops a year, which guarantees national food security and prevents food shortages.",
            "sample_audio_key": "speaking_q2"
        },
        {
            "id": "q3",
            "text": "Q3: How can governments help farmers adapt to climate change and prevent future food shortages?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Nêu 2 chính sách: Trợ giá hệ thống tưới nhỏ giọt (subsidize drip irrigation systems) chống drought + Đầu tư nghiên cứu giống cây chịu hạn và canh tác sustainable.",
            "sample_answer": "In my opinion, governments must take two proactive measures to safeguard agriculture against climate change. Firstly, they should subsidize modern drip irrigation systems so farmers can conserve water during severe droughts. Secondly, authorities need to fund research into drought-tolerant seeds and sustainable soil management to maintain high crop yields.",
            "sample_audio_key": "speaking_q3"
        }
    ],
    "targeted_sounds": [
        {"word": "agriculture", "sound": "/ˈæɡrɪkʌltʃə(r)/", "note": "Nhấn âm đầu AG- (/ˈæɡrɪkʌltʃə/)"},
        {"word": "irrigation", "sound": "/ˌɪrɪˈɡeɪʃn/", "note": "Nhấn âm tiết thứ 3: -GAI- (/ˌɪrɪˈɡeɪʃn/)"},
        {"word": "pesticide", "sound": "/ˈpestɪsaɪd/", "note": "Nhấn âm đầu PES-, âm cuối /-saɪd/"},
        {"word": "sustainable", "sound": "/səˈsteɪnəbl/", "note": "Nhấn âm tiết thứ 2: -STAIN- (/səˈsteɪnəbl/)"},
        {"word": "drought", "sound": "/draʊt/", "note": "Nguyên âm đôi /aʊ/, kết thúc bằng âm /t/ (/draʊt/)"}
    ],
    "lexical_words": ["agriculture", "cultivate", "harvest", "irrigation", "fertilizer", "pesticide", "organic", "livestock", "famine", "yield", "sustainable", "modify", "soil", "drought", "shortage"]
}
