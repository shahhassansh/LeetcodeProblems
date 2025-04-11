import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    data = {
        "student_id": [],
        "age": []
    }
    for x in student_data:
        data["student_id"].append(x[0])
        data["age"].append(x[1])
    return pd.DataFrame(data)
    
