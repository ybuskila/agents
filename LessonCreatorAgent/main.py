from chains.save_chain import state_gr_worker
from models.lesson import LessonExtraction    

lesson = LessonExtraction(
    start_text = """
        ותרת השיעור: לתת זה לקבל שיעור מפי הרב שמואל סעדון בשבת פרשת בהעלותך המסר העיקרי של הסיפור האדם הוא לא פרטי הוא צריך לתת מעצמו לכלל גם מי שנמצא בצד הרוחני לגמרי (למשל לומד כל היום תורה) וגם מי שנמצא כל היום בפרנסה צריכים שניהם להסתכל לכיוון האמצע (שהוא האלוהים) המנורה מקשה אחת היא ושני הצדדים צריכים להסתכל עליה.
    """
)
result = state_gr_worker.invoke(lesson)

print(result)