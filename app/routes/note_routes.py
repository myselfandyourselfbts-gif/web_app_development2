from flask import Blueprint, request, render_template, redirect, url_for

# 建立名為 note 的 Blueprint，以便將路由與主程式 app.py 分離
note_bp = Blueprint('note', __name__)

@note_bp.route('/')
def index():
    """
    [GET] 首頁列表
    讀取資料庫中所有讀書筆記，並渲染 index.html 顯示。
    """
    pass

@note_bp.route('/search')
def search():
    """
    [GET] 搜尋筆記
    從 Query String 中取得 `q` 參數，如果存在則以模糊查詢過濾書籍清單，
    然後渲染 index.html 將結果顯示給使用者。
    """
    pass

@note_bp.route('/add', methods=['GET', 'POST'])
def add():
    """
    [GET] 渲染新增筆記表單 (add.html)。
    [POST] 接收表單資料 (title, content, rating)，寫入資料庫後重導至首頁 (/)。
    """
    pass

@note_bp.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit(note_id):
    """
    [GET] 依據 note_id 取出特定筆記，渲染 edit.html 準備進行編輯。如果無此筆記則回報 404。
    [POST] 接收要更新的表單資料，寫入資料庫後重導至首頁 (/)。
    """
    pass

@note_bp.route('/delete/<int:note_id>', methods=['POST'])
def delete(note_id):
    """
    [POST] 安全性考量，刪除使用 POST 方法。
    依據 note_id 執行特定筆記的刪除操作後，重導至首頁 (/)。
    """
    pass
