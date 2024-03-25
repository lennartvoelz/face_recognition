from imports import pd, requests, cv2, np

firebase_url = "https://database-dc7f0-default-rtdb.europe-west1.firebasedatabase.app/images.json"

response = requests.get(firebase_url)

data = response.json()
data_list = [value for key, value in data.items()]

df = pd.DataFrame(data_list)
df = df[["name", "url"]]

def download_image(url, name):
    response = requests.get(url)
    image_data = response.content
    array = bytearray(image_data)

    image = cv2.imdecode(np.asarray(array, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite(f"../data/{name}.jpg", image)

def download_all():
    for index, row in df.iterrows():
        download_image(row["url"], row["name"])