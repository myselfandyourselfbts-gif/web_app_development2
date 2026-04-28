# 流程圖設計: 讀書筆記本 (Reading Notebook)

## 1. 使用者流程圖（User Flow）
此流程圖描述使用者在系統中「新增筆記」與「搜尋筆記」的操作路徑。

```mermaid
flowchart LR
    A([使用者進入首頁]) --> B{想做什麼？}
    B -->|新增筆記| C[點擊「新增」按鈕]
    C --> D[填寫書籍資訊與心得、評分]
    D --> E[送出表單]
    E --> F([返回首頁並顯示新筆記列表])
    
    B -->|搜尋筆記| G[在搜尋框輸入關鍵字]
    G --> H[點擊搜尋或按 Enter]
    H --> I[頁面顯示符合關鍵字的搜尋結果]
    I --> F([從結果點擊返回或首頁])
```

## 2. 系統序列圖（Sequence Diagram）
描述「新增筆記」與「搜尋筆記」背後的系統互動流程，包含瀏覽器與 Flask MVC 之間的資料流動。

### 2.1 新增筆記流程
```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser
    participant Flask as Flask Route
    participant Model as Database Model
    participant DB as SQLite

    User->>Browser: 填寫表單送出 (Title, Content, Rating)
    Browser->>Flask: POST /add (Form Data)
    Flask->>Model: 呼叫 add_note(title, content, rating)
    Model->>DB: INSERT INTO notes...
    DB-->>Model: 寫入成功
    Model-->>Flask: 成功狀態
    Flask-->>Browser: 302 Redirect 重導向至首頁 (/)
    Browser->>User: 顯示已包含新資料的首頁列表
```

### 2.2 搜尋筆記流程
```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser
    participant Flask as Flask Route
    participant Model as Database Model
    participant DB as SQLite

    User->>Browser: 輸入關鍵字並送出
    Browser->>Flask: GET /search?q=關鍵字
    Flask->>Model: 呼叫 search_notes(keyword)
    Model->>DB: SELECT * FROM notes WHERE title LIKE '%keyword%' OR ...
    DB-->>Model: 回傳多筆符合條件的 Records
    Model-->>Flask: 回傳字典陣列 (List of dict/Objects)
    Flask-->>Browser: 渲染 search_results.html
    Browser->>User: 呈現搜尋結果列表
```

## 3. 功能清單對照表

| 功能名稱 | 對應 URL 路徑 | HTTP 方法 | 功能說明 |
| :--- | :--- | :--- | :--- |
| **首頁列表** | `/` | `GET` | 讀取所有筆記並渲染列表畫面 |
| **新增頁面** | `/add` | `GET` | 顯示新增表單頁面（如需獨立頁面，亦可實作於首頁對話框） |
| **新增處理** | `/add` | `POST` | 接收新增表單內的資料並寫入資料庫 |
| **搜尋筆記** | `/search` | `GET` | 讀取 URL 參數 `?q=` 執行模糊搜尋並顯示結果 |
