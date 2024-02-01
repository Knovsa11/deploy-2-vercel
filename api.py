# fastapi --> membuat api
# uvicorn --> menjalankan api/server
from fastapi import FastAPI, HTTPException, Request, Response
import pandas as pd
# membuat object fastAPI

app = FastAPI()

# dataFrame
df = pd.DataFrame({
    "names" : ['kelvin', 'hyuga', 'tsubasa'],
    "location" : ['Tangerang', 'Toho', 'Nankatsu']
})

# # mendaftarkan endpoint (alamat contoh gramedia/categories/buku) atau url
# @app.get('/') # halaman utama
# def getHome(request: Request):
#     # melihat isi headers dari request(informasi tambahan)
#     headers = request.headers


#     # membuat response
#     response = Response("ini halaman utama")

#     # return json data
#     return {
#         "req-headers" : headers,
#         "response-headers": response.headers,
#         "response-body" : response.body
#     } 

@app.get('/') # halaman utama
def getHome(request: Request):
    # return json data
    return {
        "message" : "ini halaman utama"
    } 
@app.get('/names/{name}')
def findName(name):
    #filter df
    result = df[df['names']==name]
    # jika ada data -> tampilkan
    #jika tidak ada data --> error 404
    if len(result) == 0:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    else:
    # return hasil filter 
        return result.to_dict(orient='records')



@app.get('/see-all') # halaman see all
def getSeeAll():
    # return json data
    # return data from dataframe
    return df.to_dict(orient='records')

## python -m uvicorn api:app --reload
# running di terminal                            

