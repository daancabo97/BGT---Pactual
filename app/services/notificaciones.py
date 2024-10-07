
def enviar_notificacion(tipo: str, destinatario: str, mensaje: str):
        """
        Envía una notificación al cliente por email o SMS.
        Args:
            tipo (str): Tipo de notificación ("email" o "sms").
            destinatario (str): Destinatario del mensaje.
            mensaje (str): Contenido del mensaje.
        """
        if tipo == "email":
            
            print(f"Enviando email a {destinatario}: {mensaje}")
        elif tipo == "sms":
            
            print(f"Enviando SMS a {destinatario}: {mensaje}")
