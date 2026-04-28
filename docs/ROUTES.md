# 路由設計: 讀書筆記本 (Reading Notebook)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| **首頁列表** | `GET` | `/` | `index.html` | 顯示所有的讀書筆記列表 |
| **搜尋筆記** | `GET` | `/search` | `index.html` (共用) | 透過 `?q=關鍵字` 查詢並呈現搜尋結果 |
| **新增頁面** | `GET` | `/add` | `add.html` | 顯示新增書籍筆記的表單 |
| **建立筆記** | `POST` | `/add` | — | 接收表單並將資料寫入 DB，完成後重導回 `/` |
| **編輯頁面** | `GET` | `/edit/<int:note_id>` | `edit.html` | 顯示修改既有筆記的表單 |
| **更新筆記** | `POST`| `/edit/<int:note_id>` | — | 接收表單更新項目，存入 DB，重導回 `/` |
| **刪除筆記** | `POST`| `/delete/<int:note_id>`| — | 執行刪除特定 ID 筆記，完成後重導回 `/` |

## 2. 每個路由的詳細說明

### 任務清單 (`GET /`)
- **處理邏輯**：呼叫 `NoteModel.get_all()` 獲取所有紀錄。
- **輸出**：渲染 `index.html` 模板，並將資料集以變數傳入以繪製列表。

### 搜尋功能 (`GET /search`)
- **輸入**：URL Query String `q`（例如 `/search?q=Python`）。
- **處理邏輯**：從 Request 取得 `q` 參數。若無參數則導向首頁；若有參數則呼叫 `NoteModel.search(keyword)`。
- **輸出**：渲染 `index.html` 模板，但是只顯示符合條件的筆記。

### 新增功能 (`GET /add` 與 `POST /add`)
- **輸入 (GET)**：無。
- **輸出 (GET)**：渲染 `add.html`，顯示包含書名 (title)、心得 (content)、評分 (rating) 的表單。
- **輸入 (POST)**：`request.form` 取出欄位。
- **處理邏輯**：若必填欄位為空則不予處理或返回錯誤；合規則呼叫 `NoteModel.create()` 寫入。
- **輸出 (POST)**：`redirect(url_for('note.index'))`，返回首頁。

### 編輯功能 (`GET /edit/<note_id>` 與 `POST /edit/<note_id>`)
- **輸入 (GET)**：路徑參數 `note_id`。
- **處理邏輯**：呼叫 `NoteModel.get_by_id(note_id)` 取得既有紀錄，若無該紀錄回傳 404 錯誤。
- **輸出 (GET)**：渲染 `edit.html`，並將既有資料傳入以便填入表單。
- **輸入 (POST)**：`request.form` 修改後的欄位資料。
- **處理邏輯**：呼叫 `NoteModel.update()` 更新目標內容。
- **輸出 (POST)**：`redirect(url_for('note.index'))`，返回首頁。

### 刪除功能 (`POST /delete/<note_id>`)
- **處理邏輯**：使用 `POST` 方法可以防範惡意的 GET 請求造成的 CSRF 誤刪除風險。後端呼叫 `NoteModel.delete(note_id)` 移除紀錄。
- **輸出**：`redirect(url_for('note.index'))` 回到首頁。

## 3. Jinja2 模板清單

建立在 `app/templates/` 內的 Jinja2 模板預備清單：
1. **`base.html`**：基礎共版，包含 `<html>`, 導覽列, 共用的 CSS 與 JS。
2. **`index.html`**：繼承 `base.html`，用來顯示首頁筆記清單與搜尋卡片。
3. **`add.html`**：繼承 `base.html`，顯示新增表單。
4. **`edit.html`**：繼承 `base.html`，顯示編輯表單。

## 4. 路由骨架程式碼
開發人員可參考已建立的 `app/routes/note_routes.py`。
