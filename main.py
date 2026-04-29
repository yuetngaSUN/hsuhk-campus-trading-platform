from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os

app = FastAPI()

# 终极 CORS 配置（绝对不允许改成 True ！！！）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "campustrading.db"

# 创建或初始化轻量级数据库（SQLite）
def init_db():
    # 如果数据库文件不存在，就创建一个并塞入初始数据
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # 这里我帮你加了 image_url 字段！！！
        cursor.execute('''
            CREATE TABLE items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                seller TEXT NOT NULL,
                image_url TEXT DEFAULT 'default'
            )
        ''')
        
        initial_items = [
            ("Mechanical Keyboard", 350.0, "Electronics", "Like new, blue switches.", "Yueya", "default"),
            ("MacBook Pro M1", 6500.0, "Computers", "Used for 1 year, battery 95%.", "Xuanye", "default"),
            ("Calculus Textbook", 120.0, "Books", "A few highlights, otherwise clean.", "Yueya", "default"),
            ("Espresso Coffee Machine", 450.0, "Appliances", "Works perfectly.", "Xuanye", "default")
        ]
        
        cursor.executemany('''
            INSERT INTO items (name, price, category, description, seller, image_url)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', initial_items)
        
        conn.commit()
        conn.close()

# FastAPI 启动时自动建库
@app.on_event("startup")
def startup_event():
    init_db()

# 每次拿数据用的函数
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # 这样返回的数据才能变成字典
    return conn

# 前端发来的商品数据模型（支持 image_url 了）
class Item(BaseModel):
    name: str
    price: float
    category: str
    description: Optional[str] = None
    seller: str
    image_url: str = 'default'


@app.get("/")
async def root():
    return {"message": "Campus Trading Backend with SQLite - Online!", "docs": "/docs"}

# 读商品列表
@app.get("/items")
async def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return items

# 发商品
@app.post("/items")
async def create_item(item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO items (name, price, category, description, seller, image_url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (item.name, item.price, item.category, item.description, item.seller, item.image_url))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"message": "Item created successfully", "id": new_id}

# 删商品
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM items WHERE id = ?", (item_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"message": "Item deleted successfully"}
