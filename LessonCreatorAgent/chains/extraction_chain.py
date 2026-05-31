from models.lesson import LessonExtraction
from langchain.prompts.chat import ChatPromptTemplate
from models.llm import llm

def lesson_extractor_worker(lesson: LessonExtraction) -> LessonExtraction:
    prompt = ChatPromptTemplate.from_template("""
    אתה מערכת לחילוץ מידע משיעורי תורה.
    
    חלץ:
    1. כותרת השיעור
    2. פרשת השבוע
    3. המסר המרכזי הרוחני
    4. מסר פשוט לחיים
    5. סרטון השיעור
    
    כללים:
    - החזר בעברית בלבד
    - אל תעתיק משפטים ישירות
    - נסח את המסר בצורה עמוקה וברורה
    - חבר רעיונות דומים לרעיון אחד
    - אם מופיעה מטאפורה או סמליות, שלב אותה במסר המרכזי
    
    לגבי המסר המרכזי:
    - כתוב מסר עמוק ורוחני
    - עד שני משפטים
    - הניסוח צריך להישמע כמו סיכום של רב
    
    לגבי מסר לחיים:
    - כתוב את אותו רעיון בצורה פשוטה, חמה ויומיומית
    - כאילו מסבירים לילד, נער או חבר
    - קצר, ברור ונגיש
    - אפשר להשתמש בשפה יותר טבעית ופחות רשמית
    
    טקסט:
    {start_text}
    """)
    
    structured_llm = llm.with_structured_output(LessonExtraction)
    
    pipe = prompt | structured_llm

    result = pipe.invoke({
        "start_text": lesson.start_text
    })

    return result