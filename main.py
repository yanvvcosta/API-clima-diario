import schedule
import time
from datetime import datetime
from weather import get_weather_forecast
from clothing import recomendar_roupa
from whatsapp import WhatsAppNotifier

def job():
    """Tarefa executada às 6h da manhã"""
    print(f"⏰ Executando job em {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    # Obter clima
    clima = get_weather_forecast()
    if not clima:
        print("❌ Não foi possível obter a previsão do tempo")
        return
    
    # Gerar recomendação
    recomendacao = recomendar_roupa(
        clima["temp_max"], 
        clima["temp_min"], 
        clima["chance_chuva"], 
        clima["vento"]
    )
    
    # Inicializar WhatsApp
    whatsapp = WhatsAppNotifier()
    
    # Formatar mensagem
    mensagem = whatsapp.formatar_mensagem(clima, recomendacao)
    
    # Enviar
    print(f"📤 Enviando mensagem: {mensagem[:100]}...")
    whatsapp.enviar_mensagem(mensagem)

def main():
    """Configura o agendador"""
    # Agendar para todos os dias às 06:00
    schedule.every().day.at("06:00").do(job)
    
    print("🚀 Agendador iniciado. Aguardando 06:00 para enviar WhatsApp...")
    print("📱 Mensagens serão enviadas para:", WHATSAPP_TO)
    
    # Opcional: executar uma vez agora para teste
    # job()
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # verifica a cada minuto

if __name__ == "__main__":
    main()
