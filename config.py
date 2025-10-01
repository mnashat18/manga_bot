from telegram import InlineKeyboardButton

# التوكن
BOT_TOKEN = "8427717553:AAEeCZHXNbrec7dM8pD4Qg-3dcAggBBYz-s"

# القنوات المطلوبة للاشتراك
REQUIRED_CHANNELS = [
    {"id": "@MyLovlyManhwa", "name": "قناتنا الرسمية"},
]

# القائمة الرئيسية
main_menu_buttons = [
    [InlineKeyboardButton("📚 المانهوا", callback_data="list_manhwa")],
    [InlineKeyboardButton("📖 المانجا", callback_data="list_manga")],
    [
        InlineKeyboardButton("🎵 قناتنا على تيك توك", url="https://www.tiktok.com/@vafavatv?_t=ZS-90AfEuEkRkI&_r=1"),
        InlineKeyboardButton("ℹ️ طريقة المشاهدة", callback_data="how_to_watch"),
    ]
]

# بيانات المانهوا
MANHWA_LIST = {
    "solo": {
        "title": "Rebirth with Power: Spearhead to the Top",
        "genre": "أكشن – فانتازيا – مغامرة",
        "status": "مستمرة",
        "year": "2024",
        "image": "https://imgg.mangaina.com/ab1b8c89ab469a773b7c6f1359c5905d.webp",
        "story": "تروي المانهوا قصة بطل يحصل على فرصة ولادة جديدة بعدما فقد كل شيء في حياته السابقة. هذه المرة، ينهض وهو يحمل قوة خارقة وسلاحه المميز رأس الحربة، عازمًا على تسلق القمة وتجاوز خصومه. وبين معارك طاحنة ومخططات معقدة، يجد نفسه أمام اختبار حقيقي لإثبات أنه يستحق هذه القوة وأنه لن يكرر أخطاء الماضي",
        "chapters": [
            "https://drive.google.com/file/d/1lNz9rImQuwg2WijTd6HK_QHwe0CqltfC/view?usp=drivesdk",
            "https://drive.google.com/drive/folders/1VVfMgmaWmi3_7PsjOZEUiKnxMYTvYJzs",
            "https://sfl.gl/otZD7L",
            "https://drive.google.com/file/d/1muE5NEVPduzrXLFgu14ZsoEKxvYjWevb/view?usp=drivesdk",
            "https://sfl.gl/eqDuk3NE",
        ]
    },
    "tower": {
        "title": "The Skeleton Becomes A Cat",
        "genre": "الكوميدي -الرومانسية",
        "status": "مستمرة",
        "year": "2024",
        "image": "https://media.discordapp.net/attachments/1377643988827504732/1403895452621082706/Screenshot___Chrome.jpg?ex=68d927c7&is=68d7d647&hm=6b9e814f0230b6a7b6586edb93414c170b6975e8074801438ff0974cf5a69da4&=&format=webp&width=548&height=831",
        "story": "تدور القصة حول هيكل عظمي يعيش في عالم فانتازي، وبالصدفة يجد قطة صغيرة يتيمة في الغابة. بدلًا من تجاهلها يقرر الاعتناء بها ويصبح بمثابة أب لها. من هنا تبدأ مغامرة لطيفة مليئة بالكوميديا والمواقف اليومية المؤثرة، حيث يحاول الهيكل العظمي أن يتعلم كيف يكون أبًا مسؤولًا، ويهتم بالقطة من الطعام واللعب وحتى حمايتها من المخاطر",
        "chapters": [
            "https://drive.google.com/file/d/1D5AO9RicOvwBocJ1i16RuNShL_mOFaOh/view?usp=drivesdk",
            "https://drive.google.com/file/d/1zpfXsX9n58GEaDvqXCQfmpo6J9dsMsVn/view?usp=drivesdk",
            "https://drive.google.com/file/d/1aBshWnO_iEJBGZu_cTqsIDIc4eiob4hb/view?usp=drivesdk", 
            "https://sfl.gl/dvLvx",
            "https://drive.google.com/file/d/1kpLhWa9RUXdVCMXPtnMDtIRxk3Rph7ce/view?usp=drivesdk",
            "https://sfl.gl/YAFBeGD",
            "https://drive.google.com/file/d/146w-PZmXevzw1iTTWo_jsVCZ5Ahp0Tid/view?usp=drivesdk",
            "https://sfl.gl/7AAL",
            "https://drive.google.com/file/d/1lug7C0mJTlEXCzemUrOQ0kXIJDAnRyc1/view?usp=drivesdk",
            "https://sfl.gl/OIsTp",
            "https://drive.google.com/file/d/1gc64veeTGhvzJ-W6G1ck6-1KK70_zHL3/view?usp=drivesdk",
            "https://drive.google.com/file/d/1OOhGV4toc55xLsHLtcLs29U0TtQD5sUV/view?usp=drivesdk",
            "https://drive.google.com/file/d/1B9chMGgExzr8JkRGcvecAAeNHj0yaNP-/view?usp=drivesdk",
            "https://sfl.gl/aLjXTNkL",
            "https://drive.google.com/file/d/1D8op1p1u3B8rEw93LbX4E72CkMo1f9AO/view?usp=drivesdk",
            "https://sfl.gl/bvCv",
            "https://drive.google.com/file/d/1ZBoZPzSyBDXc4Q7EkvMPfGtoWJReB3Z_/view?usp=drivesdk",
            "https://sfl.gl/fjATyn",
            "https://drive.google.com/file/d/1G-CvEhFu9FTI2skoVHAA8V8R2FXeAkxD/view?usp=drivesdk",
            "https://sfl.gl/nBUDx",
            "https://drive.google.com/file/d/1M2VvDXHIEmz4v-dQILH7aeD6tXUNIzgX/view?usp=drivesdk",
            "https://sfl.gl/YjsLrof6",
            "https://drive.google.com/file/d/16sHBtKmTiDwcSUTyJRgFxJMIWfgHynKe/view?usp=drivesdk",
            "https://sfl.gl/9SAA4",
            "https://drive.google.com/file/d/1ovX8Urc-U07LN0pTdQeUJvXSkzTNvabg/view?usp=drivesdk",
            "https://sfl.gl/l6xRccqJ",
            "https://drive.google.com/file/d/1VmMJ_fkZQnaV5kVwI1jxHJqhiqPAluAx/view?usp=drivesdk",
            "https://sfl.gl/DdtKTkY",
            "https://drive.google.com/file/d/1wMxM2Ihyb-UUwmAKQrMzsth8WL3RDkCN/view?usp=drivesdk",
            "https://sfl.gl/ecHbSds",
            "https://drive.google.com/file/d/1KOvcsbcmkykPToQDA1fTWE2w0dbrF4Mf/view?usp=drivesdk",
            "https://sfl.gl/c72e",
            "https://drive.google.com/file/d/11ozng639ezi2QluSPZzJ6LS1q7qvwwjX/view?usp=drivesdk",
            "https://sfl.gl/zRZFz92S",
            "https://drive.google.com/file/d/1Y83AgDldAI7oVEug7WHvKvbZP4HTLZCD/view?usp=drivesdk",
            "https://sfl.gl/Z4KjhlE",
            #37# "",
            #38# "",
            #39# "",
            #40# "",
            #41# "",
            #42# "",
            #43# "",
            #44# "",
            #45# "",
            #46# "",
            #47# "",
            #48# "",
        ]
    },
    "Second": {
        "title": "I Won't Regret My Second Life: Happy Ending Comes After Revenge",
        "genre": " شوجو - فانتازيا - رومانسي - دراما",
        "status": "مستمرة",
        "year": " صدرت أولى فصولها في 2025",
        "image": "https://media.discordapp.net/attachments/1413966319921139942/1421650840778969249/IMG_20250816_134607.jpg?ex=68dd1ac5&is=68dbc945&hm=44afbd2c1eba8683d19c21582c85960bbf5656d8ef8e18f9ee5006eccd130d1b&=&format=webp&width=571&height=833",
        "story": "الزوج الذي أحبته، والصديقة الوحيدة الأقرب إلى قلبها التي وثقت بها... لكن على حافة الموت، أدركت سيرينييل الحقيقة. كان كل شيء مؤامرة حاكتها الأكاذيب والخيانة. في تلك اللحظة، تحول الحب إلى كراهية، وتعهدت بالانتقام. وعلى شفير اليأس، كان الشخص الذي تواصلت معه هو الدوق الذي يخشاه الجميع بوصفه 'كلب الإمبراطور'، بلا رحمة أو شفقة... وقد قدم لها شرطين فقط لمساعدتها: 'أولهما هو أن تتخلي تمامًا عن ذلك الرجل الذي لا قيمة له. وثانيهما هو...' وهكذا بدأ العقد الخطير بين الاثنين. لقد بدأت حياة سيرينييل الثانية من أجل الانتقام فقط.",
        "chapters": [
            "https://drive.google.com/drive/folders/15UJ90J4x64cu8PfWLaWQEPSDWnuybFuJ",
            "https://drive.google.com/drive/folders/1jTBSWA7mx4Na63HjYOVOLFfN355t7gow",
            "https://sfl.gl/wvUmaafx",
            "https://drive.google.com/file/d/1H7bqRKwjm8-fKY06xlp0Jn8JAvxQ79-2/view?usp=drivesdk",
            "https://sfl.gl/f2T57rn",
            "https://drive.google.com/drive/folders/1ilmdzzVfyt2NWkeApq1ixjPic4b_npei",
            "https://sfl.gl/jXZpJ",
        ]
    },
    "thierd": {
        "title": "Tale Of Hyangdan",
        "genre": " تاريخى -  خيال - دراما - رومانسى - شوجو - كوميديا",
        "status": "مستمرة",
        "year": " صدرت أولى فصولها في 2025",
        "image": "https://media.discordapp.net/attachments/1377643988827504732/1406076512687357953/z7Q6XJ.png?ex=68d92e0c&is=68d7dc8c&hm=23179592efc5cb9350730f310d49db341a7d20a792b34fdf74af9d41ffcd6e05&=&format=webp&quality=lossless&width=581&height=833",
        "story": "هو نوع كوميدي رومانسي يعيد تفسير “قصة تشون يانغ” بحساسية حديثة. البطلة الحديثة امتلكت عن طريق الخطأ هيانغ دان من تشون هيانغ جوم و تحمي تشون هيانغ من الكاهن الشرير بيون هاك دو. إنه يتعامل مع قصة تتكشف أثناء النضال من أجل شيء ما.",
        "chapters": [
            "https://drive.google.com/drive/folders/1sWQB1_2ijXNBsVNWJYnxQULkz9wd6cO2",
            "https://drive.google.com/drive/folders/1cqKLbV340baaLsAyhsdmPoGp2hQnrMz1",
            "https://drive.google.com/drive/folders/1Xk4NWoYsdXQZIFkVSEOOdq-hCwIODUwS",
            "https://sfl.gl/LOYv",
            "https://drive.google.com/drive/folders/1F5E3CrKj4V3dUtvILJdJ-3BjcK3Ng059",
            "https://sfl.gl/RbxG",
            "https://drive.google.com/drive/folders/1L8UufAeg1gMJ1WiZMWKHi3M92htT28d8",
            "https://sfl.gl/jVHHjq",
            "https://drive.google.com/drive/folders/1P-2xF7QQo9Ns59OhY1O-IllvO-kKeIY6",
            "https://sfl.gl/AkH1",
            "https://drive.google.com/drive/folders/1DBFhkQ4FYucCueljycaFwQb7QEoPkNxf",
            "https://sfl.gl/KV1n7S",
            "https://drive.google.com/drive/folders/1WY5N85DLiQBAG2MaCu3dwGFlzc1hmdz7",
            "https://sfl.gl/lSavJDX",
            "https://sfl.gl/Z13z",

        ]
    },
    "fourth": {
        "title":    "I Was Born As The Daughter Of The Kaldang Harem",
        "genre": "تاريخي - دراما - رومانسي -حياة يومية - خيال - إعادة ولادة ",
        "status":   "مستمرة",
        "year": "2021",
        "image":    "https://media.discordapp.net/attachments/1413966319921139942/1421649205729955860/image_processing20241111-2-o51aw1-1.jpg?ex=68dd193f&is=68dbc7bf&hm=84e46b6226dbf176a9e9927419f37536cbfe69c2d14b6be91557d296e310a9e4&=&format=webp&width=581&height=831",
        "story":    "تدور القصة حول فتاة من عصر حديث تجد نفسها وقد وُلدت من جديد كابنة لإحدى المحظيات داخل القصر الملكي. وسط المؤامرات السياسية وصراعات الحريم، تحاول أن تحافظ على حياتها وتشق طريقها في بيئة معقدة مليئة بالمكائد. فهل ستتمكن من تغيير مصيرها المظلم والعيش بحرية كما تشاء؟",
        "chapters": [
            "https://drive.google.com/drive/folders/1u_NC_-hsDFU9MR22CIaysaKcZ6mxmPI9",
            "https://drive.google.com/drive/folders/1pjEtIWJ-eGXcWC4p57CuHPBgkdD-sXT_",
            "https://sfl.gl/BsGaQlQ",
            "https://drive.google.com/file/d/1Ic0DsZpHsCsbRInyO--BhOjWFdpuKThz/view?usp=drivesdk",
            "https://sfl.gl/HpTtzEvK",
            "https://drive.google.com/file/d/1dWe_cDHfkz5s49oSCk3TNCOua2ll68wj/view?usp=drivesdk",
            "https://sfl.gl/0RezUC",
        ]5
    },
    "five":{
        "title":"castle-2",
        "genre":    "اكشن - تراجيدي - دراما - سينين - نفسى",
        "status":"مستمرة",
        "year":"2024",
        "image":"https://media.discordapp.net/attachments/1413966319921139942/1421649326710722603/image0.png?ex=68de6adc&is=68dd195c&hm=b25405c147917582e5a004039ff28ad5567b61719df884ed6002fcdbdc4da5d9&=&format=webp&quality=lossless&width=491&height=713",
        "story":"كيم شين، قاتلٌ بارعٌ جمع رجالًا من جميع أنحاء البلاد وأسس منظمة بايك يي لتدمير  قلعة العالم السفلي ذات السلطة المطلقة. بعد مفاوضات، دخل القلعة وبدأ العمل مع العدو... فهل سيتمكن كيم شين من هدمها وتحقيق انتقامه كما كان يأمل؟",
        "chapters": [
            "https://sfl.gl/qhmElRt0",
            "https://sfl.gl/MAP3WU8G",
            "https://sfl.gl/v0XIwkO1",
            "https://sfl.gl/7RfXmB",
            "https://sfl.gl/FvwdEI9",
            "https://sfl.gl/pVwKU",
            "https://sfl.gl/68VoKXA",
            "https://sfl.gl/27T0",
        ]
    }
}

