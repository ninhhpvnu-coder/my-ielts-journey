# -*- coding: utf-8 -*-
"""
IELTS Academic Mastery Kit — Band 5.0 - 6.0
Unit 01: Global Demographics & Urban Growth
Focus: Academic Writing Task 1 (Line Graph Trends & Rates of Change) + Speaking Part 2 & Part 3 (The Long Turn)
"""

UNIT_CONFIG = {
    "unit_id": "B5-01",
    "unit_num": 1,
    "tier": "B5",
    "stage_label": "CHẶNG 1 • DỮ LIỆU ĐỘNG & BÀI NÓI DÀI PART 2",
    "title": "Unit 1: Global Demographics & Urban Growth",
    "badge": "IELTS Band 5.0 — 6.0",
    "audio_dir": "audio/b5_unit01",
    "reading_title": "The Rise of Global Megacities: Density, Infrastructure and Ecological Strain",
    "reading_word_count": "~650 words • Cambridge Academic Level"
}

VOCAB_LIST = [
    {
        "word": "demographic",
        "pos": "adj / n",
        "ipa": "/ˌdem.əˈɡræf.ɪk/",
        "meaning": "(Thuộc về) nhân khẩu học; cấu trúc dân số theo độ tuổi, giới tính, nơi ở.",
        "colloc": "demographic transition / demographic shift",
        "example": "Developing countries are undergoing a profound demographic transition as birth rates decline."
    },
    {
        "word": "urbanisation",
        "pos": "n",
        "ipa": "/ˌɜː.bən.aɪˈzeɪ.ʃən/",
        "meaning": "Sự đô thị hóa; quá trình chuyển dịch dân cư từ nông thôn ra thành thị.",
        "colloc": "unprecedented urbanisation / rapid urbanisation",
        "example": "Unprecedented urbanisation in Southeast Asia has placed immense strain on water resources."
    },
    {
        "word": "megacity",
        "pos": "n",
        "ipa": "/ˈmeɡ.ə.sɪt.i/",
        "meaning": "Siêu đô thị (thành phố có quy mô dân số trên 10 triệu người).",
        "colloc": "sprawling megacity / emerging megacities",
        "example": "Tokyo remains the world's most populous megacity, housing over 37 million residents."
    },
    {
        "word": "infrastructure",
        "pos": "n",
        "ipa": "/ˈɪn.frəˌstrʌk.tʃər/",
        "meaning": "Cơ sở hạ tầng cơ bản (giao thông, mạng lưới điện nước, trường học, bệnh viện).",
        "colloc": "transport infrastructure / upgrade civic infrastructure",
        "example": "Heavy municipal investment is required to modernise antiquated transport infrastructure."
    },
    {
        "word": "exponential",
        "pos": "adj",
        "ipa": "/ˌek.spəˈnen.ʃəl/",
        "meaning": "Tăng theo cấp số nhân; tăng vọt với tốc độ ngày càng dồn dập.",
        "colloc": "exponential growth / increase exponentially",
        "example": "Urban energy consumption has experienced exponential growth over the past three decades."
    },
    {
        "word": "surpass",
        "pos": "v",
        "ipa": "/səˈpɑːs/",
        "meaning": "Vượt trội hơn; vượt qua một mức số liệu hoặc kỷ lục trước đó.",
        "colloc": "surpass initial projections / surpass the previous record",
        "example": "By 2030, the metropolitan population is forecast to surpass twenty million inhabitants."
    },
    {
        "word": "plateau",
        "pos": "v / n",
        "ipa": "/ˈplæt.əʊ/",
        "meaning": "Chững lại ở mức cao sau một thời kỳ tăng trưởng mạnh; trạng thái bình ổn.",
        "colloc": "reach a plateau / plateau at approximately 75%",
        "example": "After a dramatic surge in the 1990s, urbanization rates in Europe have plateaued at 80%."
    },
    {
        "word": "fluctuate",
        "pos": "v",
        "ipa": "/ˈflʌk.tʃu.eɪt/",
        "meaning": "Dao động liên tục; biến thiên lên xuống không ổn định.",
        "colloc": "fluctuate erratically / moderate fluctuations",
        "example": "Migration rates to coastal metropolises fluctuated erratically during the economic recession."
    },
    {
        "word": "plummet",
        "pos": "v",
        "ipa": "/ˈplʌm.ɪt/",
        "meaning": "Lao dốc, sụt giảm mạnh và đột ngột (từ vựng Task 1 cao cấp).",
        "colloc": "plummet drastically / plummet to an all-time low",
        "example": "Rural employment figures plummeted drastically following the mechanisation of agriculture."
    },
    {
        "word": "stabilise",
        "pos": "v",
        "ipa": "/ˈsteɪ.bəl.aɪz/",
        "meaning": "Bình ổn trở lại; giữ ở trạng thái ổn định và cân bằng.",
        "colloc": "gradually stabilise / stabilise at a manageable level",
        "example": "Population growth is expected to stabilise once national fertility rates reach replacement levels."
    },
    {
        "word": "density",
        "pos": "n",
        "ipa": "/ˈden.sə.ti/",
        "meaning": "Mật độ dân số; độ dày đặc của người hoặc vật thể trong một đơn vị diện tích.",
        "colloc": "high population density / density per square kilometre",
        "example": "High population density in inner districts exacerbates air pollution and housing deficits."
    },
    {
        "word": "sprawl",
        "pos": "n / v",
        "ipa": "/sprɔːl/",
        "meaning": "Sự mở rộng tràn lan vô trật tự của thành phố ra các vùng ngoại ô.",
        "colloc": "unchecked urban sprawl / curb suburban sprawl",
        "example": "Strict zoning regulations are introduced to curb uncontrolled urban sprawl into agricultural land."
    },
    {
        "word": "inhabitant",
        "pos": "n",
        "ipa": "/ɪnˈhæb.ɪ.tənt/",
        "meaning": "Cư dân cư trú; người sinh sống lâu dài tại một địa bàn (paraphrase của resident/citizen).",
        "colloc": "urban inhabitants / long-term inhabitants",
        "example": "Over half of the world's inhabitants now dwell in metropolitan and urban centres."
    },
    {
        "word": "overburden",
        "pos": "v",
        "ipa": "/ˌəʊ.vəˈbɜː.dən/",
        "meaning": "Tạo áp lực quá tải; đè nặng gánh nặng lên hệ thống dịch vụ công.",
        "colloc": "overburden public services / overburden the healthcare system",
        "example": "Sudden population influxes severely overburden local sanitation and hospital systems."
    },
    {
        "word": "projection",
        "pos": "n",
        "ipa": "/prəˈdʒek.ʃən/",
        "meaning": "Số liệu dự báo mang tính thống kê khoa học cho tương lai.",
        "colloc": "statistical projection / according to current demographic projections",
        "example": "According to UN demographic projections, Asia will house several new megacities by 2040."
    },
    {
        "word": "disparity",
        "pos": "n",
        "ipa": "/dɪˈspær.ə.ti/",
        "meaning": "Sự phân hóa, bất bình đẳng sâu sắc giữa hai nhóm đối tượng hoặc khu vực.",
        "colloc": "wealth disparity / regional economic disparity",
        "example": "Widening economic disparity between rural provinces and capital cities fuels mass migration."
    },
    {
        "word": "congestion",
        "pos": "n",
        "ipa": "/kənˈdʒes.tʃən/",
        "meaning": "Tình trạng tắc nghẽn giao thông hoặc quá tải cục bộ.",
        "colloc": "severe traffic congestion / ease vehicular congestion",
        "example": "The expansion of subway networks is vital to alleviate chronic vehicular congestion."
    },
    {
        "word": "depopulation",
        "pos": "n",
        "ipa": "/diːˌpɒp.jəˈleɪ.ʃən/",
        "meaning": "Sự suy giảm dân số nghiêm trọng (thường xảy ra ở vùng nông thôn khi người trẻ bỏ đi).",
        "colloc": "rural depopulation / severe depopulation of farming hamlets",
        "example": "Many agricultural towns face severe rural depopulation as young graduates seek urban careers."
    },
    {
        "word": "sustainable",
        "pos": "adj",
        "ipa": "/səˈsteɪ.nə.bəl/",
        "meaning": "Bền vững; đáp ứng nhu cầu hiện tại mà không làm tổn hại đến tương lai.",
        "colloc": "sustainable urban development / environmentally sustainable models",
        "example": "Architects are prioritizing green roofs and renewable energy to build sustainable communities."
    },
    {
        "word": "predominantly",
        "pos": "adv",
        "ipa": "/prɪˈdɒm.ɪ.nənt.li/",
        "meaning": "Chiếm ưu thế tuyệt đối; phần lớn, chủ yếu.",
        "colloc": "predominantly rural / predominantly urbanised region",
        "example": "A century ago, the global population was predominantly rural and engaged in agrarian labor."
    }
]

VOCAB_QUESTIONS = [
    {
        "id": 1,
        "q": "The rapid influx of workers into the industrial hub has threatened to ______ municipal utilities and emergency services.",
        "options": ["A. overburden", "B. plateau", "C. depopulate", "D. fluctuate"],
        "answer": 0,
        "explain": "'overburden' nghĩa là làm quá tải các tiện ích công cộng và dịch vụ cứu nạn."
    },
    {
        "id": 2,
        "q": "By 2040, the proportion of citizens dwelling in metropolitan centers is projected to ______ the 70% threshold.",
        "options": ["A. plummet", "B. surpass", "C. sprawl", "D. congest"],
        "answer": 1,
        "explain": "'surpass' là từ học thuật diễn tả việc 'vượt qua' một ngưỡng mốc số liệu (threshold)."
    },
    {
        "id": 3,
        "q": "Following a sharp increase between 2000 and 2010, the migration rate seems to have ______ at around 45,000 arrivals annually.",
        "options": ["A. plummeted", "B. plateaued", "C. overburdened", "D. depopulated"],
        "answer": 1,
        "explain": "'plateaued' (động từ quá khứ) diễn tả trạng thái chững lại và đi ngang ở mức cao."
    },
    {
        "id": 4,
        "q": "Statistical ______ released by global analysts indicate that developing nations will drive the next wave of urbanisation.",
        "options": ["A. disparities", "B. projections", "C. congestions", "D. inhabitants"],
        "answer": 1,
        "explain": "'statistical projections' là cụm collocation học thuật chỉ 'các số liệu dự báo thống kê'."
    },
    {
        "id": 5,
        "q": "The local government passed new legislation to prevent unchecked urban ______ into prime agricultural zones.",
        "options": ["A. sprawl", "B. density", "C. infrastructure", "D. demographic"],
        "answer": 0,
        "explain": "'urban sprawl' là thuật ngữ chỉ sự mở rộng đất đô thị tràn lan xâm lấn đất nông nghiệp."
    },
    {
        "id": 6,
        "q": "Due to mechanisation in farming, young people moved away, causing severe rural ______ in remote hamlets.",
        "options": ["A. congestion", "B. depopulation", "C. density", "D. projection"],
        "answer": 1,
        "explain": "'rural depopulation' là hiện tượng sụt giảm dân số nông thôn do giới trẻ di cư."
    },
    {
        "id": 7,
        "q": "During the pandemic, public transport passenger volumes ______ to an unprecedented all-time low.",
        "options": ["A. plummeted", "B. stabilised", "C. plateaued", "D. surpassed"],
        "answer": 0,
        "explain": "'plummeted' là từ vựng Writing Task 1 xuất sắc mô tả sự sụt giảm nghiêm trọng và nhanh chóng."
    },
    {
        "id": 8,
        "q": "Significant wealth ______ between urban elites and rural laborers continues to spark socio-economic debates.",
        "options": ["A. infrastructure", "B. disparity", "C. inhabitant", "D. density"],
        "answer": 1,
        "explain": "'wealth disparity' mang nghĩa 'sự chênh lệch giàu nghèo sâu sắc'."
    },
    {
        "id": 9,
        "q": "A metropolis with a population of over ten million people is formally classified by geographers as a ______.",
        "options": ["A. suburb", "B. province", "C. megacity", "D. demographic"],
        "answer": 2,
        "explain": "Đô thị có dân số trên 10 triệu người theo định nghĩa khoa học là 'megacity'."
    },
    {
        "id": 10,
        "q": "Investing in modern mass transit systems is imperative to alleviate chronic vehicular ______ in city centres.",
        "options": ["A. congestion", "B. sprawl", "C. transition", "D. projection"],
        "answer": 0,
        "explain": "'vehicular congestion' là cụm collocation học thuật chỉ tình trạng ùn tắc xe cộ."
    },
    {
        "id": 11,
        "q": "In 1900, the global populace was ______ rural, with less than fifteen percent living in towns.",
        "options": ["A. exponentially", "B. predominantly", "C. erratically", "D. drastically"],
        "answer": 1,
        "explain": "'predominantly rural' có nghĩa là 'chủ yếu / phần lớn là dân số nông thôn'."
    },
    {
        "id": 12,
        "q": "The country is undergoing an unprecedented ______ shift characterized by an aging population and declining birth rates.",
        "options": ["A. demographic", "B. sustainable", "C. mechanical", "D. congested"],
        "answer": 0,
        "explain": "'demographic shift' là 'sự chuyển dịch cơ cấu nhân khẩu học'."
    },
    {
        "id": 13,
        "q": "Tokyo exhibits an exceptionally high population ______, with thousands of people per square kilometer.",
        "options": ["A. disparity", "B. density", "C. sprawl", "D. projection"],
        "answer": 1,
        "explain": "'population density' là thuật ngữ chuẩn chỉ 'mật độ dân số'."
    },
    {
        "id": 14,
        "q": "After months of unpredictability, market prices have begun to ______ at an acceptable equilibrium.",
        "options": ["A. plummet", "B. stabilise", "C. overburden", "D. fluctuate"],
        "answer": 1,
        "explain": "'stabilise' có nghĩa là 'bình ổn, giữ ở trạng thái ổn định'."
    },
    {
        "id": 15,
        "q": "A sustainable city must balance industrial productivity with green spaces to ensure the wellbeing of every ______.",
        "options": ["A. infrastructure", "B. inhabitant", "C. projection", "D. sprawl"],
        "answer": 1,
        "explain": "'inhabitant' là danh từ chỉ cư dân sinh sống, rất hay dùng thay thế cho citizen/resident."
    },
    {
        "id": 16,
        "q": "Throughout the early 2000s, employment numbers in manufacturing ______ between 12% and 15% before declining.",
        "options": ["A. fluctuated", "B. surpassed", "C. plateaued", "D. depopulated"],
        "answer": 0,
        "explain": "'fluctuated' diễn tả sự dao động biến thiên trong khoảng 12% - 15%."
    },
    {
        "id": 17,
        "q": "Advanced smart cities rely on green energy grids to create an environmentally ______ urban environment.",
        "options": ["A. congested", "B. sustainable", "C. demographic", "D. overburdened"],
        "answer": 1,
        "explain": "'environmentally sustainable' nghĩa là 'bền vững về mặt môi trường'."
    },
    {
        "id": 18,
        "q": "The mayor announced an ambitious ten-year scheme to rehabilitate the capital's ageing water and sewage ______.",
        "options": ["A. infrastructure", "B. disparity", "C. sprawl", "D. projection"],
        "answer": 0,
        "explain": "'infrastructure' chỉ hệ thống cấp thoát nước và điện đường trường trạm cơ bản."
    },
    {
        "id": 19,
        "q": "Computing power and data exchange have registered ______ expansion, revolutionising communications.",
        "options": ["A. exponential", "B. predominantly", "C. depopulated", "D. erratic"],
        "answer": 0,
        "explain": "'exponential expansion' là 'sự mở rộng theo cấp số nhân'."
    },
    {
        "id": 20,
        "q": "Governments must address income ______ if they wish to mitigate social friction in expanding metropolises.",
        "options": ["A. infrastructure", "B. disparity", "C. inhabitant", "D. projection"],
        "answer": 1,
        "explain": "'income disparity' là sự chênh lệch thu nhập trong xã hội đô thị."
    }
]

GRAMMAR_THEORY = {
    "title": "Ngữ Pháp Task 1: Miêu Tả Xu Hướng Biến Thiên & Tốc Độ Thay Đổi",
    "points": [
        "1. Cặp Cấu Trúc Động Từ vs Danh Từ: 'The population increased significantly' (V + Adv) ⟷ 'There was a significant increase in the population' (There was a/an + Adj + N + in).",
        "2. Đa Dạng Hóa Từ Chỉ Tốc Độ & Biên Độ: Dramatic / Sharp / Steep (mạnh mẽ); Steady / Moderate / Gradual (đều đặn, vừa phải); Marginal / Slight (nhẹ, không đáng kể).",
        "3. Ngôn Ngữ Dự Báo Tương Lai (Projections): 'is projected / predicted / forecast to reach X' hoặc 'is anticipated to see an upward trend'."
    ]
}

GRAMMAR_QUESTIONS = [
    {
        "id": 1,
        "q": "Between 1990 and 2010, the urban populace in Asia ______ significantly, rising from 32% to over 48%.",
        "options": ["A. increases", "B. increased", "C. was increasing", "D. has increased"],
        "answer": 1,
        "explain": "Mốc thời gian xác định trong quá khứ (1990 - 2010) bắt buộc dùng thì Quá khứ đơn 'increased'."
    },
    {
        "id": 2,
        "q": "There was a ______ decline in rural inhabitants after industrial factories were built in nearby suburbs.",
        "options": ["A. dramatically", "B. dramatic", "C. drama", "D. dramatise"],
        "answer": 1,
        "explain": "Đứng trước danh từ 'decline' phải là tính từ 'dramatic' theo công thức 'There was a + Adj + N'."
    },
    {
        "id": 3,
        "q": "The proportion of city dwellers is projected ______ 85% by the middle of the twenty-first century.",
        "options": ["A. reaching", "B. to reach", "C. reached", "D. reach"],
        "answer": 1,
        "explain": "Cấu trúc bị động chỉ số liệu dự báo tương lai: 'is projected to + V-inf'."
    },
    {
        "id": 4,
        "q": "While North American urbanization rates stood at 75%, ______ figures for Africa remained significantly lower at 25%.",
        "options": ["A. whereas", "B. the corresponding", "C. similarly", "D. likewise"],
        "answer": 1,
        "explain": "'the corresponding figures' là cụm từ Task 1 kinh điển dùng để chỉ 'số liệu tương ứng của đối tượng kia'."
    },
    {
        "id": 5,
        "q": "The number of motor vehicles increased exponentially, ______ severe traffic bottlenecks in the downtown core.",
        "options": ["A. resulted in", "B. resulting in", "C. results in", "D. was resulting in"],
        "answer": 1,
        "explain": "Mệnh đề phân từ hiện tại (Present Participle 'resulting in') dùng để diễn đạt kết quả logic của vế trước."
    },
    {
        "id": 6,
        "q": "The birth rate in European metropolises saw a gradual downturn, ______ by a period of relative stability.",
        "options": ["A. followed", "B. following", "C. was followed", "D. follow"],
        "answer": 0,
        "explain": "Cấu trúc rút gọn diễn tả trình tự thời gian trong Task 1: '..., followed by a period of...'."
    },
    {
        "id": 7,
        "q": "In contrast ______ the rapid surge observed in Latin America, African urban growth remained relatively modest.",
        "options": ["A. with / to", "B. from", "C. against", "D. of"],
        "answer": 0,
        "explain": "Cụm giới từ chuẩn so sánh đối chiếu: 'In contrast to / In contrast with'."
    },
    {
        "id": 8,
        "q": "By the year 2040, demographers anticipate that developing regions ______ the majority of global megacities.",
        "options": ["A. will host", "B. hosted", "C. are hosting", "D. have hosted"],
        "answer": 0,
        "explain": "Diễn đạt dự đoán tương lai với mốc thời gian 'By 2040': dùng 'will host'."
    },
    {
        "id": 9,
        "q": "Expenditure on civic infrastructure increased ______ over the 15-year observation period.",
        "options": ["A. steady", "B. steadily", "C. steadiness", "D. steadfast"],
        "answer": 1,
        "explain": "Bổ nghĩa cho động từ thường 'increased' cần một trạng từ 'steadily'."
    },
    {
        "id": 10,
        "q": "The graph depicts a pattern ______ migration peaks during spring months and troughs during mid-winter.",
        "options": ["A. which", "B. where", "C. who", "D. whose"],
        "answer": 1,
        "explain": "'where' được dùng trong văn phong học thuật để bổ nghĩa cho 'a pattern / a situation' (trong đó)."
    }
]

# Cambridge Section 2 Monologue: Urban Development Planning Briefing (15 turns)
DIALOGUE_LINES = [
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Good morning, council members. Today I am presenting the 2030 Master Urban Development Plan for Riverside New City."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Over the past two decades, our municipal region has witnessed rapid and unprecedented demographic expansion."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Currently, our metropolitan boundaries house approximately 1.4 million inhabitants, surpassing all statistical projections."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Consequently, this influx has begun to overburden our primary arterial roads and public healthcare facilities."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "To counteract unchecked urban sprawl, the zoning committee has designated three compact high-density development corridors."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "First, looking at the city center map, the dilapidated industrial docks on the eastern riverfront will be demolished."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "In their place, we are establishing a zero-emission pedestrian promenade featuring mixed-use commercial and residential towers."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Second, vehicular congestion on the Western Expressway will be alleviated through a new electric tram network."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Construction of the tram terminus will begin directly adjacent to the existing Central Railway Station next spring."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Furthermore, we must address the acute wealth disparity between the affluent northern hills and the low-income southern flats."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Our plan mandates that thirty percent of all new residential units in the southern zone must be designated as affordable social housing."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Regarding public amenities, two major green corridors will connect the central park directly to the southern waterfront."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "These corridors will incorporate cycling superhighways and bioswales to mitigate urban heat islands and flash flooding."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "By 2030, we forecast that carbon emissions per capita will plummet by forty percent compared to 2010 baselines."},
    {"speaker": "Planner", "voice": "en-GB-RyanNeural", "text": "Thank you for your attention. I am now delighted to take questions on this sustainable development blueprint."}
]

LISTENING_QUESTIONS = [
    {
        "id": "L1",
        "type": "short_answer",
        "question": "What is the current population of Riverside New City? (Write NO MORE THAN TWO WORDS AND/OR A NUMBER)",
        "placeholder": "Enter current population...",
        "answers": ["1.4 million", "1.4m", "1,400,000"],
        "explain": "Vị trí đoạn nói: '...currently our metropolitan boundaries house approximately 1.4 million inhabitants...'."
    },
    {
        "id": "L2",
        "type": "short_answer",
        "question": "What facilities on the eastern riverfront will be demolished? (Write NO MORE THAN TWO WORDS)",
        "placeholder": "Enter facilities to be demolished...",
        "answers": ["industrial docks", "docks"],
        "explain": "Vị trí đoạn nói: '...the dilapidated industrial docks on the eastern riverfront will be demolished...'."
    },
    {
        "id": "L3",
        "type": "short_answer",
        "question": "Where will the new electric tram terminus be constructed? (Write NO MORE THAN THREE WORDS)",
        "placeholder": "Enter location...",
        "answers": ["central railway station", "adjacent to railway station", "railway station"],
        "explain": "Vị trí: '...tram terminus will begin directly adjacent to the existing Central Railway Station...'."
    },
    {
        "id": "L4",
        "type": "short_answer",
        "question": "What percentage of new housing in the southern zone must be affordable social housing? (Write ONE NUMBER)",
        "placeholder": "Enter percentage...",
        "answers": ["30%", "30 percent", "thirty percent", "30"],
        "explain": "Vị trí: '...mandates that thirty percent of all new residential units in the southern zone must be designated as affordable...'."
    },
    {
        "id": "L5",
        "type": "short_answer",
        "question": "What two hazards will the green bioswales mitigate? (Write NO MORE THAN THREE WORDS)",
        "placeholder": "Enter hazards...",
        "answers": ["heat and flooding", "heat islands flooding", "heat flooding", "flash flooding", "urban heat islands"],
        "explain": "Vị trí: '...to mitigate urban heat islands and flash flooding.'."
    },
    {
        "id": "L6",
        "type": "short_answer",
        "question": "By what percentage will per capita carbon emissions drop by 2030? (Write ONE NUMBER)",
        "placeholder": "Enter percentage drop...",
        "answers": ["40%", "40 percent", "forty percent", "40"],
        "explain": "Vị trí: '...carbon emissions per capita will plummet by forty percent compared to 2010 baselines.'."
    }
]

READING_PASSAGE = """
<b>Paragraph A</b>
For the vast majority of human history, our species was predominantly agrarian and rural. As late as 1800, fewer than ten percent of human beings lived in settlements that could plausibly be termed cities. However, the onset of the Industrial Revolution catalyzed an unprecedented demographic upheaval. The mechanisation of agricultural machinery dramatically diminished the demand for farm labor, triggering widespread rural depopulation across Western Europe. Simultaneously, emerging textile factories, shipping docks, and coal-fired steel mills in urban centers generated a voracious demand for human workforce, magnetizing millions of impoverished rural inhabitants to expanding cities.

<b>Paragraph B</b>
Today, humanity has irrevocably crossed an evolutionary threshold. According to statistical projections released by the United Nations Population Division, over 56 percent of the world's population currently resides in metropolitan conurbations, a metric forecast to surpass 68 percent by 2050. This surge is creating a new geographic phenomenon: the megacity. In 1950, only New York and Tokyo surpassed the ten-million-inhabitant threshold. By 2025, there were more than 33 recognized megacities, and demographers anticipate that this number will expand exponentially, particularly across the Global South. Emerging powerhouses such as Dhaka, Lagos, and Kinshasa are expanding at rates that challenge conventional urban engineering.

<b>Paragraph C</b>
This explosive concentration of populace creates both profound socioeconomic opportunities and alarming structural vulnerabilities. On the economic ledger, high population density fosters remarkable agglomeration efficiencies. Dense metropolises generate more patents, attract larger venture capital investments, and produce greater economic output per capita than smaller townships. By concentrating educational institutions, research hospitals, and corporate headquarters within accessible transit radii, megacities serve as engines of national innovation and global trade integration.

<b>Paragraph D</b>
Conversely, the negative externalities of unchecked expansion are acute. When urbanization outpaces municipal planning, cities succumb to chronic urban sprawl, transforming fertile green belts into vast suburban peripheries lacking water mains, public schools, or sewage treatment. The resulting vehicle reliance causes catastrophic vehicular congestion and toxic air pollution that shortens life expectancy. Furthermore, sudden population growth threatens to overburden public healthcare systems and municipal housing stocks, widening the socio-economic disparity between fortified luxury compounds and informal hillside slums.

<b>Paragraph E</b>
The central governance challenge of the coming century is therefore not to prevent urbanisation—an endeavor history suggests is both futile and economically counterproductive—but to render it environmentally sustainable. Progressive municipal authorities in cities like Curitiba, Singapore, and Copenhagen demonstrate that strategic civic investment can decouple demographic density from ecological degradation. By prioritizing high-capacity electrified mass transit, enforcing mandatory green building insulation standards, and revitalizing blue-green civic infrastructure, cities can house millions of inhabitants while reducing per-capita environmental footprints. The future of human civilisation will decisively be won or lost in our megacities.
"""

READING_QUESTIONS = [
    {
        "id": "R1",
        "type": "short_answer",
        "question": "What historical event initially sparked the widespread migration of farm laborers into cities? (Write NO MORE THAN TWO WORDS)",
        "placeholder": "Enter historical event...",
        "answers": ["Industrial Revolution", "the Industrial Revolution"],
        "evidence": "Paragraph A: 'However, the onset of the Industrial Revolution catalyzed an unprecedented demographic upheaval.'",
        "explain": "Đoạn A xác định rõ cuộc Cách mạng Công nghiệp (Industrial Revolution) là ngòi nổ kích hoạt sự di cư này."
    },
    {
        "id": "R2",
        "type": "short_answer",
        "question": "What percentage of the global population is projected to dwell in urban areas by 2050? (Write ONE NUMBER)",
        "placeholder": "Enter projected percentage...",
        "answers": ["68%", "68 percent", "68"],
        "evidence": "Paragraph B: '...a metric forecast to surpass 68 percent by 2050.'",
        "explain": "Đoạn B khẳng định tỷ lệ dân số sống ở thành thị dự báo sẽ vượt qua 68% vào năm 2050."
    },
    {
        "id": "R3",
        "type": "short_answer",
        "question": "How many megacities existed worldwide in the year 1950? (Write ONE NUMBER)",
        "placeholder": "Enter number of megacities...",
        "answers": ["two", "2", "only two"],
        "evidence": "Paragraph B: 'In 1950, only New York and Tokyo surpassed the ten-million-inhabitant threshold.'",
        "explain": "Năm 1950 chỉ có đúng 2 thành phố (New York và Tokyo) đạt chuẩn megacity."
    },
    {
        "id": "R4",
        "type": "short_answer",
        "question": "According to Paragraph C, dense metropolises generate higher economic output and more ______ per capita than smaller towns. (Write ONE WORD)",
        "placeholder": "Enter output item...",
        "answers": ["patents"],
        "evidence": "Paragraph C: 'Dense metropolises generate more patents, attract larger venture capital investments...'",
        "explain": "Đoạn C liệt kê các thành phố mật độ cao tạo ra nhiều bằng sáng chế ('patents') hơn tính theo đầu người."
    },
    {
        "id": "R5",
        "type": "short_answer",
        "question": "What type of reliance results from unchecked urban sprawl and long commutes? (Write NO MORE THAN TWO WORDS)",
        "placeholder": "Enter reliance type...",
        "answers": ["vehicle reliance", "vehicle"],
        "evidence": "Paragraph D: 'The resulting vehicle reliance causes catastrophic vehicular congestion...'",
        "explain": "Sự mở rộng đô thị tràn lan dẫn tới sự phụ thuộc vào phương tiện cá nhân ('vehicle reliance')."
    },
    {
        "id": "R6",
        "type": "short_answer",
        "question": "According to Paragraph E, attempting to completely halt the process of urbanisation is deemed ______. (Write ONE WORD)",
        "placeholder": "Enter adjective...",
        "answers": ["futile"],
        "evidence": "Paragraph E: '...not to prevent urbanisation—an endeavor history suggests is both futile and economically counterproductive...'",
        "explain": "Đoạn E khẳng định nỗ lực ngăn chặn đô thị hóa là vô ích ('futile') và phản tác dụng về mặt kinh tế."
    }
]

WRITING_TASK = {
    "topic": "✍️ IELTS Academic Writing Task 1: Line Graph Analysis",
    "prompt": "The line graph below illustrates the percentage of the total population living in urban areas in four different continents between 1970 and 2020, with official projections up to 2040.\n\nSummarise the information by selecting and reporting the main features, and make comparisons where relevant. Write at least 150 words.",
    "criteria": "Task Achievement (Overview rõ ràng + nhóm số liệu logic), Coherence & Cohesion (từ nối xu hướng), Lexical Resource (ngữ vựng biến thiên cao cấp), GRA (thì quá khứ, dự báo tương lai & câu phức).",
    "target_words": 150,
    "unit_vocab": ["demographic", "urbanisation", "infrastructure", "surpass", "plateau", "fluctuate", "plummet", "stabilise", "inhabitant", "projection", "predominantly"],
    "model_essay": """The line graph delineates the proportion of inhabitants dwelling in metropolitan regions across four distinct continents from 1970 to 2020, accompanied by statistical projections through to 2040.

Overall, it is readily apparent that all four continents experience substantial upward trajectories in urban population shares over the 70-year timeframe. Throughout the period, North America consistently records the highest percentage of city dwellers, whereas Africa registers the lowest urbanisation rates, despite exhibiting the steepest acceleration.

In 1970, North America led the demographic data at approximately 72%, followed closely by Europe at 64%. Over the subsequent five decades, both regions underwent steady growth, with North America rising to 82% and Europe ascending to 75% by 2020. Projections indicate that this gradual expansion will continue, culminating at roughly 87% and 82% respectively by 2040, where figures are anticipated to reach a plateau.

Conversely, in 1970, Asian and African populations were predominantly rural, with urban rates standing at merely 20% and 15% respectively. However, Asia experienced exponential urbanization, surging to nearly 50% by 2020 and projected to surpass 65% by 2040. While African urbanisation climbed more modestly to 42% in 2020, it is forecast to accelerate rapidly, nearly quadrupling its initial 1970 baseline to reach 58% by the end of the period.""",
    "model_analysis": """<b>Phân Tích Cấu Trúc Đạt Band 8.5+:</b>
• <b>Introduction (Đoạn 1):</b> Paraphrase linh hoạt đề bài: <i>'illustrates the percentage of the population'</i> ⟷ <i>'delineates the proportion of inhabitants dwelling in metropolitan regions'</i>.
• <b>Overview (Đoạn 2 - Chìa khóa Band 6.0+):</b> Nêu 2 xu hướng nổi bật bao quát: (1) Cả 4 châu lục đều tăng trưởng mạnh; (2) Bắc Mỹ luôn dẫn đầu, trong khi Châu Phi xuất phát điểm thấp nhất nhưng có tốc độ bứt phá dốc nhất. Tuyệt đối không đưa số liệu vụn vặt vào Overview.
• <b>Body 1 (Đoạn 3 - Nhóm khu vực phát triển):</b> Nhóm Bắc Mỹ và Châu Âu (xuất phát điểm cao $\ge 60\%$, tăng trưởng đều đặn và bình ổn).
• <b>Body 2 (Đoạn 4 - Nhóm khu vực đang phát triển):</b> Nhóm Châu Á và Châu Phi (xuất phát điểm rất thấp $\le 20\%$, nhưng tăng trưởng theo cấp số nhân và bứt phá mạnh mẽ nhất).""",
    "model_translation": """<b>Bản Dịch Đối Chiếu Tiếng Việt:</b>
Biểu đồ đường biểu thị tỷ lệ cư dân sinh sống tại các khu vực đô thị ở bốn châu lục khác nhau từ năm 1970 đến năm 2020, kèm theo các dự báo thống kê đến năm 2040.

Nhìn chung, có thể thấy rõ ràng rằng cả bốn châu lục đều trải qua xu hướng tăng trưởng đáng kể về tỷ trọng dân số thành thị trong khung thời gian 70 năm. Trong toàn bộ giai đoạn, Bắc Mỹ luôn ghi nhận tỷ lệ cư dân thành thị cao nhất, trong khi Châu Phi ghi nhận tỷ lệ đô thị hóa thấp nhất, mặc dù có tốc độ gia tăng nhanh nhất.

Vào năm 1970, Bắc Mỹ dẫn đầu dữ liệu nhân khẩu học ở mức xấp xỉ 72%, theo sát phía sau là Châu Âu ở mức 64%. Trong năm thập kỷ tiếp theo, cả hai khu vực đều trải qua sự tăng trưởng đều đặn, với Bắc Mỹ tăng lên 82% và Châu Âu vươn lên 75% vào năm 2020. Các dự báo chỉ ra rằng sự mở rộng dần dần này sẽ tiếp tục, đạt đỉnh ở mức khoảng 87% và 82% vào năm 2040, nơi các số liệu được kỳ vọng sẽ chững lại.

Ngược lại, vào năm 1970, dân số Châu Á và Châu Phi chủ yếu là nông thôn, với tỷ lệ thành thị chỉ lần lượt ở mức 20% và 15%. Tuy nhiên, Châu Á đã trải qua quá trình đô thị hóa theo cấp số nhân, tăng vọt lên gần 50% vào năm 2020 và được dự báo sẽ vượt qua 65% vào năm 2040. Mặc dù đô thị hóa ở Châu Phi tăng khiêm tốn hơn lên mức 42% vào năm 2020, nhưng dự báo sẽ tăng tốc nhanh chóng, gần gấp bốn lần mốc cơ sở năm 1970 ban đầu để đạt 58% vào cuối kỳ."""
}

SPEAKING_TASK = {
    "title": "🗣️ IELTS Speaking Lab (Part 2: The Long Turn & Part 3: Analytical Discussion)",
    "targeted_sounds": "Trọng âm từ đa âm tiết: de-mo-GRA-phic, ur-ba-ni-SA-tion, in-fra-STRUC-ture, ex-po-NEN-tial",
    "lexical_words": "megacity, demographic shift, urban sprawl, infrastructure, sustainable living",
    "questions": [
        {
            "id": "SP1",
            "part": 2,
            "title": "Part 2: The Long Turn (Describe a city or town you have visited)",
            "prompt": "Describe an interesting city or town you have visited.\n\nYou should say:\n• Where it is and when you went there\n• What the people and the atmosphere were like\n• What urban infrastructure or attractions impressed you\n• And explain why this city left a lasting impression on you.",
            "guide": "<b>Chiến thuật 2 phút Part 2:</b><br>• Dành 60s chuẩn bị ghi chú theo 4 gạch đầu dòng (Past - Present - Future).<br>• Dùng các tính từ gợi tả không gian: <i>vibrant metropolis, architectural marvel, cutting-edge infrastructure</i>.<br>• Mở rộng cảm xúc cá nhân và bài học rút ra.",
            "sample_answer": "I would like to talk about my visit to Singapore, a remarkably vibrant and futuristic city-state in Southeast Asia that I had the privilege of exploring two years ago. What immediately struck me upon arrival was the extraordinary efficiency of its civic infrastructure. Unlike many sprawling megacities burdened by chronic traffic congestion, Singapore features an ultra-modern electrified transit network that seamlessly connects every municipal district. The urban inhabitants are exceptionally polite, culturally diverse, and deeply committed to maintaining public cleanliness. What fascinated me most was their visionary approach to sustainable architecture, exemplified by the iconic Gardens by the Bay with its towering solar-powered Supertrees. This trip left an indelible mark on my perspective because it proved that high population density does not inevitably cause environmental degradation, provided there is forward-thinking urban planning."
        },
        {
            "id": "SP2",
            "part": 3,
            "title": "Part 3: Question 1 — Rural to Urban Migration",
            "prompt": "Why are so many young individuals abandoning rural areas to relocate to major cities?",
            "guide": "<b>Công thức A.R.E.A:</b><br>• <b>Answer:</b> Trả lời trực diện (việc làm & giáo dục).<br>• <b>Reason:</b> Giải thích sự chênh lệch cơ sở hạ tầng (disparity).<br>• <b>Example:</b> Ví dụ sinh viên tốt nghiệp.<br>• <b>Alternative:</b> Trừ khi vùng quê được số hóa và đầu tư.",
            "sample_answer": "In my view, the primary catalyst driving rural-to-urban migration is the profound socio-economic disparity between agrarian hamlets and metropolitan centers. Major cities offer a concentration of prestigious universities, diverse career opportunities, and superior healthcare infrastructure that rural zones simply cannot match. For instance, ambitious young graduates frequently migrate to capital cities because multinational corporations rarely establish headquarters in farming villages. Unless governments vigorously subsidize rural entrepreneurship and high-speed digital connectivity, this demographic outflow is bound to persist."
        },
        {
            "id": "SP3",
            "part": 3,
            "title": "Part 3: Question 2 — Municipal Challenges of Rapid Growth",
            "prompt": "What major difficulties do municipal authorities face when a city expands too rapidly?",
            "guide": "<b>Công thức A.R.E.A:</b><br>• <b>Answer:</b> Quá tải hạ tầng & nhà ở.<br>• <b>Reason:</b> Tốc độ xây dựng không bắt kịp dân số.<br>• <b>Example:</b> Ùn tắc giao thông và khu ổ chuột.<br>• <b>Alternative:</b> Cần quy hoạch đô thị vệ tinh thông minh.",
            "sample_answer": "When urbanization outpaces administrative planning, city planners inevitably encounter severe bottlenecks. The most immediate crisis is the overburdening of basic public amenities such as clean water distribution, sewage disposal, and public hospitals. Furthermore, housing deficits frequently cause property prices to skyrocket, forcing low-income inhabitants into informal settlements with inadequate sanitation. A prime example can be observed in emerging megacities where unchecked urban sprawl generates chronic vehicular congestion, which in turn severely degrades ambient air quality."
        },
        {
            "id": "SP4",
            "part": 3,
            "title": "Part 3: Question 3 — The Future Sustainability of Megacities",
            "prompt": "Do you believe the continued growth of massive megacities is sustainable in the long run?",
            "guide": "<b>Công thức A.R.E.A:</b><br>• <b>Answer:</b> Quan điểm cân bằng (chỉ bền vững nếu chuyển đổi xanh).<br>• <b>Reason:</b> Tiêu thụ tài nguyên & biến đổi khí hậu.<br>• <b>Example:</b> Thành phố thông minh dùng năng lượng tái tạo.<br>• <b>Alternative:</b> Ngược lại sẽ sụp đổ vì thiếu nước sạch và rác thải.",
            "sample_answer": "I believe the sustainability of future megacities hinges entirely on whether municipal governments embrace ecological modernisation. If cities continue to rely on fossil-fuel transportation and linear consumption models, their ecological footprint will become utterly catastrophic. However, if urban centers actively transition towards circular economies—investing heavily in electrified mass transit, vertical farming, and renewable energy grids—high population density can actually be more resource-efficient per capita than dispersed suburban living."
        }
    ]
}
