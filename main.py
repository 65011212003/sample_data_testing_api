from faker import Faker
from tinydb import TinyDB, Query
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize Faker and TinyDB
fake = Faker()
db = TinyDB('db.json')

# Create FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a Query object
User = Query()

# Generate and store 1000 fake records
for _ in range(1000):
    fake_user = {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'phone': fake.phone_number(),
        'job': fake.job(),
        'image': f"https://i.pravatar.cc/150?u={fake.uuid4()}"  # Add random avatar image
    }
    db.insert(fake_user)

# Create endpoint to serve db.json
@app.get("/db.json")
async def get_db():
    return db.all()

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
