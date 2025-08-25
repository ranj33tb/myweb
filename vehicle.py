import requests, brotli, zlib, json

headers = {
    "user-agent": "Mozilla/5.0",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "cookie": "trackerid=ec605b28-f369-4835-8e12-8f1004f4b835; acko_visit=eumN889AK19m1MFcrfgoRg; _gcl_au=1.1.707375770.1753788732; _gid=GA1.2.874984606.1753788733; _fbp=fb.1.1753788734208.696259702773011507; _hjSessionUser_3514615=eyJpZCI6Ijg2MGQ3MGIyLTdiYTMtNTkzMS04ZjlkLWJiMjBiYTNmYzMzNCIsImNyZWF0ZWQiOjE3NTM3ODg3MzQ3ODMsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_3514615=eyJpZCI6ImNiMTdlNjlmLTU4ZjAtNDUwNi1iY2IwLWMxYjFiNWFhZGMzOCIsImMiOjE3NTM3ODg3MzQ3ODUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _clck=1f2u5il%7C2%7Cfy0%7C0%7C2036; __cf_bm=ElhInRPrcTwzyJb9hdmqeU8gnFFK50PJuA3AnF9Gy78-1753788741-1.0.1.1-yUwnoimZ.8quczjLDYNwLfQa8.qAzWgYmUCZS4yAv9cZ1lgTk7go6WEKm1xELdSV9BNYVmv_APyKbpM84_molnCA10DkbcBdNYDLDt.DeZI; user_id=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJFUHhtZUwzV0hDLTVsNTQ1VHNld2kwYTU3SFRlZy0ySXpmZk9zM0hOUEhNIn0.eyJleHAiOjE3NTM3OTA1NjEsImlhdCI6MTc1Mzc4ODc2MSwiYXV0aF90aW1lIjoxNzUzNzg4NzYwLCJqdGkiOiJlM2JjMzU4OS1lOWIxLTQ0NjYtODQ2Zi1jODBlZWE5NWM3MDMiLCJpc3MiOiJodHRwczovL2NlbnRyYWwtYXV0aC1wcm9kLmludGVybmFsLmxpdmUuYWNrby5jb20vcmVhbG1zL2Fja28iLCJzdWIiOiJOdXNSaVRxSTBlSFFaeVY2R2FTNjR3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYWNrb193ZWJhcHAiLCJzZXNzaW9uX3N0YXRlIjoiOTQ5NDcxOTQtOTFhZC00YTdjLTgxYTItNzczNjM4OGY0MmRkIiwic2NvcGUiOiJvZmZsaW5lX2FjY2VzcyIsInNpZCI6Ijk0OTQ3MTk0LTkxYWQtNGE3Yy04MWEyLTc3MzYzODhmNDJkZCJ9.rT3MWPPotDLGAUR0O3_pI8aR0MN610UBncpA1rjVadO-9FY6nbXIkxFXuPpXt9fmQ_QLSbG-DdrIRlgOOyNka_7f5HrQTMAY3ELHeU6eHTXnGyAcTTR09QIchQ513yYlEQnt-ZOHgb9xp0jUaJ-_TRnOnMx1rh4i7Q3BGAikXzYCHcAuSXBQLn55c76CWEr3gI7v0mZSlc6exIl67gDk5hAiRgOT5TlyCcnjE5LSitSHjSvNzh61cjdv-GY6ypeWI9deGfVcWnRLfwv1MsQwMm_wezrclgcZ5DlL_bRChi9vzpuAE7_3HRtOU6dM0tZAhO3mQMouqH8h9u9ZjseNJA; refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIwZmVmYzE3Yi03OGUwLTRkZjUtOGI4OC1iZmVmNDlkMGRkZTgifQ.eyJpYXQiOjE3NTM3ODg3NjEsImp0aSI6IjIxMjgyN2E0LTc4MjEtNDdkZS1hZDE2LTdkMzgyNmMxNDgzNCIsImlzcyI6Imh0dHBzOi8vY2VudHJhbC1hdXRoLXByb2QuaW50ZXJuYWwubGl2ZS5hY2tvLmNvbS9yZWFsbXMvYWNrbyIsImF1ZCI6Imh0dHBzOi8vY2VudHJhbC1hdXRoLXByb2QuaW50ZXJuYWwubGl2ZS5hY2tvLmNvbS9yZWFsbXMvYWNrbyIsInN1YiI6Ik51c1JpVHFJMGVIUVp5VjZHYVM2NHciLCJ0eXAiOiJPZmZsaW5lIiwiYXpwIjoiYWNrb193ZWJhcHAiLCJzZXNzaW9uX3N0YXRlIjoiOTQ5NDcxOTQtOTFhZC00YTdjLTgxYTItNzczNjM4OGY0MmRkIiwic2NvcGUiOiJvZmZsaW5lX2FjY2VzcyIsInNpZCI6Ijk0OTQ3MTk0LTkxYWQtNGE3Yy04MWEyLTc3MzYzODhmNDJkZCJ9.LSMaugQ-9B1T9IcE-dHOuHX7FIzwlcp0Jk15g18dA78; _ga=GA1.1.2097642092.1753788733; _ga_W47KBK64MF=GS2.1.s1753788734$o1$g0$t1753788766$j28$l0$h0; _uetsid=aca6af306c6f11f0a6dbd1d155cd43f0; _uetvid=aca715806c6f11f0ba9bc93318dc1431; wisepops=%7B%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A54%2C%22cid%22%3A%2267186%22%2C%22v%22%3A5%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_session=%7B%22arrivalOnSite%22%3Anull%2C%22mtime%22%3A1753788768187%2C%22pageviews%22%3A0%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22embeds%22%3A%7B%7D%2C%22sticky%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3Anull%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D; _clsk=g7w3s5%7C1753788769466%7C2%7C1%7Cq.clarity.ms%2Fcollect"
    }
base_url = "https://www.acko.com"

def fetch_data(url):
    try:
        response = requests.get(url, headers=headers, stream=True)
        encoding = response.headers.get("Content-Encoding", "")
        raw = response.raw.read()

        if response.status_code != 200:
            return {"error": f"status {response.status_code}"}

        if "br" in encoding:
            decoded = brotli.decompress(raw).decode("utf-8")
        elif "gzip" in encoding:
            decoded = zlib.decompress(raw, zlib.MAX_WBITS | 16).decode("utf-8")
        elif "deflate" in encoding:
            decoded = zlib.decompress(raw).decode("utf-8")
        else:
            decoded = raw.decode("utf-8")

        return json.loads(decoded)
    except Exception as e:
        return {"error": str(e)}

def get_vehicle_info(vehicle_number: str):
    vehicle_url = f"{base_url}/asset_service/api/assets/search/vehicle/{vehicle_number}?validate=false&source=vas_fastag"
    puc_url = f"{base_url}/vas/api/v1/pucs?registration-number={vehicle_number}"
    challan_url = f"{base_url}/vas/api/v1/challans/?registration-number={vehicle_number}&source=CHALLAN_PAGE"

    return {
        "vehicle": fetch_data(vehicle_url),
        "pollution": fetch_data(puc_url),
        "challan": fetch_data(challan_url)
    }

# Optional: agar tum directly python vehicle.py run karte ho
if __name__ == "__main__":
    num = input("Enter Vehicle Number: ").strip().upper()
    result = get_vehicle_info(num)
    print(json.dumps(result, indent=2))
