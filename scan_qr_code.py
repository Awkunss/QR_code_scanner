
# import cv2
# from pyzbar.pyzbar import decode

# def scan_qr():
#     cap = cv2.VideoCapture(0)  # Mở camera
#     while True:
#         _, frame = cap.read()
#         qr_codes = decode(frame)
#         for qr_code in qr_codes:
#             qr_data = qr_code.data.decode('utf-8')
#             print(f"QR Code detected: {qr_data}")
#             cap.release()
#             return qr_data  # Trả về mã hash từ QR code
#         cv2.imshow('QR Code Scanner', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()


