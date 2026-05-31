from pydantic import BaseModel, Field, validator

class LessonExtraction(BaseModel):
    class Config:        
        populate_by_name = True
        
    start_text: str = Field(
        description="הטקסט שהבאת מהשיעור",
        alias="טקסט התחלתי"
    )
    
    lesson_title: str = Field(
        description="כותרת השיעור",
        alias="כותרת השיעור",
        default=None
    )

    weekly_torah_portion: str = Field(
        description="פרשת השבוע",
        alias="פרשת השבוע",
        default=None
    )

    central_message: str = Field(
        description=(
            "המסר המרכזי של השיעור "
            "בניסוח רוחני, עמוק ותמציתי "
            "של עד שני משפטים"
        ),
        alias="המסר המרכזי",
        default=None
    )

    relatable_message: str = Field(
        description=(
            "אותו רעיון מרכזי אך בניסוח פשוט, "
            "קליל ונגיש שמתאים לשיחה עם ילד, נער או חבר"
        ),
        alias="מסר לחיים",
        default=None
    )

    youtube_link: str = Field(
        description="השיעור ב youtube",
        alias="סרטון השיעור",
        default=None
    )