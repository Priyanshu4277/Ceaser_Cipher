import string
import socket



# Set up a socket connection to me (default port is 5000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hn = socket.gethostname()

sock.connect((hn, 5000))


def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char in string.ascii_letters:
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(ciphertext):
    for shift in range(26):
        decrypted_text = caesar_decrypt(ciphertext, shift)

        query = f'Tell me whether the text is meaningfull or not, if any part of the text meaningful give me output "Meaningfull" if it not is meaningfull your response should be only "Notmeaningfull". text: "{decrypted_text}"'

        # Send the message
        sock.sendall(str.encode(decrypted_text))

        # Receive the response
        data = sock.recv(1024)
        
        conf = data.decode("utf-8")

        if conf =="Meaningfull":
            print(f"Shift {shift}: {decrypted_text}")
            sock.close()
            break



# Example usage
ciphertext = "Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn."
brute_force_caesar(ciphertext)
