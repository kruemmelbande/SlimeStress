import asyncio
import sender
import time
import math
mac = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06] # change this if you want to run multilpe slimewiir sessions on the same network


async def start_connect(mac):
    s = sender.sender(mac)
    print("Starting connection to SlimeVR server...")
    await s.setup()
    print(f"Connected to server at {s.get_slimevr_ip()}")
    return s
    

    
s = asyncio.run(start_connect(mac))
for i in range(1,256):
    asyncio.run(s.create_imu(i))
    time.sleep(0.005)

print("added imus.")
while True:
    now = math.sin(time.time())
    for i in range(1,256):
        asyncio.run(s.set_quaternion_rotation(i, [now, -now, now, 2*now], resend=1))
