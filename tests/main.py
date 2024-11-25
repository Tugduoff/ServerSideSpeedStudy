import httpx
import asyncio
import time

async def test_speed():
    async with httpx.AsyncClient() as client:
        start_time = time.time()
        response = await client.get("http://127.0.0.1:8000/")
        end_time = time.time()
        print(f"GET / - Status: {response.status_code}, Time: {end_time - start_time:.4f} seconds")

        start_time = time.time()
        response = await client.get("http://127.0.0.1:8000/items/1?q=test")
        end_time = time.time()
        print(f"GET /items/1?q=test - Status: {response.status_code}, Time: {end_time - start_time:.4f} seconds")

        start_time = time.time()
        response = await client.get("http://127.0.0.1:8000/user/15/workspace/1/board/19/list/3/card/5")
        end_time = time.time()
        print(f"GET /user/15/workspace/1/board/19/list/3/card/5 - Status: {response.status_code}, Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(test_speed())
