from umqtt.simple import MQTTClient
import json

class Tuple:
    def __init__(self, broker, room, etype="m.room.message", client="esp-tuple"):
        self.client = MQTTClient(client, broker)
        self.room = room
        self.etype = etype
        self.client.connect()

    def get_send_topic(self):
        return str.encode("_tuple/client/r0/rooms/" + self.room + "/send/" + self.etype)

    def send(self, data, text=None):
        topic = self.get_send_topic()
        mx_msg = {
            "msgtype": "de.eiselecloud.weather",
            "body": text or repr(data),
            "weather": data
        }
        msg = str.encode(json.dumps(mx_msg))
        self.client.publish(topic, msg)

    def done(self):
        self.client.disconnect()
