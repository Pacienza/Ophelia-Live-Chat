from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "VLinfo_LuVi0801"
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def gerenciar_mensagem(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)




@app.route("/")
def hello():
    return render_template("index.html")

    ########a parte a seguir é um de projeto de login que vou implementar no futuro

    # user_ip = request.remote_addr
    # if user_ip in user_ip_data:
    #    username = user_ip_data[user_ip]
    #    return render_template("chat.html", username=username)
    # else:
    #    return render_template("login.html")

# @app.route("/set_username", methods=["POST"])
# def setUsername():
#     user_ip = request.remote_addr
#     username = request.form.get("username")
#     user_ip_data[user_ip] = username
#     response = make_response(redirect("/"))
#     response.set_cookie("username", username)
#     return response



if __name__ == "__main__":
    socketio.run(app, host="localhost") #substitui isso aq pelo seu ip
