import pandas as pd

text='VERSION BUILD=1011 RECORDER=CR' '\n' 'URL GOTO=https://www.monotaro.id/s018248883.html' '\n' 'WAIT SECONDS=3' '\n' 'TAG POS=1 TYPE=BUTTON FORM=ID:product_addtocart_form ATTR=ID:product-addtocart-button' '\n' 'WAIT SECONDS=3' '\n' 'TAG POS=1 TYPE=A ATTR=TXT:Lihat<SP>keranjang<SP>belanja' '\n' 'WAIT SECONDS=3'

result=[]
for x in range(100):
    for i in text.split('\n'):
        result.append(i)

df1=pd.DataFrame(result)
df1.to_csv('result_concate.csv')
