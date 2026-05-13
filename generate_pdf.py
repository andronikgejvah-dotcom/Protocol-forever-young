from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT = "/home/user/Protocol-forever-young/сценарии_forever_young.pdf"

GOLD = HexColor("#c9a96e")
DARK = HexColor("#0e0c10")
DARK2 = HexColor("#18151f")
LIGHT = HexColor("#f0ece4")
GREY = HexColor("#888888")
RED = HexColor("#e8534a")

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
    title="Сценарии прогрева · Forever Young · Andronik"
)

styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

title_style = S("Title2", fontSize=28, textColor=GOLD, alignment=TA_CENTER,
                spaceAfter=6, fontName="Helvetica-Bold", leading=34)
sub_style = S("Sub", fontSize=11, textColor=GREY, alignment=TA_CENTER,
              spaceAfter=4, fontName="Helvetica")
h2_style = S("H2", fontSize=16, textColor=GOLD, spaceAfter=8,
             fontName="Helvetica-Bold", spaceBefore=16)
badge_style = S("Badge", fontSize=9, textColor=white, fontName="Helvetica-Bold",
                backColor=GOLD, spaceAfter=4, borderPadding=(3,8,3,8))
badge_launch_style = S("BadgeLaunch", fontSize=9, textColor=white,
                        fontName="Helvetica-Bold", backColor=RED,
                        spaceAfter=4, borderPadding=(3,8,3,8))
video_title_style = S("VTitle", fontSize=20, textColor=LIGHT, spaceAfter=3,
                       fontName="Helvetica-Bold")
stage_style = S("Stage", fontSize=9, textColor=GOLD, spaceAfter=12,
                fontName="Helvetica", leading=13)
script_style = S("Script", fontSize=12, textColor=LIGHT,
                  fontName="Helvetica", leading=20, spaceAfter=8,
                  leftIndent=12)
shoot_head_style = S("ShootH", fontSize=9, textColor=GOLD, fontName="Helvetica-Bold",
                      spaceAfter=6, spaceBefore=4, textTransform="uppercase")
shoot_style = S("Shoot", fontSize=11, textColor=GREY, fontName="Helvetica",
                leading=17, spaceAfter=4, leftIndent=14)
footer_style = S("Footer", fontSize=9, textColor=GREY, alignment=TA_CENTER)

elems = []

# COVER
elems.append(Spacer(1, 1.5*cm))
elems.append(Paragraph("FOREVER YOUNG", title_style))
elems.append(Paragraph("Сценарии прогрева · Andronik · День 365 · Лонч первого потока", sub_style))
elems.append(Spacer(1, 0.4*cm))
elems.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=20))
elems.append(Spacer(1, 0.5*cm))

# SCHEDULE TABLE
elems.append(Paragraph("Расписание публикаций", h2_style))
sched_data = [
    ["День", "Видео", "Платформы"],
    ["День 361", "#0 — Origin Story · «Два типа мужчин»", "TG + Instagram + TikTok"],
    ["День 362", "#1 — «362 дня подряд»", "TG + Instagram + TikTok"],
    ["День 363", "#2 — «Почему стареют неправильно»", "TG + Instagram + TikTok"],
    ["День 364", "#3 — «10 лет системы»", "TG + Instagram + TikTok"],
    ["День 365 🔥", "#4 — ЛОНЧ · Первый поток", "Telegram — тёплая аудитория"],
]
sched_table = Table(sched_data, colWidths=[3*cm, 9*cm, 5.5*cm])
sched_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GOLD),
    ("TEXTCOLOR", (0,0), (-1,0), DARK),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 9),
    ("BACKGROUND", (0,1), (-1,-1), DARK2),
    ("TEXTCOLOR", (0,1), (-1,-1), LIGHT),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-1), 10),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#18151f"), HexColor("#1e1a27")]),
    ("GRID", (0,0), (-1,-1), 0.5, HexColor("#2a2530")),
    ("PADDING", (0,0), (-1,-1), 8),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TEXTCOLOR", (0,5), (0,5), RED),
    ("FONTNAME", (0,5), (0,5), "Helvetica-Bold"),
]))
elems.append(sched_table)
elems.append(Spacer(1, 1*cm))

# VIDEOS
videos = [
    {
        "num": "0",
        "day": "ДЕНЬ 361",
        "launch": False,
        "title": "Origin Story",
        "stage": "Стадия: Неосведомлённый · Посеять вопрос через историю",
        "script": [
            "Я из военного рода.",
            "На семейных праздниках я видел два типа мужчин — большие и толстые, и стройные, в хорошей спортивной форме.",
            "Уже тогда я знал к какому лагерю присоединюсь.",
            "В 14 лет сделал штангу из палки и пластиковых бутылок — качался всё лето. В университете начал изучать йогу, китайский массаж, танцы, акупрессуру — жил в Дубае, Москве, Бали, собирал систему всю жизнь.",
            "Следующие 3 дня покажу что из этого получилось.",
        ],
        "shoot": [
            "Сидишь, прямо в камеру, крупный план лица",
            "Пауза после «военного рода» — дай секунду тишины",
            "Говоришь спокойно, как другу, без суеты",
            "Без музыки в начале",
            "Длина: 40–50 сек",
        ],
    },
    {
        "num": "1",
        "day": "ДЕНЬ 362",
        "launch": False,
        "title": "362 дня подряд",
        "stage": "Стадия: Неосведомлённый · Зацепить фактом",
        "script": [
            "362 дня подряд. Каждый день. Ни одного пропуска.",
            "Была авария на байке. Разбитая нога. Температура. Всё на видео.",
            "Я всё равно вставал на руки.",
            "Не потому что псих — потому что система работает даже когда ты не можешь.",
            "Следующие 3 дня покажу эту систему. Бесплатно. Всё.",
        ],
        "shoot": [
            "Открываешь кадром стойки на руках — рассвет Бали",
            "Разворачиваешься в камеру, говоришь стоя",
            "B-roll: архив с байком если есть",
            "Длина: 30–40 сек",
        ],
    },
    {
        "num": "2",
        "day": "ДЕНЬ 363",
        "launch": False,
        "title": "Почему стареют неправильно",
        "stage": "Стадия: Осознание проблемы · Назвать боль + дать инструмент",
        "script": [
            "Большинство людей в 35 начинают стареть. Просыпаются уставшими. Спина болит без причины. Пробуют зал, диеты, йогу — через месяц откат.",
            "Проблема не в лени. Никто не учил работать с телом как с системой.",
            "Один инструмент прямо сейчас — техника 5-10-15.",
            "5 глубоких медленных вдохов и выдохов — задержка дыхания 30 секунд. 10 вдохов и выдохов — задержка 30 секунд. 15 вдохов и выдохов — задержка сколько можешь.",
            "Успокаивает нервную систему лучше любого успокоительного. Делай утром.",
            "Завтра покажу откуда берётся вся система.",
        ],
        "shoot": [
            "Говоришь стоя или сидя, энергично",
            "Когда перечисляешь 5-10-15 — показываешь пальцами",
            "Показываешь как делаешь сам — задержка дыхания, камера крупно на лицо",
            "Длина: 50–60 сек",
        ],
    },
    {
        "num": "3",
        "day": "ДЕНЬ 364",
        "launch": False,
        "title": "10 лет системы",
        "stage": "Стадия: Осознание решения · Показать механизм и экспертизу",
        "script": [
            "10 лет. Университет — китайская медицина, акупрессура, йога, движение, танцы. Потом Дубай, Москва, Бали. Тренеры-друзья по всему миру.",
            "Я не читал про это в книгах — я жил в этом.",
            "Все эти практики работают. Но только когда это система, а не рандомные упражнения.",
            "Вот одна точка прямо сейчас — Хэ-гу. Между большим и указательным пальцем. Нажми, держи 30 секунд. Убирает воспаление, даёт энергию.",
            "Завтра — День 365. Расскажу кое-что важное.",
        ],
        "shoot": [
            "Стоишь, природа Бали на фоне",
            "Крупный план руки — оператор зумит на точку Хэ-гу",
            "Пауза перед «завтра день 365»",
            "Длина: 50–60 сек",
        ],
    },
    {
        "num": "4",
        "day": "ДЕНЬ 365 · ЛОНЧ 🔥",
        "launch": True,
        "title": "Первый поток открыт",
        "stage": "Стадия: Максимальная осведомлённость · Прямая продажа",
        "script": [
            "Сегодня День 365. Год без пропусков.",
            "Авария на байке, сломанная нога, температура — я не остановился.",
            "Открываю первый поток. 4 места.",
            "Два Zoom — сначала диагностирую тебя, потом показываю твою утреннюю практику. Всё.",
            "$500. Два основателя. Пиши @andron_dicktatoora — слово FOREVER.",
        ],
        "shoot": [
            "Открываешь лучшим кадром стойки — рассвет, самый красивый из всего года",
            "Садишься, смотришь в камеру спокойно и уверенно",
            "Текст на экране: $500 · @andron_dicktatoora · FOREVER",
            "Публикуешь только в Telegram — тёплая аудитория",
            "Длина: 20–30 сек",
        ],
    },
]

for v in videos:
    block = []
    badge_s = badge_launch_style if v["launch"] else badge_style
    block.append(Paragraph(v["day"], badge_s))
    block.append(Spacer(1, 0.2*cm))
    block.append(Paragraph(f"#{v['num']} — {v['title']}", video_title_style))
    block.append(Paragraph(v["stage"], stage_style))
    block.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#2a2530"), spaceAfter=10))

    # Script box
    script_rows = [[Paragraph(line, script_style)] for line in v["script"]]
    st = Table(script_rows, colWidths=[16.5*cm])
    st.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), DARK2),
        ("LEFTPADDING", (0,0), (-1,-1), 16),
        ("RIGHTPADDING", (0,0), (-1,-1), 16),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LINEAFTER", (0,0), (0,-1), 3, GOLD),
        ("ROUNDEDCORNERS", [4,4,4,4]),
    ]))
    block.append(st)
    block.append(Spacer(1, 0.3*cm))

    # Shoot plan
    block.append(Paragraph("ПЛАН СЪЁМКИ", shoot_head_style))
    for s in v["shoot"]:
        block.append(Paragraph(f"— {s}", shoot_style))

    block.append(Spacer(1, 0.8*cm))
    block.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#2a2530"), spaceAfter=20))
    elems.append(KeepTogether(block))

# SHOOT SCHEDULE
elems.append(Spacer(1, 0.5*cm))
elems.append(Paragraph("Порядок съёмки · Одно утро", h2_style))
shoot_data = [
    ["Время", "Что снимаем"],
    ["06:00", "Стойка на руках — рассвет, лучший кадр (для #1 и #4)"],
    ["06:30", "Видео #4 — Лонч · пока эмоция от утра живая"],
    ["07:00", "Видео #0 — Origin Story"],
    ["07:20", "Видео #1 — День 362"],
    ["07:40", "Видео #2 — Проблема + дыхание 5-10-15"],
    ["08:00", "Видео #3 — Система + точка Хэ-гу крупным планом"],
    ["08:20", "B-roll запас — движение, руки, Бали, взгляды"],
]
shoot_table = Table(shoot_data, colWidths=[2.5*cm, 14.5*cm])
shoot_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), GOLD),
    ("TEXTCOLOR", (0,0), (-1,0), DARK),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,0), 9),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#18151f"), HexColor("#1e1a27")]),
    ("TEXTCOLOR", (0,1), (-1,-1), LIGHT),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,1), (-1,-1), 10),
    ("GRID", (0,0), (-1,-1), 0.5, HexColor("#2a2530")),
    ("PADDING", (0,0), (-1,-1), 8),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))
elems.append(shoot_table)

elems.append(Spacer(1, 1*cm))
elems.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=12))
elems.append(Paragraph("Forever Young · andronik.pro · @andron_dicktatoora", footer_style))

doc.build(elems)
print(f"PDF создан: {OUTPUT}")
