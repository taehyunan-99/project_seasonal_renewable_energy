# 오브젝트값에서 "," 제거 후 int로 형변환
def delete_comma(df):
    for col in df.columns[1:]:
        df[col] = df[col].astype(str).str.replace(',', '').astype(float).round(0).astype(int)
    return df