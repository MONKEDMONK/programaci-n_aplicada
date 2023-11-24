import machine
import network
import urequests
import time

# Reemplazar con los datos de tu red WiFi
ssid = "Honor X7"
password = "Hola Rateros"

# Inicializar BOT Telegram
BOTtoken = "6862462489:AAE15Uzh_NDDdaBt8l7WkCfFzq0slLybObU"  # Tu Bot Token (Obtener de Botfather)
CHAT_ID = "6674626409"

buz_pin = machine.Pin(25, machine.Pin.OUT)
motion_sensor_pin = machine.Pin(27, machine.Pin.IN)

motion_detected = False

def detects_movement(pin):
    global motion_detected
    motion_detected = True

motion_sensor_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=detects_movement)

# Configurar la conexión WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    time.sleep(1)

print("Conexión WiFi exitosa")
print("Dirección IP:", wifi.ifconfig()[0])

# Inicializar el bot de Telegram
def send_message(chat_id, text):
    url = "https://api.telegram.org/bot{}/sendMessage".format(BOTtoken)
    data = {"chat_id": chat_id, "text": text}
    urequests.post(url, json=data)

send_message(CHAT_ID, "Bot iniciado")

# Bucle principal
try:
    while True:
        # Verificar nuevos mensajes de Telegram
        response = urequests.get("https://api.telegram.org/bot{}/getUpdates?offset={}".format(BOTtoken, bot.last_message_received + 1))
        messages = response.json().get("result", [])
        response.close()
        if messages:
            for message in messages:
                chat_id = str(message["message"]["chat"]["id"])
                if chat_id != CHAT_ID:
                    send_message(chat_id, "Usuario No Autorizado")
                    continue

                text = message["message"]["text"]

                if text == "/alarma_on":
                    send_message(chat_id, "Alarma activada")
                    buz_pin.value(1)

                if text == "/alarma_off":
                    send_message(chat_id, "Alarma desactivada")
                    buz_pin.value(0)

        # Manejar detección de movimiento
        if motion_detected:
            send_message(CHAT_ID, "¡Movimiento detectado!")
            motion_detected = False

        time.sleep(1)

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario")

finally:
    wifi.disconnect()
    print("Desconectado de la red WiFi")
    machine.reset()
