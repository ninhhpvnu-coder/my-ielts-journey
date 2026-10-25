# -*- coding: utf-8 -*-
"""
Unit 15 Data Definition - IELTS Foundation Stage 3 Milestone (Band 4.5 - 5.0)
Topic: Law, Crime Prevention, Justice & Social Order
"""

UNIT_CONFIG = {
    "unit_id": "15",
    "unit_num": 15,
    "title": "Unit 15: Law, Crime Prevention, Justice & Social Order",
    "badge": "My IELTS journey",
    "audio_dir": "audio/unit15",
    "reading_title": "Punishment versus Rehabilitation: What Is the Best Way to Prevent Crime?",
    "reading_word_count": "~375 words • IELTS Foundation Stage 3 Milestone Review",
}

VOCAB_LIST = [
    {
        "word": "legislation",
        "pos": "n",
        "ipa": "/ˌledʒɪsˈleɪʃn/",
        "meaning": "luật pháp, hệ thống đạo luật do quốc hội/chính phủ ban hành (không đếm được)",
        "colloc": "introduce new legislation, strict legislation",
        "example": "The government introduced strict legislation to protect citizens from online fraud."
    },
    {
        "word": "offense",
        "pos": "n",
        "ipa": "/əˈfens/",
        "meaning": "hành vi phạm pháp, tội danh (từ học thuật thay cho crime)",
        "colloc": "commit an offense, minor offense, serious offense",
        "example": "Driving without a valid license is a serious traffic offense in every country."
    },
    {
        "word": "deterrent",
        "pos": "n",
        "ipa": "/dɪˈterənt/",
        "meaning": "biện pháp răn đe, ngăn chặn hành vi phạm tội trước khi nó xảy ra",
        "colloc": "act as a deterrent, effective deterrent against crime",
        "example": "Heavy fines act as a strong deterrent against illegal littering and pollution."
    },
    {
        "word": "rehabilitate",
        "pos": "v",
        "ipa": "/ˌriːəˈbɪlɪteɪt/",
        "meaning": "cải tạo, giáo dục phục hồi để người lầm lỗi tái hòa nhập xã hội (n: rehabilitation)",
        "colloc": "rehabilitate prisoners, vocational rehabilitation",
        "example": "Prisons should focus on educating and rehabilitating offenders rather than merely punishing them."
    },
    {
        "word": "offender",
        "pos": "n",
        "ipa": "/əˈfendə(r)/",
        "meaning": "người phạm pháp, kẻ vi phạm pháp luật",
        "colloc": "first-time offender, repeat offender, young offender",
        "example": "Community service is often more suitable than prison for a first-time offender."
    },
    {
        "word": "juvenile",
        "pos": "adj/n",
        "ipa": "/ˈdʒuːvənaɪl/",
        "meaning": "thuộc về vị thành niên (dưới 18 tuổi)",
        "colloc": "juvenile crime, juvenile delinquency",
        "example": "Supportive family upbringing and after-school sports help reduce juvenile delinquency."
    },
    {
        "word": "surveillance",
        "pos": "n",
        "ipa": "/sɜːˈveɪləns/",
        "meaning": "sự giám sát an ninh (đặc biệt qua hệ thống camera công cộng)",
        "colloc": "video surveillance, surveillance camera, under surveillance",
        "example": "Installing street lighting and surveillance cameras makes city parks much safer at night."
    },
    {
        "word": "penalty",
        "pos": "n",
        "ipa": "/ˈpenəlti/",
        "meaning": "hình phạt, mức phạt theo quy định pháp luật",
        "colloc": "severe penalty, financial penalty, impose a penalty",
        "example": "Corporations that dump toxic waste into rivers must face severe financial penalties."
    },
    {
        "word": "enforce",
        "pos": "v",
        "ipa": "/ɪnˈfɔːs/",
        "meaning": "thực thi, cưỡng chế chấp hành luật pháp (n: law enforcement)",
        "colloc": "enforce the law, strictly enforce regulations",
        "example": "Traffic police use speed cameras to enforce road safety laws on highways."
    },
    {
        "word": "cybercrime",
        "pos": "n",
        "ipa": "/ˈsaɪbəkraɪm/",
        "meaning": "tội phạm mạng (lừa đảo trực tuyến, đánh cắp dữ liệu, tấn công mạng)",
        "colloc": "combat cybercrime, rise in cybercrime",
        "example": "As digital banking grows, police departments need technical experts to combat cybercrime."
    },
    {
        "word": "victim",
        "pos": "n",
        "ipa": "/ˈvɪktɪm/",
        "meaning": "nạn nhân (của tội phạm, tai nạn hoặc lừa đảo)",
        "colloc": "innocent victim, fall victim to",
        "example": "Elderly people who are unfamiliar with the internet sometimes fall victim to phone scams."
    },
    {
        "word": "verdict",
        "pos": "n",
        "ipa": "/ˈvɜːdɪkt/",
        "meaning": "phán quyết của tòa án hoặc bồi thẩm đoàn",
        "colloc": "reach a verdict, guilty verdict",
        "example": "After examining all the evidence carefully, the court reached a fair verdict."
    },
    {
        "word": "prevent",
        "pos": "v",
        "ipa": "/prɪˈvent/",
        "meaning": "ngăn ngừa, phòng chống (prevent sb/sth from V-ing)",
        "colloc": "prevent crime, crime prevention",
        "example": "Providing equal job opportunities is the most sustainable way to prevent crime."
    },
    {
        "word": "poverty",
        "pos": "n",
        "ipa": "/ˈpɒvəti/",
        "meaning": "sự nghèo đói, thiếu thốn kinh tế",
        "colloc": "reduce poverty, live in poverty",
        "example": "Sociologists point out that unemployment and poverty are major root causes of street crime."
    },
    {
        "word": "justice",
        "pos": "n",
        "ipa": "/ˈdʒʌstɪs/",
        "meaning": "công lý, sự công bằng của pháp luật; hệ thống tư pháp",
        "colloc": "criminal justice system, social justice, law-abiding citizen",
        "example": "A fair justice system protects law-abiding citizens and upholds human rights."
    }
]

GRAMMAR_THEORY = {
    "tier1": {
        "title": "🟢 Tầng 1: Cấu Trúc Mục Đích Học Thuật (So That / In Order To) & Prevent ... From V-ing",
        "content": [
            "• <b><code>in order to / so as to + V (nguyên mẫu)</code>:</b> Diễn tả mục đích của chính phủ/pháp luật một cách trang trọng.<br>&nbsp;&nbsp;<i>Ví dụ:</i> Governments install public surveillance cameras <b>in order to deter</b> potential offenders.",
            "• <b><code>so that / in order that + S + can/will/would + V</code>:</b> Nối mệnh đề mục đích.<br>&nbsp;&nbsp;<i>Ví dụ:</i> Prisons should provide vocational training <b>so that</b> former offenders <b>can find</b> honest employment.",
            "• <b><code>prevent / deter + Object + from + V-ing</code>:</b> Ngăn chặn ai làm điều gì.<br>&nbsp;&nbsp;<i>Ví dụ:</i> Strict penalties <b>prevent corporations from polluting</b> the environment."
        ]
    },
    "tier2": {
        "title": "🔵 Tầng 2: Trạng Từ Kết Quả 'Thereby + V-ing' & Bị Động Với Động Từ Khuyết Thiếu",
        "content": [
            "• <b>Cấu trúc <code>, thereby + V-ing</code> (Qua đó / Nhờ đó dẫn đến kết quả là... — Cấu trúc C1 đắt giá cho Task 2):</b><br>&nbsp;&nbsp;<i>Ví dụ:</i> Schools should teach cybersecurity awareness, <b>thereby protecting</b> students from becoming victims of cybercrime.",
            "• <b>Bị động với Modal Verbs trong Luật pháp:</b> <code>must / should / ought to + be + V3/ed</code><br>&nbsp;&nbsp;<i>Ví dụ:</i> Traffic legislation <b>must be strictly enforced</b> to ensure public safety."
        ]
    }
}

VOCAB_QUESTIONS = [
    {
        "q": "1. Parliament passed new environmental ________ to ban single-use toxic chemicals.",
        "opts": ["legislation", "offender", "victim", "verdict"],
        "ans": 0,
        "exp": "<b>legislation</b> (n - không đếm được): luật pháp, đạo luật."
    },
    {
        "q": "2. Driving under the influence of alcohol is a serious ________ that endangers innocent lives.",
        "opts": ["offense", "deterrent", "justice", "poverty"],
        "ans": 0,
        "exp": "<b>commit a serious offense</b>: phạm một tội nghiêm trọng."
    },
    {
        "q": "3. Visible police patrols on city streets act as a powerful ________ against robbery.",
        "opts": ["deterrent", "verdict", "victim", "offender"],
        "ans": 0,
        "exp": "<b>act as a deterrent against</b>: đóng vai trò là biện pháp răn đe chống lại..."
    },
    {
        "q": "4. Vocational classes in prison help ________ inmates so they can work legally after release.",
        "opts": ["rehabilitate", "enforce", "plummet", "manipulate"],
        "ans": 0,
        "exp": "<b>rehabilitate</b> (v): cải tạo, phục hồi nhân phẩm và kỹ năng."
    },
    {
        "q": "5. A first-time ________ who commits a minor shoplifting crime may be given community service.",
        "opts": ["offender", "victim", "legislation", "surveillance"],
        "ans": 0,
        "exp": "<b>first-time offender</b>: người phạm lỗi lần đầu."
    },
    {
        "q": "6. Youth clubs and free sports facilities play a vital role in reducing ________ delinquency.",
        "opts": ["juvenile", "affordable", "dramatic", "nuclear"],
        "ans": 0,
        "exp": "<b>juvenile delinquency / crime</b>: tội phạm vị thành niên."
    },
    {
        "q": "7. High-definition ________ cameras at banks and train stations help police identify suspects quickly.",
        "opts": ["surveillance", "poverty", "verdict", "warranty"],
        "ans": 0,
        "exp": "<b>surveillance cameras</b>: camera giám sát an ninh."
    },
    {
        "q": "8. The maximum ________ for hacking into government databases is ten years in prison.",
        "opts": ["penalty", "deterrent", "victim", "revenue"],
        "ans": 0,
        "exp": "<b>penalty</b> (n): hình phạt, mức phạt."
    },
    {
        "q": "9. Passing good laws is useless unless the police have enough resources to ________ them fairly.",
        "opts": ["enforce", "rehabilitate", "boycott", "fluctuate"],
        "ans": 0,
        "exp": "<b>enforce the law</b>: thực thi pháp luật."
    },
    {
        "q": "10. Phishing emails and online identity theft are common forms of modern ________.",
        "opts": ["cybercrime", "surveillance", "legislation", "Burnout"],
        "ans": 0,
        "exp": "<b>cybercrime</b> (n): tội phạm mạng."
    },
    {
        "q": "11. The charity provides free legal advice and counseling to any ________ of domestic violence.",
        "opts": ["victim", "offender", "competitor", "candidate"],
        "ans": 0,
        "exp": "<b>victim</b> (n): nạn nhân."
    },
    {
        "q": "12. After three days of deliberation, the jury returned a 'not guilty' ________.",
        "opts": ["verdict", "penalty", "offense", "deterrent"],
        "ans": 0,
        "exp": "<b>reach / return a verdict</b>: đưa ra phán quyết của tòa."
    },
    {
        "q": "13. Educating citizens about strong passwords can ________ hackers from stealing bank accounts.",
        "opts": ["prevent", "enforce", "endorse", "surpass"],
        "ans": 0,
        "exp": "<b>prevent sb from V-ing</b>: ngăn chặn ai làm gì."
    },
    {
        "q": "14. Investing in public education and job creation helps lift disadvantaged families out of ________.",
        "opts": ["poverty", "surveillance", "justice", "loyalty"],
        "ans": 0,
        "exp": "<b>lift out of poverty</b>: thoát khỏi cảnh nghèo đói."
    },
    {
        "q": "15. Every citizen deserves equal treatment under the criminal ________ system, regardless of wealth.",
        "opts": ["justice", "impulse", "inflation", "preference"],
        "ans": 0,
        "exp": "<b>criminal justice system</b>: hệ thống tư pháp hình sự."
    },
    {
        "q": "16. [Ôn tập Unit 14] Two-factor authentication protects every online banking ________ from cybercrime.",
        "opts": ["transaction", "storefront", "demographic", "upbringing"],
        "ans": 0,
        "exp": "<b>transaction</b> (Unit 14): giao dịch."
    },
    {
        "q": "17. [Ôn tập Unit 13] Consumer protection laws ban false commercials that try to ________ buyers.",
        "opts": ["manipulate", "rehabilitate", "stabilize", "commute"],
        "ans": 0,
        "exp": "<b>manipulate</b> (Unit 13): thao túng, lừa dối."
    },
    {
        "q": "18. [Ôn tập Unit 12] Government ________ on public education and policing increased by 12% this year.",
        "opts": ["expenditure", "burnout", "adolescence", "celebrity"],
        "ans": 0,
        "exp": "<b>government expenditure</b> (Unit 12): chi tiêu ngân sách chính phủ."
    },
    {
        "q": "19. [Ôn tập Unit 11] Prisoners who gain a vocational ________ have a much better chance of finding a job.",
        "opts": ["qualification", "proportion", "commercial", "sibling"],
        "ans": 0,
        "exp": "<b>qualification</b> (Unit 11): bằng cấp, chứng chỉ nghề."
    },
    {
        "q": "20. [Ôn tập Unit 6] Parents have a legal and moral ________ to guide their children during adolescence.",
        "opts": ["responsibility", "remuneration", "warranty", "itinerary"],
        "ans": 0,
        "exp": "<b>responsibility</b> (Unit 6): trách nhiệm."
    }
]

GRAMMAR_QUESTIONS = [
    {
        "q": "1. Strict cybersecurity legislation must ________ to protect citizens from online scams.",
        "opts": ["enforce", "be enforced", "enforcing", "enforced"],
        "ans": 1,
        "exp": "Bị động với động từ khuyết thiếu: <code>must + be + V3/ed (be enforced)</code>."
    },
    {
        "q": "2. High-definition surveillance cameras are installed in city centres in order ________ street crime.",
        "opts": ["deter", "to deter", "deterring", "deterred"],
        "ans": 1,
        "exp": "Cấu trúc chỉ mục đích <code>in order to + V (nguyên mẫu)</code> -> <b>to deter</b>."
    },
    {
        "q": "3. Heavy financial penalties prevent industrial corporations from ________ toxic waste into rivers.",
        "opts": ["dump", "to dump", "dumping", "dumped"],
        "ans": 2,
        "exp": "Cấu trúc <code>prevent + Object + from + V-ing</code> -> <b>dumping</b>."
    },
    {
        "q": "4. Prisons provide vocational training courses ________ former offenders can earn an honest living.",
        "opts": ["so that", "in order to", "because of", "despite"],
        "ans": 0,
        "exp": "Theo sau là một mệnh đề đầy đủ ('former offenders can earn...') chỉ mục đích -> dùng <b>so that</b>."
    },
    {
        "q": "5. Governments should invest in youth sports centres, thereby ________ juvenile delinquency.",
        "opts": ["reduce", "to reduce", "reducing", "reduced"],
        "ans": 2,
        "exp": "Cấu trúc trạng từ kết quả C1: <code>, thereby + V-ing</code> (qua đó làm giảm...) -> <b>reducing</b>."
    },
    {
        "q": "6. Note that " + "legislation" + " is an uncountable noun: New legislation ________ passed last month to combat cybercrime.",
        "opts": ["was", "were", "have been", "are"],
        "ans": 0,
        "exp": "Danh từ không đếm được 'legislation' chia động từ số ít ở quá khứ ('last month') -> <b>was</b>."
    },
    {
        "q": "7. First-time juvenile offenders ought to ________ through education rather than sent to adult prisons.",
        "opts": ["rehabilitate", "be rehabilitated", "rehabilitating", "rehabilitated"],
        "ans": 1,
        "exp": "Cấu trúc bị động với <code>ought to + be + V3/ed</code> -> <b>be rehabilitated</b>."
    },
    {
        "q": "8. If poverty and unemployment ________ reduced, the overall crime rate would fall dramatically.",
        "opts": ["are", "were", "will be", "have been"],
        "ans": 1,
        "exp": "Ôn tập Câu điều kiện loại 2 (Unit 13): Mệnh đề chính có 'would fall' -> mệnh đề If dùng <b>were</b>."
    },
    {
        "q": "9. Offenders ________ commit violent crimes must face severe penalties to protect law-abiding citizens.",
        "opts": ["who", "which", "whose", "where"],
        "ans": 0,
        "exp": "Ôn tập MĐQH (Unit 11): Thay cho danh từ chỉ người 'Offenders' làm chủ ngữ -> <b>who</b>."
    },
    {
        "q": "10. Between 2015 and 2025, reported cases of online fraud surged ________ 45%, whereas street robbery declined.",
        "opts": ["by", "at", "of", "between"],
        "ans": 0,
        "exp": "Ôn tập giới từ số liệu Task 1 (Unit 12): Tăng thêm một khoảng bao nhiêu % -> <code>surged by 45%</code>."
    }
]

DIALOGUE_LINES = [
    {
        "speaker": "Police Officer",
        "text": "Good afternoon! Welcome to the Campus Safety and Cybercrime Prevention Workshop.",
        "hint": ""
    },
    {
        "speaker": "Student Coordinator",
        "text": "Good afternoon, Officer! Thank you for visiting our university to speak with our first-year students.",
        "hint": ""
    },
    {
        "speaker": "Police Officer",
        "text": "My pleasure. Before we begin, could I confirm your surname for our community policing report? Is it Graham?",
        "hint": ""
    },
    {
        "speaker": "Student Coordinator",
        "text": "Actually, it is spelled Davidson. D - A - V - I - D - S - O - N.",
        "hint": "💡 Đáp án câu 1 (Đánh vần họ): DAVIDSON"
    },
    {
        "speaker": "Police Officer",
        "text": "Thank you, Mr. Davidson. How many students have registered to attend today's safety seminar?",
        "hint": ""
    },
    {
        "speaker": "Student Coordinator",
        "text": "We initially expected 120, but 165 students have signed up.",
        "hint": "💡 Bẫy số dự kiến vs thực tế câu 2: 165"
    },
    {
        "speaker": "Police Officer",
        "text": "That is wonderful. What is the most common offense affecting university students on campus recently?",
        "hint": ""
    },
    {
        "speaker": "Student Coordinator",
        "text": "Bicycle theft used to be the main issue, but this year online banking fraud has become the biggest problem.",
        "hint": "💡 Bẫy quá khứ vs hiện tại câu 3: online banking fraud / fraud"
    },
    {
        "speaker": "Police Officer",
        "text": "Yes, cybercrime is rising nationwide. Criminals send fake scholarship emails to trick students into sharing passwords.",
        "hint": "💡 Đáp án câu 4: scholarship"
    },
    {
        "speaker": "Student Coordinator",
        "text": "Have the university authorities improved physical security around the dormitories as well?",
        "hint": ""
    },
    {
        "speaker": "Police Officer",
        "text": "Yes, twenty-four new surveillance cameras have been installed along the main campus pathways.",
        "hint": "💡 Đáp án câu 5: surveillance cameras"
    },
    {
        "speaker": "Student Coordinator",
        "text": "That will certainly act as a strong deterrent. Where should a student go if they fall victim to a scam?",
        "hint": ""
    },
    {
        "speaker": "Police Officer",
        "text": "They should report it immediately to the Campus Security Desk in the Student Union Building.",
        "hint": "💡 Đáp án câu 6: Student Union"
    },
    {
        "speaker": "Student Coordinator",
        "text": "Is there a direct emergency hotline number we can print on our student handbooks?",
        "hint": ""
    },
    {
        "speaker": "Police Officer",
        "text": "Yes, students can call our 24-hour helpline free of charge. Let's head into the lecture hall now!",
        "hint": ""
    }
]

LISTENING_QUESTIONS = [
    {
        "id": "l1",
        "label": "1. Coordinator's surname: Mr.",
        "placeholder": "Điền họ đánh vần (Davidson)",
        "answers": ["davidson"]
    },
    {
        "id": "l2",
        "label": "2. Actual number of students registered for the workshop:",
        "placeholder": "Số sinh viên đăng ký thực tế (165)",
        "answers": ["165"]
    },
    {
        "id": "l3",
        "label": "3. Most common offense affecting students this year: online banking ________",
        "placeholder": "Loại tội phạm phổ biến nhất năm nay (fraud)",
        "answers": ["fraud", "online banking fraud", "scams"]
    },
    {
        "id": "l4",
        "label": "4. Fake emails sent by criminals pretend to offer a university ________",
        "placeholder": "Mồi nhử trong email giả (scholarship)",
        "answers": ["scholarship"]
    },
    {
        "id": "l5",
        "label": "5. New security equipment installed along pathways: 24 new ________ cameras",
        "placeholder": "Thiết bị an ninh (surveillance)",
        "answers": ["surveillance", "surveillance cameras"]
    },
    {
        "id": "l6",
        "label": "6. Location of the Campus Security Desk: the ________ Building",
        "placeholder": "Tên tòa nhà (Student Union)",
        "answers": ["student union", "union"]
    }
]

READING_PASSAGE = {
    "title": "Punishment versus Rehabilitation: What Is the Best Way to Prevent Crime?",
    "paragraphs": [
        {
            "label": "Paragraph A - The Role of Strict Legislation and Deterrence",
            "content": "For centuries, governments have debated the most effective way to maintain social order and uphold <b>justice</b>. Traditionalists argue that strict <b>legislation</b> and severe prison <b>penalties</b> are essential because they act as a powerful <b>deterrent</b>. When potential criminals know that the police will strictly <b>enforce</b> the law and that courts will deliver a tough <b>verdict</b>, they are less likely to commit a serious <b>offense</b>. In addition, installing public <b>surveillance</b> cameras helps protect innocent <b>victims</b> in urban areas."
        },
        {
            "label": "Paragraph B - Addressing Root Causes and Rehabilitating Offenders",
            "content": "However, criminologists point out that long prison sentences alone do not solve the root causes of crime, such as <b>poverty</b>, unemployment, and lack of education. If a first-time or <b>juvenile</b> <b>offender</b> is locked up with hardened criminals without any support, they often reoffend after leaving prison. Therefore, modern justice systems invest heavily in programs designed to <b>rehabilitate</b> prisoners through vocational training, psychological counseling, and literacy classes."
        },
        {
            "label": "Paragraph C - Preventing Modern Cybercrime",
            "content": "In the twenty-first century, law enforcement also faces the rapid rise of <b>cybercrime</b>, including online banking fraud and identity theft. To <b>prevent</b> these digital offenses, governments must combine international police cooperation with public education, thereby empowering citizens to protect their personal data online."
        }
    ]
}

READING_QUESTIONS = [
    {
        "id": "r1",
        "label": "1. Why vocational training and addressing poverty are necessary to stop repeat crime: (Paragraph A, B or C)",
        "placeholder": "Nhập A, B hoặc C",
        "answers": ["b", "paragraph b"]
    },
    {
        "id": "r2",
        "label": "2. How strict penalties and surveillance cameras act as a deterrent: (Paragraph A, B or C)",
        "placeholder": "Nhập A, B hoặc C",
        "answers": ["a", "paragraph a"]
    },
    {
        "id": "r3",
        "label": "3. The modern challenge of digital fraud and identity theft: (Paragraph A, B or C)",
        "placeholder": "Nhập A, B hoặc C",
        "answers": ["c", "paragraph c"]
    },
    {
        "id": "r4",
        "label": "4. What do strict legislation and severe penalties act as? A powerful ________. (ONE WORD)",
        "placeholder": "Điền 1 từ trong đoạn A (deterrent)",
        "answers": ["deterrent"]
    },
    {
        "id": "r5",
        "label": "5. Besides unemployment and lack of education, what is named as a root cause of crime? (ONE WORD)",
        "placeholder": "Điền 1 từ trong đoạn B (poverty)",
        "answers": ["poverty"]
    },
    {
        "id": "r6",
        "label": "6. What type of training helps rehabilitate prisoners in Paragraph B? ________ training. (ONE WORD)",
        "placeholder": "Điền 1 từ trong đoạn B (vocational)",
        "answers": ["vocational"]
    }
]

WRITING_TASK = {
    "topic": "✍️ Academic Writing Lab (Task 2 Discussion — Tổng Duyệt Chặng 3): Hình Phạt Tù Nghiêm Khắc vs. Giáo Dục Cải Tạo Tội Phạm",
    "prompt": "Some people think that the best way to reduce crime is to give longer prison sentences. Others, however, believe there are better alternative ways of reducing crime. Write a paragraph (75 - 95 words) discussing both views and giving your opinion.",
    "criteria": "Tiêu chuẩn: Sử dụng cấu trúc mục đích/kết quả (in order to / so that / , thereby + V-ing), bị động với Modal Verb (must be enforced / should be rehabilitated) và ít nhất 5 từ vựng Unit 15 (legislation, deterrent, penalty, rehabilitate, offender, prevent, poverty, justice).",
    "target_words": 85,
    "unit_vocab": ["legislation", "offense", "deterrent", "rehabilitate", "offender", "juvenile", "surveillance", "penalty", "enforce", "cybercrime", "victim", "verdict", "prevent", "poverty", "justice"],
    "model_essay": "While severe prison penalties play an important role in maintaining justice, I believe that education and social reform are far more effective in preventing crime in the long run. On the one hand, strict legislation must be enforced so that heavy sentences act as a strong deterrent for violent offenders and protect innocent victims. On the other hand, long imprisonment alone does not address the root causes of crime, such as poverty and unemployment. Therefore, governments should provide vocational training to rehabilitate juvenile and first-time offenders, thereby helping them become law-abiding citizens.",
    "model_analysis": [
        "<b>Câu 1 (Topic Sentence nêu rõ quan điểm cả 2 chiều):</b> Mở đầu bằng <code>While severe prison penalties play an important role in maintaining justice, I believe that...</code>",
        "<b>Câu 2 (Lập luận vế 1 với Bị động Modal + Mệnh đề mục đích 'so that'):</b> <code>strict legislation must be enforced so that heavy sentences act as a strong deterrent...</code>",
        "<b>Câu 3 & 4 (Lập luận vế 2 + Cấu trúc C1 ', thereby + V-ing'):</b> Phân tích nguyên nhân gốc rễ (<code>poverty and unemployment</code>) và chốt bằng <code>rehabilitate juvenile and first-time offenders, thereby helping them become law-abiding citizens</code>."
    ],
    "model_translation": "Mặc dù các hình phạt tù nghiêm khắc đóng vai trò quan trọng trong việc duy trì công lý, tôi tin rằng giáo dục và cải cách xã hội hiệu quả hơn nhiều trong việc ngăn ngừa tội phạm về lâu dài. Một mặt, luật pháp nghiêm minh cần phải được thực thi để những bản án nặng đóng vai trò như một biện pháp răn đe mạnh mẽ đối với những kẻ phạm tội bạo lực và bảo vệ các nạn nhân vô tội. Mặt khác, việc giam giữ lâu dài đơn thuần không giải quyết được những nguyên nhân gốc rễ của tội phạm như sự nghèo đói và thất nghiệp. Do đó, chính phủ nên cung cấp đào tạo nghề để cải tạo những người phạm pháp vị thành niên và vi phạm lần đầu, qua đó giúp họ trở thành những công dân thượng tôn pháp luật."
}

SPEAKING_TASK = {
    "title": "🗣️ Speaking Lab: Phỏng Vấn Chủ Đề Pháp Luật, An Toàn Đô Thị & Phòng Chống Tội Phạm Mạng",
    "questions": [
        {
            "id": "q1",
            "text": "Q1: Do you think installing surveillance cameras in public places is a good idea?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Đồng tình + Giải thích vai trò của surveillance cameras như một effective deterrent giúp prevent crime và bảo vệ innocent victims vào ban đêm.",
            "sample_answer": "Yes, I strongly believe that installing surveillance cameras in public parks and train stations is beneficial. They act as an effective deterrent against street crime and help the police identify offenders quickly to protect innocent victims.",
            "sample_audio_key": "speaking_q1"
        },
        {
            "id": "q2",
            "text": "Q2: Should prisons focus more on punishing or rehabilitating offenders?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Đưa ra góc nhìn cân bằng + Giải thích vì sao việc rehabilitate first-time offenders bằng đào tạo nghề (vocational qualifications) giúp giảm tái phạm.",
            "sample_answer": "In my view, the criminal justice system ought to prioritize rehabilitating offenders, especially juvenile and first-time offenders. Providing vocational training in prison gives them practical qualifications so that they can find honest work instead of returning to crime.",
            "sample_audio_key": "speaking_q2"
        },
        {
            "id": "q3",
            "text": "Q3: How can individuals and governments prevent the rise of cybercrime?",
            "guide": "💡 <b>Gợi ý công thức 1+2:</b> Nêu trách nhiệm của chính phủ (enforce strict legislation against cybercrime) + Trách nhiệm cá nhân (bảo mật digital transactions để không trở thành victim).",
            "sample_answer": "To combat the rapid rise of cybercrime, governments must enforce strict legislation and impose heavy penalties on online hackers. At the same time, citizens need to protect their digital transactions with strong passwords so they do not fall victim to scams.",
            "sample_audio_key": "speaking_q3"
        }
    ],
    "targeted_sounds": [
        {"word": "legislation", "sound": "/ˌledʒɪsˈleɪʃn/", "note": "Nhấn âm tiết thứ 3: -LAI- (/ˌledʒɪsˈleɪʃn/)"},
        {"word": "rehabilitate", "sound": "/ˌriːəˈbɪlɪteɪt/", "note": "Nhấn âm tiết thứ 3: -BIL- (/ˌriːəˈbɪlɪteɪt/)"},
        {"word": "surveillance", "sound": "/sɜːˈveɪləns/", "note": "Nhấn âm tiết thứ 2: -VEIL- (/sɜːˈveɪləns/)"},
        {"word": "deterrent", "sound": "/dɪˈterənt/", "note": "Nhấn âm tiết thứ 2: -TER- (/dɪˈterənt/)"},
        {"word": "juvenile", "sound": "/ˈdʒuːvənaɪl/", "note": "Nhấn âm đầu JU-, âm cuối /-naɪl/"}
    ],
    "lexical_words": ["legislation", "offense", "deterrent", "rehabilitate", "offender", "juvenile", "surveillance", "penalty", "enforce", "cybercrime", "victim", "verdict", "prevent", "poverty", "justice"]
}
