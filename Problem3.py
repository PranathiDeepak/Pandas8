import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].nunique().reset_index()
    courses_filtered = courses[courses['student']>=5 ]
    return courses_filtered[['class']]