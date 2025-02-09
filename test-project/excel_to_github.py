import pandas as pd

def csv_to_html(csv_file, output_file="index.html"):
    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file)
    
    # 轉換成 HTML
    html_content = df.to_html(index=False)
    
    # 加上基本的 HTML 標籤
    html_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>CSV Data</title>
    </head>
    <body>
        <h2>CSV Data</h2>
        {html_content}
    </body>
    </html>
    """
    
    # 儲存成 HTML 檔案
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_page)
    
    print(f"HTML file generated: {output_file}")

# 使用範例
csv_to_html("data.csv")
