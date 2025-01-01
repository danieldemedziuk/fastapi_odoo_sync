import httpx

NAV_URL = "https://nav-server:7048/BC/ODataV4/Company('MyCompany')/Customers"

async def fetch_nav_data(skip=0, top=100):
    """
    Pobiera dane z NAV z wykorzystaniem OData.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            NAV_URL,
            params={"$top": top, "$skip": skip},
            headers={"Authorization": "Bearer <your-token>"}
        )
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
