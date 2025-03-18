import os
import sys
import time
import random
import requests
import socket
import threading
from os import system
from time import sleep

try:
    import colorama
    from colorama import Fore, Back, Style, init
    init(autoreset=True, strip=True, convert=True)  # Added strip=True and convert=True
except ImportError:
    os.system('pip install colorama')
    import colorama
    from colorama import Fore, Back, Style, init
    init(autoreset=True, strip=True, convert=True)  # Added strip=True and convert=True

# Renkler
R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
B = Fore.BLUE + Style.BRIGHT
M = Fore.MAGENTA + Style.BRIGHT
# Move hprint function definition before the logo
def hprint(s):
    """Animasyonlu yazı yazdırma fonksiyonu"""
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.5 / 100)  # Yavaş animasyon

# Then define the logo
logo = f"""
{G}   _____      _                     __  __       _ _ _           
{G}  / ____|    | |                   |  \\/  |     (_) | |          
{G} | |    _   _| |__   ___ _ __      | \\  / | __ _ _| | | ___ _ __ 
{G} | |   | | | | '_ \\ / _ \\ '__|     | |\\/| |/ _` | | | |/ _ \\ '__|
{G} | |___| |_| | |_) |  __/ |     _  | |  | | (_| | | | |  __/ |   
{G}  \\_____\\__, |_.__/ \\___|_|    (_) |_|  |_|\\__,_|_|_|_|\\___|_|   
{G}         __/ |                                                    
{G}        |___/                                                     
{C} ●■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■●
{Y} ✦ Mail Server Test Aracı                 ✦ API Key Gerektirmeyen Versiyon ✦
{W}                     https://github.com/captainmgc
{C} ●■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■●
"""

def get_random_agent():
    """Rastgele user agent döndürür"""
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(agents)

def generate_random_string(length=10):
    """Belirtilen uzunlukta rastgele string oluşturur"""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def check_service_availability(service_name, url, timeout=5):
    """Bir servisin kullanılabilir olup olmadığını kontrol eder"""
    try:
        response = requests.head(url, timeout=timeout)
        if response.status_code < 400:
            return True
        return False
    except Exception:
        return False

# API key gerektirmeyen servisler
services = {
    "FormSubmit": {
        "name": "FormSubmit - API key gerektirmeyen form-email dönüştürücü",
        "check_url": "https://formsubmit.co/ajax/",
        "handler": None,  # Aşağıda tanımlanacak
        "working": False
    }
}

def send_email_formsubmit(to_email, subject, message_body):
    """FormSubmit servisi üzerinden email gönderir (API key gerektirmez)"""
    try:
        session = requests.Session()
        user_agent = get_random_agent()
        
        # FormSubmit endpoint
        api_url = "https://formsubmit.co/ajax/" + to_email
        
        # Rastgele email adresi
        random_name = generate_random_string(8)
        email_addr = f"{random_name}@testmail.org"
        
        hprint(G + f" ➤ Gönderen adresi olarak kullanılıyor: {email_addr}")
        
        # Form verilerini hazırla
        payload = {
            "name": "Mail Server Test",
            "email": email_addr,
            "subject": subject,
            "_subject": subject,  # FormSubmit bu formatı kullanır
            "message": message_body,
            "_captcha": "false"  # Captcha'yı devre dışı bırakmaya çalış
        }
        
        headers = {
            "User-Agent": user_agent,
            "Origin": "https://mailtest.local",  # Sahte origin
            "Referer": "https://mailtest.local/testform.html"  # Sahte referrer
        }
        
        hprint(C + " ➤ FormSubmit üzerinden email gönderiliyor...")
        
        # Gerçek gönderim işlemi
        response = session.post(api_url, data=payload, headers=headers)
        
        if response.status_code == 200 and '"success"' in response.text.lower():
            hprint(G + " ✓ FormSubmit gönderimi başarılı görünüyor")
            success = True
        else:
            hprint(R + " ✗ FormSubmit gönderimi başarısız - muhtemelen anti-bot önlemleri tarafından engellendi")
            success = False
        
        return success
    
    except Exception as e:
        hprint(R + f" ✗ Hata: {str(e)}")
        return False

def send_email_anonymous(to_email, subject, message_body):
    """AnonymousEmail benzeri bir servise form gönderimi yapar"""
    try:
        session = requests.Session()
        user_agent = get_random_agent()
        
        # Test için httpbin.org kullanıyoruz
        api_url = "https://httpbin.org/post"
        
        # Rastgele email adresi
        random_name = generate_random_string(8)
        email_addr = f"{random_name}@anonymous.mail"
        
        hprint(G + f" ➤ Gönderen adresi olarak kullanılıyor: {email_addr}")
        
        # Form verilerini hazırla
        payload = {
            "sender": email_addr,
            "recipient": to_email,
            "subject": subject,
            "message": message_body
        }
        
        headers = {
            "User-Agent": user_agent,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        hprint(C + " ➤ Anonymous Email simülasyonu yapılıyor...")
        
        # Bu bir test gönderimi - gerçekte çalışmaz
        response = session.post(api_url, data=payload, headers=headers)
        
        if response.status_code == 200:
            hprint(Y + " ℹ Test başarılı, ancak gerçek bir email gönderilmedi")
            hprint(Y + " ℹ Bu sadece HTTP request testi için kullanılmıştır")
            success = False
        else:
            hprint(R + " ✗ Test başarısız")
            success = False
        
        return success
    
    except Exception as e:
        hprint(R + f" ✗ Hata: {str(e)}")
        return False

def send_email_publicapi(to_email, subject, message_body):
    """Açık API kullanarak email göndermeyi simüle eder"""
    try:
        session = requests.Session()
        user_agent = get_random_agent()
        
        # WordpressAPI'nin contact-form özelliğini kullanmaya çalışırız
        api_url = "https://public-api.wordpress.com/rest/v1.1/sites/test.blog/posts/feedback"
        
        random_name = generate_random_string(8)
        email_addr = f"{random_name}@test.org"
        
        hprint(G + f" ➤ Gönderen adresi olarak kullanılıyor: {email_addr}")
        
        # Payload hazırla
        payload = {
            "email": email_addr,
            "comment": message_body,
            "name": "Test User",
            "URL": "",
            "contact_form_id": "feedback-test",
            "_feedback_subject": subject,
            "_feedback_author": "Test User",
            "_feedback_author_email": email_addr,
            "_feedback_recipient": to_email
        }
        
        headers = {
            "User-Agent": user_agent,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        hprint(C + " ➤ WordPress API test isteği gönderiliyor...")
        
        # Bu sadece WordPress API'sini test etmek için - gerçekte çalışmaz
        # Sadece test amaçlı
        
        hprint(Y + " ℹ Test gönderimi simüle ediliyor, ancak gerçek bir email gönderilmedi")
        hprint(Y + " ℹ WordPress API'sı, uygun site kimliği ve yapılandırma gerektirmektedir")
        success = False
        
        return success
    
    except Exception as e:
        hprint(R + f" ✗ Hata: {str(e)}")
        return False

def send_email_webform(to_email, subject, message_body):
    """HTML form gönderimi tekniğini kullanarak email göndermeyi dener"""
    try:
        # Gerçekte burada bir web form gönderimi yapılır
        # Bu genellikle bir web sitesindeki iletişim formunu kullanır
        
        session = requests.Session()
        user_agent = get_random_agent()
        
        # Test için bir URL - gerçek bir email formu URL'si olması gerekir
        form_url = "https://httpbin.org/post"
        
        random_name = generate_random_string(8)
        email_addr = f"{random_name}@sender.test"
        
        hprint(G + f" ➤ Gönderen adresi olarak kullanılıyor: {email_addr}")
        
        # Form verilerini hazırla
        form_data = {
            "name": "Server Tester",
            "email": email_addr,
            "recipient": to_email,
            "subject": subject,
            "message": message_body,
            "send_copy": "0"
        }
        
        headers = {
            "User-Agent": user_agent,
            "Referer": "https://servertest.local/contact.html",
            "Origin": "https://servertest.local"
        }
        
        hprint(C + " ➤ Web form gönderimi test ediliyor...")
        
        # Gerçekte iletişim formuna yönlendirilecek bir HTTP isteği
        response = session.post(form_url, data=form_data, headers=headers)
        
        if response.status_code == 200:
            hprint(Y + " ℹ HTTP isteği başarılı, ancak gerçek bir email gönderilmedi")
            hprint(Y + " ℹ Gerçek bir email formu URL'si gereklidir")
            success = False
        else:
            hprint(R + " ✗ Form gönderimi başarısız")
            success = False
        
        return success
    
    except Exception as e:
        hprint(R + f" ✗ Hata: {str(e)}")
        return False

def test_direct_smtp(to_email, subject, message_body):
    """Alıcının SMTP sunucusuna direkt bağlantı deneyerek mail testini yapar"""
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        recipient_domain = to_email.split('@')[1]
        hprint(G + f" ➤ Alıcı domaini analiz ediliyor: {recipient_domain}")
        
        # MX kayıtlarını kontrol et
        try:
            import dns.resolver
            hprint(G + " ➤ MX kayıtları sorgulanıyor...")
            mx_records = dns.resolver.resolve(recipient_domain, 'MX')
            mx_hosts = [str(rdata.exchange).rstrip('.') for rdata in mx_records]
            
            if not mx_hosts:
                hprint(R + f" ✗ {recipient_domain} için MX kaydı bulunamadı")
                return False
                
            # İlk MX kaydını kullan
            mx_host = mx_hosts[0]
            hprint(G + f" ✓ MX sunucusu bulundu: {mx_host}")
            
            # Rastgele email adresi oluştur
            random_name = generate_random_string(8)
            email_addr = f"{random_name}@{recipient_domain}"  # Genellikle aynı domain kullanmak gerekir
            
            hprint(G + f" ➤ Test göndereni: {email_addr}")
            hprint(G + f" ➤ {mx_host}:25 bağlantısı deneniyor...")
            
            # SMTP bağlantısı
            try:
                # Zaman aşımı süresini kısa tut
                server = smtplib.SMTP(mx_host, 25, timeout=10)
                server.set_debuglevel(0)  # 1 olarak değiştirilerek daha detaylı log alınabilir
                
                # EHLO komutu
                server.ehlo_or_helo_if_needed()
                
                hprint(G + " ✓ SMTP bağlantısı kuruldu")
                
                # E-posta oluştur
                msg = MIMEMultipart()
                msg['From'] = email_addr
                msg['To'] = to_email
                msg['Subject'] = subject
                
                # İçerik ekle
                msg.attach(MIMEText(message_body, 'plain'))
                
                # Mail gönderimi dene
                hprint(C + " ➤ SMTP TEST: Mail gönderimi deneniyor...")
                
                # Bu işlem genellikle başarısız olur, çünkü modern SMTP sunucuları kimlik doğrulama gerektirir
                try:
                    server.sendmail(email_addr, to_email, msg.as_string())
                    hprint(G + " ✓ Mail başarıyla gönderildi!")
                    success = True
                except smtplib.SMTPException as e:
                    hprint(R + f" ✗ Mail gönderimi başarısız: {str(e)}")
                    hprint(Y + " ℹ Modern SMTP sunucuları genellikle kimlik doğrulama gerektirir")
                    success = False
                
                server.quit()
                return success
                
            except (socket.timeout, smtplib.SMTPException, ConnectionRefusedError) as e:
                hprint(R + f" ✗ SMTP bağlantısı başarısız: {str(e)}")
                return False
                
        except ImportError:
            hprint(R + " ✗ DNS çözümleyici kütüphanesi bulunamadı")
            hprint(Y + " ➤ dnspython yükleniyor...")
            os.system('pip install dnspython')
            try:
                import dns.resolver
                hprint(G + " ✓ DNS kütüphanesi yüklendi, lütfen komutu tekrar çalıştırın")
            except ImportError:
                hprint(R + " ✗ DNS çözümleyici kütüphanesi yüklenemedi")
            return False
        
    except Exception as e:
        hprint(R + f" ✗ Hata: {str(e)}")
        return False

# Her servis için fonksiyonları tanımla
services["FormSubmit"]["handler"] = send_email_formsubmit

def check_all_services():
    """Tüm servislerin durumunu kontrol eder ve günceller"""
    hprint(G + " ➤ Servis erişilebilirliği kontrol ediliyor...")
    working_services = []
    
    # Sequential checking instead of threading
    for service_id, service_info in services.items():
        try:
            available = check_service_availability(service_id, service_info["check_url"])
            services[service_id]["working"] = available
            
            if available:
                hprint(G + f" ✓ {service_id} servisi erişilebilir görünüyor")
                working_services.append((service_id, service_info))
            else:
                hprint(R + f" ✗ {service_id} servisi erişilemez görünüyor")
        except Exception as e:
            hprint(R + f" ✗ {service_id} kontrolünde hata: {str(e)}")
            services[service_id]["working"] = False
    
    # FormSubmit'i her zaman ekle
    form_submit_found = False
    for service_id, _ in working_services:
        if service_id == "FormSubmit":
            form_submit_found = True
            break
    
    if not form_submit_found:
        working_services.append(("FormSubmit", services["FormSubmit"]))
    
    # Direkt SMTP testi de ekle
    working_services.append(("DirectSMTP", {
        "name": "Direkt SMTP - Alıcının mail sunucusunu test et   ",
        "working": True,
        "handler": test_direct_smtp
    }))
    
    return working_services

def check_service_and_update(service_id, service_info):
    """Bir servisi kontrol et ve çalışma durumunu güncelle"""
    try:
        available = check_service_availability(service_id, service_info["check_url"])
        services[service_id]["working"] = available
        
        # Add a small delay to prevent output overlap
        time.sleep(0.1)
        
        # Format the status message with proper spacing
        if available:
            status_message = f" ✓ {service_id} servisi erişilebilir görünüyor"
            hprint(G + status_message)
        else:
            status_message = f" ✗ {service_id} servisi erişilemez görünüyor"
            hprint(R + status_message)
        
    except Exception as e:
        time.sleep(0.1)
        error_message = f" ✗ {service_id} kontrolünde hata: {str(e)}"
        hprint(R + error_message)
        services[service_id]["working"] = False

# Ana program
if __name__ == "__main__":
    if os.name == 'nt':
        system("cls")
    else:
        system("clear")
    print(logo)
    print('')
    hprint(M + ' ■ Mail Server Test Aracı Başlatılıyor...')
    sleep(1)
    print('')

    # Kullanıcıyı bilgilendir
    hprint(Y + " █ BİLGİLENDİRME:")
    hprint(Y + " █ Bu araç mail sunucunuzu test etmek için tasarlanmıştır.")
    hprint(Y + " █ Modern email sistemleri anonim gönderimi engeller.")
    hprint(G + " █ Bu test aracı sunucunuzun mail alabilirliğini kontrol eder.")
    print('')

    # Servisleri kontrol et
    hprint(C + " ➤ Kullanılabilir servisler kontrol ediliyor...")
    working_services = check_all_services()

    # Kullanılabilir servisleri görüntüle
    print(G + "\n ◉ Kullanılabilir Email Servisleri:")
    border = C + " ╔" + "═" * 67 + "╗"
    print(border)
    
    for i, (service_id, service_info) in enumerate(working_services, 1):
        status = G + "AKTİF" if service_info.get("working", False) else Y + "PASİF (DENENEBİLİR)"
        name = service_info.get('name', '')
        
        # Add an empty line between services
        if i > 1:
            print(C + " ║" + " " * 67 + "║")
        
        # Calculate exact padding needed for perfect alignment
        total_width = 67  # Total width inside the box
        index_width = 4   # Width for "[1] "
        status_width = 6  # Width for "AKTİF"
        name_space = total_width - index_width - status_width - 1  # -1 for extra space before status
        
        service_line = (C + " ║ " + Y + f"[{i}] " + W + f"{name:<{name_space}}" + 
                       G + f"{status}" + C + "║")
        print(service_line)
    
    border_bottom = C + " ╚" + "═" * 67 + "╝"
    print(border_bottom)
    print('')

    # Önerilen servis
    recommended = None
    if working_services:
        for service_id, service_info in working_services:
            if service_id == "FormSubmit":
                recommended = "FormSubmit"
                hprint(G + f" ✰ ÖNERİLEN SERVİS: FormSubmit - API key olmadan çalışma ihtimali en yüksek")
                break
        
        if not recommended:
            recommended = working_services[0][0]
            hprint(G + f" ✰ ÖNERİLEN SERVİS: {recommended} - erişilebilir görünüyor")

    # Servis seçimi
    selected_service = None
    while True:
        try:
            service_choice = int(input(G + f"\n ▶ Servis seçin (1-{len(working_services)})" + C + " : " + Y))
            if 1 <= service_choice <= len(working_services):
                selected_service = working_services[service_choice-1]
                break
            else:
                print(R + f" ✗ Lütfen 1-{len(working_services)} arasında bir sayı girin.")
        except ValueError:
            print(R + " ✗ Lütfen geçerli bir sayı girin.")

    print('')
    to = input(G + " ▶ Alıcı Email" + C + " : " + Y)
    print('')
    subject = input(G + " ▶ Email Konusu" + C + " : " + Y)
    print("")
    msg = input(G + " ▶ Email İçeriği" + C + " : " + Y)
    print("")

    # İnternet bağlantısı kontrolü
    try:
        hprint(C + " ➤ İnternet bağlantısı kontrol ediliyor...")
        test_connection = requests.get("https://www.google.com", timeout=5)
        hprint(G + " ✓ İnternet bağlantısı aktif")
    except (requests.ConnectionError, requests.Timeout):
        print(R + " ✗ İnternet bağlantısı bulunamadı. Lütfen ağınızı kontrol edin ve tekrar deneyin." + W)
        sys.exit(1)

    # Seçilen servisi kullanarak email gönder
    service_id, service_info = selected_service
    handler = service_info.get("handler")

    if handler:
        print(C + "\n ╔" + "═" * 60 + "╗")
        hprint(C + " ║" + G + f" {service_id} servisi kullanılıyor..." + " " * (37 - len(service_id)) + C + "║")
        print(C + " ╚" + "═" * 60 + "╝")
        
        success = handler(to, subject, msg)
        
        if success:
            print("")
            print(G + " ✅ " + "═" * 58 + "✅")
            hprint(G + " ✅ Email başarıyla gönderildi!! Mail kutunuzu kontrol edin ✅")
            print(G + " ✅ " + "═" * 58 + "✅")
        else:
            print("")
            print(R + " ❌ " + "═" * 58 + "❌")
            hprint(R + " ❌ Email gönderimi başarısız oldu ❌")
            print(R + " ❌ " + "═" * 58 + "❌")
            
            # Alternatif öneri
            print("")
            hprint(Y + " ⚠️ ÖNERİ: Mail sunucu testleri için aşağıdakileri deneyebilirsiniz:")
            hprint(Y + " ⚠️ 1. Manuel olarak web-tabanlı bir mail hesabı kullanmak")
            hprint(Y + " ⚠️ 2. SMTP kimlik doğrulama bilgilerinizi kullanmak")
            hprint(Y + " ⚠️ 3. Sunucunuzda mail log'larını kontrol etmek")
    else:
        hprint(R + f" ✗ {service_id} için uygulama fonksiyonu bulunamadı.")

    print('')
    sleep(1)
    hprint(Y + " ℹ HATIRLATMA: Modern email sistemleri güçlü anti-spam önlemlerine sahiptir")
    hprint(Y + " ℹ Test email'leri spam klasörüne düşebilir veya tamamen engellenebilir")
    print('')
    print(G + "\n ◉ Mail Server Test Aracı tamamlandı" + W)
    print('')