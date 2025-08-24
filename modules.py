# 오브젝트값에서 "," 제거 후 int로 형변환
def delete_comma(df):
    for col in df.columns[1:]:
        # df[col] = df[col].astype(str).str.replace(',', '').astype(float).apply(lambda x: int(x) if x.is_integer() else int(round(x)))
        df[col] = df[col].astype(str).str.replace(',', '').astype(float).round(0).astype(int)
    return df

# 이용률 계산
def get_capacity_factor(ic, gen):
    pass