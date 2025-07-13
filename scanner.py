import cv2


# Fonction principale pour scanner le QR code
def scan_qr_code():
    # Initialiser la caméra
    cap = cv2.VideoCapture(0)  # 0 pour utiliser la caméra par défaut

    if not cap.isOpened():
        print("Erreur : impossible d'accéder à la caméra.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur lors de la lecture de l'image.")
            break

        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Détecter le QR code
        detector = cv2.QRCodeDetector()
        value, pts, qr_code = detector(gray)

        if value:
            print(f"QR Code détecté: {value}")
            # Affichage du QR code détecté sur l'image
            cv2.putText(frame, f"QR Code: {value}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Afficher l'image capturée en temps réel
        cv2.imshow("Scanner QR Code", frame)

        # Quitter en appuyant sur la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer les ressources
    cap.release()
    cv2.destroyAllWindows()


# Lancer la fonction de scan
scan_qr_code()