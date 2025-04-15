from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO
import logging

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# WebSocket log handler
class WebSocketLogger(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        socketio.emit('log_message', {'data': log_entry})

# Attach handler
log_handler = WebSocketLogger()
log_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
log_handler.setFormatter(formatter)
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

@app.route("/")
def home():
    return render_template("logs.html")

@app.route("/public/mawj/confirm_appointment/<appointment_id>", methods=["GET"])
def confirm_appointment(appointment_id):
    app.logger.info(f"✅ Confirming appointment: {appointment_id}")
    return jsonify({"success": True, "message": f"Appointment {appointment_id} confirmed successfully"})

@app.route("/public/mawj/cancel_appointment/<appointment_id>", methods=["GET"])
def cancel_appointment(appointment_id):
    app.logger.info(f"❌ Cancelling appointment: {appointment_id}")
    return jsonify({"success": True, "message": f"Appointment {appointment_id} cancelled successfully"})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
