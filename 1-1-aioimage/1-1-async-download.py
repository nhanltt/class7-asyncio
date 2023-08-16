import io
import time
import asyncio
import aiohttp, aiofiles
from PIL import Image

unsplash_search_url = "https://source.unsplash.com/random/300x300"

async def download_image_async(session: aiohttp.ClientSession, num: int = 1):
    print(f"{time.ctime()} - Start download image {num}")
    async with session.get(unsplash_search_url) as response:
        if response.status == 200:
            image_buffer = await response.read()
            img = Image.open(io.BytesIO(image_buffer))
            print(f"{time.ctime()} = Image {num} shape: {img.size}")

    async with aiofiles.open(f'./filename{num}.jpg', "wb") as new_file:
        print(f"{time.ctime()} - Writing to 'filename{num}.jpg'...")
        await new_file.write(image_buffer)

async def download_images_async(n: int = 10):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(session, i + 1) for i in range(n)]
        _ = await asyncio.gather(*tasks)

    return

if __name__ == "__main__":
    tick = time.perf_counter()
    asyncio.run(download_images_async())
    tock = time.perf_counter()
    print(f"{time.ctime()} = elapsed: {tock-tick:.2f} seconds")

# Running Result
# Wed Aug 16 13:23:55 2023 - Start download image 1
# Wed Aug 16 13:23:55 2023 - Start download image 2
# Wed Aug 16 13:23:55 2023 - Start download image 3
# Wed Aug 16 13:23:55 2023 - Start download image 4
# Wed Aug 16 13:23:55 2023 - Start download image 5
# Wed Aug 16 13:23:55 2023 - Start download image 6
# Wed Aug 16 13:23:55 2023 - Start download image 7
# Wed Aug 16 13:23:55 2023 - Start download image 8
# Wed Aug 16 13:23:55 2023 - Start download image 9
# Wed Aug 16 13:23:55 2023 - Start download image 10
# Wed Aug 16 13:23:56 2023 = Image 1 shape: (300, 300)
# Wed Aug 16 13:23:56 2023 - Writing to 'filename1.jpg'...
# Wed Aug 16 13:23:56 2023 = Image 10 shape: (300, 300)
# Wed Aug 16 13:23:56 2023 - Writing to 'filename10.jpg'...
# Wed Aug 16 13:23:56 2023 = Image 8 shape: (300, 300)
# Wed Aug 16 13:23:56 2023 - Writing to 'filename8.jpg'...
# Wed Aug 16 13:23:56 2023 = Image 7 shape: (300, 300)
# Wed Aug 16 13:23:56 2023 - Writing to 'filename7.jpg'...
# Wed Aug 16 13:23:56 2023 = Image 6 shape: (300, 300)
# Wed Aug 16 13:23:56 2023 - Writing to 'filename6.jpg'...
# Wed Aug 16 13:23:56 2023 = Image 3 shape: (300, 300)
# Wed Aug 16 13:23:56 2023 - Writing to 'filename3.jpg'...
# Wed Aug 16 13:23:56 2023 = Image 4 shape: (300, 300)
# Wed Aug 16 13:23:56 2023 - Writing to 'filename4.jpg'...
# Wed Aug 16 13:23:56 2023 = Image 2 shape: (300, 300)
# Wed Aug 16 13:23:56 2023 - Writing to 'filename2.jpg'...
# Wed Aug 16 13:23:57 2023 = Image 5 shape: (300, 300)
# Wed Aug 16 13:23:57 2023 - Writing to 'filename5.jpg'...
# Wed Aug 16 13:23:57 2023 = Image 9 shape: (300, 300)
# Wed Aug 16 13:23:57 2023 - Writing to 'filename9.jpg'...
# Wed Aug 16 13:23:57 2023 = elapsed: 2.91 seconds