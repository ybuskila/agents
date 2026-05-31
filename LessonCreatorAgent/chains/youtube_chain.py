from models.lesson import LessonExtraction
from services.youtube_service import find_youtube_link

def lesson_youtube_link_loader(lesson: LessonExtraction) -> LessonExtraction:    
    lesson.youtube_link=find_youtube_link(lesson.lesson_title)
    return lesson