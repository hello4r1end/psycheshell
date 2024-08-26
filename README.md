<h1>🚀 PhycheShell</h1>

<h2>🔍 Overview</h2>

<p><strong>PhycheShell</strong> is a versatile tool designed to generate reverse shells for both Linux and Windows environments, with a specific focus on bypassing Windows Defender. It provides various options for obfuscation, encoding, SSL encryption, and persistence, making it an essential resource for cybersecurity professionals interested in understanding and mitigating potential threats.</p>

<h2>✨ Features</h2>

<ul>
<li><strong>Cross-Platform Support:</strong> Generate reverse shells for both Linux and Windows.</li>
<li><strong>Obfuscation:</strong> Bypass detection mechanisms through code obfuscation.</li>
<li><strong>SSL Encryption:</strong> Secure your reverse shells with SSL to evade interception.</li>
<li><strong>Persistence:</strong> Maintain access through various persistence techniques.</li>
<li><strong>Customizable:</strong> Choose the shell type, whether to encode or obfuscate, and configure SSL settings.</li>
</ul>

<h2>💻 Usage</h2>

<h3>📂 Clone the Repository</h3>
<pre>
<code>
git clone https://github.com/hello4r1end/phycheshell.git
cd phycheshell
</code>
</pre>


<h3>🔑 Generate SSL Keys</h3>
<p>To use the SSL encryption feature, you need to generate a private key and a certificate. You can do this using the following OpenSSL commands:</p>
<pre>
<code>
openssl genrsa -out key.pem 2048
openssl req -new -key key.pem -out csr.pem
openssl x509 -req -days 365 -in csr.pem -signkey key.pem -out cert.pem
</code>
</pre>

<h3>⚙️ Choose Target OS</h3>
<p>The tool supports reverse shell generation for Linux and Windows. You can specify the target OS and the desired shell type.</p>
<pre>
<code>
sudo python3 phycheshell.py
</code>
</pre>

<h3>🚦 Follow the Prompts</h3>
<p>The tool will guide you through selecting the target OS, shell type, and additional options like encoding, obfuscation, and SSL encryption.</p>
<p><em>The GIF below shows how the bypass is achieved on Windows Defender, as well as with a simple antivirus like Avast.</em></p>

![ezgif-2-45f2122007](https://github.com/user-attachments/assets/3c693f5b-069b-4af7-b754-a1bf9f800d3b)

<h3>🎧 Set Up a Listener</h3>
<p>Once the reverse shell is generated, you can set up a listener to capture the incoming connection if you don't want to generate the listener automatically.</p>

<p><strong>For a basic listener:</strong></p>
<pre>
<code>
nc -lvnp &lt;listener-port&gt;
</code>
</pre>

![Screenshot 2024-08-26 193257](https://github.com/user-attachments/assets/e660784e-365b-4192-86f7-fc19aa5a7e6d)

<p><strong>For an encrypted listener using OpenSSL:</strong></p>
<pre>
<code>
sudo openssl s_server -quiet -key key.pem -cert cert.pem -port &lt;listener-port&gt;
</code>
</pre>

![Screenshot 2024-08-26 193509](https://github.com/user-attachments/assets/65839816-97c3-4e1c-be8b-b9de96b23cf6)

<h3>🚀 Execute the Payload</h3>
<p>Run the generated reverse shell code on the target system. The tool provides obfuscated and/or encoded payloads to evade detection.</p>

<h2>⚠️ Disclaimer</h2>

<p><strong>PhycheShell</strong> is intended <strong>solely for educational and research purposes</strong>. This tool was created to help security professionals, ethical hackers, and researchers understand potential vulnerabilities and improve defensive measures against similar threats. <strong>Unauthorized use of this tool on systems that you do not own or have explicit permission to test is illegal and unethical.</strong></p>

<p>The author is not responsible for any misuse or damage caused by this tool. Always ensure you have proper authorization before conducting any form of penetration testing or ethical hacking.</p>

<h2>🤝 Contributing</h2>

<p>If you'd like to contribute to the project, feel free to submit a pull request or open an issue.</p>

<h2>📧 Contact</h2>

<p>For any inquiries, feel free to contact me.</p>
Contributing
If you'd like to contribute to the project, feel free to submit a pull request or open an issue.

Contact
For any inquiries, feel free to contact me
