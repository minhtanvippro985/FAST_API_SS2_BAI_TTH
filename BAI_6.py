from fastapi import FastAPI , HTTPException

app = FastAPI()


courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    }
]

@app.get("/health")
def system_check():
    return {
        "message" : "API IS RUNNING"
    }

@app.get("/courses")
def get_courses():
    if len(courses) == 0:
        return{
            "message":"Hiện không có khóa học nào",
            "data" : []
        }
    else:
        return{
            "message" : "Danh sách khóa học",
            "data" : courses
        }
    
@app.get("/courses/{course_id}")
def get_courses_details(course_id :int):
    if course_id <= 0:
        raise HTTPException(status_code=400 , detail="Mã không được là số <=0")
        

    for course in courses:
        if course['id'] == course_id:
            found = True
            return{
                "message" : "Thông tin chi tiết của khóa học",
                "data" : course
            }

    raise HTTPException(status_code=404 , detail=f"Không tìm thấy khóa học có id {course_id}") 
    
    