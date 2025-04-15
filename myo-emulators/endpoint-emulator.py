from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/public/mawj/confirm_appointment/<appointment_id>", methods=["GET"])
def confirm_appointment(appointment_id):
    print(f"[✅] Confirming appointment: {appointment_id}")
    return jsonify({
        "success": True,
        "message": f"Appointment {appointment_id} confirmed successfully"
    })

@app.route("/public/mawj/cancel_appointment/<appointment_id>", methods=["GET"])
def cancel_appointment(appointment_id):
    print(f"[❌] Cancelling appointment: {appointment_id}")
    return jsonify({
        "success": True,
        "message": f"Appointment {appointment_id} cancelled successfully"
    })

if __name__ == "__main__":
    app.run(port=5005)


# eyJpdiI6IndwWm0vTHZobHFVVWs5dzdkN0szbmc9PSIsInZhbHVlIjoiNDBJajlLeENkaUpHNkU5TzhjV1ZpQT09IiwibWFjIjoiMGI5Y2JkNThkZWVlNTgwYzY4NzBlZjE4YzVhYWVlZmZmNTZhMzhmZjJkNzU1NzdiNzkxMDdlYjc2ZDM2ODkwMCIsInRhZyI6IiJ9