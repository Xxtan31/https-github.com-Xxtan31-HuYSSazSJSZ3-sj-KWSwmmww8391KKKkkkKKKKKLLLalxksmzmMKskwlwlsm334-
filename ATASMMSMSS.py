from telethon import TelegramClient, events

# API kimlik bilgilerinizi buraya girin
api_id = '2271684'
api_hash = '4bc323bef24cc0e119eb7360e832d42'
phone_number = '+905303948093'

# Kaynak ve hedef kanalların ID'lerini buraya girin
kaynak_kanal_id = 2165954150  # Örneğin: -1001234567890
hedef_kanal_id = 4139654383  # Örneğin: -1009876543210

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    try:
        # Kaynak kanaldan en eski mesajdan başlayarak en son mesaja kadar al
        async for mesaj in client.iter_messages(kaynak_kanal_id):
            try:
                # Mesajı hedef kanala ilet
                await client.send_message(hedef_kanal_id, mesaj)
                print(f"Mesaj {mesaj.id} hedef kanala iletildi.")
            except Exception as e:
                print(f"Mesaj {mesaj.id} hedef kanalına iletilirken hata oluştu: {e}")
            
            # Her mesajdan sonra 50 saniye bekle
            await asyncio.sleep(50)
    
    except Exception as e:
        print(f"Mesaj alınırken hata oluştu: {e}")

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
