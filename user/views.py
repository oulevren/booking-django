from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend

# Create your views here.


def user_login(req):
    # İstek method'u kontrolü
    if req.method == 'POST':
        # POST isteği geldiyse, formdan email ve parola bilgilerini al
        email = req.POST.get('email')
        parola = req.POST.get('parola')
        
        # Kullanıcının girdiği bilgileri ekrana yazdır
        print(f"Email: {email}, Parola: {parola}")

        try:
            # Veritabanında kullanıcıyı email ile ara
            user = User.objects.get(email=email)
            
            # Eğer kullanıcı bulunursa ve parola doğruysa
            if user is not None and user.check_password(parola):
                # Doğrulama başarılı, kullanıcıyı oturum açtır ve kayıt sayfasına yönlendir
                print(f"Giriş başarılı: {user}")
                login(req, user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('base')
            else:
                # Eğer kullanıcı bulunsa da parola yanlışsa
                print("Giriş başarısız: Parola yanlış")
                return render(req, 'user_login.html', {'hata': 'Kullanıcı adı veya parola yanlış'})
        except User.DoesNotExist:
            # Eğer kullanıcı bulunamazsa
            print("Giriş başarısız: Kullanıcı bulunamadı")
            return render(req, 'user_login.html', {'hata': 'Kullanıcı adı veya parola yanlış'})

    else:
        # GET isteği geldiyse, giriş sayfasını göster
        return render(req, 'user_login.html')
    

def register(req):
    if req.method == 'POST':
        kullanici_adi = req.POST['kullanici_adi']
        email = req.POST['email']
        parola = req.POST['parola']
        parola_tekrar = req.POST['parola_tekrar']
        
        if parola == parola_tekrar:
            if User.objects.filter(username=kullanici_adi).exists():
                return render(req, 'register.html', {"hata": "Kullanıcı adı kullanılıyor"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(req, 'register.html', {"hata": "E-mail kullanılıyor"})
                else:
                    user = User.objects.create_user(username=kullanici_adi, email=email, password=parola)
                    user.save()
                    return redirect('login')
        else:
            return render(req, 'register.html', {"hata": "Parola uyuşmuyor"})
    else:
        return render(req, 'register.html')

def cikis (req):
    logout(req)
    return redirect('base')