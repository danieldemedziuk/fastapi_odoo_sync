from fastapi import FastAPI, BackgroundTasks
from app.tasks import fetch_and_sync_data

app = FastAPI()

@app.post("/sync-data")
async def sync_data(background_tasks: BackgroundTasks):
    """
    Pobiera dane z NAV i synchronizuje je z Odoo.
    """
    background_tasks.add_task(fetch_and_sync_data)
    return {"status": "Synchronizacja rozpoczęta"}
