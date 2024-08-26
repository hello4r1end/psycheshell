PhycheShell
Overview
PhycheShell is a versatile tool designed to generate reverse shells for both Linux and Windows environments, with a specific focus on bypassing Windows Defender. It provides various options for obfuscation, encoding, SSL encryption, and persistence, making it an essential resource for cybersecurity professionals interested in understanding and mitigating potential threats.

Features
Cross-Platform Support: Generate reverse shells for both Linux and Windows.
Obfuscation: Bypass detection mechanisms through code obfuscation.
SSL Encryption: Secure your reverse shells with SSL to evade interception.
Persistence: Maintain access through various persistence techniques.
Customizable: Choose the shell type, whether to encode or obfuscate, and configure SSL settings.
Usage
1. Clone the Repository
 ```
   git clone https://github.com/hello4r1end/psycheshell.git
   cd phycheshell
   ```
2. Generate SSL Keys
To use the SSL encryption feature, you need to generate a private key and a certificate. You can do this using the following OpenSSL commands:
```
openssl genrsa -out key.pem 2048
openssl req -new -key key.pem -out csr.pem
openssl x509 -req -days 365 -in csr.pem -signkey key.pem -out cert.pem
```
3. Choose Target OS
The tool supports reverse shell generation for Linux and Windows. You can specify the target OS and the desired shell type.
```
sudo python3 psycheshell.py
```
4. Follow the Prompts
The tool will guide you through selecting the target OS, shell type, and additional options like encoding, obfuscation, and SSL encryption.
"The GIF shows how the bypass is achieved on Windows Defender, as well as with a simple antivirus like Avast."
![ezgif-2-6b22f10553](https://github.com/user-attachments/assets/81000c38-9de1-4472-b84d-4479c3e38053)
5. Set Up a Listener
Once the reverse shell is generated, you can set up a listener to capture the incoming connection if you dont want to generate automatically the listener.

For a basic listener:
```
nc -lvnp <listener-port>
```
![Screenshot 2024-08-26 193257](https://github.com/user-attachments/assets/e660784e-365b-4192-86f7-fc19aa5a7e6d)

For an encrypted listener using OpenSSL:

```
sudo openssl s_server -quiet -key key.pem -cert cert.pem -port <listener-port>
```
![Screenshot 2024-08-26 193509](https://github.com/user-attachments/assets/65839816-97c3-4e1c-be8b-b9de96b23cf6)

6. Execute the Payload
Run the generated reverse shell code on the target system. The tool provides obfuscated and/or encoded payloads to evade detection.

**Disclaimer**
PhycheShell is intended solely for educational and research purposes. This tool was created to help security professionals, ethical hackers, and researchers understand potential vulnerabilities and improve defensive measures against similar threats. Unauthorized use of this tool on systems that you do not own or have explicit permission to test is illegal and unethical.

The author is not responsible for any misuse or damage caused by this tool. Always ensure you have proper authorization before conducting any form of penetration testing or ethical hacking.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
If you'd like to contribute to the project, feel free to submit a pull request or open an issue.

Contact
For any inquiries, feel free to contact me
