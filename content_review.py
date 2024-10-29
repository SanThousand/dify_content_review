from fastapi import FastAPI,HTTPException,Header,Body
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

def load_key_word():
    
    file_name = "key_word.txt"
    
    if os.path.exists(file_name) is not True:
        raise HTTPException(status_code=404, detail=f"File'{file_name}' not found")
    
    #初始化敏感词列表
    key_word = []
    try:
        with open(file_name, "r", encoding='utf-8') as f:
            for line in f:
                key_word.append(line.strip())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading key words from {file_name}: {str(e)}")
    
    return key_word


# 定义请求模型，用于验证请求数据的格式
class ModerationInput(BaseModel):
    point: str
    params: dict = {}
    

#创建一个路由处理函数，用于处理内容审查请求，dify请求的接口
@app.post("/api/dify/receive")
async def dify_recive(data: ModerationInput, authorization: str = Header(...)):
    expected_api_key = "123456"
    auth_scheme, _, api_key = authorization.partition(' ')
    if auth_scheme.lower() != "bearer" or api_key != expected_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    point = data.point
    params = data.params
    print("point: ", point)
    print("params: ", params)
    
    if point == "ping":
        return {
            "result": "pong"
        }
    
    if point == "app.moderation.input":
        return handle_moderation_request(params)
    
def handle_moderation_request(params: dict):
    """
    处理用户审查输入内容审查
    """
    inputs = params.get("inputs", {})
    query = params.get("query", "")
    
    key_word = load_key_word()
    
    # print("key_word: ", key_word)
    
    if any(word in query or any(word in value for value in inputs.values()) for word in key_word):
            return {
                    "flagged": True,
                    "action": "direct_output",
                    "preset_response": "您的内容违反了我们的使用政策。"
                    }
    else:
        return {"flagged": False,
                "action": "direct_output"
                }

if __name__ == "__main__":
    uvicorn.run("content_review:app", host="0.0.0.0", port=8000, reload=True)