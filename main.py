from pyrogram import Client
import time as t

api_id = 29151511
api_hash = '2936b4e3d67f93bfeaf016c4a4699a7e'

app = Client("my_account", api_id=api_id, api_hash=api_hash)

while True:
    async def main():
        async with app:
            await app.send_message(-1001249763625, '/tea')
            t.sleep(1)
            await app.send_message(-1001249763625, '/coffee')


    app.run(main())
    t.sleep(3600)