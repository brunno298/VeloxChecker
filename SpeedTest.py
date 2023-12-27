import speedtest

def exibir_banner():
    banner = '''
    ███████╗░░█████╗░███████╗███████╗███╗░░░███╗
    ██╔══██╗██╔══██╗╚════██║██╔════╝████╗░████║
    ██████╔╝██║░░██║░░░░██╔╝█████╗░░██╔████╔██║
    ██╔═══╝░██║░░██║░░░██╔╝░██╔══╝░░██║╚██╔╝██║
    ██║░░░░░╚█████╔╝░░░██╔╝░░███████╗██║░╚═╝░██║
    '''
    print(banner)

def exibir_template(nome, instagram):
    template = f'''
               {nome}       Instagram: @{instagram}
    '''

    print(template)

def testar_velocidade():
    st = speedtest.Speedtest()

    print("Iniciando VELOX...\n")
    
    exibir_banner()

    print("\nTestando latência...")
    st.get_best_server()  # Esse método realiza a medição de latência automaticamente
    latencia = st.results.ping
    print(f"Latência: {latencia} ms")

    print("\nTestando velocidade de download...")
    download_speed = st.download() / 10**6  # Convertendo para megabits por segundo
    print(f"Velocidade de Download: {download_speed:.2f} Mbps")

    print("\nTestando velocidade de upload...")
    upload_speed = st.upload() / 10**6  # Convertendo para megabits por segundo
    print(f"Velocidade de Upload: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    testar_velocidade()
