from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "/home/user/Protocol-forever-young/diagnostic_forever_young.pdf"

GOLD  = HexColor("#c9a96e")
DARK  = HexColor("#0e0c10")
DARK2 = HexColor("#18151f")
LIGHT = HexColor("#f0ece4")
GREY  = HexColor("#888888")
LINE  = HexColor("#2a2530")

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    rightMargin=1.8*cm, leftMargin=1.8*cm,
    topMargin=1.8*cm, bottomMargin=1.8*cm,
    title="Диагностика · Forever Young · Andronik"
)

def S(name, **kw): return ParagraphStyle(name, **kw)

title_s  = S("T", fontSize=24, textColor=GOLD, alignment=TA_CENTER, fontName="Helvetica-Bold", leading=28, spaceAfter=4)
sub_s    = S("Sub", fontSize=10, textColor=GREY, alignment=TA_CENTER, fontName="Helvetica", spaceAfter=2)
sec_s    = S("Sec", fontSize=8, textColor=GOLD, fontName="Helvetica-Bold", leading=10,
             spaceBefore=14, spaceAfter=6, textTransform="uppercase", letterSpacing=2)
q_s      = S("Q", fontSize=10, textColor=LIGHT, fontName="Helvetica-Bold", leading=14, spaceAfter=2)
opt_s    = S("Opt", fontSize=9, textColor=GREY, fontName="Helvetica", leading=12, spaceAfter=1, leftIndent=10)
line_s   = S("Line", fontSize=9, textColor=HexColor("#3a3040"), fontName="Helvetica", leading=18)
note_s   = S("Note", fontSize=8, textColor=GREY, fontName="Helvetica", leading=11, spaceAfter=10)
client_s = S("Client", fontSize=12, textColor=LIGHT, fontName="Helvetica", leading=16)

def section(title):
    return [
        Spacer(1, 0.2*cm),
        HRFlowable(width="100%", thickness=0.5, color=LINE, spaceAfter=6),
        Paragraph(title, sec_s),
    ]

def question(text, options=None, lines=1):
    items = [Paragraph(text, q_s)]
    if options:
        row = "   ".join([f"☐ {o}" for o in options])
        items.append(Paragraph(row, opt_s))
    else:
        for _ in range(lines):
            items.append(Paragraph("_" * 95, line_s))
    return items

def two_questions(q1, opts1, q2, opts2):
    left = [Paragraph(q1, q_s), Paragraph("   ".join([f"☐ {o}" for o in opts1]), opt_s)]
    right = [Paragraph(q2, q_s), Paragraph("   ".join([f"☐ {o}" for o in opts2]), opt_s)]
    left_p  = [[p] for p in left]
    right_p = [[p] for p in right]
    lt = Table(left_p,  colWidths=[8.5*cm]); lt.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    rt = Table(right_p, colWidths=[8.5*cm]); rt.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1)]))
    t = Table([[lt, rt]], colWidths=[9*cm, 9*cm])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),4),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
    return [t]

elems = []

# COVER
elems.append(Spacer(1, 0.5*cm))
elems.append(Paragraph("FOREVER YOUNG", title_s))
elems.append(Paragraph("Диагностика клиента · Andronik · Личная консультация", sub_s))
elems.append(Spacer(1, 0.3*cm))
elems.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=14))

# CLIENT HEADER
header_data = [
    [Paragraph("Имя клиента:", client_s), Paragraph("_" * 38, line_s),
     Paragraph("Дата:", client_s), Paragraph("_" * 20, line_s)],
]
ht = Table(header_data, colWidths=[3*cm, 7*cm, 2*cm, 5*cm])
ht.setStyle(TableStyle([
    ("VALIGN",(0,0),(-1,-1),"BOTTOM"),
    ("LEFTPADDING",(0,0),(-1,-1),0),
    ("RIGHTPADDING",(0,0),(-1,-1),6),
    ("BOTTOMPADDING",(0,0),(-1,-1),2),
]))
elems.append(ht)
elems.append(Spacer(1, 0.3*cm))

# ─── 1. БАЗОВЫЕ ДАННЫЕ ───
elems += section("1 · Базовые данные")
meas = [
    ["Возраст", "Пол", "Рост", "Вес"],
    [Paragraph("_"*18, line_s), Paragraph("☐ М   ☐ Ж", opt_s), Paragraph("_"*14, line_s), Paragraph("_"*14, line_s)],
]
mt = Table(meas, colWidths=[4*cm, 3.5*cm, 3.5*cm, 3.5*cm])
mt.setStyle(TableStyle([
    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,0),8),
    ("TEXTCOLOR",(0,0),(-1,0),GREY),
    ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),6),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),("TOPPADDING",(0,0),(-1,-1),2),
]))
elems.append(mt)
elems.append(Spacer(1, 0.2*cm))

meas2 = [
    ["Бицепс (пик)", "Грудь", "Талия", "Бёдра", "Нога (бедро)"],
    [Paragraph("_"*13, line_s), Paragraph("_"*13, line_s), Paragraph("_"*13, line_s), Paragraph("_"*13, line_s), Paragraph("_"*13, line_s)],
]
mt2 = Table(meas2, colWidths=[3.5*cm, 3.5*cm, 3.5*cm, 3.5*cm, 3.5*cm])
mt2.setStyle(TableStyle([
    ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,0),8),
    ("TEXTCOLOR",(0,0),(-1,0),GREY),
    ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),("TOPPADDING",(0,0),(-1,-1),2),
]))
elems.append(mt2)

# ─── 2. ОБРАЗ ЖИЗНИ ───
elems += section("2 · Образ жизни")
elems += two_questions(
    "Работа", ["Сидячая", "Смешанная", "Физическая"],
    "Тренировки сейчас", ["Не тренируется", "1–2 р/нед", "3–4 р/нед", "Каждый день"]
)
elems += two_questions(
    "Сон (часов)", ["менее 5", "5–6", "7–8", "больше 8"],
    "Просыпается", ["Легко, бодрым", "Тяжело, разбитым", "По-разному"]
)
elems += two_questions(
    "Энергия в течение дня", ["Стабильная", "Спад после обеда", "Постоянная усталость", "Скачет"],
    "Уровень стресса (1–5)", ["1", "2", "3", "4", "5"]
)

# ─── 3. ПИТАНИЕ ───
elems += section("3 · Питание")
elems += two_questions(
    "Тип питания", ["Всеядный", "Вегетарианец", "Веган", "Кето", "Другое"],
    "Мясо", ["Ежедневно", "Несколько р/нед", "Редко", "Не ем"]
)
elems += two_questions(
    "Сахар / сладкое", ["Каждый день", "Иногда", "Редко", "Не ем"],
    "Кофе", ["Не пью", "1 чашка", "2–3 чашки", "3+ чашек"]
)
elems += two_questions(
    "Молочные продукты", ["Ежедневно", "Иногда", "Не ем", "Непереносимость"],
    "Глютен", ["Ем нормально", "Ограничиваю", "Непереносимость / целиакия"]
)
elems += question("Пищевые аллергии и непереносимости:", lines=1)
elems += question("Питание в целом (своими словами):", lines=2)

# ─── 4. ВРЕДНЫЕ ПРИВЫЧКИ ───
elems += section("4 · Вредные привычки")
elems += two_questions(
    "Курение", ["Не курит", "Курит", "Бросил", "Вейп"],
    "Алкоголь", ["Не пьёт", "Редко", "1–2 р/нед", "Часто"]
)
elems += question("Другие вещества / препараты:", ["Нет", "Иногда", "Регулярно"])

# ─── 5. ЗДОРОВЬЕ ───
elems += section("5 · Здоровье")
elems += question("Хронические заболевания:", lines=1)
elems += question("Травмы, операции, ограничения:", lines=1)
elems += question("Текущие медикаменты:", lines=1)
elems += question("Текущие БАДы (что уже принимает):", lines=1)
elems += question("Анализы крови (если есть — D3, B12, ферритин, магний, гормоны):", lines=1)

elems.append(Paragraph("Симптомы (отметить всё что есть):", q_s))
symptoms = [
    ["☐ Усталость", "☐ Плохой сон", "☐ Выпадение волос", "☐ Ломкие ногти"],
    ["☐ Сухая кожа", "☐ Акне / воспаления", "☐ Боли в суставах", "☐ Боль в спине"],
    ["☐ Слабый иммунитет", "☐ Вздутие / газы", "☐ Нарушение пищеварения", "☐ Низкое либидо"],
    ["☐ Тревожность", "☐ Туман в голове", "☐ Отёки", "☐ Холодные руки/ноги"],
]
sym_rows = [[Paragraph(c, opt_s) for c in row] for row in symptoms]
st = Table(sym_rows, colWidths=[4.5*cm, 4.5*cm, 4.5*cm, 4.5*cm])
st.setStyle(TableStyle([
    ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),2),
    ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
]))
elems.append(st)
elems.append(Spacer(1, 0.2*cm))

# ─── 6. ПИЩЕВАРЕНИЕ ───
elems += section("6 · Пищеварение")
elems += two_questions(
    "Работа кишечника", ["Регулярно, нормально", "Вздутие/газы", "Запоры", "Диарея", "Чередуется"],
    "Ощущение после еды", ["Лёгкость", "Тяжесть", "Сонливость", "Вздутие"]
)

# ─── 7. КОЖА И FACE BUILDING ───
elems += section("7 · Кожа и Face Building")
elems += two_questions(
    "Тип кожи лица", ["Нормальная", "Сухая", "Жирная", "Комбинированная", "Чувствительная"],
    "Проблемы кожи", ["Акне", "Морщины", "Пигментация", "Отёки лица", "Дряблость", "Нет"]
)
elems += question("Интерес к Face Building:", ["Да, главная цель", "Да, как дополнение", "Пока нет"])
elems += question("Что хочет улучшить в лице:", lines=1)

# ─── 8. ЦЕЛИ ───
elems += section("8 · Цели и мотивация")
elems.append(Paragraph("Главная цель (отметить всё):", q_s))
goals = ["☐ Похудеть", "☐ Набрать мышцы", "☐ Рельеф", "☐ Больше энергии",
         "☐ Здоровье изнутри", "☐ Лицо и внешность", "☐ Антивозрастное", "☐ Всё вместе"]
goal_rows = [[Paragraph(goals[i], opt_s), Paragraph(goals[i+1], opt_s)] for i in range(0, len(goals), 2)]
gt = Table(goal_rows, colWidths=[9*cm, 9*cm])
gt.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2)]))
elems.append(gt)
elems.append(Spacer(1, 0.2*cm))
elems += question("Конкретный запрос (его словами):", lines=2)
elems += question("Почему сейчас? Что триггернуло:", lines=1)
elems += question("Бюджет на БАДы в месяц:", ["до $30", "$30–70", "$70–150", "без ограничений"])
elems += question("Пробовал раньше — что и почему бросил:", lines=1)

# ─── 9. ЗАМЕТКИ ───
elems += section("9 · Заметки Андроника")
elems += question("БАДы выписать:", lines=2)
elems += question("Упор в тренировках:", lines=1)
elems += question("Особые ограничения / противопоказания:", lines=1)
elems += question("Впечатление от человека / дополнительно:", lines=2)

elems.append(Spacer(1, 0.5*cm))
elems.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=10))
elems.append(Paragraph("Forever Young · andronik.pro · @Dicktatoora", S("F", fontSize=8, textColor=GREY, alignment=TA_CENTER)))

doc.build(elems)
print(f"PDF создан: {OUTPUT}")
