from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import asyncio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Я рад приветствовать Вас в команде профессионалов АО «НК «ҚТЖ»! Теперь Вы работник системообразующего транспортно-логистического холдинга Казахстана. Миссией АО «НК «ҚТЖ» является обеспечение качественной основы устойчивого роста бизнеса наших клиентов, служение на пользу потребителям и обществу в целом путем оказания безопасных и конкурентоспособных перевозочных услуг. Нажмите /help для подробной информации")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
    Эти команды помогут вам узнать больше о нашей компании:
    
    /start -> Приветствие
    /help -> Команды
    /content -> Новости
    /Systems -> Система обучения и развития
    /Holidays -> Отпуска
    /Instructions -> Прохождение вводного инструктажа
    /Skillup -> Возможности для работников
    /contact -> Как с нами связаться
    """)

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Последние новости : https://youtu.be/T3UgNCAQEqs?si=Uw8Do9vW9S5iUalY")

async def systems_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("СИСТЕМА ОБУЧЕНИЯ И РАЗВИТИЯ : Принцип 70/20/10 заключается в следующем: 70% обучения происходит через практику, включая самостоятельное выполнение задач, участие в новых проектах для приобретения навыков и стажировку; 20% — обучение на рабочем месте с коучем или наставником, менторство и обратная связь; и 10% — традиционное обучение, включая курсы, тренинги, семинары и самостоятельное изучение материалов.")

async def holidays_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("ОТПУСКА : Согласно коллективному договору, отпуск составляет: для центрального аппарата 30 дней, для филиалов 28 дней, с добавлением 2 дней за каждый последующий год работы, но не более 6 календарных дней, при этом одна часть отпуска не может быть менее 14 дней. Отпуск можно переносить на следующий год. В случае необходимости взять отпуск вне графика на несколько дней, это нужно согласовать с непосредственным начальником. Коллективный договор на 2021-2023 годы можно найти на сайте КТЖ в разделе Цкард и библиотека документов.")

async def instructions_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("ПРОХОЖДЕНИЕ ВВОДНОГО ИНСТРУКТАЖА : При оформлении приема на работу ответственный работник Департамента/службы по управлению персоналом обеспечивает: направление вновь принятых работников, командированных, стажеров, учащихся и студентов, прибывших на производственное обучение или практику, в соответствующие службы для прохождения инструктажа; получение подписи ответственных работников служб пожарной безопасности, безопасности и охраны труда в заявлении/приказе о приеме на работу о проведении вводного противопожарного инструктажа, вводного инструктажа по безопасности и охране труда.")

async def skillup_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("ВОЗМОЖНОСТИ ДЛЯ РАБОТНИКОВ : молодежная политика, жилищная политика, управление преемственностью, карьерное развитие, соцпакет, премии, обучение, наставничество, признание, корпоративные мероприятия")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Вы можете связаться с нами по следующим контактным данным: 8 (7172) 60 30 30")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"You said {update.message.text}, use the commands using /")

async def main() -> None:
    application = ApplicationBuilder().token("7394382443:AAFWCfMK1Tc290FOhIGNUPqQoIRVAw6OcCk").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("content", content))
    application.add_handler(CommandHandler("Systems", systems_command))
    application.add_handler(CommandHandler("Holidays", holidays_command))
    application.add_handler(CommandHandler("Instructions", instructions_command))
    application.add_handler(CommandHandler("Skillup", skillup_command))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await application.run_polling()

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
